# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396734098.561751
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
        rental = context.get('rental', UNDEFINED)
        catItems = context.get('catItems', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        serial = context.get('serial', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 198
        __M_writer('  \n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rental = context.get('rental', UNDEFINED)
        catItems = context.get('catItems', UNDEFINED)
        def content():
            return render_content(context)
        serial = context.get('serial', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n\n <h2>Inventory Management</h2>\n<hr/>\n<br/>\n\n<ul class="nav nav-tabs">\n  <li class="active">\n    <a href="#Catalog" data-toggle="tab"><strong>Catalog</strong></a>\n  </li>\n  <li>\n    <a href="#Sale" data-toggle="tab"><strong>Sales Inventory</strong></a>\n  </li>\n  <li>\n    <a href="#Rental" data-toggle="tab"><strong>Rental Inventory</strong></a>\n  </li>\n</ul>\n\n<br/>\n<div class="tab-content">\n\n  <div class="tab-pane active" id="Catalog"><!-- Catalog Tab -->\n    <div class="tab-content">\n\n      <table class="table table-hover">\n        <thead>\n          <tr>\n            <th>SKU</th>\n            <th>Manufacturer</th>\n            <th>Name</th>\n            <th>List Prices</th>\n            <th>Cost</th>\n            <th>Category</th>\n          </tr>\n        </thead>\n        <tbody>\n')
        # SOURCE LINE 42
        for i in catItems:
            # SOURCE LINE 43
            __M_writer('          <tr class="clickableRow" href="/manager/inventory/')
            __M_writer(str(i.id))
            __M_writer('">\n            <td>')
            # SOURCE LINE 44
            __M_writer(str(i.sku))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 45
            __M_writer(str(i.manufacturer))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 46
            __M_writer(str(i.name))
            __M_writer('</td>\n            <td>$ ')
            # SOURCE LINE 47
            __M_writer(str(i.listPrice))
            __M_writer('</td>\n            <td>$ ')
            # SOURCE LINE 48
            __M_writer(str(i.cost))
            __M_writer('</td>\n            <td>')
            # SOURCE LINE 49
            __M_writer(str(i.category.subName))
            __M_writer('</td>\n          </tr>\n')
        # SOURCE LINE 52
        __M_writer('        </tbody>\n      </table>\n\n    </div>\n  </div><!--  End Catalog Tab -->\n\n  <div class="tab-pane" id="Sale"><!--  Sale Inventory Tab -->\n    <div class="tab-content">\n          <div class="panel-group" id="accordion">\n          ')
        # SOURCE LINE 61
 

        previousName = ''
        newName = ''
        
        
        
        # SOURCE LINE 66
        __M_writer('\n')
        # SOURCE LINE 67
        for i in serial:
            # SOURCE LINE 68
            __M_writer('\n          ')
            # SOURCE LINE 69
            newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
            
            __M_writer('\n\n')
            # SOURCE LINE 71
            if newName != previousName and previousName != '':
                # SOURCE LINE 72
                __M_writer('                      </tbody>\n                    </table>\n                  </div>\n                </div>\n              </div>\n')
            # SOURCE LINE 78
            __M_writer('\n')
            # SOURCE LINE 79
            if newName != previousName:
                # SOURCE LINE 80
                __M_writer('                <div class="panel panel-default">\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                # SOURCE LINE 81
                __M_writer(str(i.id))
                __M_writer('">\n                    <h4 id=\'title_')
                # SOURCE LINE 82
                __M_writer(str(i.id))
                __M_writer('\' class="panel-title">\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                # SOURCE LINE 83
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('\n                    </h4>\n                  </div>\n                  <div id="collapse_')
                # SOURCE LINE 86
                __M_writer(str(i.id))
                __M_writer('" class="panel-collapse collapse">\n                    <div class="panel-body">\n                      <table class=\'table table-hover\'>\n                        <thead>\n                          <tr>\n                            <th>Serial Number</th>\n                            <th>Name</th>\n                            <th>List Prices</th>\n                            <th>Cost</th>\n                            <th>Condition</th>\n                            <th>Category</th>\n                          </tr>\n                        </thead>\n                        <tbody>\n')
            # SOURCE LINE 101
            __M_writer('\n                          <tr>\n                            <td>')
            # SOURCE LINE 103
            __M_writer(str(i.serialNum))
            __M_writer('</td>\n                            <td>')
            # SOURCE LINE 104
            __M_writer(str(i.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.catalogItem.name))
            __M_writer('</td>\n                            <td>$ ')
            # SOURCE LINE 105
            __M_writer(str(i.listPrice))
            __M_writer('</td>\n                            <td>$ ')
            # SOURCE LINE 106
            __M_writer(str(i.cost))
            __M_writer('</td>\n                            <td>')
            # SOURCE LINE 107
            __M_writer(str(i.condition.condition))
            __M_writer('</td>\n                            <td>')
            # SOURCE LINE 108
            __M_writer(str(i.catalogItem.category.subName))
            __M_writer('</td>\n                          </tr>\n\n            ')
            # SOURCE LINE 111
            previousName = newName 
            
            __M_writer('\n')
        # SOURCE LINE 113
        __M_writer('                  </tbody>\n                </table>\n              </div>\n            </div>\n          </div>\n        </div>\n    </div>\n  </div><!--  End Rental Inventory Tab -->\n\n\n\n\n\n\n  <div class="tab-pane" id="Rental"><!--  Rental Inventory Tab -->\n    <div class="tab-content">\n          <div class="panel-group" id="accordion">\n          ')
        # SOURCE LINE 130
 

        previousName = ''
        newName = ''
        
        
        
        # SOURCE LINE 135
        __M_writer('\n')
        # SOURCE LINE 136
        for i in rental:
            # SOURCE LINE 137
            __M_writer('\n          ')
            # SOURCE LINE 138
            newName = i.catalogItem.manufacturer +' '+ i.catalogItem.name 
            
            __M_writer('\n\n')
            # SOURCE LINE 140
            if newName != previousName and previousName != '':
                # SOURCE LINE 141
                __M_writer('                      </tbody>\n                    </table>\n                  </div>\n                </div>\n              </div>\n')
            # SOURCE LINE 147
            __M_writer('\n')
            # SOURCE LINE 148
            if newName != previousName:
                # SOURCE LINE 149
                __M_writer('                <div class="panel panel-default">\n                  <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse_')
                # SOURCE LINE 150
                __M_writer(str(i.id))
                __M_writer('">\n                    <h4 id=\'title_')
                # SOURCE LINE 151
                __M_writer(str(i.id))
                __M_writer('\' class="panel-title">\n                        <span class=\'glyphicon glyphicon-plus\'></span>&nbsp; ')
                # SOURCE LINE 152
                __M_writer(str(i.catalogItem.manufacturer))
                __M_writer(' ')
                __M_writer(str(i.catalogItem.name))
                __M_writer('\n                    </h4>\n                  </div>\n                  <div id="collapse_')
                # SOURCE LINE 155
                __M_writer(str(i.id))
                __M_writer('" class="panel-collapse collapse">\n                    <div class="panel-body">\n                      <table class=\'table table-hover\'>\n                        <thead>\n                          <tr>\n                            <th>Serial Number</th>\n                            <th>Name</th>\n                            <th>Price/Day</th>\n                            <th>Replacement Fee</th>\n                            <th>Category</th>\n                            <th></th>\n                          </tr>\n                        </thead>\n                        <tbody>\n')
            # SOURCE LINE 170
            __M_writer('\n                          <tr>\n                            <td>')
            # SOURCE LINE 172
            __M_writer(str(i.serialNum))
            __M_writer('</td>\n                            <td>')
            # SOURCE LINE 173
            __M_writer(str(i.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.catalogItem.name))
            __M_writer('</td>\n                            <td>$ ')
            # SOURCE LINE 174
            __M_writer(str(i.pricePerDay))
            __M_writer('</td>\n                            <td>$ ')
            # SOURCE LINE 175
            __M_writer(str(i.replacementFee))
            __M_writer('</td>\n                            <td>')
            # SOURCE LINE 176
            __M_writer(str(i.catalogItem.category.subName))
            __M_writer("</td>\n                            <td><button id='rent_")
            # SOURCE LINE 177
            __M_writer(str(i.id))
            __M_writer("' class='btn btn-warning'><span class='glyphicon glyphicon-shopping-cart'></span>&nbsp; Rent</button></td>\n                          </tr>\n\n            ")
            # SOURCE LINE 180
            previousName = newName 
            
            __M_writer('\n')
        # SOURCE LINE 182
        __M_writer('                  </tbody>\n                </table>\n              </div>\n            </div>\n          </div>\n        </div>\n    </div>\n  </div><!--  End Rental Inventory Tab -->\n</div>\n\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


