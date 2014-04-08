# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396926926.756479
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/newcatalogitem.html'
_template_uri = 'newcatalogitem.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['shopping_cart_navigation_option', 'content']


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
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        # SOURCE LINE 3
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 40
        __M_writer('   ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shopping_cart_navigation_option(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(' ')
 

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\r\n')
        # SOURCE LINE 6
 

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shopping_cart_navigation_option'):
            context['self'].shopping_cart_navigation_option(**pageargs)
        

        # SOURCE LINE 7
        __M_writer(' \r\n\r\n<h2>New Catalog Item</h2><hr/>\r\n</br>\r\n\r\n<!-- Custom Form -->\r\n<form class ="form-horizontal" role="form" method ="POST" enctype="multipart/form-data">\r\n\r\n<!--   Loop through the fields of the form -->\r\n')
        # SOURCE LINE 16
        for f in form:
            # SOURCE LINE 17
            __M_writer('\r\n    <div class="form-group">\r\n      <label class="col-sm-3 control-label" for="id_')
            # SOURCE LINE 19
            __M_writer(str( f.name ))
            __M_writer('">')
            __M_writer(str( f.label ))
            __M_writer('</label> <!-- the label -->\r\n        <div class="col-sm-6">\r\n          ')
            # SOURCE LINE 21
            __M_writer(str(f))
            __M_writer(' <!-- The input box -->\r\n          ')
            # SOURCE LINE 22
            __M_writer(str(f.errors))
            __M_writer('\r\n        </div>\r\n    </div>\r\n\r\n')
        # SOURCE LINE 27
        __M_writer('\r\n  <div class="form-group">\r\n    <div class="col-sm-offset-3 col-sm-6">\r\n      <input class="btn btn-success" type="submit" value="Save">\r\n    </div>\r\n  </div>\r\n</form>\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


