# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391139158.442732
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/manageinventory.html'
_template_uri = 'manageinventory.html'
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
        

        # SOURCE LINE 30
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
        __M_writer('\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n\n\n\n<div class="background-image">\n<div class="custom1">\n\n  <h1>Inventory Management</h1>\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n  <a href="/manager/searchinventory/" class="btn btn-primary btn-lg">Inventory</a>\n  <a href="/manager/newcatalogitem/" class="btn btn-success btn-lg">New Catalog Item</a>\n  <a href="/manager/newinventoryitem/" class="btn btn-success btn-lg">New Store Item</a>\n\n\n</div>\n</div>\n\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


