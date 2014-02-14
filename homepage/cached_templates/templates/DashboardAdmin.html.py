# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1390271446.310486
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/DashboardAdmin.html'
_template_uri = 'DashboardAdmin.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'adminOptions', 'title']


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
    return runtime._inherit_from(context, 'base_dash.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def adminOptions():
            return render_adminOptions(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        # SOURCE LINE 6
        __M_writer('\n')
        # SOURCE LINE 9
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 13
        __M_writer(' \n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'adminOptions'):
            context['self'].adminOptions(**pageargs)
        

        # SOURCE LINE 23
        __M_writer(' \n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 31
        __M_writer('   ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer('\n')
        # SOURCE LINE 27
        __M_writer('\n    <p>Welcome back!</p>\n\n    <p>Use the left-side navigation bar to view connecting pages and options.</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_adminOptions(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def adminOptions():
            return render_adminOptions(context)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer('\n\t <li>\n        <a href="/manageUsers/">View/Edit User Information</a>\n    </li>\n    <li>\n    \t<a href="/reports/">Print Reports</a>\n    </li>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer('\n\t<strong>Admin Dashboard</strong>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


