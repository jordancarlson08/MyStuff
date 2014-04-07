# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396888245.695214
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/catalog/templates/search.htm'
_template_uri = 'search.htm'
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
        brands = context.get('brands', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
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
        # SOURCE LINE 107
        __M_writer('\n        Site content goes here in sub-templates.\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        brands = context.get('brands', UNDEFINED)
        def content():
            return render_content(context)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n<div class="content">\n  <div class="row">\n    <div class="col-md-2">\n      <div class="bs-sidebar hidden-print" role="complementary">\n        <ul class="nav bs-sidenav">\n        <div class="btn-group">\n          <button class="btn btn-default btn dropdown-toggle" type="button" data-toggle="dropdown">\n            <span class="glyphicon glyphicon-tags"></span><span class="lead"> Inventory</span> <span class="caret"></span>\n          </button>\n          <ul class="dropdown-menu">\n            <ul class="nav nav-pills nav-stacked">\n                <li>\n                    <!--Inventory Management-->\n                   \n                    <a href="/manager/searchinventory/"><span class="glyphicon glyphicon-search"></span>\n                        <small>Search</small></a>\n                    <a href="/manager/newcatalogitem/"><span class="glyphicon glyphicon-new-window"></span>\n                        <small>New Catalog Item</small></a>\n                    <a href="/manager/newserializeditem/"><span class="glyphicon glyphicon-new-window"></span>\n                      <small>New Serialized Item</small></a>\n                    <a href="/manageinventory/"><span class="glyphicon glyphicon-star"></span>\n                    <small>Inventory Dashboard</small></a>\n\n                    <li class="divider"></li>\n\n                    <!--Overall Menu Items-->\n                    \n                    <li><a href="/managestores/"><span class="glyphicon glyphicon-tower"></span> \n                    <span class="lead"><small>Stores</small></span></a></li>\n                    <li><a href="/manageusers/"><span class="glyphicon glyphicon-user"></span> \n                    <span class="lead"><small>Users</small></span></a></li>\n                    <li><a href="/"><span class="glyphicon glyphicon-star"></span>\n                        <span class="lead"><small>Dashboard</small></span></a></li>\n                </li>\n            </ul>\n          </ul>\n        </div>\n\n        <br/>\n        <br/>\n\n\n          <li>\n            <div class="input-group">\n              <input type="text" class="form-control" placeholder=\'Search\'>\n              <span class="input-group-btn">\n                <button class="btn btn-default" type="submit"><span class="glyphicon glyphicon-search"></span></button>\n              </span>\n            </div><!-- /input-group -->\n\n          </li>\n\n        <br/>\n\n          <li><p>\n            Brand\n            <select id=\'brand\' class="form-control">\n              <option value=\'All\'>All</option>\n')
        # SOURCE LINE 65
        for i in brands:
            # SOURCE LINE 66
            __M_writer("              <option value='")
            __M_writer(str(i.manufacturer))
            __M_writer("'>")
            __M_writer(str(i.manufacturer))
            __M_writer('</option>\n')
        # SOURCE LINE 68
        __M_writer('            </select>\n          </p></li>\n          <li><p>\n            Inventory Type\n            <select class="form-control">\n              <option>All</option>\n              <option>Catalog</option>\n              <option>In-Store</option>\n              <option>Rental</option>\n            </select>\n          </p></li>\n          <li><p>\n            Store\n            <select class="form-control">\n              <option>All</option>\n              <option>Sandy</option>\n              <option>Provo</option>\n              <option>Ogden</option>\n            </select>\n          </p></li>\n          \n          <li><p>\n            Category\n            <select class="form-control">\n              <option>All</option>\n              <option>Digital Cameras</option>\n              <option>Digital SLR Cameras</option>\n              <option>Lenses</option>\n              <option>Tripods</option>\n              <option>Bags & Case</option>\n              <option>Accessories</option>\n            </select>\n          </p></li>\n        </ul>\n      </div>\n    </div>\n\n      <div class="col-md-10" role="main">\n\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 109
        __M_writer('   ')
 

        __M_writer('         \n      </div>\n\n\n    </div>  \n    </div>\n    </div>\n    </div>  \n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


