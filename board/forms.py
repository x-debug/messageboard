# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~
    A brief description goes here.
    :copyright: (c) 2016 by chenxf@partnerch.com.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

from django import forms


class SubmitMessageForm(forms.Form):
    name = forms.CharField(label='姓名', required=True, error_messages={
        'required': '姓名必须填写'
    })

    email = forms.EmailField(label='邮件地址', required=True, error_messages={
        'required': '邮件地址必须填写'
    })

    address = forms.CharField(label='联系地址', required=True, error_messages={
        'required': '联系地址必须填写'
    })

    content = forms.CharField(label='留言内容', required=True, error_messages={
        'required': '留言内容必须填写'
    })
