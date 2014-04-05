# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396734001.592664
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main', 'top']


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
        def main():
            return render_main(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 46
        __M_writer('  \n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 48
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n\n\n\n<div class="background-image">\n<div class="custom1">\n\n  <h1>Welcome</h1>\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n  <a href="/catalog/search/" class="btn btn-primary btn-lg">View Catalog</a>\n\n')
        # SOURCE LINE 20
        if request.user.is_anonymous() == True:	
            # SOURCE LINE 21
            __M_writer('  \t<a id="login_button2" class="btn btn-success btn-lg">Log In</a>\n')
            # SOURCE LINE 22
        else:
            # SOURCE LINE 23
            __M_writer('\n')
            # SOURCE LINE 24
            if request.user.is_staff == False:
                # SOURCE LINE 25
                __M_writer('  \t<a class="btn btn-success btn-lg" href="/account/user/')
                __M_writer(str(request.user.id))
                __M_writer('">My Account</a>\n')
                # SOURCE LINE 26
            else:
                # SOURCE LINE 27
                __M_writer('  \t<a class="btn btn-success btn-lg" href="/manager/employee/')
                __M_writer(str(request.user.id))
                __M_writer('">My Account</a>\n')
            # SOURCE LINE 29
            __M_writer('\n\n')
        # SOURCE LINE 32
        __M_writer('\n</div>\n</div>\n\n\n\n\n\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n\n')
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


