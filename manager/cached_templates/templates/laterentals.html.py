# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396927891.733976
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/laterentals.html'
_template_uri = 'laterentals.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['shopping_cart_navigation_option', 'content']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        rental30_info_list = context.get('rental30_info_list', UNDEFINED)
        rental60_info_list = context.get('rental60_info_list', UNDEFINED)
        rental90_info_list = context.get('rental90_info_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 130
        __M_writer('  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shopping_cart_navigation_option(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(' ')
 

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context)
        def content():
            return render_content(context)
        rental30_info_list = context.get('rental30_info_list', UNDEFINED)
        rental60_info_list = context.get('rental60_info_list', UNDEFINED)
        rental90_info_list = context.get('rental90_info_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
 

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shopping_cart_navigation_option'):
            context['self'].shopping_cart_navigation_option(**pageargs)
        

        # SOURCE LINE 4
        __M_writer('\r\n\r\n  <h2>Outstanding Rentals</h2><hr/><br/>\r\n\r\n  <div class="panel-group" id="accordion">\r\n    <div class="panel panel-default">\r\n      <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapseOne">\r\n        <h4 class="panel-title">\r\n            30 Days\r\n        </h4>\r\n      </div>\r\n      <div id="collapseOne" class="panel-collapse collapse in">\r\n        <div class="panel-body">\r\n          <table class=\'table table-hover\'>\r\n            <thead>\r\n              <tr>\r\n                <th>Rental ID</th>\r\n                <th>Serial Number</th>\r\n                <th>Item</th>\r\n                <th>Customer</th>\r\n                <th>Date Out</th>\r\n                <th>Date Due</th>\r\n                <th>Days Late</th>\r\n              </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        # SOURCE LINE 30
        for r in rental30_info_list:
            # SOURCE LINE 31
            __M_writer('              <tr>\r\n                <td>')
            # SOURCE LINE 32
            __M_writer(str(r.rental.id))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 33
            __M_writer(str(r.item.serialNum))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 34
            __M_writer(str(r.item.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(r.item.catalogItem.name))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 35
            __M_writer(str(r.user.first_name))
            __M_writer(' ')
            __M_writer(str(r.user.last_name))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 36
            __M_writer(str(r.rental.dateOut))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 37
            __M_writer(str(r.rental.dateDue))
            __M_writer('</td> \r\n                <td>')
            # SOURCE LINE 38
            __M_writer(str(r.daysLate))
            __M_writer('</td>\r\n              </tr>\r\n')
        # SOURCE LINE 41
        __M_writer('            </tbody>\r\n          </table>\r\n        </div>\r\n      </div>\r\n    </div>\r\n    <div class="panel panel-default">\r\n      <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">\r\n        <h4 class="panel-title">\r\n            60 Days\r\n        </h4>\r\n      </div>\r\n      <div id="collapseTwo" class="panel-collapse collapse">\r\n        <div class="panel-body">\r\n          <table class=\'table table-hover\'>\r\n            <thead>\r\n              <tr>\r\n                <th>Rental ID</th>\r\n                <th>Serial Number</th>\r\n                <th>Item</th>\r\n                <th>Customer</th>\r\n                <th>Date Out</th>\r\n                <th>Date Due</th>\r\n                <th>Days Late</th>\r\n              </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        # SOURCE LINE 67
        for r in rental60_info_list:
            # SOURCE LINE 68
            __M_writer('              <tr>\r\n                <td>')
            # SOURCE LINE 69
            __M_writer(str(r.rental.id))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 70
            __M_writer(str(r.item.serialNum))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 71
            __M_writer(str(r.item.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(r.item.catalogItem.name))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 72
            __M_writer(str(r.user.first_name))
            __M_writer(' ')
            __M_writer(str(r.user.last_name))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 73
            __M_writer(str(r.rental.dateOut))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 74
            __M_writer(str(r.rental.dateDue))
            __M_writer('</td> \r\n                <td>')
            # SOURCE LINE 75
            __M_writer(str(r.daysLate))
            __M_writer('</td>\r\n              </tr>\r\n')
        # SOURCE LINE 78
        __M_writer('            </tbody>\r\n          </table>\r\n        </div>\r\n      </div>\r\n    </div>\r\n    <div class="panel panel-default">\r\n      <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapseThree">\r\n        <h4 class="panel-title">\r\n            90+ Days\r\n        </h4>\r\n      </div>\r\n      <div id="collapseThree" class="panel-collapse collapse">\r\n        <div class="panel-body">\r\n          <table class=\'table table-hover\'>\r\n            <thead>\r\n              <tr>\r\n                <th>Rental ID</th>\r\n                <th>Serial Number</th>\r\n                <th>Item</th>\r\n                <th>Customer</th>\r\n                <th>Date Out</th>\r\n                <th>Date Due</th>\r\n                <th>Days Late</th>\r\n              </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        # SOURCE LINE 104
        for r in rental90_info_list:
            # SOURCE LINE 105
            __M_writer('              <tr>\r\n                <td>')
            # SOURCE LINE 106
            __M_writer(str(r.rental.id))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 107
            __M_writer(str(r.item.serialNum))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 108
            __M_writer(str(r.item.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(r.item.catalogItem.name))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 109
            __M_writer(str(r.user.first_name))
            __M_writer(' ')
            __M_writer(str(r.user.last_name))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 110
            __M_writer(str(r.rental.dateOut))
            __M_writer('</td>\r\n                <td>')
            # SOURCE LINE 111
            __M_writer(str(r.rental.dateDue))
            __M_writer('</td> \r\n                <td>')
            # SOURCE LINE 112
            __M_writer(str(r.daysLate))
            __M_writer('</td>\r\n              </tr>\r\n')
        # SOURCE LINE 115
        __M_writer('            </tbody>\r\n          </table>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n  <br/>\r\n  <a href="/manager/laterentals__email/" class=\'btn btn-primary\'><span class=\'glyphicon glyphicon-send\'></span>&nbsp; Send Overdue Notice</a> #FixLater --- Jquery animate/ change text to "sent"\r\n\r\n  <div class="vertical_spacer6"></div>\r\n  <div class="vertical_spacer6"></div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


