# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396927147.569891
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/searchusers.html'
_template_uri = 'searchusers.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['shopping_cart_navigation_option', 'content']


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
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        emps = context.get('emps', UNDEFINED)
        user_list = context.get('user_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 95
        __M_writer('  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shopping_cart_navigation_option(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(' ')
 

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context)
        def content():
            return render_content(context)
        emps = context.get('emps', UNDEFINED)
        user_list = context.get('user_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n')
        # SOURCE LINE 5
 

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shopping_cart_navigation_option'):
            context['self'].shopping_cart_navigation_option(**pageargs)
        

        # SOURCE LINE 6
        __M_writer(' \r\n  <h2>User Management</h2>\r\n  <hr/>\r\n  <br/>\r\n\r\n  <ul class="nav nav-tabs">\r\n    <li class="active">\r\n      <a href="#Employee" data-toggle="tab"><strong>Employees</strong></a>\r\n    </li>\r\n    <li>\r\n      <a href="#User" data-toggle="tab"><strong>Users</strong></a>\r\n    </li>\r\n  </ul>\r\n\r\n\r\n  <div class="tab-content">\r\n\r\n    <div class="tab-pane active" id="Employee"><!-- Employee Tab -->\r\n      <div class="tab-content">\r\n\r\n        <table class="table table-hover">\r\n          <thead>\r\n            <tr>\r\n              <th>Role</th>\r\n              <th>Username</th>\r\n              <th>First Name</th>\r\n              <th>Last Name</th>\r\n              <th>Email</th>\r\n            </tr>\r\n          </thead>\r\n          <tbody>\r\n')
        # SOURCE LINE 37
        for u in emps:
            # SOURCE LINE 38
            __M_writer('            <tr class="clickableRow" href="/manager/employee/')
            __M_writer(str(u.user.id))
            __M_writer('">\r\n')
            # SOURCE LINE 39
            if u.user.is_superuser==True:
                # SOURCE LINE 40
                __M_writer('              <td><span class="label label-info">Admin</span></td>\r\n')
                # SOURCE LINE 41
            elif u.user.is_staff==True:
                # SOURCE LINE 42
                __M_writer('              <td><span class="label label-success">Manager</span></td>\r\n')
                # SOURCE LINE 43
            else:
                # SOURCE LINE 44
                __M_writer('              <td><span class="label label-danger">Employee</span></td>\r\n')
            # SOURCE LINE 46
            __M_writer('              <td>')
            __M_writer(str(u.user.username))
            __M_writer('</td>\r\n              <td>')
            # SOURCE LINE 47
            __M_writer(str(u.user.first_name))
            __M_writer('</td>\r\n              <td>')
            # SOURCE LINE 48
            __M_writer(str(u.user.last_name))
            __M_writer('</td>\r\n              <td>')
            # SOURCE LINE 49
            __M_writer(str(u.user.email))
            __M_writer('</td>\r\n            </tr>\r\n')
        # SOURCE LINE 52
        __M_writer('          </tbody>\r\n        </table>\r\n      </div>\r\n    </div><!--  End Employee Tab -->\r\n\r\n    <div class="tab-pane" id="User"><!-- User Tab -->\r\n      <div class="tab-content">\r\n\r\n        <table class="table table-hover">\r\n          <thead>\r\n            <tr>\r\n              <th>Username</th>\r\n              <th>First Name</th>\r\n              <th>Last Name</th>\r\n              <th>Email</th>\r\n            </tr>\r\n          </thead>\r\n          <tbody>\r\n')
        # SOURCE LINE 70
        for u in user_list:
            # SOURCE LINE 71
            __M_writer('            <tr class="clickableRow" href="/account/user/')
            __M_writer(str(u.id))
            __M_writer('">\r\n              <td>')
            # SOURCE LINE 72
            __M_writer(str(u.username))
            __M_writer('</td>\r\n              <td>')
            # SOURCE LINE 73
            __M_writer(str(u.first_name))
            __M_writer('</td>\r\n              <td>')
            # SOURCE LINE 74
            __M_writer(str(u.last_name))
            __M_writer('</td>\r\n              <td>')
            # SOURCE LINE 75
            __M_writer(str(u.email))
            __M_writer('</td>\r\n            </tr>\r\n')
        # SOURCE LINE 78
        __M_writer('          </tbody>\r\n        </table>\r\n      </div>\r\n    </div><!--  End User Tab -->\r\n\r\n\r\n\r\n\r\n\r\n\r\n  \r\n\r\n  <div class="vertical_spacer6"></div>\r\n  <div class="vertical_spacer6"></div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


