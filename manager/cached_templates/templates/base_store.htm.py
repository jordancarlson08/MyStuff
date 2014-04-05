# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396734060.111186
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/base_store.htm'
_template_uri = 'base_store.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'left_side', 'main']


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
        def left_side():
            return render_left_side(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 149
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
        # SOURCE LINE 131
        __M_writer("\n                  \n                    <script>\n                        $(function () {\n                            $('#myTab a:last').tab('show')\n                        })\n                    </script>\n                  ")
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
        # SOURCE LINE 11
        __M_writer('\n            <div class="container bs-docs-container">\n              <div class="row">\n\n\n                <div class="col-md-2">\n                  <div class="bs-sidebar hidden-print" role="complementary">\n                    <ul class="nav bs-sidenav">\n                    <div class="btn-group">\n                      <button class="btn btn-default btn dropdown-toggle" type="button" data-toggle="dropdown">\n                        <span class="glyphicon glyphicon-tower"></span><span class="lead"> Stores</span> <span class="caret"></span>\n                      </button>\n                      <ul class="dropdown-menu">\n                        <ul class="nav nav-pills nav-stacked">\n                            <li>\n                                <!--Store Management-->\n                                <a href="/manager/searchstores/"><span class="glyphicon glyphicon-search"></span>\n                                    <small>Search</small></a>\n                                <a href="/manager/newstore/"><span class="glyphicon glyphicon-new-window"></span>\n                                    <small>New Store</small></a>\n\n                                <a href="/homepage/managestores/"><span class="glyphicon glyphicon-home"></span>\n                                <small>Store Dashboard</small></a>\n\n                                <li class="divider"></li>\n\n                                <!--Overall Menu Items-->\n                                \n                                <li><a href="/homepage/manageinventory"><span class="glyphicon glyphicon-tags"></span> \n                                <span class="lead"><small> Inventory</small></span></a></li>\n                                <li><a href="/homepage/manageusers"><span class="glyphicon glyphicon-user"></span> \n                                <span class="lead"><small>Users</small></span></a></li>\n                                <li><a href="/homepage/index/"><span class="glyphicon glyphicon-star"></span>\n                                    <span class="lead"><small>Dashboard</small></span></a></li>\n                            </li>\n                        </ul>\n                      </ul>\n\n\n\n                    </div>\n\n                        <!-- Modal -->\n                                <div class="modal fade" id="NewInventoryItem" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n                                  <div class="modal-dialog">\n                                    <div class="modal-content">\n                                      <div class="modal-header">\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                                        <h4 class="modal-title" id="myModalLabel">New Product</h4>\n                                      </div>\n                                      <div class="modal-body">\n\n                                      <form role="form">\n                                              <p>GUID: 456</p>\n                                              <div class="form-group">\n                                                <label for="exampleInput">Product Name:</label>\n                                                <input type="password" class="form-control" id="exampleInputName" placeholder="Ex. Nikon 123">\n                                              </div>\n                                              <div class="form-group">\n                                                <small>Profit Percentage: 12.09%</small>\n                                                <label for="exampleInput">Wholesale Price</label>\n                                                <input type="password" class="form-control" id="exampleInputWholesalePrice" placeholder="Ex. $799.00">\n                                              </div>\n                                              <div class="form-group">\n                                                <label for="exampleInput">Quantity In-Stock</label>\n                                                <input type="password" class="form-control" id="exampleInputWholesalePrice" placeholder="Ex. 12">\n                                              </div>\n                                              <div class="checkbox">\n                                                <label>\n                                                  <input type="checkbox"> Taxable?\n                                                </label>\n                                              </div>\n                                            </form>\n\n                                     \n                                        \n                                      </div>\n                                      <div class="modal-footer">\n\n                                        <!-- Delete Rental Item -->\n                                        <button type="button" class="btn btn-success" data-dismiss="modal">Cancel</button>\n                                        <button type="button" class="btn btn-success" data-dismiss="modal">Save & Close</button>\n\n                                        \n                                \n                                      </div>\n                                    </div><!-- /.modal-content -->\n                                  </div><!-- /.modal-dialog -->\n                                </div><!-- /.modal -->\n\n                                <!-- Modal -->\n                                <div class="modal fade" id="DeleteItem" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n                                  <div class="modal-dialog">\n                                    <div class="modal-content">\n                                      <div class="modal-header">\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                                        <h4 class="modal-title" id="myModalLabel">Nikon  Deleted</h4>\n                                      </div>\n                                      <div class="modal-body">\n\n                                      The Nikon 1 V2 Camera has been deleted.\n\n                                     \n                                        \n                                      </div>\n                                      <div class="modal-footer">\n\n                                        <!-- Delete Rental Item -->\n                                        <button type="button" class="btn btn-danger" data-dismiss="modal">Retrieve Deleted Item from Database</button>\n                                        \n                                      </div>\n                                    </div><!-- /.modal-content -->\n                                  </div><!-- /.modal-dialog -->\n                                </div><!-- /.modal -->\n\n                  </div>\n                </div>\n\n                <div class="col-md-9" role="main">\n\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 138
        __M_writer('   \n                  \n                </div>\n              </div>  \n            </div>\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def left_side():
            return render_left_side(context)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n\n  <div class="content"> \n    <div class="row">\n      <div class="col-md-2">\n        <div class="container"> \n\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 143
        __M_writer(' \n\n        </div>\n      </div>  \n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


