# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397248306.179853
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/inventory.html'
_template_uri = 'inventory.html'
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
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        stores_list = context.get('stores_list', UNDEFINED)
        conditions_list = context.get('conditions_list', UNDEFINED)
        form = context.get('form', UNDEFINED)
        item = context.get('item', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 320
        __M_writer('   \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rentals = context.get('rentals', UNDEFINED)
        def content():
            return render_content(context)
        stores_list = context.get('stores_list', UNDEFINED)
        conditions_list = context.get('conditions_list', UNDEFINED)
        form = context.get('form', UNDEFINED)
        item = context.get('item', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n')
        # SOURCE LINE 4
 

        __M_writer('\r\n\r\n<h1>')
        # SOURCE LINE 6
        __M_writer(str(item.manufacturer))
        __M_writer(' ')
        __M_writer(str(item.name))
        __M_writer('</h1><hr>\r\n\r\n<!--################# Initializing Tab Names, ETC #################-->\r\n\r\n<ul class="nav nav-tabs">\r\n  <li class="active">\r\n    <a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#inStock" data-toggle="tab"><strong>Serialized</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Rentals" data-toggle="tab"><strong>Rental</strong></a>\r\n  </li>\r\n</ul>\r\n\r\n<!--################# TABS #################-->\r\n\r\n<div class="tab-content">\r\n\r\n\r\n\r\n  <!--################# RENTAL TAB ##################-->\r\n  <div class="tab-pane" id="Rentals">\r\n    <div class="tab-content">\r\n      <div class="text-center">\r\n        <h3><strong>Rental Inventory</strong></h3>\r\n      </div>\r\n      <hr>\r\n\r\n      <!--TABLE-->\r\n      <table class="table table-hover">\r\n\r\n        <thead>\r\n          <tr>\r\n\r\n            <th>Store Name</th>\r\n            <th>Condition</th>\r\n            <th>Serial Number</th>\r\n            <th>Price/Day</th>\r\n            <th>Replacement Fee</th>\r\n            <th>Late Fee</th>\r\n            <th>Return Date</th>\r\n            <th></th>\r\n            <th></th>\r\n\r\n          </tr>\r\n\r\n\r\n\r\n        </thead>\r\n\r\n')
        # SOURCE LINE 58
        for r in rentals:
            # SOURCE LINE 59
            __M_writer('        <tr onclick="input" data-toggle="modal" href="#rental">\r\n          <td><span class=\'label label-primary\'>')
            # SOURCE LINE 60
            __M_writer(str(r.store))
            __M_writer('</span></td>\r\n          <td>')
            # SOURCE LINE 61
            __M_writer(str(r.condition.condition))
            __M_writer('</td>\r\n          <td>')
            # SOURCE LINE 62
            __M_writer(str(r.serialNum))
            __M_writer('</td>\r\n          <td>')
            # SOURCE LINE 63
            __M_writer(str(r.pricePerDay))
            __M_writer('</td>\r\n          <td>')
            # SOURCE LINE 64
            __M_writer(str(r.replacementFee))
            __M_writer('</td>\r\n          <td>')
            # SOURCE LINE 65
            __M_writer(str(r.lateFee))
            __M_writer('</td>\r\n          <td>')
            # SOURCE LINE 66
            __M_writer(str(r.created))
            __M_writer('</td>\r\n\r\n\r\n        </tr>\r\n')
        # SOURCE LINE 71
        __M_writer('\r\n\r\n\r\n      \r\n\r\n\r\n\r\n      </table>\r\n\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      \r\n      </div>\r\n\r\n  \t</div><!-- END RENTAL TAB -->\r\n\r\n    <!--################# SERIALIZED #################-->\r\n    <div class="tab-pane" id="inStock">\r\n      <div class="tab-content">\r\n        <div class="text-center">\r\n          <h3><strong>Serialized Items</strong></h3>\r\n        </div>\r\n\r\n        <hr>\r\n\r\n\r\n        <table class="table table-hover">\r\n          <thead>\r\n            <th>Store</th>\r\n            <th>Condition</th>\r\n            <th>Serial Number</th>\r\n            <th>List Price</th>\r\n            <th>Cost</th>\r\n            <th>Shelf Location</th>\r\n            <th>Date Received</th>\r\n            <th>Rental Item?</th>\r\n\r\n\r\n          </thead>\r\n          <tbody>\r\n            <tr>\r\n              <td>          \r\n                <select class="form-control">\r\n                  <option>All</option>\r\n')
        # SOURCE LINE 119
        for s in stores_list:
            # SOURCE LINE 120
            __M_writer('                  <option>')
            __M_writer(str(s.locationName))
            __M_writer('</option>\r\n')
        # SOURCE LINE 122
        __M_writer('                </select>\r\n              </td>\r\n              <td>\r\n                <select class="form-control">\r\n                  <option>All</option>\r\n')
        # SOURCE LINE 127
        for c in conditions_list:
            # SOURCE LINE 128
            __M_writer('                  <option>')
            __M_writer(str(c.condition))
            __M_writer('</option>\r\n')
        # SOURCE LINE 130
        __M_writer('                </select>\r\n              </td>\r\n              <td></td>\r\n              <td></td>\r\n              <td></td>\r\n              <td></td>\r\n              <td>\r\n                <select class="form-control">\r\n                  <option>All</option>\r\n                  <option>December</option>\r\n                  <option>January</option>\r\n                  <option>February</option>\r\n                </select>\r\n              </td>\r\n            </tr>\r\n\r\n\r\n')
        # SOURCE LINE 147
        for s in serial:
            # SOURCE LINE 148
            __M_writer("          <tr id='item_button_")
            __M_writer(str(s.id))
            __M_writer("'>        \r\n            <!-- The serialized items go here! in  a loop -->\r\n            <td><span class='label label-primary'>")
            # SOURCE LINE 150
            __M_writer(str(s.store))
            __M_writer('</span></td>\r\n            <td>')
            # SOURCE LINE 151
            __M_writer(str(s.condition.condition))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 152
            __M_writer(str(s.serialNum))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 153
            __M_writer(str(s.listPrice))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 154
            __M_writer(str(s.cost))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 155
            __M_writer(str(s.shelfLocation))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 156
            __M_writer(str(s.created))
            __M_writer('</td>\r\n')
            # SOURCE LINE 157
            if s.isRental ==True:
                # SOURCE LINE 158
                __M_writer('            <td>Yes</td>\r\n')
                # SOURCE LINE 159
            else:
                # SOURCE LINE 160
                __M_writer('            <td>No</td>\r\n')
            # SOURCE LINE 162
            __M_writer('          </tr>\r\n')
        # SOURCE LINE 164
        __M_writer('          </tbody>\r\n\r\n        </table>  \r\n        <div class=\'text-right\'>\r\n          <a href=\'/manager/newserializeditem/\' class=\'btn btn-primary btn-sm\'>Add Items</a>\r\n          \r\n        </div>\r\n      </div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n\r\n    </div> <!-- end serialized tab -->\r\n\r\n    <!--################# CATALOG #################-->\r\n    <div class="tab-pane active" id="Catalog">\r\n      <div class="tab-content">\r\n\r\n\r\n        <div class="text-center">\r\n          <h3><strong>Catalog Details</strong></h3>\r\n        </div>\r\n        <hr>\r\n\r\n        <table class="table table-hover">\r\n          <thead>\r\n            <tr>\r\n              <th>Category</th>\r\n              <th>SKU</th>\r\n              <th>List Price</th>\r\n              <th>Cost</th>\r\n              <th>Commission Rate</th>\r\n              <th>Lead Time</th>\r\n\r\n\r\n            </tr>\r\n          </thead>\r\n\r\n          <tr onclick="input" data-toggle="modal" href="#catalog">\r\n\r\n            <td>\r\n              <label>')
        # SOURCE LINE 207
        __M_writer(str(item.category.subName))
        __M_writer('</label>\r\n            </td>\r\n            <td>')
        # SOURCE LINE 209
        __M_writer(str(item.sku))
        __M_writer('</td>\r\n            <td>$ ')
        # SOURCE LINE 210
        __M_writer(str(item.listPrice))
        __M_writer('</td>\r\n            <td>$ ')
        # SOURCE LINE 211
        __M_writer(str(item.cost))
        __M_writer('</td>\r\n            <td>')
        # SOURCE LINE 212
        __M_writer(str(item.commissionRate))
        __M_writer('</td>\r\n            <td>')
        # SOURCE LINE 213
        __M_writer(str(item.leadTime))
        __M_writer('</td>\r\n\r\n\r\n          </tr>\r\n\r\n        </table>\r\n\r\n          <!-- Catalog Edit Button and Delete -->\r\n          <div class="modal fade bs-modal-lg" id="catalog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n            <div class="modal-dialog modal-lg">\r\n              <div class="modal-content">\r\n\r\n                <div class="modal-header">\r\n                  <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                  <h4 class="modal-title" id="myModalLabel">Edit Product Information</h4>\r\n                </div>\r\n\r\n                <div class="modal-body">\r\n\r\n\r\n                  <form class ="form-horizontal" role="form" method ="POST" enctype="multipart/form-data">\r\n\r\n')
        # SOURCE LINE 235
        for field in form:
            # SOURCE LINE 236
            __M_writer('\r\n                      <div class="form-group">\r\n                        <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 238
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\r\n                          <div class="col-sm-8">\r\n                            ')
            # SOURCE LINE 240
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\r\n                            <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 241
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\r\n                          </div>\r\n                      </div>\r\n\r\n')
        # SOURCE LINE 246
        __M_writer('                    \r\n                  </div>\r\n                  <div class ="modal-footer">\r\n                    <div class="form-group">\r\n                      <div class="col-sm-offset-7 col-sm-4">\r\n                        <input class="btn btn-success" type="submit" value="Save Changes">\r\n                      </div>\r\n                    </div>\r\n                  </form>\r\n\r\n                </div>\r\n\r\n\r\n              </div>\r\n              <!-- /.modal-content -->\r\n            </div>\r\n            <!-- /.modal-dialog -->\r\n          </div>\r\n          <!-- /.modal -->  \r\n\r\n\r\n\r\n        <br/>\r\n        <h3>Product Description</h3>\r\n        <hr>\r\n        <p>')
        # SOURCE LINE 271
        __M_writer(str(item.description))
        __M_writer('</p>\r\n\r\n\r\n        <br/>\r\n        <h3>Tech Specs</h3>\r\n        <hr/>\r\n        ')
        # SOURCE LINE 277
        __M_writer(str(item.techSpecs))
        __M_writer('\r\n\r\n\r\n\r\n        <hr/>\r\n        <br/>\r\n        <button class="btn btn-danger" data-toggle="modal" data-target="#Delete">Archive </button>\r\n\r\n        <!-- Modal -->\r\n        <div class="modal fade" id="Delete" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n          <div class="modal-dialog">\r\n            <div class="modal-content">\r\n\r\n              <div class="modal-header">\r\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                <h4 class="modal-title" id="myModalLabel">Delete Catalog Item</h4>\r\n              </div>\r\n\r\n              <div class="modal-body">\r\n                <h4>Are you sure you want to delete this item?</h4>  \r\n                <br/>\r\n                You will not be able to undo this action.\r\n              </div>\r\n\r\n              <div class="modal-footer">\r\n                <a href=\'/manager/inventory__delete/')
        # SOURCE LINE 302
        __M_writer(str(item.id))
        __M_writer('\' class=\'btn btn-danger\'>Delete</a>\r\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n              </div>\r\n            </div>\r\n            <!-- /.modal-content -->\r\n          </div>\r\n          <!-- /.modal-dialog -->\r\n        </div>\r\n        <!-- /.modal -->\r\n\r\n\r\n\r\n      </div>\r\n  \t</div>\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


