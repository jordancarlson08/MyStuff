# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396929477.061098
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/newemployee.html'
_template_uri = 'newemployee.html'
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
    return runtime._inherit_from(context, 'base_manager.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 39
        __M_writer('   ')
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
 

        __M_writer('\n\n<h2>New Employee Account</h2><hr/>\n</br>\n\n<form class ="form-horizontal" role="form" method ="POST">\n\n')
        # SOURCE LINE 10
        for f in form:
            # SOURCE LINE 11
            __M_writer('\n')
            # SOURCE LINE 12
            if f.name == 'street1':
                # SOURCE LINE 13
                __M_writer('  <h3>Address</h3><hr/>\n')
            # SOURCE LINE 15
            __M_writer('\n\n    <div class="form-group">\n      <label class="col-sm-3 control-label" for="id_')
            # SOURCE LINE 18
            __M_writer(str( f.name ))
            __M_writer('">')
            __M_writer(str( f.label ))
            __M_writer('</label>\n        <div class="col-sm-6">\n          ')
            # SOURCE LINE 20
            __M_writer(str(f))
            __M_writer(' ')
            __M_writer(str(f.errors))
            __M_writer('\n        </div>\n    </div>\n\n')
        # SOURCE LINE 25
        __M_writer('\n  <div class="form-group">\n    <div class="col-sm-offset-3 col-sm-6">\n\n\n      <input class="btn btn-success" type="submit" value="Save">\n\n    </div>\n  </div>\n</form>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


