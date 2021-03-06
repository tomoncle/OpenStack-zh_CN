# Copyright 2014 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""oslo.i18n integration module.

See http://docs.openstack.org/oslo.i18n/latest/user/index.html .

"""

import oslo_i18n as i18n

DOMAIN = 'cinder'

_translators = i18n.TranslatorFactory(domain=DOMAIN, localedir='locale')

# The primary translation function using the well-known name "_"
_ = _translators.primary


def enable_lazy(enable=True):
    return i18n.enable_lazy(enable)


def translate(value, user_locale='zh_CN'):
    return i18n.translate(value, user_locale)


def get_available_languages():
    return i18n.get_available_languages(DOMAIN)


# test language
# print get_available_languages()
# print _("no")

