# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1395439433.828835
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
        rental = context.get('rental', UNDEFINED)
        catItems = context.get('catItems', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 91
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rental = context.get('rental', UNDEFINED)
        catItems = context.get('catItems', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n\n <h2>Inventory Management</h2>\n<hr/>\n<br/>\n\n<ul class="nav nav-tabs">\n  <li class="active">\n    <a href="#Sale" data-toggle="tab"><strong>Sales Inventory</strong></a>\n  </li>\n  <li>\n    <a href="#Rental" data-toggle="tab"><strong>Rental Inventory</strong></a>\n  </li>\n</ul>\n\n<br/>\n<div class="tab-content">\n\n  <div class="tab-pane active" id="Sale">\n    <div class="tab-content">\n\n      <table class="table table-hover">\n        <thead>\n          <tr>\n            <th>SKU</th>\n            <th>Manufacturer</th>\n            <th>Name</th>\n            <th>List Prices</th>\n            <th>Cost</th>\n            <th>Category</th>\n          </tr>\n        </thead>\n        <tbody>\n')
        # SOURCE LINE 39
        for i in catItems:
            # SOURCE LINE 40
            __M_writer('          <tr class="clickableRow" href="/manager/inventory/')
            __M_writer(str(i.id))
            __M_writer('">\n            <td>')
            # SOURCE LINE 41
            __M_writer(str(i.sku))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 42
            __M_writer(str(i.manufacturer))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 43
            __M_writer(str(i.name))
            __M_writer('</td>\n            <td>$ ')
            # SOURCE LINE 44
            __M_writer(str(i.listPrice))
            __M_writer('</td>\n            <td>$ ')
            # SOURCE LINE 45
            __M_writer(str(i.cost))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 46
            __M_writer(str(i.category.subName))
            __M_writer('</td>\n          </tr>\n')
        # SOURCE LINE 49
        __M_writer('        </tbody>\n      </table>\n\n    </div>\n  </div>\n\n  <div class="tab-pane" id="Rental">\n    <div class="tab-content">\n      <table class="table table-hover">\n        <thead>\n          <tr>\n            <th>Serial Number</th>\n            <th>Manufacturer</th>\n            <th>Name</th>\n            <th>Price/Day</th>\n            <th>Replacement Fee</th>\n            <th>Category</th>\n          </tr>\n        </thead>\n        <tbody>\n')
        # SOURCE LINE 69
        for i in rental:
            # SOURCE LINE 70
            __M_writer('          <tr class="clickableRow" href="/manager/inventory/')
            __M_writer(str(i.catalogItem.id))
            __M_writer('">\n            <td>')
            # SOURCE LINE 71
            __M_writer(str(i.serialNum))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 72
            __M_writer(str(i.catalogItem.manufacturer))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 73
            __M_writer(str(i.catalogItem.name))
            __M_writer('</td>\n            <td>$ ')
            # SOURCE LINE 74
            __M_writer(str(i.pricePerDay))
            __M_writer('</td>\n            <td>$ ')
            # SOURCE LINE 75
            __M_writer(str(i.replacementFee))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 76
            __M_writer(str(i.catalogItem.category.subName))
            __M_writer('</td>\n          </tr>\n')
        # SOURCE LINE 79
        __M_writer('        </tbody>\n      </table>\n    </div>\n  </div>\n</div>\n\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


