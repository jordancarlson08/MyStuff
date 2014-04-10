# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397158813.614967
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/base_manager.htm'
_template_uri = 'base_manager.htm'
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def left_side():
            return render_left_side(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 91
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 83
        __M_writer(' ')
 

        __M_writer('\r\n          Site content goes here in sub-templates.\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(' ')
 

        __M_writer('\r\n\r\n        ')
        # SOURCE LINE 11

        from base_app.user_util import manager_check
        isManager = manager_check(request.user)
        
        
        # SOURCE LINE 14
        __M_writer('\r\n\r\n')
        # SOURCE LINE 16
        if isManager == True:
            # SOURCE LINE 17
            __M_writer("          <h4 class='extra-padding'>")
            __M_writer(str(request.user.first_name))
            __M_writer(' ')
            __M_writer(str(request.user.last_name))
            __M_writer('</h4>\r\n            <ul class="nav nav-sidebar">\r\n              <li><a href="/manager/dash/"><strong>Dashboard</strong></a></li>\r\n            </ul>\r\n\r\n            <ul class="nav nav-sidebar">\r\n              <li class="active"><a href="/manager/searchinventory/"><strong>Inventory</strong></a></li>\r\n              <li><a href="/manager/newcatalogitem/"> New Catalog Item</a></li>\r\n              <li><a href="/manager/newserializeditem/"> New Serialized Item</a></li>\r\n            </ul>\r\n            \r\n            <ul class="nav nav-sidebar">\r\n              <li class="active"><a href="/manager/searchusers/"><strong>Users</strong></a></li>\r\n              <li><a href="/account/newuser/"> New User</a></li>\r\n              <li><a href="/account/newemployee/"> New Employee</a></li>\r\n              <li><a href="/manager/commissions/"> Commissions</a></li>\r\n            </ul>\r\n\r\n            <ul class="nav nav-sidebar">\r\n              <li class="active"><a href="/manager/searchstores/"><strong>Stores</strong></a></li>\r\n              <li><a href="/manager/newstore/"> New Store</a></li>\r\n            </ul>\r\n\r\n            <ul class="nav nav-sidebar">\r\n              <li class="active"><a href="/manager/searchinventory/#Rental"><strong>Rentals</strong></a></li>\r\n              <li><a href="/manager/returns/"> Returns</a></li>\r\n              <li><a href="/manager/laterentals/"> Outstanding Rentals</a></li>\r\n            </ul>\r\n\r\n            <ul class="nav nav-sidebar">\r\n              <li class="active"><a href="/manager/repairs/"><strong>Repairs</strong></a></li>\r\n              <li><a href="/manager/newrepair/"> New Repair</a></li>\r\n              <li><a href="/manager/repairs/"> Checkout Repair</a></li>\r\n            </ul>\r\n')
            # SOURCE LINE 51
        else:
            # SOURCE LINE 52
            __M_writer("          <h4 class='extra-padding'>")
            __M_writer(str(request.user.first_name))
            __M_writer(' ')
            __M_writer(str(request.user.last_name))
            __M_writer('</h4>\r\n            <ul class="nav nav-sidebar">\r\n              <li><a href="/manager/dash/"><strong>Dashboard</strong></a></li>\r\n            </ul>\r\n            <ul class="nav nav-sidebar">\r\n              <li class="active"><a href="/manager/searchinventory/"><strong>Inventory</strong></a></li>\r\n              <li><a href="/manager/newserializeditem/"> New Serialized Item</a></li>\r\n            </ul>\r\n            \r\n            <ul class="nav nav-sidebar">\r\n              <li class="active"><a href="/manager/searchusers/"><strong>Users</strong></a></li>\r\n              <li><a href="/account/newuser/"> New User</a></li>\r\n            </ul>\r\n\r\n            <ul class="nav nav-sidebar">\r\n              <li class="active"><a href="/manager/searchinventory/#Rental"><strong>Rentals</strong></a></li>\r\n              <li><a href="/manager/returns/"> Returns</a></li>\r\n            </ul>\r\n\r\n            <ul class="nav nav-sidebar">\r\n              <li class="active"><a href="/manager/repairs/"><strong>Repairs</strong></a></li>\r\n              <li><a href="/manager/newrepair/"> New Repair</a></li>\r\n              <li><a href="/manager/repairs/"> Checkout Repair</a></li>\r\n            </ul>\r\n')
        # SOURCE LINE 77
        __M_writer('          </div>\r\n                \r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        def left_side():
            return render_left_side(context)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(' ')
 

        __M_writer('\r\n\r\n  <div class="container-fluid"> \r\n    <div class="row">\r\n      <div id=\'sidebar\' class="col-md-2 sidebar">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 79
        __M_writer(' \r\n      </div>\r\n\r\n      <div class="col-md-offset-2 col-md-10">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 85
        __M_writer('\r\n      </div>\r\n\r\n    </div>  \r\n  </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


