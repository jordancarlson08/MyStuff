# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396927200.152463
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/base_manager.htm'
_template_uri = 'base_manager.htm'
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
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 94
        __M_writer('\r\n')
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
        __M_writer(' ')
 

        __M_writer('\r\n\r\n  <div class="container-fluid"> \r\n    <div class="row">\r\n\r\n      <div class="col-md-2 fixed-sidebar">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 82
        __M_writer(' \r\n      </div>\r\n\r\n      <div class="col-md-offset-2 col-md-10">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 88
        __M_writer('\r\n      </div>\r\n\r\n    </div>  \r\n  </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 86
        __M_writer(' ')
 

        __M_writer('\r\n          Site content goes here in sub-templates.\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(' ')
 

        __M_writer('\r\n          <p><h3>Manager Options</h3></p>\r\n                <div class="panel-group" id="accordion">\r\n                  <div class="panel panel-default">\r\n                    <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapseOne">\r\n                      <h4 class="panel-title">Inventory</h4>\r\n                    </div>\r\n                    <div id="collapseOne" class="panel-collapse collapse">\r\n                      <div class="panel-body">\r\n                        <ul class="list-unstyled">\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/searchinventory/\'>Search</a></li>\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/newcatalogitem\'>New Catalog Item</a></li>\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/newserializeditem/\'>New Serialized Item</a></li>\r\n                        </ul>\r\n                      </div><!--ends panel body-->\r\n                    </div><!--ends collapseOne-->\r\n                  </div><!--ends panel default-->\r\n                  <div class="panel panel-default">\r\n                    <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">\r\n                      <h4 class="panel-title">Users</h4>\r\n                    </div>\r\n                    <div id="collapseTwo" class="panel-collapse collapse">\r\n                      <div class="panel-body">\r\n                        <ul class="list-unstyled">\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/searchusers/\'>Search</a></li>\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/account/newuser\'>New User</a></li>\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/account/newemployee/\'>New Employee</a></li>\r\n                        </ul>\r\n                      </div><!--ends panel body-->\r\n                    </div><!--ends collapseTwo-->\r\n                  </div><!--ends panel default-->\r\n                  <div class="panel panel-default">\r\n                    <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapseThree">\r\n                      <h4 class="panel-title">Stores</h4>\r\n                    </div>\r\n                    <div id="collapseThree" class="panel-collapse collapse">\r\n                      <div class="panel-body">\r\n                        <ul class="list-unstyled">\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/searchstores/\'>Search</a></li>\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/newstore\'>New Store</a></li>\r\n                        </ul>\r\n                      </div><!--ends panel body-->\r\n                    </div><!--ends collapseThree-->\r\n                  </div><!--ends panel default-->\r\n                  <div class="panel panel-default">\r\n                    <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapseFour">\r\n                      <h4 class="panel-title">Rentals</h4>\r\n                    </div>\r\n                    <div id="collapseFour" class="panel-collapse collapse">\r\n                      <div class="panel-body">\r\n                        <ul class="list-unstyled">\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/searchinventory/\'>Search</a></li>\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/returns/\'>Returns</a></li>\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/laterentals/\'>Late Rentals</a></li>\r\n                        </ul>\r\n                      </div><!--ends panel body-->\r\n                    </div><!--ends collapseFour-->\r\n                  </div><!--ends panel default-->\r\n                  <div class="panel panel-default">\r\n                    <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapseFive">\r\n                      <h4 class="panel-title">Repairs</h4>\r\n                    </div>\r\n                    <div id="collapseFive" class="panel-collapse collapse">\r\n                      <div class="panel-body">\r\n                        <ul class="list-unstyled">\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/newrepair/\'>New Repairs</a></li>\r\n                          <li><a class=\'btn btn-default btn-block\' href=\'/manager/repairs/\'>Check Out</a></li>\r\n                        </ul>\r\n                      </div><!--ends panel body-->\r\n                    </div><!--ends collapseFive-->\r\n                  </div><!--ends panel default-->\r\n                </div><!--ends panel group and accordion-->\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


