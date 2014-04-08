# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396927117.300988
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/base_profile.htm'
_template_uri = 'base_profile.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main', 'content', 'left_side']


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
        def left_side():
            return render_left_side(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 156
        __M_writer('\n\n\n\n                  ')
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
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n\n  <div class="content"> \n    <div class="row">\n      <div class="col-md-3">\n        <div class="container"> \n\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 150
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
        # SOURCE LINE 119
        __M_writer('\n                  <ul class="nav nav-tabs">\n                    <li class="active"><a href="#Product" data-toggle="tab"><strong>In-Stock</strong></a></li>\n                    <li><a href="#Rentals" data-toggle="tab"><strong>Rental</strong></a></li>\n                    <li><a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a></li>\n                  </ul>\n\n                  <div class="tab-content">\n                    <div class="tab-pane active" id="Product">\n                        Product Class\n\n                    </div>\n                    <div class="tab-pane" id="Catalog">\n                        Catalog Class\n\n                    </div>\n\n                    <div class="tab-pane" id="Rentals">\n                        Rental Class\n\n                    </div>\n                    <script>\n                        $(function () {\n                            $(\'#myTab a:last\').tab(\'show\')\n                        })\n                    </script>\n                  ')
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
        __M_writer('\n            <div class="container bs-docs-container">\n              <div class="row">\n\n\n                <div class="col-md-3">\n                  <div class="bs-sidebar hidden-print" role="complementary">\n                    <ul class="nav bs-sidenav">\n                    <div class="btn-group">\n                      <button class="btn btn-default btn dropdown-toggle" type="button" data-toggle="dropdown">\n                        <span class="lead">Inventory Mgmt</span> <span class="caret"></span>\n                      </button>\n                      <ul class="dropdown-menu">\n                        <ul class="nav nav-pills nav-stacked">\n                            <li>\n                                <a href="/searchinventory/"><span class="glyphicon glyphicon-search"></span> Search </a>\n                                <a href="/delete/" data-toggle="modal" data-target="#DeleteItem"><span class="glyphicon glyphicon-trash"></span> Delete </a>\n                                <a href="/save/" data-toggle="modal" data-target="#CatalogItem"><span class="glyphicon glyphicon-star"></span> New </a>\n                                </li>\n                            </ul>\n                      </ul>\n                    </div>\n\n                        <!-- Modal -->\n                                <div class="modal fade" id="CatalogItem" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n                                  <div class="modal-dialog">\n                                    <div class="modal-content">\n                                      <div class="modal-header">\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                                        <h4 class="modal-title" id="myModalLabel">New Product</h4>\n                                      </div>\n                                      <div class="modal-body">\n\n                                      <form role="form">\n                                              <p>GUID: 456</p>\n                                              <div class="form-group">\n                                                <label for="exampleInputPassword1">Product Name:</label>\n                                                <input type="password" class="form-control" id="exampleInputName" placeholder="Ex. Nikon 123">\n                                              </div>\n                                              <div class="form-group">\n                                                <label for="exampleInputPassword1">Wholesale Price</label>\n                                                <input type="password" class="form-control" id="exampleInputWholesalePrice" placeholder="Ex. $799.00">\n                                              </div>\n                                              <div class="form-group">\n                                                <label for="exampleInputPassword1">Quantity In-Stock</label>\n                                                <input type="password" class="form-control" id="exampleInputWholesalePrice" placeholder="Ex. 12">\n                                              </div>\n                                              <div class="checkbox">\n                                                <label>\n                                                  <input type="checkbox"> Taxable?\n                                                </label>\n                                              </div>\n                                            </form>\n\n                                     \n                                        \n                                      </div>\n                                      <div class="modal-footer">\n\n                                        <!-- Delete Rental Item -->\n                                        <button type="button" class="btn btn-success" data-dismiss="modal">Cancel</button>\n                                        <button type="button" class="btn btn-success" data-dismiss="modal">Save & Close</button>\n\n                                        \n                                \n                                      </div>\n                                    </div><!-- /.modal-content -->\n                                  </div><!-- /.modal-dialog -->\n                                </div><!-- /.modal -->\n\n                                <!-- Modal -->\n                                <div class="modal fade" id="DeleteItem" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n                                  <div class="modal-dialog">\n                                    <div class="modal-content">\n                                      <div class="modal-header">\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                                        <h4 class="modal-title" id="myModalLabel">Inventory Deleted</h4>\n                                      </div>\n                                      <div class="modal-body">\n\n                                      The Nikon 1 V2 Camera has been deleted.\n\n                                     \n                                        \n                                      </div>\n                                      <div class="modal-footer">\n\n                                        <!-- Delete Rental Item -->\n                                        <button type="button" class="btn btn-danger" data-dismiss="modal">Retrieve Deleted Item from Database</button>\n                                        \n                                      </div>\n                                    </div><!-- /.modal-content -->\n                                  </div><!-- /.modal-dialog -->\n                                </div><!-- /.modal -->\n\n\n\n\n\n\n\n\n\n                  </div>\n                </div>\n\n                <div class="col-md-9" role="main">\n\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 145
        __M_writer('   \n                  \n                </div>\n              </div>  \n            </div>\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


