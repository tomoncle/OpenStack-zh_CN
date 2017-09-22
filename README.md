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

## cinder

### `Ubuntu-14.04`

##### 1.系统默认语言改为：`zh_CN.UTF-8`
> dpkg依赖包：
>   `language-pack-zh-hans_1%3a14.04+20160720_all.deb`
>   `language-pack-zh-hans-base_1%3a14.04+20160720_all.deb`

* `apt-get` 直接安装：
 ```bash
 $ sudo apt-get install language-pack-zh-hans language-pack-zh-hans-base
 ``` 

* `dpkg` 安装：
 ```bash
 $ dpkg -i language-pack-zh-hans*
 ```

* 环境变量设置 : 
 ```bash
 $ export LANG=zh_CN.UTF-8
 ```

* 查看依赖语言包：安装完查看`/usr/share/locale-langpack`是否存在`zh_CN`:
 ```bash
 $ ls /usr/share/locale-langpack
 en  en_AU  en@boldquot  en_CA  en_GB  en_NZ  en@quot  en@shaw  en_US  en_US@piglatin  zh  zh_CN
 ```

##### 源码修改: 
* 位置1: `/usr/lib/python2.7/dist-packages/cinder/api/openstack/wsgi.py`　改为:
  ```bash
  +1322 : i18n.translate(explanation, locale) > i18n.translate(explanation, 'zh_CN')
  +1385 : i18n.translate(msg, locale) > i18n.translate(msg, 'zh_CN')
  ```
  
* 位置2: `/usr/lib/python2.7/dist-packages/cinder/i18n.py` 改为:
  ```
  +27 _translators = i18n.TranslatorFactory(domain=DOMAIN, localedir='locale')
  +36 def translate(value, user_locale='zh_CN'):
  ```

##### 生成翻译文件: 
> 将翻译好的 [`cinder.po`](https://github.com/openstack/cinder/blob/master/cinder/locale/zh_CN/LC_MESSAGES/cinder.po) 文件生成 `cinder.mo` 文件
* 生成.mo文件命令：`msgfmt -o cinder.mo cinder.po` 
* cinder.mo文件存放位置：
  * 1.拷贝cinder.mo 到`/usr/lib/python2.7/dist-packages/cinder/locale/zh_CN/LC_MESSAGES/`
  * 2.拷贝cinder.mo 到`/usr/share/locale-langpack/zh_CN/LC_MESSAGES/`

* 3.重启api服务: `service cinder-api restart`

##### 测试：
* 编辑`/usr/lib/python2.7/dist-packages/cinder/i18n.py`：添加打印测试：
 ```python
 print _('Resource could not be found.')
 ```
* 执行命令：`$ python i18n.py`
