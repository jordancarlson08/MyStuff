# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397112866.671732
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/item.html'
_template_uri = 'item.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        s = context.get('s', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 31
        __M_writer('   \n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        s = context.get('s', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n\n\n<form class ="form-horizontal" role="form" method ="POST" action=\'/manager/item/')
        # SOURCE LINE 8
        __M_writer(str(s.id))
        __M_writer("'>\n")
        # SOURCE LINE 9
        for field in form:
            # SOURCE LINE 10
            __M_writer('\n\n      <div class="form-group">\n        <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 13
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n          <div class="col-sm-6">\n            ')
            # SOURCE LINE 15
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\n            <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 16
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\n          </div>\n      </div>\n\n')
        # SOURCE LINE 21
        __M_writer('\n    <div class="form-group">\n      <div class="col-sm-offset-4 col-sm-4">\n        <button id=\'submit_button\' class="btn btn-success" type="submit" >Save Changes</button>\n      </div>\n    </div>\n  </form>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


