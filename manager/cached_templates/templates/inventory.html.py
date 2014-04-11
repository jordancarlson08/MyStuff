# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397236117.000586
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/manager/templates/inventory.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        serial = context.get('serial', UNDEFINED)
        form = context.get('form', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        stores_list = context.get('stores_list', UNDEFINED)
        conditions_list = context.get('conditions_list', UNDEFINED)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 458
        __M_writer('   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        serial = context.get('serial', UNDEFINED)
        form = context.get('form', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        stores_list = context.get('stores_list', UNDEFINED)
        conditions_list = context.get('conditions_list', UNDEFINED)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n<h1>')
        # SOURCE LINE 6
        __M_writer(str(item.manufacturer))
        __M_writer(' ')
        __M_writer(str(item.name))
        __M_writer('</h1><hr>\n\n<!--################# Initializing Tab Names, ETC #################-->\n\n<ul class="nav nav-tabs">\n  <li class="active">\n    <a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a>\n  </li>\n  <li>\n    <a href="#inStock" data-toggle="tab"><strong>Serialized</strong></a>\n  </li>\n  <li>\n    <a href="#Rentals" data-toggle="tab"><strong>Rental</strong></a>\n  </li>\n</ul>\n\n<!--################# TABS #################-->\n\n<div class="tab-content">\n\n\n\n  <!--################# RENTAL TAB ##################-->\n  <div class="tab-pane" id="Rentals">\n    <div class="tab-content">\n      <div class="text-center">\n        <h3><strong>Rental Inventory</strong></h3>\n      </div>\n      <hr>\n\n      <!--TABLE-->\n      <table class="table table-hover">\n\n        <thead>\n          <tr>\n\n            <th>Store Name</th>\n            <th>Condition</th>\n            <th>Serial Number</th>\n            <th>Price/Day</th>\n            <th>Replacement Fee</th>\n            <th>Late Fee</th>\n            <th>Return Date</th>\n            <th></th>\n            <th></th>\n\n          </tr>\n\n\n\n        </thead>\n\n')
        # SOURCE LINE 58
        for r in rentals:
            # SOURCE LINE 59
            __M_writer('        <tr onclick="input" data-toggle="modal" href="#rental">\n          <td><span class=\'label label-primary\'>')
            # SOURCE LINE 60
            __M_writer(str(r.store))
            __M_writer('</span></td>\n          <td>')
            # SOURCE LINE 61
            __M_writer(str(r.condition.condition))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 62
            __M_writer(str(r.serialNum))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 63
            __M_writer(str(r.pricePerDay))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 64
            __M_writer(str(r.replacementFee))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 65
            __M_writer(str(r.lateFee))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 66
            __M_writer(str(r.created))
            __M_writer('</td>\n\n\n        </tr>\n')
        # SOURCE LINE 71
        __M_writer('\n\n\n        <!-- Rental Edit Button and Delete -->\n        <div class="modal fade" id="rental" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                <h4 class="modal-title" id="myModalLabel">Nikon 1 V2 - Edit Rental Information</h4>\n              </div>\n              <div class="modal-body">\n\n\n                <div class="form-group">\n\n                  <p class="lead"><small>Rental Information</small>\n                  </p>\n                  <hr>\n\n                  <div class="form-group">\n                    <div class="col-sm-4">\n                    </div>\n\n                    <div class="col-sm-8">\n                      <label>\n                        <input type="checkbox" value="">Rental?</label>\n                    </div>\n                  </div>\n\n                  <br/>\n\n                  <div class="form-group">\n                    <label for="avgCost" class="col-sm-4 control-label">Price per Day</label>\n                    <div class="col-sm-8">\n                      <input type="avgCost" class="form-control" id="avgCost" placeholder="$25.75">\n                    </div>\n                  </div>\n\n                  <br/>\n\n                  <div class="form-group">\n                    <label for="avgCost" class="col-sm-4 control-label">Replacement Price</label>\n                    <div class="col-sm-8">\n                      <input type="avgCost" class="form-control" id="avgCost" placeholder="$799.00">\n                    </div>\n                  </div>\n\n                  <br/>\n\n                  <div class="form-group">\n                    <label for="avgCost" class="col-sm-4 control-label">Late Fee per Day</label>\n                    <div class="col-sm-8">\n                      <input type="avgCost" class="form-control" id="avgCost" placeholder="$7.75">\n                    </div>\n                  </div>\n\n\n                  <br/>\n\n\n                </div>\n                <!-- /.modal-body -->\n                <div class="modal-footer">\n                  <button type="button" class="btn btn-danger" data-dismiss="modal">Archive</button>\n\n                  <button type="button" class="btn btn-success" data-dismiss="modal">Save</button>\n                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                </div>\n              </div>\n              <!-- /.modal-content -->\n            </div>\n            <!-- /.modal-dialog -->\n          </div>\n          <!-- /.modal -->\n\n\n\n      </table>\n\n      <div class=\'vertical_spacer6\'></div>\n      <div class=\'vertical_spacer6\'></div>\n      <div class=\'vertical_spacer6\'></div>\n      <div class=\'vertical_spacer6\'></div>\n      <div class=\'vertical_spacer6\'></div>\n      <div class=\'vertical_spacer6\'></div>\n      \n      </div>\n\n  \t</div><!-- END RENTAL TAB -->\n\n    <!--################# SERIALIZED #################-->\n    <div class="tab-pane" id="inStock">\n      <div class="tab-content">\n        <div class="text-center">\n          <h3><strong>Serialized Items</strong></h3>\n        </div>\n\n        <hr>\n\n\n        <table class="table table-hover">\n          <thead>\n            <th>Store</th>\n            <th>Condition</th>\n            <th>Serial Number</th>\n            <th>List Price</th>\n            <th>Cost</th>\n            <th>Shelf Location</th>\n            <th>Date Received</th>\n            <th>Rental Item?</th>\n\n\n          </thead>\n          <tbody>\n            <tr>\n              <td>          \n                <select class="form-control">\n                  <option>All</option>\n')
        # SOURCE LINE 190
        for s in stores_list:
            # SOURCE LINE 191
            __M_writer('                  <option>')
            __M_writer(str(s.locationName))
            __M_writer('</option>\n')
        # SOURCE LINE 193
        __M_writer('                </select>\n              </td>\n              <td>\n                <select class="form-control">\n                  <option>All</option>\n')
        # SOURCE LINE 198
        for c in conditions_list:
            # SOURCE LINE 199
            __M_writer('                  <option>')
            __M_writer(str(c.condition))
            __M_writer('</option>\n')
        # SOURCE LINE 201
        __M_writer('                </select>\n              </td>\n              <td></td>\n              <td></td>\n              <td></td>\n              <td></td>\n              <td>\n                <select class="form-control">\n                  <option>All</option>\n                  <option>December</option>\n                  <option>January</option>\n                  <option>February</option>\n                </select>\n              </td>\n            </tr>\n\n\n')
        # SOURCE LINE 218
        for s in serial:
            # SOURCE LINE 219
            __M_writer("          <tr id='item_button_")
            __M_writer(str(s.id))
            __M_writer("'>        \n            <!-- The serialized items go here! in  a loop -->\n            <td><span class='label label-primary'>")
            # SOURCE LINE 221
            __M_writer(str(s.store))
            __M_writer('</span></td>\n            <td>')
            # SOURCE LINE 222
            __M_writer(str(s.condition.condition))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 223
            __M_writer(str(s.serialNum))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 224
            __M_writer(str(s.listPrice))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 225
            __M_writer(str(s.cost))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 226
            __M_writer(str(s.shelfLocation))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 227
            __M_writer(str(s.created))
            __M_writer('</td>\n')
            # SOURCE LINE 228
            if s.isRental ==True:
                # SOURCE LINE 229
                __M_writer('            <td>Yes</td>\n')
                # SOURCE LINE 230
            else:
                # SOURCE LINE 231
                __M_writer('            <td>No</td>\n')
            # SOURCE LINE 233
            __M_writer('          </tr>\n')
        # SOURCE LINE 235
        __M_writer('          </tbody>\n\n        </table>  \n        <div class=\'text-right\'>\n          <a href=\'/manager/newserializeditem/\' class=\'btn btn-primary btn-sm\'>Add Items</a>\n          \n        </div>\n      </div>\n      <div class=\'vertical_spacer6\'></div>\n      <div class=\'vertical_spacer6\'></div>\n      <div class=\'vertical_spacer6\'></div>\n      <div class=\'vertical_spacer6\'></div>\n      <div class=\'vertical_spacer6\'></div>\n\n    </div> <!-- end serialized tab -->\n\n    <!--################# CATALOG #################-->\n    <div class="tab-pane active" id="Catalog">\n      <div class="tab-content">\n\n\n        <div class="text-center">\n          <h3><strong>Catalog Details</strong></h3>\n        </div>\n        <hr>\n\n        <table class="table table-hover">\n          <thead>\n            <tr>\n              <th>Category</th>\n              <th>SKU</th>\n              <th>List Price</th>\n              <th>Cost</th>\n              <th>Commission Rate</th>\n              <th>Lead Time</th>\n\n\n            </tr>\n          </thead>\n\n          <tr onclick="input" data-toggle="modal" href="#catalog">\n\n            <td>\n              <label>')
        # SOURCE LINE 278
        __M_writer(str(item.category.subName))
        __M_writer('</label>\n            </td>\n            <td>')
        # SOURCE LINE 280
        __M_writer(str(item.sku))
        __M_writer('</td>\n            <td>$ ')
        # SOURCE LINE 281
        __M_writer(str(item.listPrice))
        __M_writer('</td>\n            <td>$ ')
        # SOURCE LINE 282
        __M_writer(str(item.cost))
        __M_writer('</td>\n            <td>')
        # SOURCE LINE 283
        __M_writer(str(item.commissionRate))
        __M_writer('</td>\n            <td>')
        # SOURCE LINE 284
        __M_writer(str(item.leadTime))
        __M_writer('</td>\n\n\n          </tr>\n\n        </table>\n\n          <!-- Catalog Edit Button and Delete -->\n          <div class="modal fade bs-modal-lg" id="catalog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n            <div class="modal-dialog modal-lg">\n              <div class="modal-content">\n\n                <div class="modal-header">\n                  <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                  <h4 class="modal-title" id="myModalLabel">Edit Product Information</h4>\n                </div>\n\n                <div class="modal-body">\n\n\n                  <form class ="form-horizontal" role="form" method ="POST" enctype="multipart/form-data">\n\n')
        # SOURCE LINE 306
        for field in form:
            # SOURCE LINE 307
            __M_writer('\n                      <div class="form-group">\n                        <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 309
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n                          <div class="col-sm-8">\n                            ')
            # SOURCE LINE 311
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\n                            <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 312
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\n                          </div>\n                      </div>\n\n')
        # SOURCE LINE 317
        __M_writer('                    \n                  </div>\n                  <div class ="modal-footer">\n                    <div class="form-group">\n                      <div class="col-sm-offset-7 col-sm-4">\n                        <input class="btn btn-success" type="submit" value="Save Changes">\n                      </div>\n                    </div>\n                  </form>\n\n                </div>\n\n\n              </div>\n              <!-- /.modal-content -->\n            </div>\n            <!-- /.modal-dialog -->\n          </div>\n          <!-- /.modal -->  \n\n\n\n\n\n        <ul class="nav nav-pills">\n\n          <li class="active">\n            <button class="btn btn-success btn" data-toggle="modal" data-target="#ImageLibrary">Image Library <span class="badge">1</span>\n            </button>\n          </li>\n\n\n        </ul>\n\n\n\n        <!-- Modal -->\n        <div class="modal fade" id="ImageLibrary" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                <h4 class="modal-title" id="myModalLabel">Modal title</h4>\n              </div>\n              <div class="modal-body">\n\n                <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\n                  <!-- Indicators -->\n                  <ol class="carousel-indicators">\n                    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\n                    <li data-target="#carousel-example-generic" data-slide-to="1"></li>\n                    <li data-target="#carousel-example-generic" data-slide-to="2"></li>\n                  </ol>\n\n                  <!-- Wrapper for slides -->\n                  <div class="carousel-inner">\n                    <div class="item active">\n                      <img src="')
        # SOURCE LINE 374
        __M_writer(str( STATIC_URL))
        __M_writer('base_app/images/NikonCamera.jpg" alt="Nikon Camera 1 V2" class="img-rounded">\n                      <div class="carousel-caption">\n                        IMG1.jpg\n                      </div>\n                    </div>\n                    ...\n                  </div>\n\n                  <!-- Controls -->\n                  <a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">\n                    <span class="glyphicon glyphicon-chevron-left"></span>\n                  </a>\n                  <a class="right carousel-control" href="#carousel-example-generic" data-slide="next">\n                    <span class="glyphicon glyphicon-chevron-right"></span>\n                  </a>\n                </div>\n\n\n              </div>\n              <div class="modal-footer">\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                <button type="button" class="btn btn-primary">Save changes</button>\n              </div>\n            </div>\n            <!-- /.modal-content -->\n          </div>\n          <!-- /.modal-dialog -->\n        </div>\n        <!-- /.modal -->\n\n\n\n        <br/>\n        <h3>Product Description</h3>\n        <hr>\n        <p>')
        # SOURCE LINE 409
        __M_writer(str(item.description))
        __M_writer('</p>\n\n\n        <br/>\n        <h3>Tech Specs</h3>\n        <hr/>\n        ')
        # SOURCE LINE 415
        __M_writer(str(item.techSpecs))
        __M_writer('\n\n\n\n        <hr/>\n        <br/>\n        <button class="btn btn-danger" data-toggle="modal" data-target="#Delete">Archive </button>\n\n        <!-- Modal -->\n        <div class="modal fade" id="Delete" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                <h4 class="modal-title" id="myModalLabel">Delete Catalog Item</h4>\n              </div>\n\n              <div class="modal-body">\n                <h4>Are you sure you want to delete this item?</h4>  \n                <br/>\n                You will not be able to undo this action.\n              </div>\n\n              <div class="modal-footer">\n                <a href=\'/manager/inventory__delete/')
        # SOURCE LINE 440
        __M_writer(str(item.id))
        __M_writer('\' class=\'btn btn-danger\'>Delete</a>\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n              </div>\n            </div>\n            <!-- /.modal-content -->\n          </div>\n          <!-- /.modal-dialog -->\n        </div>\n        <!-- /.modal -->\n\n\n\n      </div>\n  \t</div>\n</div>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


