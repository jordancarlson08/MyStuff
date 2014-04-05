# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396734010.319633
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/base_inventory.htm'
_template_uri = 'base_inventory.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'main', 'left_side']


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
        def content():
            return render_content(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        def left_side():
            return render_left_side(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 3
 

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 80
        __M_writer('\n\n\n\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 65
        __M_writer('\n                        ')
        # SOURCE LINE 66
 

        __M_writer('\n                          <!--This is the content block, it should be overwritten. -->\n                          Content\n                      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def main():
            return render_main(context)
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n  ')
        # SOURCE LINE 6
 

        __M_writer('\n\n    <div class="content">\n      <div class="row">\n        <div class="col-md-3">\n          <div class="container">\n\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 74
        __M_writer('\n\n          </div>\n        </div>\n      </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer('\n              ')
        # SOURCE LINE 14
 

        __M_writer('\n                <div class="container bs-docs-container">\n                  <div class="row">\n\n\n                    <div class="col-md-2">\n                      <div class="bs-sidebar hidden-print" role="complementary">\n                        <ul class="nav bs-sidenav">\n                          <div class="btn-group">\n                            <button class="btn btn-default btn dropdown-toggle" type="button" data-toggle="dropdown">\n                              <span class="glyphicon glyphicon-tags"></span><span class="lead"> Inventory</span>  <span class="caret"></span>\n                            </button>\n                            <ul class="dropdown-menu">\n                              <ul class="nav nav-pills nav-stacked">\n                                <li>\n                                  <!--Inventory Management-->\n\n                                  <a href="/manager/searchinventory/"><span class="glyphicon glyphicon-search"></span>\n                                    <small>Search</small></a>\n                                  <a href="/manager/newcatalogitem/"><span class="glyphicon glyphicon-new-window"></span>\n                                    <small>New Catalog Item</small></a>\n                                  <a href="/manager/newserializeditem/"><span class="glyphicon glyphicon-new-window"></span>\n                                    <small>New Serialized Item</small></a>\n                                  <a href="/manageinventory/"><span class="glyphicon glyphicon-star"></span>\n                                <small>Inventory Dashboard</small></a>\n\n                                  <li class="divider"></li>\n\n                                  <!--Overall Menu Items-->\n\n                                  <li><a href="/managestores"><span class="glyphicon glyphicon-tower"></span> \n                                <span class="lead"><small>Stores</small></span></a>\n                                  </li>\n                                  <li><a href="/manageusers"><span class="glyphicon glyphicon-user"></span> \n                                <span class="lead"><small>Users</small></span></a>\n                                  </li>\n                                  <li><a href="/index/"><span class="glyphicon glyphicon-star"></span>\n                                    <span class="lead"><small>Dashboard</small></span></a>\n                                  </li>\n                                </li>\n                              </ul>\n                            </ul>\n                          </div>\n\n\n                          \n                      </div>\n                    </div>\n\n                    <div class="col-md-9" role="main">\n\n                      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 69
        __M_writer('\n\n                    </div>\n                  </div>\n                </div>\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


