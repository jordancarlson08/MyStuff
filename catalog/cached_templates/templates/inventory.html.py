# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396812786.146086
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/inventory.html'
_template_uri = 'inventory.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'left_side']


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
        rental_count = context.get('rental_count', UNDEFINED)
        form = context.get('form', UNDEFINED)
        item_count = context.get('item_count', UNDEFINED)
        def left_side():
            return render_left_side(context._locals(__M_locals))
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 103
        __M_writer('   \r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 109
        __M_writer('   ')
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
        __M_writer('\r\n')
        # SOURCE LINE 4
 

        __M_writer('\r\n\r\n\r\n\r\n<h1>')
        # SOURCE LINE 8
        __M_writer(str(item.manufacturer))
        __M_writer(' ')
        __M_writer(str(item.name))
        __M_writer('</h1><hr>\r\n\r\n      <div class="tab-content">\r\n        <div class="text-center">\r\n          <h3><strong>Details</strong></h3>\r\n          <hr>\r\n          <ul class=\'list-inline\'>\r\n            <li>\r\n              <!--####### Need to store image path in database as string for dynamic lookup -->\r\n              <img id=\'img\' src=\'')
        # SOURCE LINE 17
        __M_writer(str(item.img))
        __M_writer('\' width=\'300px\'/>\r\n            </li>\r\n            <li>\r\n              <ul class=\'list-unstyled\'>\r\n                <li>\r\n                  <table class="table table-striped">\r\n                    <thead>\r\n                      <tr>\r\n                        <th>Category</th>\r\n                        <th>SKU</th>\r\n                        <th>List Price</th>\r\n                      </tr>\r\n                    </thead>\r\n                    <tr>\r\n                      <td>\r\n                        <label>')
        # SOURCE LINE 32
        __M_writer(str(item.category.subName))
        __M_writer('</label>\r\n                      </td>\r\n                      <td>')
        # SOURCE LINE 34
        __M_writer(str(item.sku))
        __M_writer('</td>\r\n                      <td>$ ')
        # SOURCE LINE 35
        __M_writer(str(item.listPrice))
        __M_writer("</td>\r\n                    </tr>\r\n                  </table>\r\n                </li>\r\n                <li>\r\n                  &nbsp;\r\n                </li>\r\n\r\n                <li>\r\n                  <form class='form-horizontal' role='form' method='POST'>\r\n                    <ul class='list-inline'>\r\n")
        # SOURCE LINE 46
        for f in form:
            # SOURCE LINE 47
            __M_writer('                      <li>\r\n                        <strong>')
            # SOURCE LINE 48
            __M_writer(str(f.label))
            __M_writer('</strong>\r\n                      </li>\r\n                      <li>\r\n                        ')
            # SOURCE LINE 51
            __M_writer(str(f))
            __M_writer('\r\n                      </li>\r\n')
        # SOURCE LINE 54
        __M_writer("                      <li>\r\n                        <a>\r\n                        <button id='add_button' class='btn btn-primary' type='submit'><span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Add to Cart</button>\r\n                        </a>\r\n                      </li>\r\n                    </ul>\r\n                  </form>\r\n                </li>\r\n                <li>\r\n                  &nbsp;\r\n                </li>\r\n                <ul class='list list-inline'>\r\n                  <li> <!-- #FixLater : Check if isSerial == false set it so its always in stock -->\r\n")
        # SOURCE LINE 67
        if item_count == 0:
            # SOURCE LINE 68
            __M_writer("                    <span class='label label-danger'>Out of Stock.</span>\r\n")
            # SOURCE LINE 69
        else:
            # SOURCE LINE 70
            __M_writer("                    <span class='label label-success'>In Stock.</span>\r\n")
        # SOURCE LINE 72
        __M_writer('                  </li>\r\n                  <li> <!-- #FixLater : Check if isSerial == false and dont show this if it does -->\r\n')
        # SOURCE LINE 74
        if rental_count == 0:
            # SOURCE LINE 75
            __M_writer("                    <span class='label label-danger'>No Rentals Available.</span>\r\n")
            # SOURCE LINE 76
        else:
            # SOURCE LINE 77
            __M_writer("                    <span class='label label-warning'>Rent Now.</span>\r\n")
        # SOURCE LINE 79
        __M_writer('                  </li>\r\n                </ul>\r\n\r\n              </ul>\r\n            </li>\r\n          </ul>\r\n      </div>\r\n\r\n        <br/>\r\n        <h3>Product Description</h3>\r\n        <hr>\r\n        <p>')
        # SOURCE LINE 90
        __M_writer(str(item.description))
        __M_writer('</p>\r\n\r\n        <br/>\r\n        <h3>Tech Specs</h3>\r\n        <hr/>\r\n        ')
        # SOURCE LINE 95
        __M_writer(str(item.techSpecs))
        __M_writer('\r\n        <hr>\r\n\r\n      </div>\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 106
        __M_writer('\r\n')
        # SOURCE LINE 107
 

        __M_writer("\r\n<a id='back_button' class='btn btn-default btn-small'><span class='glyphicon glyphicon-arrow-left'></span>&nbsp;Back</a>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


