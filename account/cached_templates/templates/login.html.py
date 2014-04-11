# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397184439.786936
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'top']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 83
        __M_writer('  \r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 85
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n')
        # SOURCE LINE 4
 

        __M_writer('\r\n \r\n\r\n<br/>\r\n<div class="container-fluid">\r\n\r\n\r\n<form class ="form-horizontal" role="form" method ="POST" action=\'/account/login/\'>\r\n\r\n')
        # SOURCE LINE 13
        for f in form:
            # SOURCE LINE 14
            if f.name!='remember':
                # SOURCE LINE 15
                __M_writer('  <div class="row">\r\n    <div class="form-group">\r\n      <label class="col-md-3 control-label" for="id_')
                # SOURCE LINE 17
                __M_writer(str( f.name ))
                __M_writer('">')
                __M_writer(str( f.label ))
                __M_writer('</label>\r\n\r\n        <div class="col-md-7">\r\n          ')
                # SOURCE LINE 20
                __M_writer(str(f))
                __M_writer(' \r\n          \r\n          ')
                # SOURCE LINE 22
                __M_writer(str(f.errors))
                __M_writer(' \r\n        </div>\r\n    </div>\r\n  </div>\r\n')
        # SOURCE LINE 28
        __M_writer('\r\n  <div class="form-group">\r\n    <label for="inputPassword3" class="col-md-3 control-label"></label>\r\n    <div class="col-md-4">\r\n      <a href="/account/forgotpassword/">Forgot My Password?</a>\r\n    </div>\r\n  </div>\r\n\r\n')
        # SOURCE LINE 36
        for f in form:
            # SOURCE LINE 37
            if f.name=='remember':
                # SOURCE LINE 38
                __M_writer('    <div class="form-group">\r\n      <div class="col-md-offset-3 col-md-4">\r\n        <div class="checkbox">\r\n          <label>\r\n        ')
                # SOURCE LINE 42
                __M_writer(str(f))
                __M_writer(' \r\n          ')
                # SOURCE LINE 43
                __M_writer(str(f.errors))
                __M_writer(' Remember me\r\n          </label>\r\n         </div>\r\n      </div>\r\n    </div>\r\n')
        # SOURCE LINE 50
        __M_writer("\r\n<br/>\r\n\r\n<div class='row'>\r\n  <div class='col-md-3'>\r\n  </div>\r\n")
        # SOURCE LINE 56
        if form.non_field_errors():
            # SOURCE LINE 57
            __M_writer('  <div class=\'col-md-7\'>\r\n     <div class="alert alert-danger">\r\n       ')
            # SOURCE LINE 59
            __M_writer(str(form.non_field_errors()))
            __M_writer('\r\n      </div>\r\n  </div>\r\n')
        # SOURCE LINE 63
        __M_writer('</div>\r\n\r\n  <div class="form-group">\r\n    <div class="col-md-offset-3 col-md-8">\r\n\r\n      <ul class=\'list-inline\'>\r\n        <li><button id=\'submit_button\' class="btn btn-primary" type="submit">Sign In</button></li>\r\n        <li><a href="/account/newuser/" class="btn btn-success">Create Account</a></li>\r\n      </ul>\r\n\r\n    </div>\r\n  </div> \r\n</form>\r\n  \r\n  \r\n\r\n\r\n\r\n\r\n\r\n')
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


