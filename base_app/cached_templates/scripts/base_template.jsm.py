# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393566858.451289
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\base_app\\scripts/base_template.jsm'
_template_uri = 'base_template.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer("\n\n//Ajax call, basic example\n$(function() {\n\n\t$('#login_button').off('click.login').on('click.login', function(){\n\n\t\t$('#login_button').loadmodal({\n\t\t\turl: '/account/login/',\n\t\t\tid: 'login_modal',\n\t\t\ttitle: '<h2>Login</h2>',\n\t\t\twidth: '600px',\n\t\t\tajax: {\n\t\t\t\tdataType: 'html',\n\t\t\t\tmethod: 'POST',\n\t\t\t\tsuccess: function(data, status, xhr) {\n\t\t\t\t\tconsole.log($('#login_modal'));\n\t\t\t\t},//\n\t\t\t// any other options from the regular $.ajax call (see JQuery docs)\n\t\t\t\n\t\t\t},\n\t\t});\n\t});\n});\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


