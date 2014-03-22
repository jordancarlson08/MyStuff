# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1395450924.051328
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/rental.html'
_template_uri = 'rental.html'
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
    return runtime._inherit_from(context, 'base_inventory.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 102
        __M_writer('   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n<h1>')
        # SOURCE LINE 6
        __M_writer(str(item.catalogItem.manufacturer))
        __M_writer(' ')
        __M_writer(str(item.catalogItem.name))
        __M_writer(' - ')
        __M_writer(str(item.serialNum))
        __M_writer('</h1><hr>\n\n\n        <div class="text-center">\n          <h3><strong>Rental Details</strong></h3>\n        </div>\n        <hr>\n\n        <table class="table">\n          <thead>\n            <tr>\n              <th>Category</th>\n              <th>Serial Number</th>\n              <th>Price/Day</th>\n              <th>Late Fee</th>\n              <th>Replacement Fee</th>\n              <th></th>\n              \n\n            </tr>\n          </thead>\n\n          <tr onclick="input" data-toggle="modal" href="#catalog">\n\n            <td>\n              <label>')
        # SOURCE LINE 31
        __M_writer(str(item.catalogItem.category.subName))
        __M_writer('</label>\n            </td>\n            <td>')
        # SOURCE LINE 33
        __M_writer(str(item.serialNum))
        __M_writer('</td>\n            <td>')
        # SOURCE LINE 34
        __M_writer(str(item.pricePerDay))
        __M_writer('</td>\n            <td>')
        # SOURCE LINE 35
        __M_writer(str(item.lateFee))
        __M_writer('</td>\n            <td>')
        # SOURCE LINE 36
        __M_writer(str(item.replacementFee))
        __M_writer('</td>\n            <td><button class=\'btn btn-warning btn-sm\'>Edit</button></td>\n\n\n          </tr>\n\n        </table>\n\n        <div class=\'vertical_spacer6\'></div>\n\n        <h3>Rental Status: <label class=\'label label-danger\'>Out for Rent</label>/<label class=\'label label-success\'>Available</label></h3>\n        <hr/>\n        <table class=\'table\'>\n          <thead>\n            <th>Cust. ID</th>\n            <th>Customer</th>\n            <th>Date Out</th>\n            <th>Expected Return</th>  \n          </thead>\n          <tbody>\n            <td>3</td>\n            <td>N. Ford</td>\n            <td>01/04/2014</td>\n            <td>01/07/2014</td>\n          </tbody>          \n        </table>\n        <button class=\'btn btn-danger\'>Return Item</button>/<button class=\'btn btn-success\'>Rent Item</button>\n        \n\n        <div class=\'vertical_spacer6\'></div>\n\n        <h3>Rental History</h3>\n        <hr/>\n\n        <table class="table table-hover">\n          <thead>\n            <tr>\n              <th>Customer</th>\n              <th>Date Out</th>\n              <th>Date In</th>\n              <th>Condition</th>\n              <th></th>           \n            </tr>\n          </thead>\n          <tbody>\n           <!--  %for h in history: -->\n            <tr class=\'clickableRow\' href=\'/manager/history/\'>\n              <td>J. Adams</td>\n              <td>12/30/2013</td>\n              <td>01/04/2014</td>\n              <td>Used - Like New</td>\n              <td><button class=\'btn btn-primary btn-sm\'>Details</button></td>\n            </tr>\n            <!-- %endfor -->\n          </tbody>\n        </table>\n\n\n\n\n      </div>\n  \t</div>\n</div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


