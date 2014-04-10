# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397155402.594666
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/searchstores.html'
_template_uri = 'searchstores.html'
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
        stores = context.get('stores', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 42
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        stores = context.get('stores', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n  <h2>Store Management</h2><hr/><br/>\n\n  <table class="table table-hover">\n  \t<thead>\n  \t\t<tr>\n  \t\t\t<th>Store</th>\n  \t\t\t<th>Street 1</th>\n        <th>Street 2</th>\n  \t\t\t<th>City</th>\n  \t\t\t<th>State</th>\n  \t\t\t<th>Zip Code</th>\n        <th>Phone</th>\n  \t\t</tr>\n  \t</thead>\n  \t<tbody>\n')
        # SOURCE LINE 22
        for s in stores:
            # SOURCE LINE 23
            __M_writer('      <tr class="clickableRow" href="/manager/stores/')
            __M_writer(str(s.id))
            __M_writer('">\n        <td>')
            # SOURCE LINE 24
            __M_writer(str(s.locationName))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 25
            __M_writer(str(s.street1))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 26
            __M_writer(str(s.street2))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 27
            __M_writer(str(s.city))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 28
            __M_writer(str(s.state))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 29
            __M_writer(str(s.zipCode))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 30
            __M_writer(str(s.phone))
            __M_writer('</td>\n      </tr>\n')
        # SOURCE LINE 33
        __M_writer('  \t</tbody>\n</table>\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


