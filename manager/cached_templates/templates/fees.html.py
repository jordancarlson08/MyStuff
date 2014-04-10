# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397148678.743988
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/fees.html'
_template_uri = 'fees.html'
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
        skip = context.get('skip', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
 

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 39
        __M_writer('  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        skip = context.get('skip', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
 

        __M_writer('\r\n\r\n  <h2>Rental Fees</h2>\r\n  <hr/>\r\n  <br/>\r\n\r\n  <!-- Custom Form -->\r\n  <form class ="form-horizontal" role="form" method ="POST">\r\n  <div class=\'col-sm-offset-3\'>\r\n    ')
        # SOURCE LINE 13
        __M_writer(str(form.non_field_errors()))
        __M_writer('\r\n  </div>\r\n  <!--   Loop through the fields of the form -->\r\n')
        # SOURCE LINE 16
        for f in form:
            # SOURCE LINE 17
            if f.label not in skip:
                # SOURCE LINE 18
                __M_writer('      <div class="form-group">\r\n        <label class="col-sm-3 control-label" for="id_')
                # SOURCE LINE 19
                __M_writer(str( f.name ))
                __M_writer('">')
                __M_writer(str( f.label ))
                __M_writer('</label> <!-- the label -->\r\n          <div class="col-sm-5">\r\n            ')
                # SOURCE LINE 21
                __M_writer(str(f))
                __M_writer(' <!-- The input box -->\r\n            ')
                # SOURCE LINE 22
                __M_writer(str(f.errors))
                __M_writer('\r\n          </div>\r\n      </div>\r\n')
        # SOURCE LINE 27
        __M_writer('\r\n    <div class="form-group">\r\n      <div class="col-sm-offset-3 col-sm-4">\r\n        <input class="btn btn-success" type="submit" value="Checkout">\r\n      </div>\r\n    </div>\r\n  </form>\r\n\r\n\r\n  <div class="vertical_spacer6"></div>\r\n  <div class="vertical_spacer6"></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


