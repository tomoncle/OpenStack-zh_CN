# OpenStack-zh_CN : OpenStack api 汉化支持
* [OpenStack Compute (code-name Nova)](https://github.com/openstack/nova): 计算服务
* [OpenStack Networking (code-name Neutron)](https://github.com/openstack/neutron): 网络服务
* [OpenStack Object Storage (code-name Swift)](https://github.com/openstack/swift): 对象存储服务
* [OpenStack Block Storage (code-name Cinder)](https://github.com/openstack/cinder): 块设备存储服务
* [OpenStack Identity (code-name Keystone)](https://github.com/openstack/keystone): 认证服务
* [OpenStack Image Service (code-name Glance)](https://github.com/openstack/glance): 镜像文件服务
* [OpenStack Dashboard (code-name Horizon)](https://github.com/openstack/horizon): 仪表盘服务
* [OpenStack Telemetry (code-name Ceilometer)](https://github.com/openstack/ceilometer): 告警服务
* [OpenStack Orchestration (code-name Heat)](https://github.com/openstack/heat): 流程服务
* [OpenStack Database (code-name Trove)](https://github.com/openstack/trove): 数据库服务


## 准备工作：
###### `Ubuntu-14.04`
##### 1.系统默认语言改为：`zh_CN.UTF-8`
* `apt-get` 直接安装：
  ```bash
  $ sudo apt-get install language-pack-zh-hans language-pack-zh-hans-base
  ``` 

* 或 `dpkg` 安装：
  * 下载安装包：[language-pack-zh-hans-base](https://github.com/tomoncle/OpenStack-zh_CN/raw/master/packages/language-pack-zh-hans-base_1%253a14.04%2B20160720_all.deb), [language-pack-zh-hans](https://github.com/tomoncle/OpenStack-zh_CN/raw/master/packages/language-pack-zh-hans_1%253a14.04%2B20160720_all.deb)
  * 安装 : `$ dpkg -i language-pack-zh-hans*`

* 环境变量设置 : 
  ```bash
  $ export LANG=zh_CN.UTF-8
  ```

* 查看依赖语言包：安装完查看`/usr/share/locale-langpack`是否存在`zh_CN`:
  ```bash 
  $ ls /usr/share/locale-langpack
  en  en_AU  en@boldquot  en_CA  en_GB  en_NZ  en@quot  en@shaw  en_US  en_US@piglatin  zh  zh_CN
  ```
* 安装gettext：`$ apt install gettext`
* 生成.mo文件命令：`msgfmt -o cinder.mo cinder.po` 

---
## [OpenStack Block Storage (code-name Cinder)](https://github.com/openstack/cinder): 块设备存储服务
* 1.在目录`/usr/lib/python2.7/dist-packages/cinder/locale/zh_CN/LC_MESSAGES`下生成`cinder.mo`文件
* 2.编辑`/usr/lib/python2.7/dist-packages/nova/i18n.py`文件,注释掉默认的 `_ = _translators.primary`,重写`"_"` ,要修改的部分如下:
  ``` python
  # The primary translation function using the well-known name "_"
  # _ = _translators.primary
  import gettext

  locale_dir = '/usr/lib/python2.7/dist-packages/cinder/locale/'
  gettext.install(DOMAIN, locale_dir)
  zh_trans = gettext.translation(DOMAIN, locale_dir, languages=['zh_CN'])
  zh_trans.install()
  _ = _
  
  # Translators for log levels.
  #
  ```
  
* 3.编辑`/usr/lib/python2.7/dist-packages/cinder/api/openstack/wsgi.py`,在文件头部加入：
  ```python
  import sys
  reload(sys)
  sys.setdefaultencoding('utf8')
  ```

* 4.重启api服务: `service cinder-api restart`

---
## [OpenStack Compute (code-name Nova)](https://github.com/openstack/nova): 计算服务
* 1.在目录`/usr/lib/python2.7/dist-packages/nova/locale/zh_CN/LC_MESSAGES`下生成`nova.mo`文件
* 2.编辑`/usr/lib/python2.7/dist-packages/nova/i18n.py`文件,注释掉默认的 `_ = _translators.primary`,重写`"_"` ,要修改的部分如下:
  ``` python
  # The primary translation function using the well-known name "_"
  # _ = _translators.primary
  import gettext

  locale_dir = '/usr/lib/python2.7/dist-packages/nova/locale/'
  gettext.install(DOMAIN, locale_dir)
  zh_trans = gettext.translation(DOMAIN, locale_dir, languages=['zh_CN'])
  zh_trans.install()
  _ = _
  
  # Translators for log levels.
  #
  ```
  
* 3.编辑`/usr/lib/python2.7/dist-packages/nova/api/openstack/__init__.py`,在文件头部加入：
  ```python
  import sys
  reload(sys)
  sys.setdefaultencoding('utf8')
  ```
* 4.重启nova-api服务：`$ service nova-api restart`

---
## [OpenStack Image Service (code-name Glance)](https://github.com/openstack/glance): 镜像文件服务
* `/usr/lib/python2.7/dist-packages/glance/i18n.py`文件,注释掉默认的 `_ = _translators.primary`,重写`"_"` 
* `/usr/lib/python2.7/dist-packages/glance/common/wsgi.py`，加入转码
* `$ service glance-api restart`

---
## [OpenStack Object Storage (code-name Swift)](https://github.com/openstack/swift): 对象存储服务
* `/usr/lib/python2.7/dist-packages/swift/__init__.py`,重写`gettext_()`方法

---
## [OpenStack Networking (code-name Neutron)](https://github.com/openstack/neutron): 网络服务
* 

---
## [OpenStack Identity (code-name Keystone)](https://github.com/openstack/keystone): 认证服务
* `/usr/lib/python2.7/dist-packages/keystone/i18n.py`文件,注释掉默认的 `_ = _translators.primary`,重写`"_"` 
