# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397243570.820811
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
        rental = context.get('rental', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        catItems = context.get('catItems', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(' ')
 

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 273
        __M_writer('  \r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rental = context.get('rental', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        def content():
            return render_content(context)
        catItems = context.get('catItems', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(' ')
 

        __M_writer('\r\n\r\n <h2>Inventory Management</h2>\r\n<hr/>\r\n<br/>\r\n\r\n<ul class="nav nav-tabs">\r\n  <li class="active">\r\n    <a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Sale" data-toggle="tab"><strong>Sales Inventory</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Rental" data-toggle="tab"><strong>Rental Inventory</strong></a>\r\n  </li>\r\n</ul>\r\n\r\n<br/>\r\n<div class="tab-content">\r\n\r\n  <div class="tab-pane active" id="Catalog"><!-- Catalog Tab -->\r\n    <div class="tab-content">\r\n\r\n      <table class="table table-hover">\r\n        <thead>\r\n          <tr>\r\n            <th>SKU</th>\r\n            <th>Manufacturer</th>\r\n            <th>Name</th>\r\n            <th>List Prices</th>\r\n            <th>Cost</th>\r\n            <th>Category</th>\r\n            <th>Views</th>\r\n          </tr>\r\n        </thead>\r\n        <tbody>\r\n\r\n          <tr>\r\n            <td>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_man\' class="form-control">\r\n                <option></option>\r\n                <option>A - Z</option>\r\n                <option>Z - A</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_name\' class="form-control">\r\n                <option></option>\r\n                <option>A - Z</option>\r\n                <option>Z - A</option> <!-- Desc --> \r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_price\' class="form-control">\r\n                <option></option>\r\n                <option>Low - High</option>\r\n                <option>High - Low</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_cost\' class="form-control">\r\n                <option></option>\r\n                <option>Low - High</option>\r\n                <option>High - Low</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_cat\' class="form-control">\r\n                <option></option>\r\n                <option>A - Z</option>\r\n                <option>Z - A</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n            <td>\r\n              <select id=\'select_views\' class="form-control">\r\n                <option></option>\r\n                <option>Low - High</option>\r\n                <option>High - Low</option> <!-- Desc -->\r\n              </select>\r\n            </td>\r\n          </tr>\r\n\r\n')
        # SOURCE LINE 90
        for i in catItems:
            # SOURCE LINE 91
            if i.isActive == True:
                # SOURCE LINE 92
                __M_writer('          <tr class="clickableRow" href="/manager/inventory/')
                __M_writer(str(i.id))
                __M_writer('">\r\n            <td>')
                # SOURCE LINE 93
                __M_writer(str(i.sku))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 94
                __M_writer(str(i.manufacturer))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 95
                __M_writer(str(i.name))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 96
                __M_writer(str(i.listPrice))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 97
                __M_writer(str(i.cost))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 98
                __M_writer(str(i.category.subName))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 99
                __M_writer(str(i.views))
                __M_writer('</td>\r\n          </tr>\r\n')
                # SOURCE LINE 101
            else:
                # SOURCE LINE 102
                __M_writer('          <tr class="clickableRow grayed-out" href="/manager/inventory/')
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
        # SOURCE LINE 113
        __M_writer('        </tbody>\r\n      </table>\r\n\r\n    </div>\r\n  </div><!--  End Catalog Tab -->\r\n\r\n  <div class="tab-pane" id="Sale"><!--  Sale Inventory Tab -->\r\n    <div class="tab-content">\r\n')
        # SOURCE LINE 121
        if serial:
            # SOURCE LINE 122
            __M_writer('          <div class="panel-group" id="accordion">\r\n          ')
            # SOURCE LINE 123
 

            previousName = ''
            newName = ''
            
            
            
            # SOURCE LINE 128
            __M_writer('\r\n')
            # SOURCE LINE 129
            for i in serial:
                # SOURCE LINE 130
                __M_writer('\r\n          ')
                # SOURCE LINE 131
                newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
                
                __M_writer('\r\n\r\n')
                # SOURCE LINE 133
                if newName != previousName and previousName != '':
                    # SOURCE LINE 134
                    __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
                # SOURCE LINE 140
                __M_writer('\r\n')
                # SOURCE LINE 141
                if newName != previousName:
                    # SOURCE LINE 142
                    __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                    # SOURCE LINE 143
                    __M_writer(str(i.id))
                    __M_writer('">\r\n                    <h4 id=\'title_')
                    # SOURCE LINE 144
                    __M_writer(str(i.id))
                    __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                    # SOURCE LINE 145
                    __M_writer(str(i.catalogItem.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(i.catalogItem.name))
                    __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                    # SOURCE LINE 148
                    __M_writer(str(i.id))
                    __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>List Prices</th>\r\n                            <th>Cost</th>\r\n                            <th>Condition</th>\r\n                            <th>Category</th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
                # SOURCE LINE 163
                __M_writer("\r\n                          <tr href='/manager/inventory/")
                # SOURCE LINE 164
                __M_writer(str(i.catalogItem.id))
                __M_writer("#inStock' class='clickableRow'>\r\n                            <td>")
                # SOURCE LINE 165
                __M_writer(str(i.serialNum))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 166
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 167
                __M_writer(str(i.listPrice))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 168
                __M_writer(str(i.cost))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 169
                __M_writer(str(i.condition.condition))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 170
                __M_writer(str(i.catalogItem.category.subName))
                __M_writer('</td>\r\n                          </tr>\r\n\r\n            ')
                # SOURCE LINE 173
                previousName = newName 
                
                __M_writer('\r\n')
            # SOURCE LINE 175
            __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n')
            # SOURCE LINE 181
        else:
            # SOURCE LINE 182
            __M_writer('\r\n        <div class="vertical_spacer6"></div>\r\n        <div class="vertical_spacer6"></div>\r\n')
        # SOURCE LINE 186
        __M_writer('    </div>\r\n  </div><!--  End Serial Inventory Tab -->\r\n\r\n\r\n\r\n\r\n\r\n\r\n  <div class="tab-pane" id="Rental"><!--  Rental Inventory Tab -->\r\n    <div class="tab-content">\r\n')
        # SOURCE LINE 196
        if rental:
            # SOURCE LINE 197
            __M_writer('          <div class="panel-group" id="accordion">\r\n          ')
            # SOURCE LINE 198
 

            previousName = ''
            newName = ''
            
            
            
            # SOURCE LINE 203
            __M_writer('\r\n')
            # SOURCE LINE 204
            for i in rental:
                # SOURCE LINE 205
                __M_writer('\r\n          ')
                # SOURCE LINE 206
                newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
                
                __M_writer('\r\n\r\n')
                # SOURCE LINE 208
                if newName != previousName and previousName != '':
                    # SOURCE LINE 209
                    __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
                # SOURCE LINE 215
                __M_writer('\r\n')
                # SOURCE LINE 216
                if newName != previousName:
                    # SOURCE LINE 217
                    __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                    # SOURCE LINE 218
                    __M_writer(str(i.id))
                    __M_writer('">\r\n                    <h4 id=\'title_')
                    # SOURCE LINE 219
                    __M_writer(str(i.id))
                    __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                    # SOURCE LINE 220
                    __M_writer(str(i.catalogItem.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(i.catalogItem.name))
                    __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                    # SOURCE LINE 223
                    __M_writer(str(i.id))
                    __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>Price/Day</th>\r\n                            <th>Replacement Fee</th>\r\n                            <th>Category</th>\r\n                            <th></th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
                # SOURCE LINE 238
                __M_writer('\r\n                          <tr>\r\n                            <td>')
                # SOURCE LINE 240
                __M_writer(str(i.serialNum))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 241
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 242
                __M_writer(str(i.pricePerDay))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 243
                __M_writer(str(i.replacementFee))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 244
                __M_writer(str(i.catalogItem.category.subName))
                __M_writer("</td>\r\n                            <td><button id='rent_")
                # SOURCE LINE 245
                __M_writer(str(i.id))
                __M_writer("' class='btn btn-warning'><span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Rent</button></td>\r\n                          </tr>\r\n\r\n            ")
                # SOURCE LINE 248
                previousName = newName 
                
                __M_writer('\r\n')
            # SOURCE LINE 250
            __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n')
            # SOURCE LINE 256
        else:
            # SOURCE LINE 257
            __M_writer('\r\n        <div class="vertical_spacer6"></div>\r\n        <div class="vertical_spacer6"></div>\r\n\r\n\r\n')
        # SOURCE LINE 263
        __M_writer('    </div>\r\n  </div><!--  End Rental Inventory Tab -->\r\n</div>\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


