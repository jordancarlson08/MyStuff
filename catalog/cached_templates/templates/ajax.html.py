# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393371870.707695
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/ajax.html'
_template_uri = 'ajax.html'
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
        catItems = context.get('catItems', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        # SOURCE LINE 3
        __M_writer('\r\n')
        # SOURCE LINE 4
 

        __M_writer('\r\n')
        # SOURCE LINE 5
        for i in catItems:
            # SOURCE LINE 6
            __M_writer("\r\n  <li class='clickable'>\r\n    <a href='/catalog/inventory/")
            # SOURCE LINE 8
            __M_writer(str(i.id))
            __M_writer('\'>\r\n    <div class="panel panel-primary" >\r\n      <div class=\'panel-heading\'><h3><strong>')
            # SOURCE LINE 10
            __M_writer(str(i.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.name))
            __M_writer("</strong></h3></div>\r\n\r\n      <div class='panel-body'> <!-- panel body starts -->\r\n        \r\n        <ul class='list-inline'>\r\n\r\n          <li>\r\n\r\n            <!--####### Need to store image path in database as string for dynamic lookup -->\r\n\r\n            <img src='/static/catalog/images/NikonCamera.jpg' width='200px'/>\r\n          </li>\r\n          <li>\r\n            <ul class='list-unstyled'>\r\n              <li>\r\n                <strong>Price: $ ")
            # SOURCE LINE 25
            __M_writer(str(i.listPrice))
            __M_writer('</strong>\r\n              </li> \r\n              <li>\r\n                SKU: ')
            # SOURCE LINE 28
            __M_writer(str(i.sku))
            __M_writer('\r\n              </li>\r\n\r\n            </ul>\r\n\r\n            \r\n          </li>\r\n        </ul>\r\n\r\n      </div> <!-- panel body ends -->\r\n    </div> <!-- panel ends -->\r\n  </a>\r\n  </li> <!-- list item ends -->\r\n\r\n')
        # SOURCE LINE 43
        __M_writer('\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


