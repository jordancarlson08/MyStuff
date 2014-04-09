# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397084406.613226
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
        def content():
            return render_content(context._locals(__M_locals))
        rental = context.get('rental', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(' ')
 

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 199
        __M_writer('  \r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        catItems = context.get('catItems', UNDEFINED)
        def content():
            return render_content(context)
        rental = context.get('rental', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(' ')
 

        __M_writer('\r\n\r\n <h2>Inventory Management</h2>\r\n<hr/>\r\n<br/>\r\n\r\n<ul class="nav nav-tabs">\r\n  <li class="active">\r\n    <a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Sale" data-toggle="tab"><strong>Sales Inventory</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Rental" data-toggle="tab"><strong>Rental Inventory</strong></a>\r\n  </li>\r\n</ul>\r\n\r\n<br/>\r\n<div class="tab-content">\r\n\r\n  <div class="tab-pane active" id="Catalog"><!-- Catalog Tab -->\r\n    <div class="tab-content">\r\n\r\n      <table class="table table-hover">\r\n        <thead>\r\n          <tr>\r\n            <th>SKU</th>\r\n            <th>Manufacturer</th>\r\n            <th>Name</th>\r\n            <th>List Prices</th>\r\n            <th>Cost</th>\r\n            <th>Category</th>\r\n            <th>Views</th>\r\n          </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        # SOURCE LINE 42
        for i in catItems:
            # SOURCE LINE 43
            __M_writer('          <tr class="clickableRow" href="/manager/inventory/')
            __M_writer(str(i.id))
            __M_writer('">\r\n            <td>')
            # SOURCE LINE 44
            __M_writer(str(i.sku))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 45
            __M_writer(str(i.manufacturer))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 46
            __M_writer(str(i.name))
            __M_writer('</td>\r\n            <td>$ ')
            # SOURCE LINE 47
            __M_writer(str(i.listPrice))
            __M_writer('</td>\r\n            <td>$ ')
            # SOURCE LINE 48
            __M_writer(str(i.cost))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 49
            __M_writer(str(i.category.subName))
            __M_writer('</td>\r\n            <td>')
            # SOURCE LINE 50
            __M_writer(str(i.views))
            __M_writer('</td>\r\n          </tr>\r\n')
        # SOURCE LINE 53
        __M_writer('        </tbody>\r\n      </table>\r\n\r\n    </div>\r\n  </div><!--  End Catalog Tab -->\r\n\r\n  <div class="tab-pane" id="Sale"><!--  Sale Inventory Tab -->\r\n    <div class="tab-content">\r\n          <div class="panel-group" id="accordion">\r\n          ')
        # SOURCE LINE 62
 

        previousName = ''
        newName = ''
        
        
        
        # SOURCE LINE 67
        __M_writer('\r\n')
        # SOURCE LINE 68
        for i in serial:
            # SOURCE LINE 69
            __M_writer('\r\n          ')
            # SOURCE LINE 70
            newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
            
            __M_writer('\r\n\r\n')
            # SOURCE LINE 72
            if newName != previousName and previousName != '':
                # SOURCE LINE 73
                __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
            # SOURCE LINE 79
            __M_writer('\r\n')
            # SOURCE LINE 80
            if newName != previousName:
                # SOURCE LINE 81
                __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                # SOURCE LINE 82
                __M_writer(str(i.id))
                __M_writer('">\r\n                    <h4 id=\'title_')
                # SOURCE LINE 83
                __M_writer(str(i.id))
                __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                # SOURCE LINE 84
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                # SOURCE LINE 87
                __M_writer(str(i.id))
                __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>List Prices</th>\r\n                            <th>Cost</th>\r\n                            <th>Condition</th>\r\n                            <th>Category</th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
            # SOURCE LINE 102
            __M_writer('\r\n                          <tr>\r\n                            <td>')
            # SOURCE LINE 104
            __M_writer(str(i.serialNum))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 105
            __M_writer(str(i.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.catalogItem.name))
            __M_writer('</td>\r\n                            <td>$ ')
            # SOURCE LINE 106
            __M_writer(str(i.listPrice))
            __M_writer('</td>\r\n                            <td>$ ')
            # SOURCE LINE 107
            __M_writer(str(i.cost))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 108
            __M_writer(str(i.condition.condition))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 109
            __M_writer(str(i.catalogItem.category.subName))
            __M_writer('</td>\r\n                          </tr>\r\n\r\n            ')
            # SOURCE LINE 112
            previousName = newName 
            
            __M_writer('\r\n')
        # SOURCE LINE 114
        __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n    </div>\r\n  </div><!--  End Rental Inventory Tab -->\r\n\r\n\r\n\r\n\r\n\r\n\r\n  <div class="tab-pane" id="Rental"><!--  Rental Inventory Tab -->\r\n    <div class="tab-content">\r\n          <div class="panel-group" id="accordion">\r\n          ')
        # SOURCE LINE 131
 

        previousName = ''
        newName = ''
        
        
        
        # SOURCE LINE 136
        __M_writer('\r\n')
        # SOURCE LINE 137
        for i in rental:
            # SOURCE LINE 138
            __M_writer('\r\n          ')
            # SOURCE LINE 139
            newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
            
            __M_writer('\r\n\r\n')
            # SOURCE LINE 141
            if newName != previousName and previousName != '':
                # SOURCE LINE 142
                __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
            # SOURCE LINE 148
            __M_writer('\r\n')
            # SOURCE LINE 149
            if newName != previousName:
                # SOURCE LINE 150
                __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                # SOURCE LINE 151
                __M_writer(str(i.id))
                __M_writer('">\r\n                    <h4 id=\'title_')
                # SOURCE LINE 152
                __M_writer(str(i.id))
                __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                # SOURCE LINE 153
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                # SOURCE LINE 156
                __M_writer(str(i.id))
                __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>Price/Day</th>\r\n                            <th>Replacement Fee</th>\r\n                            <th>Category</th>\r\n                            <th></th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
            # SOURCE LINE 171
            __M_writer('\r\n                          <tr>\r\n                            <td>')
            # SOURCE LINE 173
            __M_writer(str(i.serialNum))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 174
            __M_writer(str(i.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.catalogItem.name))
            __M_writer('</td>\r\n                            <td>$ ')
            # SOURCE LINE 175
            __M_writer(str(i.pricePerDay))
            __M_writer('</td>\r\n                            <td>$ ')
            # SOURCE LINE 176
            __M_writer(str(i.replacementFee))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 177
            __M_writer(str(i.catalogItem.category.subName))
            __M_writer("</td>\r\n                            <td><button id='rent_")
            # SOURCE LINE 178
            __M_writer(str(i.id))
            __M_writer("' class='btn btn-warning'><span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Rent</button></td>\r\n                          </tr>\r\n\r\n            ")
            # SOURCE LINE 181
            previousName = newName 
            
            __M_writer('\r\n')
        # SOURCE LINE 183
        __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n    </div>\r\n  </div><!--  End Rental Inventory Tab -->\r\n</div>\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


