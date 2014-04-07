# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396843718.221968
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
    return runtime._inherit_from(context, 'base_inventory.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        conditions_list = context.get('conditions_list', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rentals = context.get('rentals', UNDEFINED)
        item = context.get('item', UNDEFINED)
        stores_list = context.get('stores_list', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 425
        __M_writer('   \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        conditions_list = context.get('conditions_list', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        def content():
            return render_content(context)
        rentals = context.get('rentals', UNDEFINED)
        item = context.get('item', UNDEFINED)
        stores_list = context.get('stores_list', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        __M_writer('\r\n\r\n\r\n        <!-- Rental Edit Button and Delete -->\r\n        <div class="modal fade" id="rental" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n          <div class="modal-dialog">\r\n            <div class="modal-content">\r\n              <div class="modal-header">\r\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                <h4 class="modal-title" id="myModalLabel">Nikon 1 V2 - Edit Rental Information</h4>\r\n              </div>\r\n              <div class="modal-body">\r\n\r\n\r\n                <div class="form-group">\r\n\r\n                  <p class="lead"><small>Rental Information</small>\r\n                  </p>\r\n                  <hr>\r\n\r\n                  <div class="form-group">\r\n                    <div class="col-sm-4">\r\n                    </div>\r\n\r\n                    <div class="col-sm-8">\r\n                      <label>\r\n                        <input type="checkbox" value="">Rental?</label>\r\n                    </div>\r\n                  </div>\r\n\r\n                  <br/>\r\n\r\n                  <div class="form-group">\r\n                    <label for="avgCost" class="col-sm-4 control-label">Price per Day</label>\r\n                    <div class="col-sm-8">\r\n                      <input type="avgCost" class="form-control" id="avgCost" placeholder="$25.75">\r\n                    </div>\r\n                  </div>\r\n\r\n                  <br/>\r\n\r\n                  <div class="form-group">\r\n                    <label for="avgCost" class="col-sm-4 control-label">Replacement Price</label>\r\n                    <div class="col-sm-8">\r\n                      <input type="avgCost" class="form-control" id="avgCost" placeholder="$799.00">\r\n                    </div>\r\n                  </div>\r\n\r\n                  <br/>\r\n\r\n                  <div class="form-group">\r\n                    <label for="avgCost" class="col-sm-4 control-label">Late Fee per Day</label>\r\n                    <div class="col-sm-8">\r\n                      <input type="avgCost" class="form-control" id="avgCost" placeholder="$7.75">\r\n                    </div>\r\n                  </div>\r\n\r\n\r\n                  <br/>\r\n\r\n\r\n                </div>\r\n                <!-- /.modal-body -->\r\n                <div class="modal-footer">\r\n                  <button type="button" class="btn btn-danger" data-dismiss="modal">Archive</button>\r\n\r\n                  <button type="button" class="btn btn-success" data-dismiss="modal">Save</button>\r\n                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n                </div>\r\n              </div>\r\n              <!-- /.modal-content -->\r\n            </div>\r\n            <!-- /.modal-dialog -->\r\n          </div>\r\n          <!-- /.modal -->\r\n\r\n\r\n\r\n      </table>\r\n\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      <div class=\'vertical_spacer6\'></div>\r\n      </div>\r\n\r\n  \t</div><!-- END RENTAL TAB -->\r\n\r\n    <!--################# SERIALIZED #################-->\r\n    <div class="tab-pane" id="inStock">\r\n      <div class="tab-content">\r\n        <div class="text-center">\r\n          <h3><strong>Serialized Items</strong></h3>\r\n        </div>\r\n\r\n        <hr>\r\n\r\n\r\n        <table class="table table-hover">\r\n          <thead>\r\n            <th>Store</th>\r\n            <th>Condition</th>\r\n            <th>Serial Number</th>\r\n            <th>List Price</th>\r\n            <th>Cost</th>\r\n            <th>Shelf Location</th>\r\n            <th>Date Received</th>\r\n            <th>Rental Item?</th>\r\n\r\n\r\n          </thead>\r\n          <tbody>\r\n            <tr>\r\n              <td>          \r\n                <select class="form-control">\r\n                  <option>All</option>\r\n')
        # SOURCE LINE 186
        for s in stores_list:
            # SOURCE LINE 187
            __M_writer('                  <option>')
            __M_writer(str(s.locationName))
            __M_writer('</option>\r\n')
        # SOURCE LINE 189
        __M_writer('                </select>\r\n              </td>\r\n              <td>\r\n                <select class="form-control">\r\n                  <option>All</option>\r\n')
        # SOURCE LINE 194
        for c in conditions_list:
            # SOURCE LINE 195
            __M_writer('                  <option>')
            __M_writer(str(c.condition))
            __M_writer('</option>\r\n')
        # SOURCE LINE 197
        __M_writer('                </select>\r\n              </td>\r\n              <td></td>\r\n              <td></td>\r\n              <td></td>\r\n              <td></td>\r\n              <td>\r\n                <select class="form-control">\r\n                  <option>All</option>\r\n                  <option>December</option>\r\n                  <option>January</option>\r\n                  <option>February</option>\r\n                </select>\r\n              </td>\r\n            </tr>\r\n\r\n\r\n')
        # SOURCE LINE 214
        for s in serial:
            # SOURCE LINE 215
            __M_writer("          <tr class='clickableRow' href='/manager/item/")
            __M_writer(str(s.id))
            __M_writer("'>        \r\n            <!-- The serialized items go here! in  a loop -->\r\n            <td><span class='label label-primary'>")
            # SOURCE LINE 217
            __M_writer(str(s.store))
            __M_writer('</span></td>\r\n            <td>')
            # SOURCE LINE 218
            __M_writer(str(s.condition.condition))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 219
            __M_writer(str(s.serialNum))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 220
            __M_writer(str(s.listPrice))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 221
            __M_writer(str(s.cost))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 222
            __M_writer(str(s.shelfLocation))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 223
            __M_writer(str(s.created))
            __M_writer('</td>\r\n')
            # SOURCE LINE 224
            if s.isRental ==True:
                # SOURCE LINE 225
                __M_writer('            <td>Yes</td>\r\n')
                # SOURCE LINE 226
            else:
                # SOURCE LINE 227
                __M_writer('            <td>No</td>\r\n')
            # SOURCE LINE 229
            __M_writer('          </tr>\r\n')
        # SOURCE LINE 231
        __M_writer('          </tbody>\r\n\r\n        </table>  \r\n        <div class=\'text-right\'>\r\n          <a href=\'/manager/newserializeditem/\' class=\'btn btn-primary btn-sm\'>Add Items</a>\r\n          \r\n        </div>\r\n      </div>\r\n    </div> <!-- end serialized tab -->\r\n\r\n    <!--################# CATALOG #################-->\r\n    <div class="tab-pane active" id="Catalog">\r\n      <div class="tab-content">\r\n\r\n\r\n        <div class="text-center">\r\n          <h3><strong>Catalog Details</strong></h3>\r\n        </div>\r\n        <hr>\r\n\r\n        <table class="table table-hover">\r\n          <thead>\r\n            <tr>\r\n              <th>Category</th>\r\n              <th>SKU</th>\r\n              <th>List Price</th>\r\n              <th>Cost</th>\r\n              <th>Commission Rate</th>\r\n              <th>Lead Time</th>\r\n\r\n\r\n            </tr>\r\n          </thead>\r\n\r\n          <tr onclick="input" data-toggle="modal" href="#catalog">\r\n\r\n            <td>\r\n              <label>')
        # SOURCE LINE 268
        __M_writer(str(item.category.subName))
        __M_writer('</label>\r\n            </td>\r\n            <td>')
        # SOURCE LINE 270
        __M_writer(str(item.sku))
        __M_writer('</td>\r\n            <td>$ ')
        # SOURCE LINE 271
        __M_writer(str(item.listPrice))
        __M_writer('</td>\r\n            <td>$ ')
        # SOURCE LINE 272
        __M_writer(str(item.cost))
        __M_writer('</td>\r\n            <td>')
        # SOURCE LINE 273
        __M_writer(str(item.commissionRate))
        __M_writer('</td>\r\n            <td>')
        # SOURCE LINE 274
        __M_writer(str(item.leadTime))
        __M_writer('</td>\r\n\r\n\r\n          </tr>\r\n\r\n        </table>\r\n\r\n          <!-- Catalog Edit Button and Delete -->\r\n          <div class="modal fade bs-modal-lg" id="catalog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n            <div class="modal-dialog modal-lg">\r\n              <div class="modal-content">\r\n\r\n                <div class="modal-header">\r\n                  <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                  <h4 class="modal-title" id="myModalLabel">Edit Product Information</h4>\r\n                </div>\r\n\r\n                <div class="modal-body">\r\n\r\n\r\n                  <form class ="form-horizontal" role="form" method ="POST" enctype="multipart/form-data">\r\n\r\n')
        # SOURCE LINE 296
        for field in form:
            # SOURCE LINE 297
            __M_writer('\r\n                      <div class="form-group">\r\n                        <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 299
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\r\n                          <div class="col-sm-8">\r\n                            ')
            # SOURCE LINE 301
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\r\n                            <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 302
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\r\n                          </div>\r\n                      </div>\r\n\r\n')
        # SOURCE LINE 307
        __M_writer('                    \r\n                  </div>\r\n                  <div class ="modal-footer">\r\n                    <div class="form-group">\r\n                      <div class="col-sm-offset-7 col-sm-4">\r\n                        <input class="btn btn-success" type="submit" value="Save Changes">\r\n                      </div>\r\n                    </div>\r\n                  </form>\r\n\r\n                </div>\r\n\r\n\r\n              </div>\r\n              <!-- /.modal-content -->\r\n            </div>\r\n            <!-- /.modal-dialog -->\r\n          </div>\r\n          <!-- /.modal -->  \r\n\r\n\r\n\r\n\r\n\r\n        <ul class="nav nav-pills">\r\n\r\n          <li class="active">\r\n            <button class="btn btn-success btn" data-toggle="modal" data-target="#ImageLibrary">Image Library <span class="badge">1</span>\r\n            </button>\r\n          </li>\r\n\r\n\r\n        </ul>\r\n\r\n\r\n\r\n        <!-- Modal -->\r\n        <div class="modal fade" id="ImageLibrary" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n          <div class="modal-dialog">\r\n            <div class="modal-content">\r\n              <div class="modal-header">\r\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                <h4 class="modal-title" id="myModalLabel">Modal title</h4>\r\n              </div>\r\n              <div class="modal-body">\r\n\r\n                <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\r\n                  <!-- Indicators -->\r\n                  <ol class="carousel-indicators">\r\n                    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\r\n                    <li data-target="#carousel-example-generic" data-slide-to="1"></li>\r\n                    <li data-target="#carousel-example-generic" data-slide-to="2"></li>\r\n                  </ol>\r\n\r\n                  <!-- Wrapper for slides -->\r\n                  <div class="carousel-inner">\r\n                    <div class="item active">\r\n                      <img src="')
        # SOURCE LINE 364
        __M_writer(str( STATIC_URL))
        __M_writer('base_app/images/NikonCamera.jpg" alt="Nikon Camera 1 V2" class="img-rounded">\r\n                      <div class="carousel-caption">\r\n                        IMG1.jpg\r\n                      </div>\r\n                    </div>\r\n                    ...\r\n                  </div>\r\n\r\n                  <!-- Controls -->\r\n                  <a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">\r\n                    <span class="glyphicon glyphicon-chevron-left"></span>\r\n                  </a>\r\n                  <a class="right carousel-control" href="#carousel-example-generic" data-slide="next">\r\n                    <span class="glyphicon glyphicon-chevron-right"></span>\r\n                  </a>\r\n                </div>\r\n\r\n\r\n              </div>\r\n              <div class="modal-footer">\r\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n                <button type="button" class="btn btn-primary">Save changes</button>\r\n              </div>\r\n            </div>\r\n            <!-- /.modal-content -->\r\n          </div>\r\n          <!-- /.modal-dialog -->\r\n        </div>\r\n        <!-- /.modal -->\r\n\r\n\r\n\r\n        <br/>\r\n        <h3>Product Description</h3>\r\n        <hr>\r\n        <p>')
        # SOURCE LINE 399
        __M_writer(str(item.description))
        __M_writer('\r\n          <a href="http://www.nikonusa.com/en/Nikon-Products/Product/Nikon1/27602/Nikon-1-V2.html" class="btn btn-info btn-xs">Go to Nikon</a>\r\n        </p>\r\n\r\n\r\n        <p></p>\r\n\r\n\r\n\r\n        <br/>\r\n        <h3>Tech Specs</h3>\r\n        <hr/>')
        # SOURCE LINE 410
        __M_writer(str(item.techSpecs))
        __M_writer('\r\n\r\n\r\n\r\n        <hr>\r\n\r\n\r\n\r\n\r\n      </div>\r\n  \t</div>\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


