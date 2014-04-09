# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397084402.354378
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/dash.html'
_template_uri = 'dash.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('<!--## This is the base page for both the dashboards. Sprouting off of this one will be a manager and an admin page with minute\r\n')
        # SOURCE LINE 3
        __M_writer('\r\n')
        # SOURCE LINE 6
        __M_writer(' \r\n')
        # SOURCE LINE 8
        __M_writer(' ')
 

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 23
        __M_writer('<!--ends content-->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(' ')
 

        __M_writer('\r\n  <h2>Welcome back, ')
        # SOURCE LINE 11
        __M_writer(str(request.user.first_name))
        __M_writer(' ')
        __M_writer(str(request.user.last_name))
        __M_writer("!</h2></br>\r\n  <p>Use the left-side navigation bar to view connecting pages and options by clicking on each section heading. To view your own account information, log out, or return to your dashboard, use the dropdown menu in the upper right hand corner.</p>\r\n\r\n  <div class='vertical_spacer6'></div>\r\n  <div class='vertical_spacer6'></div>\r\n  <div class='vertical_spacer6'></div>\r\n  <div class='vertical_spacer6'></div>\r\n  <div class='vertical_spacer6'></div>\r\n  <div class='vertical_spacer6'></div>\r\n  <div class='vertical_spacer6'></div>\r\n  <div class='vertical_spacer6'></div>\r\n\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


