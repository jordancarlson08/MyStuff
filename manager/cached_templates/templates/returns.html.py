# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396755641.069908
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/returns.html'
_template_uri = 'returns.html'
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
    return runtime._inherit_from(context, 'searchstores.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rentalInfo_list = context.get('rentalInfo_list', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
 

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 45
        __M_writer('  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rentalInfo_list = context.get('rentalInfo_list', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
 

        __M_writer('\r\n\r\n  <h2>Rental Returns</h2>\r\n  <hr/>\r\n  <br/>\r\n\r\n  <table class="table table-hover">\r\n  \t<thead>\r\n  \t\t<tr>\r\n        <th>ID</th>\r\n  \t\t\t<th>Serial Number</th>\r\n  \t\t\t<th>Item</th>\r\n        <th>Customer</th>\r\n  \t\t\t<th>Date Out</th>\r\n        <th>Date Due</th>\r\n        <th></th>\r\n  \t\t</tr>\r\n  \t</thead>\r\n  \t<tbody>\r\n')
        # SOURCE LINE 23
        for r in rentalInfo_list:
            # SOURCE LINE 24
            __M_writer('      <tr>\r\n        <td>')
            # SOURCE LINE 25
            __M_writer(str(r.transaction.id))
            __M_writer('</td>\r\n        <td>')
            # SOURCE LINE 26
            __M_writer(str(r.item.serialNum))
            __M_writer('</td>\r\n        <td>')
            # SOURCE LINE 27
            __M_writer(str(r.item.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(r.item.catalogItem.name))
            __M_writer('</td>\r\n        <td>')
            # SOURCE LINE 28
            __M_writer(str(r.user.first_name))
            __M_writer(' ')
            __M_writer(str(r.user.last_name))
            __M_writer('</td>\r\n        <td>')
            # SOURCE LINE 29
            __M_writer(str(r.rental.dateOut))
            __M_writer('</td>\r\n')
            # SOURCE LINE 30
            if r.isLate == True: 
                # SOURCE LINE 31
                __M_writer('        <td><span class="label label-danger">')
                __M_writer(str(r.rental.dateDue))
                __M_writer("</span></td> \r\n        <td><a href='/manager/fees/")
                # SOURCE LINE 32
                __M_writer(str(r.rental.id))
                __M_writer("/late' ><button class='btn btn-warning btn-sm'><span class='glyphicon glyphicon-share'></span>&nbsp; Return</button></a></td>\r\n")
                # SOURCE LINE 33
            else:
                # SOURCE LINE 34
                __M_writer('        <td><span class="label label-success">')
                __M_writer(str(r.rental.dateDue))
                __M_writer("</span></td>\r\n        <td><a href='/manager/fees/")
                # SOURCE LINE 35
                __M_writer(str(r.rental.id))
                __M_writer("' ><button class='btn btn-warning btn-sm'><span class='glyphicon glyphicon-share'></span>&nbsp; Return</button></a></td>\r\n")
            # SOURCE LINE 37
            __M_writer('      </tr>\r\n')
        # SOURCE LINE 39
        __M_writer('  \t</tbody>\r\n</table>\r\n\r\n  <div class="vertical_spacer6"></div>\r\n  <div class="vertical_spacer6"></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


