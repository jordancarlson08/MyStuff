# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397227561.66615
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/manager/templates/repairs.html'
_template_uri = 'repairs.html'
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
        repairs = context.get('repairs', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        repairs = context.get('repairs', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n  <h2>Repairs</h2><hr/><br/>\n\n')
        # SOURCE LINE 9
        if repairs:
            # SOURCE LINE 10
            __M_writer('  <table class="table table-hover">\n  \t<thead>\n  \t\t<tr>\n  \t\t\t<th>ID</th>\n  \t\t\t<th>Item</th>\n        <th>Date Received</th>\n  \t\t\t<th>Est. Completion</th>\n  \t\t\t<th>Status</th>\n        <th>Mark as Complete</th>\n  \t\t</tr>\n  \t</thead>\n  \t<tbody>\n')
            # SOURCE LINE 22
            for r in repairs:
                # SOURCE LINE 23
                __M_writer('      <tr>\n        <td>')
                # SOURCE LINE 24
                __M_writer(str(r.id))
                __M_writer('</td>\n        <td>')
                # SOURCE LINE 25
                __M_writer(str(r.itemName))
                __M_writer('</td>\n        <td>')
                # SOURCE LINE 26
                __M_writer(str(r.dateStart))
                __M_writer('</td>\n        <td>')
                # SOURCE LINE 27
                __M_writer(str(r.estComplete))
                __M_writer('</td>\n        <td>')
                # SOURCE LINE 28
                __M_writer(str(r.status))
                __M_writer('</td>\n')
                # SOURCE LINE 29
                if r.dateComplete != None:
                    # SOURCE LINE 30
                    __M_writer("        <td>\n            <button id='complete_button_")
                    # SOURCE LINE 31
                    __M_writer(str(r.id))
                    __M_writer("' class='btn btn-default'>\n              <span class='glyphicon glyphicon-check'></span>\n            </button> \n          <button id='add_button_")
                    # SOURCE LINE 34
                    __M_writer(str(r.id))
                    __M_writer("' class='btn btn-warning'>\n            <span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Add to Cart\n          </button>\n        </td>\n")
                    # SOURCE LINE 38
                else:
                    # SOURCE LINE 39
                    __M_writer("        <td>\n            <button id='complete_button_")
                    # SOURCE LINE 40
                    __M_writer(str(r.id))
                    __M_writer("' class='btn btn-default'>\n              <span class='glyphicon glyphicon-unchecked'></span>\n            </button> \n          <button id='add_button_")
                    # SOURCE LINE 43
                    __M_writer(str(r.id))
                    __M_writer("' class='btn btn-warning'>\n            <span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Add to Cart\n          </button>\n        </td>\n")
                # SOURCE LINE 48
                __M_writer('      </tr>\n')
            # SOURCE LINE 50
            __M_writer('  \t</tbody>\n</table>\n\n')
            # SOURCE LINE 53
        else:
            # SOURCE LINE 54
            __M_writer('  <p>It looks like you don\'t have any active repairs at this time. Go find some work.</p>\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n')
        # SOURCE LINE 58
        __M_writer('\n<a href="/manager/repairs__email/" class=\'btn btn-primary\'>\n  <span class=\'glyphicon glyphicon-send\'></span>&nbsp; Send Notice of Completion\n</a> \n\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


