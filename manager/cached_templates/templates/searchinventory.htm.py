# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396734528.075784
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/searchinventory.htm'
_template_uri = 'searchinventory.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'main']


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
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 110
        __M_writer('\r\n        Site content goes here in sub-templates.\r\n      ')
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
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n')
        # SOURCE LINE 5
 

        __M_writer('\r\n\r\n<div class="content">\r\n  <div class="row">\r\n    <div class="col-md-2">\r\n      <div class="bs-sidebar hidden-print" role="complementary">\r\n        <ul class="nav bs-sidenav">\r\n        <div class="btn-group">\r\n          <button class="btn btn-default btn dropdown-toggle" type="button" data-toggle="dropdown">\r\n            <span class="glyphicon glyphicon-tags"></span><span class="lead"> Inventory</span> <span class="caret"></span>\r\n          </button>\r\n          <ul class="dropdown-menu">\r\n            <ul class="nav nav-pills nav-stacked">\r\n                <li>\r\n                    <!--Inventory Management-->\r\n                   \r\n                    <a href="/manager/searchinventory/"><span class="glyphicon glyphicon-search"></span>\r\n                        <small>Search</small></a>\r\n                    <a href="/manager/newcatalogitem/"><span class="glyphicon glyphicon-new-window"></span>\r\n                        <small>New Catalog Item</small></a>\r\n                    <a href="/manager/newserializeditem/"><span class="glyphicon glyphicon-new-window"></span>\r\n                      <small>New Serialized Item</small></a>\r\n                    <a href="/manageinventory/"><span class="glyphicon glyphicon-star"></span>\r\n                    <small>Inventory Dashboard</small></a>\r\n\r\n                    <li class="divider"></li>\r\n\r\n                    <!--Overall Menu Items-->\r\n                    \r\n                    <li><a href="/managestores/"><span class="glyphicon glyphicon-tower"></span> \r\n                    <span class="lead"><small>Stores</small></span></a></li>\r\n                    <li><a href="/manageusers/"><span class="glyphicon glyphicon-user"></span> \r\n                    <span class="lead"><small>Users</small></span></a></li>\r\n                    <li><a href="/"><span class="glyphicon glyphicon-star"></span>\r\n                        <span class="lead"><small>Dashboard</small></span></a></li>\r\n                </li>\r\n            </ul>\r\n          </ul>\r\n        </div>\r\n\r\n        <br/>\r\n        <br/>\r\n\r\n\r\n        <li>\r\n        <form class="navbar-form" role="search">\r\n                <div class="input-group">\r\n                    <input type="text" class="form-control" placeholder="Search" name="srch-term" id="srch-term">\r\n                    <div class="input-group-btn">\r\n                        <button class="btn btn-default" type="submit"><i class="glyphicon glyphicon-search"></i></button>\r\n                    </div>\r\n                </div>\r\n                </form>\r\n        </li>\r\n\r\n        <br/>\r\n\r\n          <li><p>\r\n            Inventory Type\r\n            <select class="form-control">\r\n              <option>All</option>\r\n              <option>Catalog</option>\r\n              <option>In-Store</option>\r\n              <option>Rental</option>\r\n            </select>\r\n          </p></li>\r\n          <li><p>\r\n            Store\r\n            <select class="form-control">\r\n              <option>All</option>\r\n              <option>Sandy</option>\r\n              <option>Provo</option>\r\n              <option>Ogden</option>\r\n            </select>\r\n          </p></li>\r\n          <li><p>\r\n            Brand\r\n            <select class="form-control">\r\n              <option>All</option>\r\n              <option>Canon</option>\r\n              <option>Nikon</option>\r\n              <option>Sony</option>\r\n              <option>Samsung</option>\r\n              <option>Olympus</option>\r\n              <option>Kodak</option>\r\n            </select>\r\n          </p></li>\r\n          <li><p>\r\n            Category\r\n            <select class="form-control">\r\n              <option>All</option>\r\n              <option>Digital Cameras</option>\r\n              <option>Digital SLR Cameras</option>\r\n              <option>Lenses</option>\r\n              <option>Tripods</option>\r\n              <option>Bags & Case</option>\r\n              <option>Accessories</option>\r\n            </select>\r\n          </p></li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n\r\n      <div class="col-md-10" role="main">\r\n\r\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 112
        __M_writer('   ')
 

        __M_writer('         \r\n      </div>\r\n\r\n\r\n    </div>  \r\n    </div>\r\n    </div>\r\n    </div>  \r\n    </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


