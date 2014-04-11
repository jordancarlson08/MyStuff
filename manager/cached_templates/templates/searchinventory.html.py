# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397256487.755059
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/searchinventory.html'
_template_uri = 'searchinventory.html'
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
        catItems = context.get('catItems', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(' ')
 

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 283
        __M_writer('  \r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        catItems = context.get('catItems', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(' ')
 

        __M_writer('\r\n\r\n <h2>Inventory Management</h2>\r\n<hr/>\r\n<br/>\r\n\r\n<ul class="nav nav-tabs">\r\n  <li class="active">\r\n    <a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Sale" data-toggle="tab"><strong>Sales</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Rental" data-toggle="tab"><strong>Rentals</strong></a>\r\n  </li>\r\n</ul>\r\n\r\n<br/>\r\n<div class="tab-content">\r\n\r\n  <div class="tab-pane active" id="Catalog"><!-- Catalog Tab -->\r\n    <div class="tab-content">\r\n\r\n      <form id="live-search" action="" class="form-horizontal col-md-5" method="post">\r\n          <fieldset>\r\n            <div class="input-group">\r\n              <span class="input-group-addon"><span class=\'glyphicon glyphicon-search\'></span></span>\r\n              <input type="text" class="form-control" id="filter" value="" placeholder=\'Manufacturer, Name, SKU, Price, Views\'>\r\n            </div>\r\n          </fieldset>\r\n      </form>\r\n      <br/>\r\n      <br/>\r\n      <table class="table table-hover">\r\n        <thead>\r\n          <tr>\r\n            <th>SKU</th>\r\n            <th>Manufacturer</th>\r\n            <th>Name</th>\r\n            <th>List Prices</th>\r\n            <th>Cost</th>\r\n            <th>Category</th>\r\n            <th>Views</th>\r\n          </tr>\r\n        </thead>\r\n        <tbody class=\'searchbody\'>\r\n\r\n          <tr>\r\n            <td>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_man\' class="form-control">\r\n                <option></option>\r\n                <option>A - Z</option>\r\n                <option>Z - A</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_name\' class="form-control">\r\n                <option></option>\r\n                <option>A - Z</option>\r\n                <option>Z - A</option> <!-- Desc --> \r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_price\' class="form-control">\r\n                <option></option>\r\n                <option>Low - High</option>\r\n                <option>High - Low</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_cost\' class="form-control">\r\n                <option></option>\r\n                <option>Low - High</option>\r\n                <option>High - Low</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_cat\' class="form-control">\r\n                <option></option>\r\n                <option>A - Z</option>\r\n                <option>Z - A</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_views\' class="form-control">\r\n                <option></option>\r\n                <option>Low - High</option>\r\n                <option>High - Low</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n          </tr>\r\n\r\n')
        # SOURCE LINE 100
        for i in catItems:
            # SOURCE LINE 101
            if i.isActive == True:
                # SOURCE LINE 102
                __M_writer('          <tr class="clickableRow" href="/manager/inventory/')
                __M_writer(str(i.id))
                __M_writer('">\r\n            <td>')
                # SOURCE LINE 103
                __M_writer(str(i.sku))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 104
                __M_writer(str(i.manufacturer))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 105
                __M_writer(str(i.name))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 106
                __M_writer(str(i.listPrice))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 107
                __M_writer(str(i.cost))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 108
                __M_writer(str(i.category.subName))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 109
                __M_writer(str(i.views))
                __M_writer('</td>\r\n          </tr>\r\n')
                # SOURCE LINE 111
            else:
                # SOURCE LINE 112
                __M_writer('          <tr class="clickableRow grayed-out" href="/manager/inventory/')
                __M_writer(str(i.id))
                __M_writer('">\r\n            <td>')
                # SOURCE LINE 113
                __M_writer(str(i.sku))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 114
                __M_writer(str(i.manufacturer))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 115
                __M_writer(str(i.name))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 116
                __M_writer(str(i.listPrice))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 117
                __M_writer(str(i.cost))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 118
                __M_writer(str(i.category.subName))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 119
                __M_writer(str(i.views))
                __M_writer('</td>\r\n          </tr>\r\n')
        # SOURCE LINE 123
        __M_writer('        </tbody>\r\n      </table>\r\n\r\n    </div>\r\n  </div><!--  End Catalog Tab -->\r\n\r\n  <div class="tab-pane" id="Sale"><!--  Sale Inventory Tab -->\r\n    <div class="tab-content">\r\n')
        # SOURCE LINE 131
        if serial:
            # SOURCE LINE 132
            __M_writer('          <div class="panel-group" id="accordion">\r\n          ')
            # SOURCE LINE 133
 

            previousName = ''
            newName = ''
            
            
            
            # SOURCE LINE 138
            __M_writer('\r\n')
            # SOURCE LINE 139
            for i in serial:
                # SOURCE LINE 140
                __M_writer('\r\n          ')
                # SOURCE LINE 141
                newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
                
                __M_writer('\r\n\r\n')
                # SOURCE LINE 143
                if newName != previousName and previousName != '':
                    # SOURCE LINE 144
                    __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
                # SOURCE LINE 150
                __M_writer('\r\n')
                # SOURCE LINE 151
                if newName != previousName:
                    # SOURCE LINE 152
                    __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                    # SOURCE LINE 153
                    __M_writer(str(i.id))
                    __M_writer('">\r\n                    <h4 id=\'title_')
                    # SOURCE LINE 154
                    __M_writer(str(i.id))
                    __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                    # SOURCE LINE 155
                    __M_writer(str(i.catalogItem.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(i.catalogItem.name))
                    __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                    # SOURCE LINE 158
                    __M_writer(str(i.id))
                    __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>List Prices</th>\r\n                            <th>Cost</th>\r\n                            <th>Condition</th>\r\n                            <th>Category</th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
                # SOURCE LINE 173
                __M_writer("\r\n                          <tr href='/manager/inventory/")
                # SOURCE LINE 174
                __M_writer(str(i.catalogItem.id))
                __M_writer("#inStock' class='clickableRow'>\r\n                            <td>")
                # SOURCE LINE 175
                __M_writer(str(i.serialNum))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 176
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 177
                __M_writer(str(i.listPrice))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 178
                __M_writer(str(i.cost))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 179
                __M_writer(str(i.condition.condition))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 180
                __M_writer(str(i.catalogItem.category.subName))
                __M_writer('</td>\r\n                          </tr>\r\n\r\n            ')
                # SOURCE LINE 183
                previousName = newName 
                
                __M_writer('\r\n')
            # SOURCE LINE 185
            __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n')
            # SOURCE LINE 191
        else:
            # SOURCE LINE 192
            __M_writer('\r\n        <div class="vertical_spacer6"></div>\r\n        <div class="vertical_spacer6"></div>\r\n')
        # SOURCE LINE 196
        __M_writer('    </div>\r\n  </div><!--  End Serial Inventory Tab -->\r\n\r\n\r\n\r\n\r\n\r\n\r\n  <div class="tab-pane" id="Rental"><!--  Rental Inventory Tab -->\r\n    <div class="tab-content">\r\n')
        # SOURCE LINE 206
        if rental:
            # SOURCE LINE 207
            __M_writer('          <div class="panel-group" id="accordion">\r\n          ')
            # SOURCE LINE 208
 

            previousName = ''
            newName = ''
            
            
            
            # SOURCE LINE 213
            __M_writer('\r\n')
            # SOURCE LINE 214
            for i in rental:
                # SOURCE LINE 215
                __M_writer('\r\n          ')
                # SOURCE LINE 216
                newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
                
                __M_writer('\r\n\r\n')
                # SOURCE LINE 218
                if newName != previousName and previousName != '':
                    # SOURCE LINE 219
                    __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
                # SOURCE LINE 225
                __M_writer('\r\n')
                # SOURCE LINE 226
                if newName != previousName:
                    # SOURCE LINE 227
                    __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                    # SOURCE LINE 228
                    __M_writer(str(i.id))
                    __M_writer('">\r\n                    <h4 id=\'title_')
                    # SOURCE LINE 229
                    __M_writer(str(i.id))
                    __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                    # SOURCE LINE 230
                    __M_writer(str(i.catalogItem.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(i.catalogItem.name))
                    __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                    # SOURCE LINE 233
                    __M_writer(str(i.id))
                    __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>Price/Day</th>\r\n                            <th>Replacement Fee</th>\r\n                            <th>Category</th>\r\n                            <th></th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
                # SOURCE LINE 248
                __M_writer('\r\n                          <tr>\r\n                            <td>')
                # SOURCE LINE 250
                __M_writer(str(i.serialNum))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 251
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 252
                __M_writer(str(i.pricePerDay))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 253
                __M_writer(str(i.replacementFee))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 254
                __M_writer(str(i.catalogItem.category.subName))
                __M_writer("</td>\r\n                            <td><button id='rent_")
                # SOURCE LINE 255
                __M_writer(str(i.id))
                __M_writer("' class='btn btn-warning'><span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Rent</button></td>\r\n                          </tr>\r\n\r\n            ")
                # SOURCE LINE 258
                previousName = newName 
                
                __M_writer('\r\n')
            # SOURCE LINE 260
            __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n')
            # SOURCE LINE 266
        else:
            # SOURCE LINE 267
            __M_writer('\r\n        <div class="vertical_spacer6"></div>\r\n        <div class="vertical_spacer6"></div>\r\n\r\n\r\n')
        # SOURCE LINE 273
        __M_writer('    </div>\r\n  </div><!--  End Rental Inventory Tab -->\r\n</div>\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


