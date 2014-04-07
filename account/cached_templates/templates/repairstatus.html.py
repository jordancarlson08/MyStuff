# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396892629.436706
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/repairstatus.html'
_template_uri = 'repairstatus.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        repairs = context.get('repairs', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 47
        __M_writer('  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        repairs = context.get('repairs', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n')
        # SOURCE LINE 5
 

        __M_writer('\r\n\r\n  <h2>Repair Status</h2><hr/><br/>\r\n\r\n')
        # SOURCE LINE 9
        if repairs:
            # SOURCE LINE 10
            __M_writer('  <table class="table table-hover">\r\n  \t<thead>\r\n  \t\t<tr>\r\n  \t\t\t<th>ID</th>\r\n  \t\t\t<th>Item</th>\r\n        <th>Date Received</th>\r\n  \t\t\t<th>Est. Completion</th>\r\n  \t\t\t<th>Status</th>\r\n\r\n  \t\t</tr>\r\n  \t</thead>\r\n  \t<tbody>\r\n')
            # SOURCE LINE 22
            for s in repairs:
                # SOURCE LINE 23
                __M_writer('      <tr>\r\n        <td>')
                # SOURCE LINE 24
                __M_writer(str(s.id))
                __M_writer('</td>\r\n        <td>')
                # SOURCE LINE 25
                __M_writer(str(s.itemName))
                __M_writer('</td>\r\n        <td>')
                # SOURCE LINE 26
                __M_writer(str(s.dateStart))
                __M_writer('</td>\r\n        <td>')
                # SOURCE LINE 27
                __M_writer(str(s.dateComplete))
                __M_writer('</td>\r\n        <td>')
                # SOURCE LINE 28
                __M_writer(str(s.status))
                __M_writer('</td>\r\n      </tr>\r\n')
            # SOURCE LINE 31
            __M_writer('  \t</tbody>\r\n</table>\r\n\r\n')
            # SOURCE LINE 34
        else:
            # SOURCE LINE 35
            __M_writer('  <p>It looks like you don\'t have any active repairs at this time. If you have any questions contact our repairs department at 1-800-555-5555</p>\r\n  <div class="vertical_spacer6"></div>\r\n  <div class="vertical_spacer6"></div>\r\n')
        # SOURCE LINE 39
        __M_writer('\r\n\r\n  <div class="vertical_spacer6"></div>\r\n  <div class="vertical_spacer6"></div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


