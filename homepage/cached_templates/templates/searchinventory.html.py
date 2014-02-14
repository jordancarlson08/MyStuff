# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1390434252.022761
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/searchinventory.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 64
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n  <h2>Inventory Management</h2>\n\n  <table class="table table-hover">\n  \t<thead>\n  \t\t<tr>\n  \t\t\t<th>Inventory Type</th>\n  \t\t\t<th>Name</th>\n  \t\t\t<th>List Prices</th>\n  \t\t\t<th>Description</th>\n  \t\t\t<th>Category</th>\n  \t\t</tr>\n  \t</thead>\n  \t<tbody>\n      <tr>\n        <td><span class="label label-success">Catalog</span></td>\n        <td><a href="/inventory/">Nikon 1 v2 Camera</a></td>\n        <td>$799.00</td>\n        <td>...highest standard in digital SLR Photography. The Nikon 1 v2...</td>\n        <td>Digital SLR Cameras</td>\n      </tr>\n  \t\t<tr>\n  \t\t\t<td><span class="label label-success">Catalog</span></td>\n  \t\t\t<td>Canon Powershot A2500</td>\n  \t\t\t<td>$139.99</td>\n  \t\t\t<td>...new features to Powershot digital cameras. The DIGIC 4...</td>\n  \t\t\t<td>Digital Cameras</td>\n  \t\t</tr>\n  \t\t<tr>\n  \t\t\t<td><span class="label label-success">Catalog</span></td>\n  \t\t\t<td>Canon Powershot A1400</td>\n  \t\t\t<td>$109.99</td>\n  \t\t\t<td>...easy The PowerShot A1400 digital camera gives...</td>\n  \t\t\t<td>Digital Cameras</td>\n  \t\t</tr>\n  \t\t<tr>\n  \t\t\t<td><span class="label label-warning">Rental</span></td>\n  \t\t\t<td>Canon Powershot A1400</td>\n  \t\t\t<td>$109.99</td>\n  \t\t\t<td>...easy The PowerShot A1400 digital camera gives...</td>\n  \t\t\t<td>Digital Cameras</td>\n  \t\t</tr>\n  \t\t<tr>\n  \t\t\t<td><span class="label label-primary">In-Store</span></td>\n  \t\t\t<td>Canon Powershot A1400</td>\n  \t\t\t<td>$109.99</td>\n  \t\t\t<td>...easy The PowerShot A1400 digital camera gives...</td>\n  \t\t\t<td>Digital Cameras</td>\n  \t\t</tr>\n  \t</tbody>\n\n\n\n\n\n  </table>\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


