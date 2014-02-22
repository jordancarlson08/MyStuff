# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1392956672.604883
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/searchinventory.html'
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
        catItems = context.get('catItems', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 70
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        catItems = context.get('catItems', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n\n<h2>Search for "Nikon"</h2>\n<hr/><br/>\n\n<div class=\'text-left\'>\n<ul class="list-inline">\n\n')
        # SOURCE LINE 14
        for i in catItems:
            # SOURCE LINE 15
            __M_writer('\n  <li class=\'clickable\'>\n    <a href=\'/homepage/index/\'>\n    <div class="panel panel-primary" >\n      <div class=\'panel-heading\'><h3><strong>')
            # SOURCE LINE 19
            __M_writer(str(i.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.name))
            __M_writer("</strong></h3></div>\n\n      <div class='panel-body'> <!-- panel body starts -->\n        \n        <ul class='list-inline'>\n\n          <li>\n\n            <!--####### Need to store image path in database as string for dynamic lookup -->\n\n            <img src='/static/catalog/images/NikonCamera.jpg' width='200px'/>\n          </li>\n          <li>\n            <ul class='list-unstyled'>\n              <li>\n                <strong>Price: $ ")
            # SOURCE LINE 34
            __M_writer(str(i.listPrice))
            __M_writer('</strong>\n              </li> \n              <li>\n                SKU: ')
            # SOURCE LINE 37
            __M_writer(str(i.sku))
            __M_writer('\n              </li>\n\n            </ul>\n\n            \n          </li>\n        </ul>\n\n      </div> <!-- panel body ends -->\n    </div> <!-- panel ends -->\n  </a>\n  </li> <!-- list item ends -->\n\n\n')
        # SOURCE LINE 53
        __M_writer('\n</ul>\n</div>\n\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n\n  <script>\n  jQuery(document).ready(function($) {\n        $(".clickableRow").click(function() {\n              window.document.location = $(this).attr("href");\n        });\n  });\n  </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


