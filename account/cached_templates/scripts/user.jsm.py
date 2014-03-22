# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393567747.701511
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\scripts/user.jsm'
_template_uri = 'user.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer("\n\n//Ajax call to create a modal\n$(function() {\n\n\t$('#password_button').off('click.password').on('click.password', function(){\n\n\t\t$('#password_button').loadmodal({\n\t\t\turl: '/account/user__password/")
        # SOURCE LINE 9
        __M_writer(str(user.id))
        __M_writer("',\n\t\t\tid: 'password_modal',\n\t\t\ttitle: '<h2>Edit Password</h2>',\n\t\t\twidth: '600px',\n\t\t\tajax: {\n\t\t\t\tdataType: 'html',\n\t\t\t\tmethod: 'POST',\n\t\t\t\tsuccess: function(data, status, xhr) {\n\t\t\t\t\tconsole.log($('#password_modal'));\n\t\t\t\t},//\n\t\t\t// any other options from the regular $.ajax call (see JQuery docs)\n\t\t\t\n\t\t\t},\n\t\t});\n\t});\n});\n\n//Ajax call to create a modal\n$(function() {\n\n\t$('#edit_button').off('click.edit').on('click.edit', function(){\n\n\t\t$('#edit_button').loadmodal({\n\t\t\turl: '/account/user__edit/")
        # SOURCE LINE 32
        __M_writer(str(user.id))
        __M_writer("',\n\t\t\tid: 'edit_modal',\n\t\t\ttitle: '<h2>Edit Account Info</h2>',\n\t\t\twidth: '600px',\n\t\t\tajax: {\n\t\t\t\tdataType: 'html',\n\t\t\t\tmethod: 'POST',\n\t\t\t\tsuccess: function(data, status, xhr) {\n\t\t\t\t\tconsole.log($('#edit_modal'));\n\t\t\t\t},//\n\t\t\t// any other options from the regular $.ajax call (see JQuery docs)\n\t\t\t\n\t\t\t},\n\t\t});\n\t});\n});")
        return ''
    finally:
        context.caller_stack._pop_frame()


