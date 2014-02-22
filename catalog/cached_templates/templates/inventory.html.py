# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391724147.77681
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        stores_list = context.get('stores_list', UNDEFINED)
        form = context.get('form', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        serial = context.get('serial', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 535
        __M_writer('   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        conditions_list = context.get('conditions_list', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        stores_list = context.get('stores_list', UNDEFINED)
        form = context.get('form', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context)
        serial = context.get('serial', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n<h1>')
        # SOURCE LINE 6
        __M_writer(str(item.manufacturer))
        __M_writer(' ')
        __M_writer(str(item.name))
        __M_writer('</h1><hr>\n\n<!--################# Initializing Tab Names, ETC #################-->\n\n<ul class="nav nav-tabs">\n  <li class="active">\n    <a href="#Overview" data-toggle="tab"><strong>Overview</strong></a>\n  </li>\n  <li>\n    <a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a>\n  </li>\n  <li>\n    <a href="#inStock" data-toggle="tab"><strong>Serialized</strong></a>\n  </li>\n  <li>\n    <a href="#Rentals" data-toggle="tab"><strong>Rental</strong></a>\n  </li>\n</ul>\n\n<!--################# TABS #################-->\n\n<div class="tab-content">\n\n  <!-- ################# OVERVIEW TAB #################-->\n  <div class="tab-pane active" id="Overview">\n\t    <div class="text-center">\n\t      <h3><strong>Summary Information</strong></h3>\n\t    </div>\n\t    <hr>\n\t    <table class="table table-hover">\n\t      <thead>\n\t        <tr>\n\t          <th>Store</th>\n\t          <th>Total</th>\n\t          <th>Rental</th>\n\t          <th>For-Sale</th>\n\t          <th>Fill Point</th>\n\n\t        </tr>\n\t      </thead>\n\n\t      <tr>\n\t        <td>\n\t          <button class="btn btn-info btn-sm" data-toggle="modal" data-target="#Provo">PROVO</button>\n\t        </td>\n\t        <td>10</td>\n\t        <td>2</td>\n\t        <td>8</td>\n\t        <td>\n\n\n\t          <div class="progress progress-striped">\n\t            <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100" style="width: 45%">\n\t              <span class="sr-only">45% Complete</span>\n\t            </div>\n\t          </div>\n\n\t        </td>\n\n\n\t        <!-- Provo Store Information Modal -->\n\t        <div class="modal fade" id="Provo" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n\t          <div class="modal-dialog">\n\t            <div class="modal-content">\n\t              <div class="modal-header">\n\t                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t                <h4 class="modal-title" id="myModalLabel">Provo Store Information</h4>\n\t              </div>\n\t              <div class="modal-body">\n\n\t              </div>\n\t              <div class="modal-footer">\n\t                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t                <button type="button" class="btn btn-primary">Save changes</button>\n\t              </div>\n\t            </div>\n\t            <!-- /.modal-content -->\n\t          </div>\n\t          <!-- /.modal-dialog -->\n\t        </div>\n\t        <!-- /.modal -->\n\t      </tr>\n\n\t      <tr>\n\t        <td>\n\t          <button class="btn btn-warning btn-sm" data-toggle="modal" data-target="#Orem">OGDEN</button>\n\t        </td>\n\t        <td>10</td>\n\t        <td>2</td>\n\t        <td>8</td>\n\t        <td>\n\t          <div class="progress progress-striped">\n\t            <div class="progress-bar  progress-bar-warning" role="progressbar" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100" style="width: 95%">\n\t              <span class="sr-only">75% Complete</span>\n\t            </div>\n\t          </div>\n\n\t        </td>\n\n\t      </tr>\n\n\t      <tr>\n\t        <td>\n\t          <button class="btn btn-success btn-sm" data-toggle="modal" data-target="#Orem">SANDY</button>\n\t        </td>\n\t        <td>10</td>\n\t        <td>2</td>\n\t        <td>8</td>\n\t        <td>\n\t          <div class="progress progress-striped">\n\t            <div class="progress-bar  progress-bar-success" role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100" style="width: 85%">\n\t              <span class="sr-only">45% Complete</span>\n\t            </div>\n\t          </div>\n\t        </td>\n\n\t      </tr>\n\t    </table>\n  </div>\n\n  <!--################# RENTAL TAB ##################-->\n  <div class="tab-pane" id="Rentals">\n    <div class="tab-content">\n      <div class="text-center">\n        <h3><strong>Rental Inventory</strong></h3>\n      </div>\n      <hr>\n\n      <!--TABLE-->\n      <table class="table table-hover">\n\n        <thead>\n          <tr>\n\n            <th>Store Name</th>\n            <th><a id="popoverOption" class="btn" href="#" data-content="First number is the number of product rentals currently out. Second number is the number currently in-stock." rel="popover" data-placement="top" data-original-title="Product Availability #-#"><strong>Product Availability</strong></a>\n            </th>\n            <th>QTY</th>\n            <th>Rental Fees</th>\n            <th>Late Fees</th>\n            <th>Replacement Fees</th>\n            <th>Condition</th>\n            <th></th>\n            <th></th>\n\n          </tr>\n\n\n\n        </thead>\n\n')
        # SOURCE LINE 157
        for r in rentals:
            # SOURCE LINE 158
            __M_writer('        <tr onclick="input" data-toggle="modal" href="#rental">\n          <td><span class=\'label label-primary\'>')
            # SOURCE LINE 159
            __M_writer(str(r.storeID))
            __M_writer('</span></td>\n          <td>')
            # SOURCE LINE 160
            __M_writer(str(r.conditionID.condition))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 161
            __M_writer(str(r.serialNum))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 162
            __M_writer(str(r.listPrice))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 163
            __M_writer(str(r.cost))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 164
            __M_writer(str(r.shelfLocation))
            __M_writer('</td>\n          <td>')
            # SOURCE LINE 165
            __M_writer(str(r.dateReceived))
            __M_writer('</td>\n\n        </tr>\n')
        # SOURCE LINE 169
        __M_writer('\n\n\n        <!-- Rental Edit Button and Delete -->\n        <div class="modal fade" id="rental" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                <h4 class="modal-title" id="myModalLabel">Nikon 1 V2 - Edit Rental Information</h4>\n              </div>\n              <div class="modal-body">\n\n\n                <div class="form-group">\n\n                  <p class="lead"><small>Rental Information</small>\n                  </p>\n                  <hr>\n\n                  <div class="form-group">\n                    <div class="col-sm-4">\n                    </div>\n\n                    <div class="col-sm-8">\n                      <label>\n                        <input type="checkbox" value="">Rental?</label>\n                    </div>\n                  </div>\n\n                  <br/>\n\n                  <div class="form-group">\n                    <label for="avgCost" class="col-sm-4 control-label">Price per Day</label>\n                    <div class="col-sm-8">\n                      <input type="avgCost" class="form-control" id="avgCost" placeholder="$25.75">\n                    </div>\n                  </div>\n\n                  <br/>\n\n                  <div class="form-group">\n                    <label for="avgCost" class="col-sm-4 control-label">Replacement Price</label>\n                    <div class="col-sm-8">\n                      <input type="avgCost" class="form-control" id="avgCost" placeholder="$799.00">\n                    </div>\n                  </div>\n\n                  <br/>\n\n                  <div class="form-group">\n                    <label for="avgCost" class="col-sm-4 control-label">Late Fee per Day</label>\n                    <div class="col-sm-8">\n                      <input type="avgCost" class="form-control" id="avgCost" placeholder="$7.75">\n                    </div>\n                  </div>\n\n\n                  <br/>\n\n\n                </div>\n                <!-- /.modal-body -->\n                <div class="modal-footer">\n                  <button type="button" class="btn btn-danger" data-dismiss="modal">Archive</button>\n\n                  <button type="button" class="btn btn-success" data-dismiss="modal">Save</button>\n                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                </div>\n              </div>\n              <!-- /.modal-content -->\n            </div>\n            <!-- /.modal-dialog -->\n          </div>\n          <!-- /.modal -->\n\n\n\n      </table>\n\n\n      </div>\n  \t</div><!-- END RENTAL TAB -->\n\n    <!--################# SERIALIZED #################-->\n    <div class="tab-pane" id="inStock">\n      <div class="tab-content">\n        <div class="text-center">\n          <h3><strong>Serialized Items</strong></h3>\n        </div>\n\n        <hr>\n\n\n        <table class="table table-hover">\n          <thead>\n            <th>Store</th>\n            <th>Condition</th>\n            <th>Serial Number</th>\n            <th>List Price</th>\n            <th>Cost</th>\n            <th>Shelf Location</th>\n            <th>Date Received</th>\n            <th>Rental Item?</th>\n\n\n          </thead>\n          <tbody>\n            <tr>\n              <td>          \n                <select class="form-control">\n                  <option>All</option>\n')
        # SOURCE LINE 281
        for s in stores_list:
            # SOURCE LINE 282
            __M_writer('                  <option>')
            __M_writer(str(s.locationName))
            __M_writer('</option>\n')
        # SOURCE LINE 284
        __M_writer('                </select>\n              </td>\n              <td>\n                <select class="form-control">\n                  <option>All</option>\n')
        # SOURCE LINE 289
        for c in conditions_list:
            # SOURCE LINE 290
            __M_writer('                  <option>')
            __M_writer(str(c.condition))
            __M_writer('</option>\n')
        # SOURCE LINE 292
        __M_writer('                </select>\n              </td>\n              <td></td>\n              <td></td>\n              <td></td>\n              <td></td>\n              <td>\n                <select class="form-control">\n                  <option>All</option>\n                  <option>December</option>\n                  <option>January</option>\n                  <option>February</option>\n                </select>\n              </td>\n            </tr>\n\n\n')
        # SOURCE LINE 309
        for s in serial:
            # SOURCE LINE 310
            __M_writer('          <tr class="clickableRow"  href="/manager/item/')
            __M_writer(str(s.id))
            __M_writer('">        \n            <!-- The serialized items go here! in  a loop -->\n            <td><span class=\'label label-primary\'>')
            # SOURCE LINE 312
            __M_writer(str(s.storeID))
            __M_writer('</span></td>\n            <td>')
            # SOURCE LINE 313
            __M_writer(str(s.conditionID.condition))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 314
            __M_writer(str(s.serialNum))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 315
            __M_writer(str(s.listPrice))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 316
            __M_writer(str(s.cost))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 317
            __M_writer(str(s.shelfLocation))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 318
            __M_writer(str(s.dateReceived))
            __M_writer('</td>\n')
            # SOURCE LINE 319
            if s.isRental ==True:
                # SOURCE LINE 320
                __M_writer('            <td>Yes</td>\n')
                # SOURCE LINE 321
            else:
                # SOURCE LINE 322
                __M_writer('            <td>No</td>\n')
            # SOURCE LINE 324
            __M_writer('          </tr>\n')
        # SOURCE LINE 326
        __M_writer('          </tbody>\n\n        </table>  \n        <div class=\'text-right\'>\n          <a href=\'/manager/newinventoryitem/\' class=\'btn btn-primary btn-sm\'>Add Items</a>\n          \n        </div>\n      </div>\n    </div> <!-- end serialized tab -->\n\n    <!--################# CATALOG #################-->\n    <div class="tab-pane" id="Catalog">\n      <div class="tab-content">\n\n\n        <div class="text-center">\n          <h3><strong>Catalog Details</strong></h3>\n        </div>\n        <hr>\n\n        <table class="table table-hover">\n          <thead>\n            <tr>\n              <th>Category</th>\n              <th>SKU</th>\n              <th>List Price</th>\n              <th>Cost</th>\n              <th>Commission Rate</th>\n              <th>Lead Time</th>\n\n\n            </tr>\n          </thead>\n\n          <tr onclick="input" data-toggle="modal" href="#catalog">\n\n            <td>\n              <label>')
        # SOURCE LINE 363
        __M_writer(str(item.categoryID.categoryName))
        __M_writer('</label>\n            </td>\n            <td>')
        # SOURCE LINE 365
        __M_writer(str(item.sku))
        __M_writer('</td>\n            <td>$ ')
        # SOURCE LINE 366
        __M_writer(str(item.listPrice))
        __M_writer('</td>\n            <td>$ ')
        # SOURCE LINE 367
        __M_writer(str(item.cost))
        __M_writer('</td>\n            <td>')
        # SOURCE LINE 368
        __M_writer(str(item.commissionRate))
        __M_writer('</td>\n            <td>')
        # SOURCE LINE 369
        __M_writer(str(item.leadTime))
        __M_writer('</td>\n\n\n          </tr>\n\n        </table>\n\n          <!-- Catalog Edit Button and Delete -->\n          <div class="modal fade bs-modal-lg" id="catalog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n            <div class="modal-dialog modal-lg">\n              <div class="modal-content">\n\n                <div class="modal-header">\n                  <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                  <h4 class="modal-title" id="myModalLabel">Edit Product Information</h4>\n                </div>\n\n                <div class="modal-body">\n\n\n                  <form class ="form-horizontal" role="form" method ="POST">\n\n')
        # SOURCE LINE 391
        for field in form:
            # SOURCE LINE 392
            __M_writer('\n                      <div class="form-group">\n                        <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 394
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n                          <div class="col-sm-8">\n                            ')
            # SOURCE LINE 396
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\n                            <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 397
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\n                          </div>\n                      </div>\n\n')
        # SOURCE LINE 402
        __M_writer('                    \n                  </div>\n                  <div class ="modal-footer">\n                    <div class="form-group">\n                      <div class="col-sm-offset-7 col-sm-4">\n                        <input class="btn btn-success" type="submit" value="Save Changes">\n                      </div>\n                    </div>\n                  </form>\n\n                </div>\n\n\n              </div>\n              <!-- /.modal-content -->\n            </div>\n            <!-- /.modal-dialog -->\n          </div>\n          <!-- /.modal -->  \n\n\n\n\n\n        <ul class="nav nav-pills">\n\n          <li class="active">\n            <button class="btn btn-success btn" data-toggle="modal" data-target="#ImageLibrary">Image Library <span class="badge">1</span>\n            </button>\n          </li>\n\n\n        </ul>\n\n\n\n        <!-- Modal -->\n        <div class="modal fade" id="ImageLibrary" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                <h4 class="modal-title" id="myModalLabel">Modal title</h4>\n              </div>\n              <div class="modal-body">\n\n                <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\n                  <!-- Indicators -->\n                  <ol class="carousel-indicators">\n                    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\n                    <li data-target="#carousel-example-generic" data-slide-to="1"></li>\n                    <li data-target="#carousel-example-generic" data-slide-to="2"></li>\n                  </ol>\n\n                  <!-- Wrapper for slides -->\n                  <div class="carousel-inner">\n                    <div class="item active">\n                      <img src="')
        # SOURCE LINE 459
        __M_writer(str( STATIC_URL))
        __M_writer('base_app/images/NikonCamera.jpg" alt="Nikon Camera 1 V2" class="img-rounded">\n                      <div class="carousel-caption">\n                        IMG1.jpg\n                      </div>\n                    </div>\n                    ...\n                  </div>\n\n                  <!-- Controls -->\n                  <a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">\n                    <span class="glyphicon glyphicon-chevron-left"></span>\n                  </a>\n                  <a class="right carousel-control" href="#carousel-example-generic" data-slide="next">\n                    <span class="glyphicon glyphicon-chevron-right"></span>\n                  </a>\n                </div>\n\n\n              </div>\n              <div class="modal-footer">\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                <button type="button" class="btn btn-primary">Save changes</button>\n              </div>\n            </div>\n            <!-- /.modal-content -->\n          </div>\n          <!-- /.modal-dialog -->\n        </div>\n        <!-- /.modal -->\n\n\n\n        <br/>\n        <h3>Product Description</h3>\n        <hr>\n        <p>')
        # SOURCE LINE 494
        __M_writer(str(item.description))
        __M_writer('\n          <a href="http://www.nikonusa.com/en/Nikon-Products/Product/Nikon1/27602/Nikon-1-V2.html" class="btn btn-info btn-xs">Go to Nikon</a>\n        </p>\n\n\n        <p></p>\n\n\n\n        <br/>\n        <h3>Tech Specs</h3>\n        <hr/>')
        # SOURCE LINE 505
        __M_writer(str(item.techSpecs))
        __M_writer('\n\n\n\n        <hr>\n\n\n\n\n      </div>\n  \t</div>\n</div>\n\n\n <script>\n    $(\'#popoverData\').popover();\n\t$(\'#popoverOption\').popover({ trigger: "hover" });\n\n    $(function () {\n        $(\'#myTab a:last\').tab(\'show\')\n    })\n\n    jQuery(document).ready(function($) {\n          $(".clickableRow").click(function() {\n                window.document.location = $(this).attr("href");\n          });\n    });\n\n</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


