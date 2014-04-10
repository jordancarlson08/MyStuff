# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397144876.884874
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
        serial = context.get('serial', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        catItems = context.get('catItems', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(' ')
 

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 225
        __M_writer('  \r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        serial = context.get('serial', UNDEFINED)
        def content():
            return render_content(context)
        catItems = context.get('catItems', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(' ')
 

        __M_writer('\r\n\r\n <h2>Inventory Management</h2>\r\n<hr/>\r\n<br/>\r\n\r\n<ul class="nav nav-tabs">\r\n  <li class="active">\r\n    <a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Sale" data-toggle="tab"><strong>Sales Inventory</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Rental" data-toggle="tab"><strong>Rental Inventory</strong></a>\r\n  </li>\r\n</ul>\r\n\r\n<br/>\r\n<div class="tab-content">\r\n\r\n  <div class="tab-pane active" id="Catalog"><!-- Catalog Tab -->\r\n    <div class="tab-content">\r\n\r\n      <table class="table table-hover">\r\n        <thead>\r\n          <tr>\r\n            <th>SKU</th>\r\n            <th>Manufacturer</th>\r\n            <th>Name</th>\r\n            <th>List Prices</th>\r\n            <th>Cost</th>\r\n            <th>Category</th>\r\n            <th>Views</th>\r\n          </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        # SOURCE LINE 42
        for i in catItems:
            # SOURCE LINE 43
            if i.isActive == True:
                # SOURCE LINE 44
                __M_writer('          <tr class="clickableRow" href="/manager/inventory/')
                __M_writer(str(i.id))
                __M_writer('">\r\n            <td>')
                # SOURCE LINE 45
                __M_writer(str(i.sku))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 46
                __M_writer(str(i.manufacturer))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 47
                __M_writer(str(i.name))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 48
                __M_writer(str(i.listPrice))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 49
                __M_writer(str(i.cost))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 50
                __M_writer(str(i.category.subName))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 51
                __M_writer(str(i.views))
                __M_writer('</td>\r\n          </tr>\r\n')
                # SOURCE LINE 53
            else:
                # SOURCE LINE 54
                __M_writer('          <tr class="clickableRow grayed-out" href="/manager/inventory/')
                __M_writer(str(i.id))
                __M_writer('">\r\n            <td>')
                # SOURCE LINE 55
                __M_writer(str(i.sku))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 56
                __M_writer(str(i.manufacturer))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 57
                __M_writer(str(i.name))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 58
                __M_writer(str(i.listPrice))
                __M_writer('</td>\r\n            <td>$ ')
                # SOURCE LINE 59
                __M_writer(str(i.cost))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 60
                __M_writer(str(i.category.subName))
                __M_writer('</td>\r\n            <td>')
                # SOURCE LINE 61
                __M_writer(str(i.views))
                __M_writer('</td>\r\n          </tr>\r\n')
        # SOURCE LINE 65
        __M_writer('        </tbody>\r\n      </table>\r\n\r\n    </div>\r\n  </div><!--  End Catalog Tab -->\r\n\r\n  <div class="tab-pane" id="Sale"><!--  Sale Inventory Tab -->\r\n    <div class="tab-content">\r\n')
        # SOURCE LINE 73
        if serial:
            # SOURCE LINE 74
            __M_writer('          <div class="panel-group" id="accordion">\r\n          ')
            # SOURCE LINE 75
 

            previousName = ''
            newName = ''
            
            
            
            # SOURCE LINE 80
            __M_writer('\r\n')
            # SOURCE LINE 81
            for i in serial:
                # SOURCE LINE 82
                __M_writer('\r\n          ')
                # SOURCE LINE 83
                newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
                
                __M_writer('\r\n\r\n')
                # SOURCE LINE 85
                if newName != previousName and previousName != '':
                    # SOURCE LINE 86
                    __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
                # SOURCE LINE 92
                __M_writer('\r\n')
                # SOURCE LINE 93
                if newName != previousName:
                    # SOURCE LINE 94
                    __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                    # SOURCE LINE 95
                    __M_writer(str(i.id))
                    __M_writer('">\r\n                    <h4 id=\'title_')
                    # SOURCE LINE 96
                    __M_writer(str(i.id))
                    __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                    # SOURCE LINE 97
                    __M_writer(str(i.catalogItem.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(i.catalogItem.name))
                    __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                    # SOURCE LINE 100
                    __M_writer(str(i.id))
                    __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>List Prices</th>\r\n                            <th>Cost</th>\r\n                            <th>Condition</th>\r\n                            <th>Category</th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
                # SOURCE LINE 115
                __M_writer("\r\n                          <tr href='/manager/inventory/")
                # SOURCE LINE 116
                __M_writer(str(i.catalogItem.id))
                __M_writer("#inStock' class='clickableRow'>\r\n                            <td>")
                # SOURCE LINE 117
                __M_writer(str(i.serialNum))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 118
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 119
                __M_writer(str(i.listPrice))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 120
                __M_writer(str(i.cost))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 121
                __M_writer(str(i.condition.condition))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 122
                __M_writer(str(i.catalogItem.category.subName))
                __M_writer('</td>\r\n                          </tr>\r\n\r\n            ')
                # SOURCE LINE 125
                previousName = newName 
                
                __M_writer('\r\n')
            # SOURCE LINE 127
            __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n')
            # SOURCE LINE 133
        else:
            # SOURCE LINE 134
            __M_writer('\r\n        <div class="vertical_spacer6"></div>\r\n        <div class="vertical_spacer6"></div>\r\n')
        # SOURCE LINE 138
        __M_writer('    </div>\r\n  </div><!--  End Serial Inventory Tab -->\r\n\r\n\r\n\r\n\r\n\r\n\r\n  <div class="tab-pane" id="Rental"><!--  Rental Inventory Tab -->\r\n    <div class="tab-content">\r\n')
        # SOURCE LINE 148
        if rental:
            # SOURCE LINE 149
            __M_writer('          <div class="panel-group" id="accordion">\r\n          ')
            # SOURCE LINE 150
 

            previousName = ''
            newName = ''
            
            
            
            # SOURCE LINE 155
            __M_writer('\r\n')
            # SOURCE LINE 156
            for i in rental:
                # SOURCE LINE 157
                __M_writer('\r\n          ')
                # SOURCE LINE 158
                newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
                
                __M_writer('\r\n\r\n')
                # SOURCE LINE 160
                if newName != previousName and previousName != '':
                    # SOURCE LINE 161
                    __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
                # SOURCE LINE 167
                __M_writer('\r\n')
                # SOURCE LINE 168
                if newName != previousName:
                    # SOURCE LINE 169
                    __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                    # SOURCE LINE 170
                    __M_writer(str(i.id))
                    __M_writer('">\r\n                    <h4 id=\'title_')
                    # SOURCE LINE 171
                    __M_writer(str(i.id))
                    __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                    # SOURCE LINE 172
                    __M_writer(str(i.catalogItem.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(i.catalogItem.name))
                    __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                    # SOURCE LINE 175
                    __M_writer(str(i.id))
                    __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>Price/Day</th>\r\n                            <th>Replacement Fee</th>\r\n                            <th>Category</th>\r\n                            <th></th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
                # SOURCE LINE 190
                __M_writer('\r\n                          <tr>\r\n                            <td>')
                # SOURCE LINE 192
                __M_writer(str(i.serialNum))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 193
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 194
                __M_writer(str(i.pricePerDay))
                __M_writer('</td>\r\n                            <td>$ ')
                # SOURCE LINE 195
                __M_writer(str(i.replacementFee))
                __M_writer('</td>\r\n                            <td>')
                # SOURCE LINE 196
                __M_writer(str(i.catalogItem.category.subName))
                __M_writer("</td>\r\n                            <td><button id='rent_")
                # SOURCE LINE 197
                __M_writer(str(i.id))
                __M_writer("' class='btn btn-warning'><span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Rent</button></td>\r\n                          </tr>\r\n\r\n            ")
                # SOURCE LINE 200
                previousName = newName 
                
                __M_writer('\r\n')
            # SOURCE LINE 202
            __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n')
            # SOURCE LINE 208
        else:
            # SOURCE LINE 209
            __M_writer('\r\n        <div class="vertical_spacer6"></div>\r\n        <div class="vertical_spacer6"></div>\r\n\r\n\r\n')
        # SOURCE LINE 215
        __M_writer('    </div>\r\n  </div><!--  End Rental Inventory Tab -->\r\n</div>\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


