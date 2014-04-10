# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397168049.636792
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/manager/templates/searchusers.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        emps = context.get('emps', UNDEFINED)
        user_list = context.get('user_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 94
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        emps = context.get('emps', UNDEFINED)
        user_list = context.get('user_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n  <h2>User Management</h2>\n  <hr/>\n  <br/>\n\n  <ul class="nav nav-tabs">\n    <li class="active">\n      <a href="#Employee" data-toggle="tab"><strong>Employees</strong></a>\n    </li>\n    <li>\n      <a href="#User" data-toggle="tab"><strong>Users</strong></a>\n    </li>\n  </ul>\n\n\n  <div class="tab-content">\n\n    <div class="tab-pane active" id="Employee"><!-- Employee Tab -->\n      <div class="tab-content">\n\n        <table class="table table-hover">\n          <thead>\n            <tr>\n              <th>Role</th>\n              <th>Username</th>\n              <th>First Name</th>\n              <th>Last Name</th>\n              <th>Email</th>\n            </tr>\n          </thead>\n          <tbody>\n')
        # SOURCE LINE 36
        for u in emps:
            # SOURCE LINE 37
            __M_writer('            <tr class="clickableRow" href="/manager/employee/')
            __M_writer(str(u.user.id))
            __M_writer('">\n')
            # SOURCE LINE 38
            if u.user.is_superuser==True:
                # SOURCE LINE 39
                __M_writer('              <td><span class="label label-info">Admin</span></td>\n')
                # SOURCE LINE 40
            elif u.user.is_staff==True:
                # SOURCE LINE 41
                __M_writer('              <td><span class="label label-success">Manager</span></td>\n')
                # SOURCE LINE 42
            else:
                # SOURCE LINE 43
                __M_writer('              <td><span class="label label-danger">Employee</span></td>\n')
            # SOURCE LINE 45
            __M_writer('              <td>')
            __M_writer(str(u.user.username))
            __M_writer('</td>\n              <td>')
            # SOURCE LINE 46
            __M_writer(str(u.user.first_name))
            __M_writer('</td>\n              <td>')
            # SOURCE LINE 47
            __M_writer(str(u.user.last_name))
            __M_writer('</td>\n              <td>')
            # SOURCE LINE 48
            __M_writer(str(u.user.email))
            __M_writer('</td>\n            </tr>\n')
        # SOURCE LINE 51
        __M_writer('          </tbody>\n        </table>\n      </div>\n    </div><!--  End Employee Tab -->\n\n    <div class="tab-pane" id="User"><!-- User Tab -->\n      <div class="tab-content">\n\n        <table class="table table-hover">\n          <thead>\n            <tr>\n              <th>Username</th>\n              <th>First Name</th>\n              <th>Last Name</th>\n              <th>Email</th>\n            </tr>\n          </thead>\n          <tbody>\n')
        # SOURCE LINE 69
        for u in user_list:
            # SOURCE LINE 70
            __M_writer('            <tr class="clickableRow" href="/account/user/')
            __M_writer(str(u.id))
            __M_writer('">\n              <td>')
            # SOURCE LINE 71
            __M_writer(str(u.username))
            __M_writer('</td>\n              <td>')
            # SOURCE LINE 72
            __M_writer(str(u.first_name))
            __M_writer('</td>\n              <td>')
            # SOURCE LINE 73
            __M_writer(str(u.last_name))
            __M_writer('</td>\n              <td>')
            # SOURCE LINE 74
            __M_writer(str(u.email))
            __M_writer('</td>\n            </tr>\n')
        # SOURCE LINE 77
        __M_writer('          </tbody>\n        </table>\n      </div>\n    </div><!--  End User Tab -->\n\n\n\n\n\n\n  \n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


