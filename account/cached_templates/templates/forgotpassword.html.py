# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396928667.586933
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/forgotpassword.html'
_template_uri = 'forgotpassword.html'
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 50
        __M_writer('  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n')
        # SOURCE LINE 4
 

        __M_writer('\r\n\r\n<div class="content">\r\n\r\n<div class="row">\r\n  <div class="col-md-4">\r\n\r\n  </div>\r\n  <div class="col-md-4">\r\n  <h2>Login Help</h2>\r\n  <p>Enter your username below and we will send you an email so you can reset your password</p>\r\n  </div>\r\n</div>\r\n<br/>\r\n\r\n\r\n<form class ="form-horizontal" role="form" method ="POST">\r\n\r\n')
        # SOURCE LINE 22
        for f in form:
            # SOURCE LINE 23
            __M_writer('\r\n    <div class="form-group">\r\n      <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 25
            __M_writer(str( f.name ))
            __M_writer('">')
            __M_writer(str( f.label ))
            __M_writer('</label>\r\n        <div class="col-sm-4">\r\n          ')
            # SOURCE LINE 27
            __M_writer(str(f))
            __M_writer(' ')
            __M_writer(str(f.errors))
            __M_writer('\r\n        </div>\r\n    </div>\r\n\r\n')
        # SOURCE LINE 32
        __M_writer('\r\n  <div class="form-group">\r\n    <div class="col-sm-offset-4 col-sm-4">\r\n      <input id=\'reset_button\' class="btn btn-success" type="submit" value="Reset"> \r\n    </div>\r\n  </div>\r\n</form>\r\n\r\n<div class=\'row\'>\r\n  <div class=\'col-md-offset-4 col-md-5\'>\r\n    ')
        # SOURCE LINE 42
        __M_writer(str(form.non_field_errors()))
        __M_writer('\r\n  </div>\r\n</div>\r\n\r\n<div class="vertical_spacer6"></div>\r\n\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


