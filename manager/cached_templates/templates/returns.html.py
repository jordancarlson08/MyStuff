# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397226425.652804
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/manager/templates/returns.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rentalInfo_list = context.get('rentalInfo_list', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
 

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 46
        __M_writer('  \n')
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
 

        __M_writer('\n\n\n  <h2>Rental Returns</h2>\n  <hr/>\n  <br/>\n\n  <table class="table table-hover">\n  \t<thead>\n  \t\t<tr>\n        <th>ID</th>\n  \t\t\t<th>Serial Number</th>\n  \t\t\t<th>Item</th>\n        <th>Customer</th>\n  \t\t\t<th>Date Out</th>\n        <th>Date Due</th>\n        <th></th>\n  \t\t</tr>\n  \t</thead>\n  \t<tbody>\n')
        # SOURCE LINE 24
        for r in rentalInfo_list:
            # SOURCE LINE 25
            __M_writer('      <tr>\n        <td>')
            # SOURCE LINE 26
            __M_writer(str(r.transaction.id))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 27
            __M_writer(str(r.item.serialNum))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 28
            __M_writer(str(r.item.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(r.item.catalogItem.name))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 29
            __M_writer(str(r.user.first_name))
            __M_writer(' ')
            __M_writer(str(r.user.last_name))
            __M_writer('</td>\n        <td>')
            # SOURCE LINE 30
            __M_writer(str(r.rental.dateOut))
            __M_writer('</td>\n')
            # SOURCE LINE 31
            if r.isLate == True: 
                # SOURCE LINE 32
                __M_writer('        <td><span class="label label-danger">')
                __M_writer(str(r.rental.dateDue))
                __M_writer("</span></td> \n        <td><a href='/manager/fees/")
                # SOURCE LINE 33
                __M_writer(str(r.rental.id))
                __M_writer("/late' ><button class='btn btn-warning btn-sm'><span class='glyphicon glyphicon-share'></span>&nbsp; Return</button></a></td>\n")
                # SOURCE LINE 34
            else:
                # SOURCE LINE 35
                __M_writer('        <td><span class="label label-success">')
                __M_writer(str(r.rental.dateDue))
                __M_writer("</span></td>\n        <td><a href='/manager/fees/")
                # SOURCE LINE 36
                __M_writer(str(r.rental.id))
                __M_writer("' ><button class='btn btn-warning btn-sm'><span class='glyphicon glyphicon-share'></span>&nbsp; Return</button></a></td>\n")
            # SOURCE LINE 38
            __M_writer('      </tr>\n')
        # SOURCE LINE 40
        __M_writer('  \t</tbody>\n</table>\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


