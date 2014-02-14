# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388986459.530745
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Code\\django-mako-plus-master\\calculator\\templates/calc__loadlog.html'
_template_uri = 'calc__loadlog.html'
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
    return runtime._inherit_from(context, 'base_ajax_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        calculations = context.get('calculations', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 15
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        calculations = context.get('calculations', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
        if calculations.count() == 0:
            # SOURCE LINE 5
            __M_writer('    The log is empty.\n    \n')
            # SOURCE LINE 7
        else:
            # SOURCE LINE 8
            __M_writer('    <ol id="calculation-log">\n')
            # SOURCE LINE 9
            for c in calculations:
                # SOURCE LINE 10
                __M_writer('        <li>')
                __M_writer(str( c ))
                __M_writer('</li>\n')
            # SOURCE LINE 12
            __M_writer('    </ol>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


