# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396974469.312604
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top', 'main']


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
    return runtime._inherit_from(context, 'base_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top():
            return render_top(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 54
        __M_writer('  \r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 56
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n')
        # SOURCE LINE 4
 

        __M_writer('\r\n\r\n')
        # SOURCE LINE 6
 
        from base_app.user_util import manager_check, employee_check
        
        isEmployee = employee_check(request.user)
        isManager = manager_check(request.user)
        
        
        
        # SOURCE LINE 12
        __M_writer('\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n\r\n\r\n<div class="background-image">\r\n<div class="custom1">\r\n\r\n  <h1>Welcome</h1>\r\n  <div class="vertical_spacer6"></div>\r\n  <div class="vertical_spacer6"></div>\r\n\r\n  <a href="/catalog/category/" class="btn btn-primary btn-lg">View Catalog</a>\r\n\r\n')
        # SOURCE LINE 28
        if request.user.is_anonymous() == True:	
            # SOURCE LINE 29
            __M_writer('  \t<a id="login_button2" class="btn btn-success btn-lg">Log In</a>\r\n')
            # SOURCE LINE 30
        else:
            # SOURCE LINE 31
            __M_writer('\r\n')
            # SOURCE LINE 32
            if isEmployee == False:
                # SOURCE LINE 33
                __M_writer('  \t<a class="btn btn-success btn-lg" href="/account/user/')
                __M_writer(str(request.user.id))
                __M_writer('">My Account</a>\r\n')
                # SOURCE LINE 34
            else:
                # SOURCE LINE 35
                __M_writer('  \t<a class="btn btn-success btn-lg" href="/manager/employee/')
                __M_writer(str(request.user.id))
                __M_writer('">My Account</a>\r\n')
            # SOURCE LINE 37
            __M_writer('\r\n\r\n')
        # SOURCE LINE 40
        __M_writer('\r\n</div>\r\n</div>\r\n\r\n\r\n\r\n\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


