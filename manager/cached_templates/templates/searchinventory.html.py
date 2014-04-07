# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396897244.283927
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
    return runtime._inherit_from(context, 'searchinventory.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        rental = context.get('rental', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        catItems = context.get('catItems', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 200
        __M_writer('  \r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        rental = context.get('rental', UNDEFINED)
        serial = context.get('serial', UNDEFINED)
        catItems = context.get('catItems', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n')
        # SOURCE LINE 5
 

        __M_writer('\r\n\r\n\r\n <h2>Inventory Management</h2>\r\n<hr/>\r\n<br/>\r\n\r\n<ul class="nav nav-tabs">\r\n  <li class="active">\r\n    <a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Sale" data-toggle="tab"><strong>Sales Inventory</strong></a>\r\n  </li>\r\n  <li>\r\n    <a href="#Rental" data-toggle="tab"><strong>Rental Inventory</strong></a>\r\n  </li>\r\n</ul>\r\n\r\n<br/>\r\n<div class="tab-content">\r\n\r\n  <div class="tab-pane active" id="Catalog"><!-- Catalog Tab -->\r\n    <div class="tab-content">\r\n\r\n      <table class="table table-hover">\r\n        <thead>\r\n          <tr>\r\n            <th>SKU</th>\r\n            <th>Manufacturer</th>\r\n            <th>Name</th>\r\n            <th>List Prices</th>\r\n            <th>Cost</th>\r\n            <th>Category</th>\r\n            <th>Views</th>\r\n          </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        # SOURCE LINE 43
        for i in catItems:
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
        # SOURCE LINE 54
        __M_writer('        </tbody>\r\n      </table>\r\n\r\n    </div>\r\n  </div><!--  End Catalog Tab -->\r\n\r\n  <div class="tab-pane" id="Sale"><!--  Sale Inventory Tab -->\r\n    <div class="tab-content">\r\n          <div class="panel-group" id="accordion">\r\n          ')
        # SOURCE LINE 63
 

        previousName = ''
        newName = ''
        
        
        
        # SOURCE LINE 68
        __M_writer('\r\n')
        # SOURCE LINE 69
        for i in serial:
            # SOURCE LINE 70
            __M_writer('\r\n          ')
            # SOURCE LINE 71
            newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
            
            __M_writer('\r\n\r\n')
            # SOURCE LINE 73
            if newName != previousName and previousName != '':
                # SOURCE LINE 74
                __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
            # SOURCE LINE 80
            __M_writer('\r\n')
            # SOURCE LINE 81
            if newName != previousName:
                # SOURCE LINE 82
                __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                # SOURCE LINE 83
                __M_writer(str(i.id))
                __M_writer('">\r\n                    <h4 id=\'title_')
                # SOURCE LINE 84
                __M_writer(str(i.id))
                __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                # SOURCE LINE 85
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                # SOURCE LINE 88
                __M_writer(str(i.id))
                __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>List Prices</th>\r\n                            <th>Cost</th>\r\n                            <th>Condition</th>\r\n                            <th>Category</th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
            # SOURCE LINE 103
            __M_writer('\r\n                          <tr>\r\n                            <td>')
            # SOURCE LINE 105
            __M_writer(str(i.serialNum))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 106
            __M_writer(str(i.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.catalogItem.name))
            __M_writer('</td>\r\n                            <td>$ ')
            # SOURCE LINE 107
            __M_writer(str(i.listPrice))
            __M_writer('</td>\r\n                            <td>$ ')
            # SOURCE LINE 108
            __M_writer(str(i.cost))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 109
            __M_writer(str(i.condition.condition))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 110
            __M_writer(str(i.catalogItem.category.subName))
            __M_writer('</td>\r\n                          </tr>\r\n\r\n            ')
            # SOURCE LINE 113
            previousName = newName 
            
            __M_writer('\r\n')
        # SOURCE LINE 115
        __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n    </div>\r\n  </div><!--  End Rental Inventory Tab -->\r\n\r\n\r\n\r\n\r\n\r\n\r\n  <div class="tab-pane" id="Rental"><!--  Rental Inventory Tab -->\r\n    <div class="tab-content">\r\n          <div class="panel-group" id="accordion">\r\n          ')
        # SOURCE LINE 132
 

        previousName = ''
        newName = ''
        
        
        
        # SOURCE LINE 137
        __M_writer('\r\n')
        # SOURCE LINE 138
        for i in rental:
            # SOURCE LINE 139
            __M_writer('\r\n          ')
            # SOURCE LINE 140
            newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
            
            __M_writer('\r\n\r\n')
            # SOURCE LINE 142
            if newName != previousName and previousName != '':
                # SOURCE LINE 143
                __M_writer('                      </tbody>\r\n                    </table>\r\n                  </div>\r\n                </div>\r\n              </div>\r\n')
            # SOURCE LINE 149
            __M_writer('\r\n')
            # SOURCE LINE 150
            if newName != previousName:
                # SOURCE LINE 151
                __M_writer('                <div class="panel panel-default">\r\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                # SOURCE LINE 152
                __M_writer(str(i.id))
                __M_writer('">\r\n                    <h4 id=\'title_')
                # SOURCE LINE 153
                __M_writer(str(i.id))
                __M_writer('\' class="panel-title">\r\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                # SOURCE LINE 154
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('\r\n                    </h4>\r\n                  </div>\r\n                  <div id="collapse_')
                # SOURCE LINE 157
                __M_writer(str(i.id))
                __M_writer('" class="panel-collapse collapse">\r\n                    <div class="panel-body">\r\n                      <table class=\'table table-hover\'>\r\n                        <thead>\r\n                          <tr>\r\n                            <th>Serial Number</th>\r\n                            <th>Name</th>\r\n                            <th>Price/Day</th>\r\n                            <th>Replacement Fee</th>\r\n                            <th>Category</th>\r\n                            <th></th>\r\n                          </tr>\r\n                        </thead>\r\n                        <tbody>\r\n')
            # SOURCE LINE 172
            __M_writer('\r\n                          <tr>\r\n                            <td>')
            # SOURCE LINE 174
            __M_writer(str(i.serialNum))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 175
            __M_writer(str(i.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.catalogItem.name))
            __M_writer('</td>\r\n                            <td>$ ')
            # SOURCE LINE 176
            __M_writer(str(i.pricePerDay))
            __M_writer('</td>\r\n                            <td>$ ')
            # SOURCE LINE 177
            __M_writer(str(i.replacementFee))
            __M_writer('</td>\r\n                            <td>')
            # SOURCE LINE 178
            __M_writer(str(i.catalogItem.category.subName))
            __M_writer("</td>\r\n                            <td><button id='rent_")
            # SOURCE LINE 179
            __M_writer(str(i.id))
            __M_writer("' class='btn btn-warning'><span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Rent</button></td>\r\n                          </tr>\r\n\r\n            ")
            # SOURCE LINE 182
            previousName = newName 
            
            __M_writer('\r\n')
        # SOURCE LINE 184
        __M_writer('                  </tbody>\r\n                </table>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n    </div>\r\n  </div><!--  End Rental Inventory Tab -->\r\n</div>\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


