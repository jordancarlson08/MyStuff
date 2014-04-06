# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396750674.797496
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
        def content():
            return render_content(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 75
        __M_writer('  \n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 77
        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n \n\n<br/>\n<div class="container-fluid">\n\n\n<form class ="form-horizontal" role="form" method ="POST" action=\'/account/login/\'>\n\n')
        # SOURCE LINE 13
        for f in form:
            # SOURCE LINE 14
            if f.name!='remember':
                # SOURCE LINE 15
                __M_writer('  <div class="row">\n    <div class="form-group">\n      <label class="col-md-3 control-label" for="id_')
                # SOURCE LINE 17
                __M_writer(str( f.name ))
                __M_writer('">')
                __M_writer(str( f.label ))
                __M_writer('</label>\n\n        <div class="col-md-7">\n          ')
                # SOURCE LINE 20
                __M_writer(str(f))
                __M_writer(' ')
                __M_writer(str(f.errors))
                __M_writer(' \n        </div>\n    </div>\n  </div>\n')
        # SOURCE LINE 26
        __M_writer('\n  <div class="form-group">\n    <label for="inputPassword3" class="col-md-3 control-label"></label>\n    <div class="col-md-4">\n      <a href="/account/forgotpassword/">Forgot My Password?</a>\n    </div>\n  </div>\n\n')
        # SOURCE LINE 34
        for f in form:
            # SOURCE LINE 35
            if f.name=='remember':
                # SOURCE LINE 36
                __M_writer('    <div class="form-group">\n      <div class="col-md-offset-3 col-md-4">\n        <div class="checkbox">\n          <label>\n        ')
                # SOURCE LINE 40
                __M_writer(str(f))
                __M_writer(' ')
                __M_writer(str(f.errors))
                __M_writer(' Remember me\n          </label>\n         </div>\n      </div>\n    </div>\n')
        # SOURCE LINE 47
        __M_writer('\n<br/>\n  <div class="form-group">\n    <div class="col-md-offset-3 col-md-8">\n\n      <ul class=\'list-inline\'>\n        <li><button id=\'submit_button\' class="btn btn-primary" type="submit">Sign In</button></li>\n        <li><a href="/account/newuser/" class="btn btn-success">Create Account</a></li>\n        <!-- <li><input type="submit" value="Submit" /></li> -->\n      </ul>\n\n    </div>\n  </div> \n</form>\n  \n  \n  <div class=\'row\'>\n    <div class=\'col-md-3\'>\n    </div>\n    <div class=\'col-md-5\'>\n      ')
        # SOURCE LINE 67
        __M_writer(str(form.non_field_errors()))
        __M_writer('\n    </div>\n\n  </div>\n\n\n\n\n')
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


