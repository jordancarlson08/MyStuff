# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393390988.714938
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/search.html'
_template_uri = 'search.html'
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
    return runtime._inherit_from(context, 'search.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 24
        __M_writer('  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n')
        # SOURCE LINE 5
 

        __M_writer('\r\n\r\n\r\n<h2>Search</h2>\r\n<hr/>\r\n\r\n\r\n<div class=\'text-left\'>\r\n\t<ul class="list-inline">\r\n\r\n\t\t<!-- The Ajax goes here -->\r\n\r\n\t</ul>\r\n</div>\r\n\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


