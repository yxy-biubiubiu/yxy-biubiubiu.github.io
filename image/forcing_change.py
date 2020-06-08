import xarray as xr
def forcing_change(path,period,month,yearhigh,yearlow,changelat,changelon,opt):
    in1 = xr.open_dataset('{}/sst_HadOIBl_bc_1.9x2.5_1850_2017_c180507.nc'.format(path))
    in1 = in1.assign_coords(time = in1.indexes['time'].to_datetimeindex())
    in2 = xr.open_dataset('{}/sst_HadOIBl_bc_1.9x2.5_2000climo_c180511.nc'.format(path))
    lat = in1['lat']
    lon = in2['lon']
    ice_cov_prediddle = in1['ice_cov_prediddle'].loc['{}-01'.format(2018-period):]
    SST_cpl_prediddle = in1['SST_cpl_prediddle'].loc['{}-01'.format(2018-period):]
    ice_cov_prediddle_tmp = in1['ice_cov_prediddle'].loc['{}-01'.format(2018-period):]
    SST_cpl_prediddle_tmp = in1['SST_cpl_prediddle'].loc['{}-01'.format(2018-period):]
    ice_cov = in1['ice_cov']
    SST_cpl = in1['SST_cpl']
    ice_cov_tmp = in1['ice_cov'].loc['{}-01'.format(2018-period):]
    SST_cpl_tmp = in1['SST_cpl'].loc['{}-01'.format(2018-period):]
    time = in1['time'].loc['{}-01'.format(2018-period):]
    time_tmp = in1['time'].loc['{}-01'.format(2018-period):]
    date = in1['date'].loc['{}-01-01'.format(2018-period):]
    datesec = in1['datesec'].loc['{}-01'.format(2018-period):]
    ice_cov_prediddle_c = in2['ice_cov_prediddle']
    SST_cpl_prediddle_c = in2['SST_cpl_prediddle']
    SST_cpl_c = in2['SST_cpl']
    ice_cov_c = in2['ice_cov']
    if opt == 'sst':
        SST_cpl_h = SST_cpl_tmp
        SST_cpl_l = SST_cpl_tmp
        SST_cpl_cli = SST_cpl_tmp
        sst_forcing_h = np.array(SST_cpl.loc[SST_cpl.time.dt.month.isin(month) & SST_cpl.time.dt.year.isin(yearhigh)].loc[:,changelat[0]:changelat[1],changelon[0]:changelon[1]])
        sst_forcing_h = sst_forcing_h.reshape((-1,month.shape[0],sst_forcing_h.shape[1],sst_forcing_h.shape[2])).mean((0))
        sst_forcing_l = np.array(SST_cpl.loc[SST_cpl.time.dt.month.isin(month) & ice_cov.time.dt.year.isin(yearlow)].loc[:,changelat[0]:changelat[1],changelon[0]:changelon[1]])
        sst_forcing_l = sst_forcing_l.reshape((-1,month.shape[0],sst_forcing_h.shape[1],sst_forcing_l.shape[2])).mean((0))
        sic_forcing = ice_cov_c
        for i in range(period):
            SST_cpl_h[0+12*i:12+12*i,:,:] = SST_cpl_c.values
            SST_cpl_l[0+12*i:12+12*i,:,:] = SST_cpl_c.values
            SST_cpl_cli[0+12*i:12+12*i,:,:] = SST_cpl_c.values
            ice_cov_tmp[0+12*i:12+12*i,:,:] = ice_cov_c.values
            ice_cov_prediddle_tmp[0+12*i:12+12*i,:,:] = ice_cov_prediddle_c.values
            SST_cpl_prediddle_tmp[0+12*i:12+12*i,:,:] = SST_cpl_prediddle_c.values
        for i in range(period):
            for j in range(month.shape[0]):
                SST_cpl_h.loc[:,changelat[0]:changelat[1],changelon[0]:changelon[1]][12*i+month[j]-1,:,:] = sst_forcing_h[j,:,:]
                SST_cpl_l.loc[:,changelat[0]:changelat[1],changelon[0]:changelon[1]][12*i+month[j]-1,:,:] = sst_forcing_l[j,:,:]
        f_h = xr.Dataset({'ice_cov': ice_cov_tmp,'SST_cpl':SST_cpl_h,'time':time,'date':date,'datesec':datesec,'ice_cov_prediddle':ice_cov_prediddle_tmp,'SST_cpl_prediddle':SST_cpl_prediddle_tmp})                                                                            
        f_l = xr.Dataset({'ice_cov': ice_cov_tmp,'SST_cpl':SST_cpl_l,'time':time,'date':date,'datesec':datesec,'ice_cov_prediddle':ice_cov_prediddle_tmp,'SST_cpl_prediddle':SST_cpl_prediddle_tmp})                                                                            
        f_c = xr.Dataset({'ice_cov': ice_cov_tmp,'SST_cpl':SST_cpl_cli,'time':time,'date':date,'datesec':datesec,'ice_cov_prediddle':ice_cov_prediddle_tmp,'SST_cpl_prediddle':SST_cpl_prediddle_tmp})                                                                            
        f_h.to_netcdf('{}/high.nc'.format(path))
        f_l.to_netcdf('{}/low.nc'.format(path))
        f_c.to_netcdf('{}/cli.nc'.format(path))        
    elif opt == 'sic':
        ice_cov_h = ice_cov_tmp
        ice_cov_l = ice_cov_tmp
        ice_cov_cli = ice_cov_tmp
        sic_forcing_h = np.array(ice_cov.loc[ice_cov.time.dt.month.isin(month) & ice_cov.time.dt.year.isin(yearhigh)].loc[:,changelat[0]:changelat[1],changelon[0]:changelon[1]])
        sic_forcing_h = sic_forcing_h.reshape((-1,month.shape[0],sic_forcing_h.shape[1],sic_forcing_h.shape[2])).mean((0))
        sic_forcing_l = np.array(ice_cov.loc[ice_cov.time.dt.month.isin(month) & ice_cov.time.dt.year.isin(yearlow)].loc[:,changelat[0]:changelat[1],changelon[0]:changelon[1]])
        sic_forcing_l = sic_forcing_l.reshape((-1,month.shape[0],sic_forcing_h.shape[1],sic_forcing_l.shape[2])).mean((0))
        sst_forcing = SST_cpl_c
        for i in range(period):
            ice_cov_h[0+12*i:12+12*i,:,:] = ice_cov_c.values
            ice_cov_l[0+12*i:12+12*i,:,:] = ice_cov_c.values
            ice_cov_cli[0+12*i:12+12*i,:,:] = ice_cov_c.values
            SST_cpl_tmp[0+12*i:12+12*i,:,:] = SST_cpl_c.values
            ice_cov_prediddle_tmp[0+12*i:12+12*i,:,:] = ice_cov_prediddle_c.values
            SST_cpl_prediddle_tmp[0+12*i:12+12*i,:,:] = SST_cpl_prediddle_c.values
        for i in range(period):
            for j in range(month.shape[0]):
                ice_cov_h.loc[:,changelat[0]:changelat[1],changelon[0]:changelon[1]][12*i+month[j]-1,:,:] = sic_forcing_h[j,:,:]
                ice_cov_l.loc[:,changelat[0]:changelat[1],changelon[0]:changelon[1]][12*i+month[j]-1,:,:] = sic_forcing_l[j,:,:]
        f_h = xr.Dataset({'ice_cov': ice_cov_h,'SST_cpl':SST_cpl_tmp,'time':time,'date':date,'datesec':datesec,'ice_cov_prediddle':ice_cov_prediddle_tmp,'SST_cpl_prediddle':SST_cpl_prediddle_tmp})                                                                            
        f_l = xr.Dataset({'ice_cov': ice_cov_l,'SST_cpl':SST_cpl_tmp,'time':time,'date':date,'datesec':datesec,'ice_cov_prediddle':ice_cov_prediddle_tmp,'SST_cpl_prediddle':SST_cpl_prediddle_tmp})                                                                            
        f_c = xr.Dataset({'ice_cov': ice_cov_cli,'SST_cpl':SST_cpl_tmp,'time':time,'date':date,'datesec':datesec,'ice_cov_prediddle':ice_cov_prediddle_tmp,'SST_cpl_prediddle':SST_cpl_prediddle_tmp})                                                                            
        f_h.to_netcdf('{}/high.nc'.format(path))
        f_l.to_netcdf('{}/low.nc'.format(path))
        f_c.to_netcdf('{}/cli.nc'.format(path))