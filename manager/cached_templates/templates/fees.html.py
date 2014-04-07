# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396906135.057288
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/manager/templates/fees.html'
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
    return runtime._inherit_from(context, 'searchstores.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
 

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 37
        __M_writer('  \n')
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
        # SOURCE LINE 4
 

        __M_writer('\n\n  <h2>Rental Fees</h2>\n  <hr/>\n  <br/>\n\n  <!-- Custom Form -->\n  <form class ="form-horizontal" role="form" method ="POST">\n\n  <!--   Loop through the fields of the form -->\n')
        # SOURCE LINE 14
        for f in form:
            # SOURCE LINE 15
            __M_writer('\n      <div class="form-group">\n        <label class="col-sm-3 control-label" for="id_')
            # SOURCE LINE 17
            __M_writer(str( f.name ))
            __M_writer('">')
            __M_writer(str( f.label ))
            __M_writer('</label> <!-- the label -->\n          <div class="col-sm-5">\n            ')
            # SOURCE LINE 19
            __M_writer(str(f))
            __M_writer(' <!-- The input box -->\n            ')
            # SOURCE LINE 20
            __M_writer(str(f.errors))
            __M_writer('\n          </div>\n      </div>\n\n')
        # SOURCE LINE 25
        __M_writer('\n    <div class="form-group">\n      <div class="col-sm-offset-3 col-sm-4">\n        <input class="btn btn-success" type="submit" value="Checkout">\n      </div>\n    </div>\n  </form>\n\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


