# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393364362.628417
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/searchusers.html'
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
        emps = context.get('emps', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 50
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        emps = context.get('emps', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n  <h2>Employee Management</h2><hr/><br/>\n\n  <table class="table table-hover">\n  \t<thead>\n  \t\t<tr>\n        <th>Role</th>\n  \t\t\t<th>Username</th>\n  \t\t\t<th>First Name</th>\n  \t\t\t<th>Last Name</th>\n        <th>Email</th>\n  \t\t</tr>\n  \t</thead>\n  \t<tbody>\n')
        # SOURCE LINE 20
        for u in emps:
            # SOURCE LINE 21
            __M_writer('      <tr class="clickableRow" href="/manager/employee/')
            __M_writer(str(u.user.id))
            __M_writer('">\n')
            # SOURCE LINE 22
            if u.user.is_superuser==True:
                # SOURCE LINE 23
                __M_writer('        <td><span class="label label-info">Admin</span></td>\n')
                # SOURCE LINE 24
            elif u.user.is_staff==True:
                # SOURCE LINE 25
                __M_writer('        <td><span class="label label-success">Manager</span></td>\n')
                # SOURCE LINE 26
            else:
                # SOURCE LINE 27
                __M_writer('        <td><span class="label label-danger">Employee</span></td>\n')
            # SOURCE LINE 29
            __M_writer('\n        <td>')
            # SOURCE LINE 30
            __M_writer(str(u.user.username))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 31
            __M_writer(str(u.user.first_name))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 32
            __M_writer(str(u.user.last_name))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 33
            __M_writer(str(u.user.email))
            __M_writer('</td>\n      </tr>\n\n')
        # SOURCE LINE 37
        __M_writer('  \t</tbody>\n\n\n\n\n\n  </table>\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


