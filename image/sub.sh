#!/bin/csh -f

################################################################
## set number of processes/threads for parallel job
################################################################

set echo
foreach exp (yxyhigh) # exp name 
set CCSMROOT = /nuist/u/home/zenggang/zenggang/cesm1_2_2
set CASEROOT = /nuist/u/home/zenggang/yangxy/cesm/$exp  # change to your root
set MACH     = zenggang
set COMPSET  = FC5
set RES      = f19_f19
set num     =  280 # should be same as nodes * ppn

set DIN_LOC_ROOT = /nuist/scratch/zenggang/zenggang/cesm/inputdata
rm -fr $CASEROOT

cd /nuist/u/home/zenggang/zenggang/cesm1_2_2/scripts
echo "Create_Newcase using CESM script starting ..."
   ./create_newcase -case $CASEROOT -res $RES -compset FC5 -mach $MACH
echo "Create_Newcase using CESM script done"

cd $CASEROOT
./xmlchange -file env_run.xml -id RUNDIR  -val /nuist/scratch/zenggang/yangxy/cesm/$exp/exe/run       # change to your output run 
./xmlchange -file env_run.xml -id DOUT_S_ROOT -val /nuist/scratch/zenggang/yangxy/cesm/output/$exp  # change to your output results 
./xmlchange -file env_run.xml  -id RESUBMIT             -val 0
./xmlchange -file env_run.xml  -id STOP_OPTION             -val nyears
./xmlchange -file env_run.xml  -id STOP_N                  -val 32
./xmlchange -file env_run.xml -id RUN_STARTDATE           -val 1986-01-01
./xmlchange -file env_run.xml -id SSTICE_YEAR_START      -val 1986
./xmlchange -file env_run.xml -id  SSTICE_YEAR_END   -val 2017
./xmlchange -file env_run.xml -id SSTICE_DATA_FILENAME   -val $DIN_LOC_ROOT/atm/cam/sst/yxy_high.nc  # change to your input sst file
./xmlchange -file env_run.xml -id SSTICE_GRID_FILENAME   -val $DIN_LOC_ROOT/atm/cam/ocnfrac/domain.camocn.1.9x2.5_gx1v6_090403.nc
./xmlchange -file env_mach_pes.xml -id NTASKS_ATM   -val $num
./xmlchange -file env_mach_pes.xml -id NTASKS_LND   -val $num
./xmlchange -file env_mach_pes.xml -id NTASKS_ICE   -val $num
./xmlchange -file env_mach_pes.xml -id NTASKS_OCN   -val $num
./xmlchange -file env_mach_pes.xml -id NTASKS_CPL   -val $num
./xmlchange -file env_mach_pes.xml -id NTASKS_GLC   -val $num
./xmlchange -file env_mach_pes.xml -id NTASKS_ROF   -val $num
./xmlchange -file env_mach_pes.xml -id NTASKS_WAV   -val $num

    ./xmlchange -file env_build.xml -id CESMSCRATCHROOT -val /nuist/scratch/zenggang/yangxy/cesm/$exp # change to your own
    ./xmlchange -file env_build.xml -id EXEROOT -val /nuist/scratch/zenggang/yangxy/cesm/$exp/exe # change to your own

               echo "Configure case starting ..."
               ./cesm_setup
                  echo "Configure case done"
                  echo "grid_file='/nuist/scratch/zenggang/zenggang/cesm/inputdata/atm/cam/ocnfrac/domain.camocn.1.9x2.5_gx1v6_090403.nc'" >> user_nl_cice
                  echo "kmt_file='/nuist/scratch/zenggang/zenggang/cesm/inputdata/atm/cam/ocnfrac/domain.camocn.1.9x2.5_gx1v6_090403.nc'" >> user_nl_cice

#                  echo nhtfrq = -24 >> user_nl_cam

                  cd $CASEROOT
                  echo "Build case starting ..."
                     ./$exp.build
                     echo "Build case done"

sed -i "7a#PBS -M 4669459@qq.com" $exp.run  # change to your email, but this may not be effective 
sed -i "7a#PBS -e run.err" $exp.run
sed -i "7a#PBS -S /bin/bash" $exp.run
sed -i "7a#PBS -l walltime=168:00:00" $exp.run
sed -i "7a#PBS -l nodes=10:ppn=28" $exp.run
sed -i "7a#PBS -q Longtime" $exp.run

                  qsub $exp.run
                     end
