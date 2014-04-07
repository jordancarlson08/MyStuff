# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396892643.546564
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/catalog/templates/inventory.html'
_template_uri = 'inventory.html'
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
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rental_count = context.get('rental_count', UNDEFINED)
        item_count = context.get('item_count', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 103
        __M_writer('   \n\n\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context)
        rental_count = context.get('rental_count', UNDEFINED)
        item_count = context.get('item_count', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n\n\n<h1>')
        # SOURCE LINE 8
        __M_writer(str(item.manufacturer))
        __M_writer(' ')
        __M_writer(str(item.name))
        __M_writer('</h1><hr>\n\n      <div class="tab-content">\n        <div class="text-center">\n          <h3><strong>Details</strong></h3>\n          <hr>\n          <ul class=\'list-inline\'>\n            <li>\n              <!--####### Need to store image path in database as string for dynamic lookup -->\n              <img id=\'img\' src=\'')
        # SOURCE LINE 17
        __M_writer(str(item.img))
        __M_writer('\' width=\'300px\'/>\n            </li>\n            <li>\n              <ul class=\'list-unstyled\'>\n                <li>\n                  <table class="table table-striped">\n                    <thead>\n                      <tr>\n                        <th>Category</th>\n                        <th>SKU</th>\n                        <th>List Price</th>\n                      </tr>\n                    </thead>\n                    <tr>\n                      <td>\n                        <label>')
        # SOURCE LINE 32
        __M_writer(str(item.category.subName))
        __M_writer('</label>\n                      </td>\n                      <td>')
        # SOURCE LINE 34
        __M_writer(str(item.sku))
        __M_writer('</td>\n                      <td>$ ')
        # SOURCE LINE 35
        __M_writer(str(item.listPrice))
        __M_writer("</td>\n                    </tr>\n                  </table>\n                </li>\n                <li>\n                  &nbsp;\n                </li>\n\n                <li>\n                  <form class='form-horizontal' role='form' method='POST'>\n                    <ul class='list-inline'>\n")
        # SOURCE LINE 46
        for f in form:
            # SOURCE LINE 47
            __M_writer('                      <li>\n                        <strong>')
            # SOURCE LINE 48
            __M_writer(str(f.label))
            __M_writer('</strong>\n                      </li>\n                      <li>\n                        ')
            # SOURCE LINE 51
            __M_writer(str(f))
            __M_writer('\n                      </li>\n')
        # SOURCE LINE 54
        __M_writer("                      <li>\n                        <a>\n                        <button id='add_button' class='btn btn-primary' type='submit'><span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Add to Cart</button>\n                        </a>\n                      </li>\n                    </ul>\n                  </form>\n                </li>\n                <li>\n                  &nbsp;\n                </li>\n                <ul class='list list-inline'>\n                  <li> <!-- #FixLater : Check if isSerial == false set it so its always in stock -->\n")
        # SOURCE LINE 67
        if item_count == 0:
            # SOURCE LINE 68
            __M_writer("                    <span class='label label-danger'>Out of Stock.</span>\n")
            # SOURCE LINE 69
        else:
            # SOURCE LINE 70
            __M_writer("                    <span class='label label-success'>In Stock.</span>\n")
        # SOURCE LINE 72
        __M_writer('                  </li>\n                  <li> <!-- #FixLater : Check if isSerial == false and dont show this if it does -->\n')
        # SOURCE LINE 74
        if rental_count == 0:
            # SOURCE LINE 75
            __M_writer("                    <span class='label label-danger'>No Rentals Available.</span>\n")
            # SOURCE LINE 76
        else:
            # SOURCE LINE 77
            __M_writer("                    <span class='label label-warning'>Rent Now.</span>\n")
        # SOURCE LINE 79
        __M_writer('                  </li>\n                </ul>\n\n              </ul>\n            </li>\n          </ul>\n      </div>\n\n        <br/>\n        <h3>Product Description</h3>\n        <hr>\n        <p>')
        # SOURCE LINE 90
        __M_writer(str(item.description))
        __M_writer('</p>\n\n        <br/>\n        <h3>Tech Specs</h3>\n        <hr/>\n        ')
        # SOURCE LINE 95
        __M_writer(str(item.techSpecs))
        __M_writer('\n        <hr>\n\n      </div>\n</div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


