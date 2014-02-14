# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1390367776.775571
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main']


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
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 59
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n \n<div class="content">\n\n<div class="row">\n  <div class="col-md-4">\n\n  </div>\n  <div class="col-md-4">\n  <h2>Login</h2>\n  </div>\n</div>\n<br/>\n  \n\t<form class="form-horizontal" role="form">\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Username/Email</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="Email">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputPassword3" class="col-sm-4 control-label">Password</label>\n    <div class="col-sm-4">\n      <input type="password" class="form-control" id="inputPassword3" placeholder="Password">\n    </div>\n  </div>\n  <div class="form-group">\n    <label for="inputPassword3" class="col-sm-4 control-label"></label>\n    <div class="col-sm-4">\n      <a href="/forgotpassword/">Forgot My Password?</a>\n    </div>\n  </div>\n  <div class="form-group">\n    <div class="col-sm-offset-4 col-sm-4">\n      <div class="checkbox">\n        <label>\n          <input type="checkbox"> Remember me\n        </label>\n      </div>\n    </div>\n  </div>\n  <div class="form-group">\n    <div class="col-sm-offset-4 col-sm-4">\n      <button type="submit" class="btn btn-primary">Sign in</button>\n      <button class="btn btn-success">Create Account</button>\n    </div>\n  </div>\n</form>\n\n</div>\n<div class="vertical_spacer6"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


