# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1395521619.086867
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/returnrentals.html'
_template_uri = 'returnrentals.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n<!-- could make this more beautiful if desired -->\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 210
        __M_writer('  \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer('\n  \n  <h2>Rental Returns</h2>\n  \n  <hr>\n  \n\n    <p class="text-center lead">Rental Items</p>\n      <div class="container-fluid">\n        \n        <div class="table-responsive">\n          <table class="table">\n          <thead>\n            <tr>\n              <th>T - ID</td>\n              <th>ID</td>\n              <th>Name</th>\n              <th>QTY</th>\n              <th>Price/Day</th>\n              <th>Value</th>\n              <th>Date Due</th>\n              <th>Date In</th>\n              <th>Duration</th>\n              \n              <th>Late Fees</th>\n              <th>Waived Fees</th>\n              <th>TOTAL</th>\n            </tr>\n          </thead>\n          <tr>\n            <td>1</td>\n            <td>2</td>\n            <td>Canon 550</td>\n            <td>1</td>\n            <td>$25.00</td>\n            <td>$787.50</td>\n            \n            <td>03/22/2014</td>\n            <td>03/25/2014</td>\n            <td>4d20h30min</td>\n            <td>$85.00</td>\n            <td>$ ~ </td>\n            <td>$161.50</td>\n          </tr>\n          <tr>\n            <td>1</td>\n            <td>3</td>\n            <td>Nikon 110</td>\n            <td>1</td>\n            <td>$30.00</td>\n            <td>$999.00</td>\n            \n            <td>03/25/2014</td>\n            <td>03/25/2014</td>\n            <td>4d20h30min</td>\n            <td>~</td>\n            <td>$ ~ </td>\n            <td>$150.00</td>\n          </tr>\n          <thead>\n            <tr>\n              <th> \n                \n                <!-- Button trigger modal -->\n                <button class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal">\n                  <span class="glyphicon glyphicon-hand-up"></span> Scan Rentals\n                </button>\n                \n              </td>\n              <th></th>\n              \n              <th></th>\n              <th></th>\n              <th></th>\n              <th></th>\n              <th></th>\n              <th></th>\n              <th></th>\n              <th></th>\n              <th>SUBTOTAL</th>\n              <th>$311.50</th>\n            </tr>\n          </thead>\n        </table>\n       \n\n        <!-- Modal -->\n        <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                <h4 class="modal-title" id="myModalLabel">Checkout Rental Items </h4>\n              </div>\n              <div class="modal-body">\n                <table class="table">\n                  <thead>\n                    <tr>\n                      <th>ID</td>\n                      <th>Name</th>\n                      <th>Condition</th>\n                 \n                      \n                    </tr>\n                  </thead>\n                  <tr>\n                    <td>CAN550</td>\n                    <td>Canon 550</td>\n                    <td>Good</td>\n                   \n                    \n                  </tr>\n                  <tr>\n                    <td>NIK110</td>\n                    <td>Nikon 110</td>\n                    <td>Used</td>\n                   \n                  </tr>\n                 \n                  \n                    \n                </table>\n                <button type="button" class="btn btn-info btn btn-block">Scan Rental</button>\n                \n              </div>\n              <div class="modal-footer">\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                <a href="#" class="btn btn btn-warning">Cancel</a>\n                <button type="button" class="btn btn-success">Save</button>\n              </div>\n            </div>\n          </div>\n        </div>\n        \n        \n  <div>\n  <div class="row">\n   <form class="navbar-form navbar-right" role="search">\n     <div class="form-group">\n      \n       <a href="#" class="btn btn-sm btn-warning"><span class="glyphicon glyphicon-usd"></span> Waive Late Fees</a>\n       <a href="#" class="btn btn-sm btn-danger"><span class="glyphicon glyphicon-thumbs-down"></span> Report Damage</a>\n       <a href="#" class="btn btn-sm btn-success"><span class="glyphicon glyphicon-star"></span> Accept Payment</a>\n       <a href="#" class="btn btn-sm btn-success"><span class="glyphicon glyphicon-send"></span> Email Receipt </a>\n       \n      \n     <!-- Modal -->\n     \n         \n     </div>\n     \n   </form>\n    </div>\n    </div></br>\n          \n         </br>\n             <p class="text-center lead">Aaron Nielsen - #A35921</p>\n         \n              <table class="table">\n                <thead>\n                  <tr>\n                    <th>ID</td>\n                    <th>Name</th>\n                    <th>Phone</th>\n                    <th>Email</th>\n                    <th>Start Date</th>\n                    <th>Expire Date</th>\n                    <th>Trial Membership?</th>\n                    <th>Holds?</th>\n                  </tr>\n                </thead>\n                <tr>\n                  <td>A35921</td>\n                  <td>Aaron Nielsen</td>\n                  <td>(801) 123-4567</td>\n                  <td>aanielsen@byu.edu</td>\n                  <td>01/01/14</td>\n                  <td>01/01/15</td>\n                  <td>N</td>\n                  <td>N</td>\n                </tr>\n              </table>\n           \n          </div>\n      </div>\n  <div>\n  <div class="row">\n   <form class="navbar-form navbar-right" role="search">\n     <div class="form-group">\n       \n       <a href="#" class="btn btn-sm btn-warning"><span class="glyphicon glyphicon-remove"></span> Place Hold</a>\n       \n      \n       \n     </div>\n     \n    \n     </div>\n    \n  </div>\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


