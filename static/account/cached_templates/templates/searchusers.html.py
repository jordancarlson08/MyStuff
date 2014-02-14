# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1390603037.709322
_enable_loop = True
_template_filename = 'D:\\Google Drive\\MyStuff Website\\MyStuff\\homepage\\templates/searchusers.html'
_template_uri = 'searchusers.html'
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
    return runtime._inherit_from(context, 'searchusers.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 51
        __M_writer('  \n')
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
        __M_writer('\n  <h2>User Management</h2>\n\n  <table class="table table-hover">\n  \t<thead>\n  \t\t<tr>\n  \t\t\t<th>Username</th>\n  \t\t\t<th>Given Name</th>\n  \t\t\t<th>Surname</th>\n  \t\t</tr>\n  \t</thead>\n  \t<tbody>\n      <tr>\n        <td><span class="label label-success">Manager</span></td>\n        <td><a href="/Profile/">nford189</a></td>\n        <td>Nancy</td>\n        <td>Ford</td>\n      </tr>\n  \t\t<tr>\n  \t\t\t<td><span class="label label-primary">Customer</span></td>\n  \t\t\t<td>johans66</td>\n  \t\t\t<td>Joseph</td>\n  \t\t\t<td>Hansen</td>\n  \t\t</tr>\n  \t\t<tr>\n  \t\t\t<td><span class="label label-success">Manager</span></td>\n  \t\t\t<td>Mnmturtles</td>\n  \t\t\t<td>Michael</td>\n  \t\t\t<td>Greene</td>\n  \t\t</tr>\n  \t\t<tr>\n  \t\t\t<td><span class="label label-warning">Admin</span></td>\n  \t\t\t<td>amydrew85</td>\n  \t\t\t<td>Amy</td>\n  \t\t\t<td>Andrews</td>\n  \t\t</tr>\n  \t</tbody>\n\n\n\n\n\n  </table>\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


