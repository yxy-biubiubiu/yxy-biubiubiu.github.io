---
title: 从有到无搭建一个属于自己的网站
date: 2020-05-12 11:05:44
tags: 其他
top: true
---

从萌生想法到成功搭建自己的网站前前后后花了大概半个月的时间，终于成功搭建一块了属于自己的地盘。第一篇文章就记录下搭建个人网站的全部过程吧。

大家感兴趣的话完全可以尝试文中操作，免费创建属于自己的主页或者博客。

<!--more-->

搭建自己的网站有两种方式，一种是直接部署在github上，这种是免费的，但是github属于外网控制，网速以及其他问题大家都懂的。另一种则是自己注册并购买域名，不过这种仍然推荐与github同时使用。根据自己需要选择一个合适的方案。

### 1、购买域名，备案（如果仅是通过github部署，可直接跳过1）

想要搭建属于自己的网站当然要先购买一个域名，直接百度搜索进入阿里云注册一个账号，选择购买域名，输入一个自己喜欢的域名，如果还没有被注册的话那就可以直接买下来了。购买后，按照提示的流程进行备案，通常需要三部分，第一步是阿里云账号的实名认证(秒通过)，第二步是阿里云对域名购买的人工审核(大概1天内收到回复)，第三部则是阿里云提交国家的管局进行备案(一般是20个工作日内，我大概8天就收到了短信通知备案通过)。

在等待备案通过期间，完全可以同时进行其他的部分(比如文章的撰写，网站的搭建等等)，不用干等着备案的通知。

### 2、通过HEXO搭建网站

Hexo是一款基于Node.js的静态博客框架，可以方便的生成静态网页托管在GitHub和Coding上，非常推荐入坑使用。官网入口：[hexo官网](https://hexo.io/zh-cn/)。（PS：Hexo对中文很友好。）



#### 2.1 安装GIT

Git是目前世界上最先进的分布式版本控制系统，可以有效、高速的管理hexo博客文章，并上传到GitHub。

Windows安装：

到git官网上下载, [Download here](https://gitforwindows.org/)  ,安装后使用其中的git bash端口来使用Git(使用方法就类似于windows的WSL)。

Linux安装：

```shell
sudo apt-get install git
```

使用 git --version 来查看版本，检查是否安装成功。

#### 2.2 安装nodejs

Hexo是基于nodeJS框架的，所以需要安装nodeJs和其中的npm。

Windows安装：[选择LTS版本即可](https://nodejs.org/en/download/)

Linux安装：

```shell
sudo apt-get install nodejs
sudo apt-get install npm
```

安装后使用

```shell
node -v
npm -v
```

来检查是否安装成功和相应版本。

#### 2.3 安装Hexo

在自己想保存博客(网站)源码的位置新建一个文件夹，比如文件夹名为blog，进入该文件夹后右建，选择git bash。输入命令：

```shell
npm install -g hexo-cli
```



完成安装。

接下来初始化hexo：(blogname为博客名，这个并不重要，随意起即可)

```shell
hexo init blogname
cd myblog 
npm install
```

看到cd命令，熟悉linux的小伙伴都懂了，所以说把git bash理解为一个虚拟的linux环境也没啥太大的问题。

新建完成后，指定文件夹目录下有：

- node_modules: 依赖包
- scaffolds：生成文章的一些模板
- source：用来存放你的文章
- themes：主题
- ** _config.yml: 博客的配置文件**
- *** 一些其他的文件

之后使用

```shell
hexo g
hexo server
```

生成博客，并在本地预览，浏览器中输入localhost:4000即可看到。git bash中输入ctrl+c即可断开连接。



### 3、GitHub创建个人仓库

首先去Github注册个人账户，之后在首页点击New repository创建新仓库，仓库名为*******.github.io，  *******为github的用户名，只有这样创建，将来部署到GitHub page的时候，才会被直接识别。



### 4、生成SSH并添加到GitHub

在git bash中输入

```shell
git config --global user.name "name"
git config --global user.email "email"
```



其中name为github用户名，email为github邮箱。

之后输入：

```shell
git config user.name
git config user.email
```

注：这两条直接复制输入，不要把user换成自己的用户名和邮箱。

然后创建ssh私钥和公钥。创建过程全部回车即可，但是如果以前创建过，那就要注意，中间会有提示是否覆盖以前的秘钥，一定不要确定！！！跳过这步即可，使用以前生成的秘钥就行。

```shell
ssh-keygen -t rsa -C "email"
```

进入端口提示的文件夹查看，id_rsa是你这台电脑的私人秘钥，一定要保存好，且不要泄露，id_rsa.pub是公钥，需要上传到GitHub上，这样当你链接GitHub账户时，公钥私钥进行匹配，才能够顺利的通过git上传文件到GitHub上。

进入GitHub的setting中，找到SSH keys的设置选项，点击New SSH key把公钥的内容复制进去即可。



### 5、把Hexo部署到GitHub

现在就需要把刚刚在本地创建好的博客部署到github上，也就是让大家都看到。打开blog/blogname/下的配置文件 `_config.yml`，把最后的那部分修改为

```shell
deploy:
  type: git
  repo: https://github.com/YourgithubName/***.github.io.git
  branch: master
```

***替换为注册的GitHub用户名。

之后安装部署命令：

```shell
npm install hexo-deployer-git --save
```

接着：

```shell
hexo clean
hexo g
hexo deploy
```

clean是清除先前缓存的配置，g(generate)生成新的配置文件，deploy部署到github上。

git bash没有报错的话，恭喜你，过一会大家伙就可以在http://***.github.io这个网站看到你的个人博客了。



### 6、解析域名并与github进行hook

http://***.github.io这个网站可能很长，而且不好记，如果通过第1步的方式购买了域名，那么就有一个通俗常见的.com网址了(或是其他的)。进入阿里云控制台中进行解析，将解析后的域名，在github中的settings中找到webhook，将解析的域名与之前的进行捆绑，重新使用

```shell
hexo clean
hexo g
hexo d
```

进行推送即可。



### 7、推送文章

输入

```shell
hexo new newpapername
```

创建一个新博文，然后在source/_post中打开markdown文件，就可以开始编辑了。

这里我推荐使用Typora软件去编辑博文，十分方便。

写完后重复第6步的三行指令，即可完成推送。



感兴趣的话完全可以尝试2-5和第7步的操作，创建属于自己的主页或者博客，不花一分钱噢。