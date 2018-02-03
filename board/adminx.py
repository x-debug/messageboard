# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~
    A brief description goes here.
    :copyright: (c) 2016 by chenxf@partnerch.com.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

from board.models import Message
import xadmin
from xadmin import views


class MessageAdmin(object):
    list_display = ['name', 'email', 'address']
    search_fields = ["name", 'email']


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    menu_style = 'accordion'


xadmin.site.register(Message, MessageAdmin)
