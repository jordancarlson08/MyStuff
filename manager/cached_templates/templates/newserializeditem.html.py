# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397084405.494103
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/newserializeditem.html'
_template_uri = 'newserializeditem.html'
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(' ')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 33
        __M_writer('   ')
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
 

        __M_writer('\r\n\r\n  <h2>New Serialized Item</h2><hr/>\r\n\t</br>\r\n\r\n  <form class ="form-horizontal" role="form" method ="POST">\r\n\r\n')
        # SOURCE LINE 11
        for f in form:
            # SOURCE LINE 12
            __M_writer('\r\n      <div class="form-group">\r\n        <label class="col-sm-3 control-label" for="id_')
            # SOURCE LINE 14
            __M_writer(str( f.name ))
            __M_writer('">')
            __M_writer(str( f.label ))
            __M_writer('</label>\r\n          <div class="col-sm-6">\r\n            ')
            # SOURCE LINE 16
            __M_writer(str(f))
            __M_writer(' \r\n            ')
            # SOURCE LINE 17
            __M_writer(str(f.errors))
            __M_writer('\r\n          </div>\r\n      </div>\r\n\r\n')
        # SOURCE LINE 22
        __M_writer('\r\n    <div class="form-group">\r\n      <div class="col-sm-offset-3 col-sm-6">\r\n        <input class="btn btn-success" type="submit" value="Save">\r\n      </div>\r\n    </div>\r\n  </form>\r\n\r\n<div class=\'vertical_spacer6\'></div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


