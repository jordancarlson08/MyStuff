# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1392164668.816022
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/base_users.htm'
_template_uri = 'base_users.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left_side', 'content', 'main']


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
        def left_side():
            return render_left_side(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 129
        __M_writer('\n\n\n\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_side():
            return render_left_side(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer('\n            <div class="container bs-docs-container">\n              <div class="row">\n\n\n                <div class="col-md-2">\n                  <div class="bs-sidebar hidden-print" role="complementary">\n                    <ul class="nav bs-sidenav">\n                    <div class="btn-group">\n                      <button class="btn btn-default btn dropdown-toggle" type="button" data-toggle="dropdown">\n                        <span class="glyphicon glyphicon-user"></span><span class="lead"> Users</span> <span class="caret"></span>\n                      </button>\n                      <ul class="dropdown-menu">\n                        <ul class="nav nav-pills nav-stacked">\n                            <li>\n                                <!--User Management-->\n                               \n                                <a href="/manager/searchusers/"><span class="glyphicon glyphicon-search"></span>\n                                    <small>Search</small></a>\n                                <a href="/account/newemployee/"><span class="glyphicon glyphicon-new-window"></span>\n                                    <small>New User</small></a>\n                                <a href="/manageusers/"><span class="glyphicon glyphicon-home"></span>\n                                <small>User Dashboard</small></a>\n\n                                <li class="divider"></li>\n\n                                <!--Overall Menu Items-->\n                                \n                                <li><a href="/managestores/"><span class="glyphicon glyphicon-search"></span> \n                                <span class="lead"><small>Stores</small></span></a></li>\n                                <li><a href="/manageinventory/"><span class="glyphicon glyphicon-tags"></span> \n                                <span class="lead"><small> Inventory</small></span></a></li>\n                                <li><a href="/homepage/index/"><span class="glyphicon glyphicon-star"></span>\n                                    <span class="lead"><small>Dashboard</small></span></a></li>\n                            </li>\n                        </ul>\n                      </ul>\n                    </div>\n\n                        <!-- New Users Modal -->\n                               <!--Insert Courtneys Code Here -->\n\n                                <!-- Modal -->\n                                <div class="modal fade" id="DeleteUser" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n                                  <div class="modal-dialog">\n                                    <div class="modal-content">\n                                      <div class="modal-header">\n                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                                        <h4 class="modal-title" id="myModalLabel">Nikon  Deleted</h4>\n                                      </div>\n                                      <div class="modal-body">\n\n                                      <form role="form"> \n                                          <select class="form-control">\n                                            <option>For-Sale</option>\n                                            <option>In-Stock</option>\n                                            <option>Catalog</option>\n                                            <option>Rental</option>\n                                           </select>\n                                      </form>\n\n                                      <p class="lead"> Would you like to delete this user</p>\n\n                                     \n                                        \n                                      </div>\n                                      <div class="modal-footer">\n\n                                        <!-- Delete Rental Item -->\n                                        <button type="button" class="btn btn-danger" data-dismiss="modal">Save & Close</button>\n                                        \n                                      </div>\n                                    </div><!-- /.modal-content -->\n                                  </div><!-- /.modal-dialog -->\n                                </div><!-- /.modal -->\n\n                  </div>\n                </div>\n\n                <div class="col-md-9" role="main">\n\n                  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 118
        __M_writer('   \n                  \n                </div>\n              </div>  \n            </div>\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 92
        __M_writer('\n                  <ul class="nav nav-tabs">\n                    <li class="active"><a href="#Product" data-toggle="tab"><strong>In-Stock</strong></a></li>\n                    <li><a href="#Rentals" data-toggle="tab"><strong>Rental</strong></a></li>\n                    <li><a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a></li>\n                  </ul>\n\n                  <div class="tab-content">\n                    <div class="tab-pane active" id="Product">\n                        Product Class\n\n                    </div>\n                    <div class="tab-pane" id="Catalog">\n                        Catalog Class\n\n                    </div>\n\n                    <div class="tab-pane" id="Rentals">\n                        Rental Class\n\n                    </div>\n                    <script>\n                        $(function () {\n                            $(\'#myTab a:last\').tab(\'show\')\n                        })\n                    </script>\n                  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_side():
            return render_left_side(context)
        def content():
            return render_content(context)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n\n  <div class="content"> \n    <div class="row">\n      <div class="col-md-3">\n        <div class="container"> \n\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 123
        __M_writer(' \n\n        </div>\n      </div>  \n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


