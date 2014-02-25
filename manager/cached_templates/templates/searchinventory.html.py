# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393364354.919369
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/searchinventory.html'
_template_uri = 'searchinventory.html'
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
    return runtime._inherit_from(context, 'searchinventory.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        catItems = context.get('catItems', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 41
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        catItems = context.get('catItems', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n\n  <h2>Inventory Management</h2><hr/><br/>\n\n  <table class="table table-hover">\n  \t<thead>\n  \t\t<tr>\n  \t\t\t<th>SKU</th>\n        <th>Manufacturer</th>\n        <th>Name</th>\n  \t\t\t<th>List Prices</th>\n        <th>Cost</th>\n  \t\t\t<th>Category</th>\n  \t\t</tr>\n  \t</thead>\n  \t<tbody>\n')
        # SOURCE LINE 22
        for i in catItems:
            # SOURCE LINE 23
            __M_writer('      <tr class="clickableRow" href="/manager/inventory/')
            __M_writer(str(i.id))
            __M_writer('">\n        <td>')
            # SOURCE LINE 24
            __M_writer(str(i.sku))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 25
            __M_writer(str(i.manufacturer))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 26
            __M_writer(str(i.name))
            __M_writer('</td>\n        <td>$ ')
            # SOURCE LINE 27
            __M_writer(str(i.listPrice))
            __M_writer('</td>        \n        <td>$ ')
            # SOURCE LINE 28
            __M_writer(str(i.cost))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 29
            __M_writer(str(i.categoryID.categoryName))
            __M_writer('</td>\n      </tr>\n')
        # SOURCE LINE 32
        __M_writer('  \t</tbody>\n  </table>\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


