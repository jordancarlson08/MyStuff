# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396927126.388033
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/base_dash.htm'
_template_uri = 'base_dash.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main', 'content', 'adminOptions', 'title', 'left_side']


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
    return runtime._inherit_from(context, 'base_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main():
            return render_main(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def adminOptions():
            return render_adminOptions(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def left_side():
            return render_left_side(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        def content():
            return render_content(context)
        def adminOptions():
            return render_adminOptions(context)
        def title():
            return render_title(context)
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n\n  <div class="content"> \n    <div class="row">\n      <div class="col-md-3">\n        <div class="container"> \n\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 45
        __M_writer(' \n\n        </div>\n      </div>  \n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 38
        __M_writer('\n                    Site content goes here in sub-templates.\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_adminOptions(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def adminOptions():
            return render_adminOptions(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def adminOptions():
            return render_adminOptions(context)
        def title():
            return render_title(context)
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer('\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 12
        __M_writer('</br>\n            <div class="container bs-docs-container">\n              <div class="row">\n\n                <div class="col-md-3">\n                    <div class="bs-sidebar hidden-print" role="complementary">\n                      <ul class="nav bs-sidenav">\n                        <li>\n                          <a href="/Profile/">View/Edit Personal Profile</a>\n                        </li>\n                        <li>\n                          <a href="/managestore/">View Store Information</a>\n                        </li>      \n                        <li>\n                          <a href="/inventory/">Manage Inventory</a>\n                        </li>  \n                        <hr>\n                        <li>\n                          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'adminOptions'):
            context['self'].adminOptions(**pageargs)
        

        # SOURCE LINE 30
        __M_writer('\n                        </li>              \n                      </ul>\n                    </div>\n                  </div>\n\n                <div class="col-md-9" role="main">\n\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 40
        __M_writer('   \n                  \n                </div>\n              </div>  \n            </div>\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


