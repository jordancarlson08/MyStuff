# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1395521553.441172
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/addrentals.html'
_template_uri = 'addrentals.html'
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
        __M_writer('\n<!-- could make this more beautiful if desired -->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 164
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
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
 

        __M_writer('\n\n  <h2>Checkout Rentals</h2>\n  \n  <hr>\n  \n  <div>\n  <div class="row">\n   <form class="navbar-form navbar-left" role="search">\n     <div class="form-group">\n       <input type="text" class="form-control" placeholder="Search Members">\n     </div>\n     <button type="submit" class="btn btn-default"><span class="glyphicon glyphicon-search"></span></button>\n     \n     <!-- Button trigger modal -->\n     <button class="btn btn-info btn" data-toggle="modal" data-target="#myModal">\n       New Member\n     </button>\n\n     <!-- Modal -->\n     <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n       <div class="modal-dialog">\n         <div class="modal-content">\n           <div class="modal-header">\n             <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n             <h4 class="modal-title" id="myModalLabel">New Member</h4>\n           </div>\n           <div class="modal-body">\n             This is where new member information will go and connect to a customer\n           </div>\n           <div class="modal-footer">\n             <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n             <button type="button" class="btn btn-primary">Create new member account</button>\n           </div>\n         </div>\n       </div>\n     </div>\n     \n   </form>\n    </div>\n    </div></br>\n    <p class="text-center lead">Aaron Nielsen - #A35921</p>\n      <div class="container-fluid">\n\n          <table class="table">\n            <thead>\n              <tr>\n                <th>ID</td>\n                <th>Name</th>\n                <th>Phone</th>\n                <th>Email</th>\n                <th>Start Date</th>\n                <th>Expire Date</th>\n                <th>Trial Membership?</th>\n                <th>Holds?</th>\n              </tr>\n            </thead>\n            <tr>\n              <td>A35921</td>\n              <td>Aaron Nielsen</td>\n              <td>(801) 123-4567</td>\n              <td>aanielsen@byu.edu</td>\n              <td>01/01/14</td>\n              <td>01/01/15</td>\n              <td>N</td>\n              <td>N</td>\n            </tr>\n          </table>\n         </br>\n             <p class="text-center lead">Rental Items</p>\n          <div class="table-responsive">\n            <table class="table">\n              <thead>\n                <tr>\n                  <th>ID</td>\n                  <th>Name</th>\n                  <th>Category</th>\n                  <th>Condition</th>\n                  <th>QTY</th>\n                  \n                  <th>Date Due</th>\n                  <th>Value</th>\n                  <th>Price/Day</th>\n                  \n                </tr>\n              </thead>\n              <tr>\n                <td>CAN550</td>\n                <td>Canon 550</td>\n                <td>Camera</td>\n                <td>Good</td>\n                <td>1</td>\n                \n                <td>\n                 <div class="input-append date form_datetime">\n                     <input size="8" type="text" value="" readonly>\n                     <span class="add-on"><i class="icon-th"></i></span>\n                 </div>\n \n                 <script type="text/javascript">\n                     $(".form_datetime").datetimepicker({\n                         format: "dd MM yyyy - hh:ii"\n                     });\n                 </script>\n                  \n                  \n                </td>\n                <td>$787.50</td>\n                <td>$25.00</td>\n              </tr>\n              <tr>\n                <td>NIK110</td>\n                <td>Nikon 110</td>\n                <td>Camera</td>\n                <td>Used</td>\n                <td>1</td>\n               \n                <td>03/27/2014</td>\n                <td>$989.50</td>\n                <td>$35.00</td>\n              </tr>\n              <thead>\n                <tr>\n                  <th>\n                  <a href="#" class="btn btn-xs btn-success"><span class="glyphicon glyphicon-hand-up"></span> Scan New Item</a>\n                  </td>\n                  <th></th>\n                  <th></th>\n                  <th></th>\n                  <th></th>\n                  <th></th>\n                  <th></th>\n                  <th>SUBTOTAL</th>\n                  <th>$250.00</th>\n                </tr>\n              </thead>\n            </table>\n           \n          </div>\n      </div>\n  <div>\n  <div class="row">\n   <form class="navbar-form navbar-right" role="search">\n     <div class="form-group">\n       <a href="#" class="btn btn-sm btn-danger"><span class="glyphicon glyphicon-trash"></span> Cancel</a>\n       <a href="#" class="btn btn-sm btn-warning">Email Confirmation <span class="glyphicon glyphicon-send"></span></a>\n       \n       <a href="#" class="btn btn-sm btn-primary">Reserve Rentals <span class="glyphicon glyphicon-lock"></span></a>\n       \n     </div>\n     \n    \n     </div>\n    \n  </div>\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


