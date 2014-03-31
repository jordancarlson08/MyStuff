# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1395947416.405979
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/login.html'
_template_uri = 'login.html'
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
        form = context.get('form', UNDEFINED)
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 91
        __M_writer('  \n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

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
        form = context.get('form', UNDEFINED)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n<div class="content">\n\n<div class="row">\n  <div class="col-md-4">\n\n  </div>\n  <div class="col-md-4">\n  <h2>Login</h2>\n  </div>\n</div>\n<br/>\n  \n<form class ="form-horizontal" role="form" method ="POST">\n\n\n')
        # SOURCE LINE 21
        for f in form:
            # SOURCE LINE 22
            if f.name!='remember':
                # SOURCE LINE 23
                __M_writer('    <div class="form-group">\n      <label class="col-sm-4 control-label" for="id_')
                # SOURCE LINE 24
                __M_writer(str( f.name ))
                __M_writer('">')
                __M_writer(str( f.label ))
                __M_writer('</label>\n\n        <div class="col-sm-3">\n          ')
                # SOURCE LINE 27
                __M_writer(str(f))
                __M_writer(' ')
                __M_writer(str(f.errors))
                __M_writer(' \n        </div>\n    </div>\n')
        # SOURCE LINE 32
        __M_writer("  <div class='col-md-4'>\n  </div>\n  <div class='col-md-5'>\n    ")
        # SOURCE LINE 35
        __M_writer(str(form.non_field_errors()))
        __M_writer('\n  </div>\n  <div class="form-group">\n    <label for="inputPassword3" class="col-sm-4 control-label"></label>\n    <div class="col-sm-4">\n      <a href="/account/forgotpassword/">Forgot My Password?</a>\n    </div>\n  </div>\n\n')
        # SOURCE LINE 44
        for f in form:
            # SOURCE LINE 45
            if f.name=='remember':
                # SOURCE LINE 46
                __M_writer('    <div class="form-group">\n      <div class="col-sm-offset-4 col-sm-4">\n        <div class="checkbox">\n          <label>\n        ')
                # SOURCE LINE 50
                __M_writer(str(f))
                __M_writer(' ')
                __M_writer(str(f.errors))
                __M_writer(' Remember me\n          </label>\n         </div>\n      </div>\n    </div>\n')
        # SOURCE LINE 57
        __M_writer('\n\n  <div class="form-group">\n    <div class="col-sm-offset-4 col-sm-4">\n\n\n      <input class="btn btn-primary" type="submit" value="Sign In">\n      <a href="/account/newuser/" class="btn btn-success">Create Account</a>\n    </div>\n  </div>\n</form>\n</div>\n\n<hr/>\n\n<div class="content">\n\n  <div class="row">\n    <div class="col-md-4"></div>\n    <div class="col-md-4">\n      <h2>Login with Facebook</h2>\n      <br/>\n      <fb:login-button show-faces="true" width="200" max-rows="1"></fb:login-button>\n    </div>\n  </div>\n</div>\n\n\n\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


