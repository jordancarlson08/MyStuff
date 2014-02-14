# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1390427377.840444
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/userscourtney.html'
_template_uri = 'userscourtney.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['adminOptions', 'content']


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
        def adminOptions():
            return render_adminOptions(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        # SOURCE LINE 6
        __M_writer('\n')
        # SOURCE LINE 9
        __M_writer('\n')
        # SOURCE LINE 11
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'adminOptions'):
            context['self'].adminOptions(**pageargs)
        

        # SOURCE LINE 15
        __M_writer(' \n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 71
        __M_writer('   \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_adminOptions(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def adminOptions():
            return render_adminOptions(context)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer('\n\t<span class="glyphicon glyphicon-search">&nbsp;</span>Search User Accounts\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer('\n    <h2>Manage Users</h2>\n\n    <table class="table table-hover">\n        <thead>\n    \t<tr>\n    \t\t<th>ID</th>\n            <th>Name</th>\n            <th>User Name</th>\n            <th>Store</th>\n    \t</tr>\n        </thead>\n        <tbody>\n    \t<tr>\n    \t\t<td>1</td>\n            <td>Jim Adams</td>\n            <td>jadams13</td>\n            <td>Ogden</td>\n    \t</tr>\n    \t<tr>\n    \t\t<td>2</td>\n            <td>Carl Frandsen</td>\n            <td>carl.frandsen</td>\n            <td>Provo</td>\n    \t</tr>\n    \t<tr>\n    \t\t<td>3</td>\n            <td>Melanie Jones</td>\n            <td>Mel.Jones</td>\n            <td>Provo</td>\n    \t</tr>\n    \t<tr>\n    \t\t<td>4</td>\n            <td>Tim Carrigan</td>\n            <td>timcarrigan</td>\n            <td>Sandy</td>\n    \t</tr>\n        </tbody>\n    </table>\n    </br>\n\n    <div class="btn-group">\n\t  <div class="row">\n\t\t  <button class="btn btn-warning dropdown-toggle">\n\t\t    Edit\n\t\t  </button>\n\t\t  <button class="btn btn-success dropdown-toggle">\n\t\t    Save\n\t\t  </button>\n\t\t  <button class="btn btn-danger dropdown-toggle">\n\t\t    Delete\n\t\t  </button>\n\t  </div>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


