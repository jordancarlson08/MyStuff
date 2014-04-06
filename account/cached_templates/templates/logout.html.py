# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396750669.004695
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/logout.html'
_template_uri = 'logout.html'
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
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 33
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
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n<meta http-equiv="refresh" content="2;url=/index/">\n\n<div class=\'vertical_spacer6\'></div>\n<div class="content">\n\n<div class="row">\n  <div class="col-md-4">\n\n  </div>\n  <div class="col-md-4">\n    <div class=\'alert alert-success\'>\n      <h2>Sign-out Successful</h2>\n      <br/>\n      <p>You have successfully signed out of MyStuff\'s Central Authentication Service.</p>\n      <br/>\n    </div>\n  </div>\n</div>\n</div>\n\n\n\n<div class=\'vertical_spacer6\'></div>\n<div class=\'vertical_spacer6\'></div>\n\n  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


