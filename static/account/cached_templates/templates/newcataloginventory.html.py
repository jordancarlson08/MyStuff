# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1390626844.824617
_enable_loop = True
_template_filename = 'D:\\Google Drive\\MyStuff Website\\MyStuff\\homepage\\templates/newcataloginventory.html'
_template_uri = 'newcataloginventory.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        # SOURCE LINE 6
        __M_writer('\n')
        # SOURCE LINE 9
        __M_writer('\n')
        # SOURCE LINE 11
        __M_writer('\n')
        # SOURCE LINE 12
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 152
        __M_writer('   ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer('\n    <p class="lead"><strong>New Catalog Item</strong></p>\n\t</br>\n <form class="form-horizontal" role="form">\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Name</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="Nikon 1 V2">\n    </div>\n  </div>\n  \n  <div class="form-group">\n      <label for="pageLoc" class="col-sm-4 control-label"> Category </label>    \n          <div class="col-sm-4">\n              <p class = "lead">\n          <select>\n              <option>Digital Camera</option>\n              <option>Digital SLR Cameras</option>\n              <option>Accessories</option>\n              <option>Lenses</option>\n          </select></p>\n          </div>\n      </div>  \n      \n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">List Price</label>\n    <div class="col-sm-4">\n      <input type="password" class="form-control" id="inputPassword3" placeholder="$799.00">\n    </div>\n  </div>\n  \n  <div class="form-group">\n      <label for="avgCost" class="col-sm-4 control-label">SKU</label>\n      <div class="col-sm-4">\n        <input type="avgCost" class="form-control" id="avgCost" placeholder="A123B4">\n      </div>\n  </div>  \n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Commission Rate</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="20.00%">\n    </div>\n  </div>\n  \n  <div class="form-group">\n      <label for="pageLoc" class="col-sm-4 control-label">Page Location</label>\n      <div class="col-sm-2">\n        <input type="pageLoc" class="form-control" id="pageLoc" placeholder="p. 220">\n      </div>\n  </div>\n  \n      <div class="form-group">\n          <label for="avgCost" class="col-sm-4 control-label">Fill Point</label>\n          <div class="col-sm-2">\n            <input type="avgCost" class="form-control" id="avgCost" placeholder="3">\n          </div>\n      </div>  \n      \n     \n      <p class = "lead">Rental Information</p>\n      <hr>\n      \n     \n              <div class="form-group">\n                <label for="inputEmail3" class="col-sm-4 control-label">Rental Item</label>\n                <div class="col-sm-5">\n                  <label class="btn btn-default">\n                    <input type="radio" name="Rental" id="rentalNo" value="No"> <strong>No</strong></label>\n                  <label class="btn btn-default">\n                    <input type="radio" name="Rental" id="rentalYes" value="Yes"> <strong>Yes</strong></label>\n                </div>\n              </div>\n          \n       \n \n      <div class="form-group">\n          <label for="avgCost" class="col-sm-4 control-label">Price per Day</label>\n          <div class="col-sm-4">\n            <input type="avgCost" class="form-control" id="avgCost" placeholder="$25.75">\n          </div>\n      </div>  \n      \n      <div class="form-group">\n          <label for="avgCost" class="col-sm-4 control-label">Replacement Price</label>\n          <div class="col-sm-4">\n            <input type="avgCost" class="form-control" id="avgCost" placeholder="$799.00">\n          </div>\n      </div>  \n      \n      <div class="form-group">\n          <label for="avgCost" class="col-sm-4 control-label">Late Fee per Day</label>\n          <div class="col-sm-4">\n            <input type="avgCost" class="form-control" id="avgCost" placeholder="$7.75">\n          </div>\n      </div>  \n      \n      <p class = "lead">Catalog Information</p>\n      <hr>\n      \n      <div class="form-group">\n          <label for="avgCost" class="col-sm-3 control-label">Availability Date</label>\n          <div class="col-sm-8">\n            <input type="avgCost" class="form-control" id="avgCost" placeholder="2 Weeks">\n          </div>\n      </div>\n      \n      <div class="form-group">\n          <label for="productDescription" class="col-sm-3 control-label">Product Description</label>\n          <div class="col-sm-8">\n            <textarea class="form-control" rows="8"></textarea>\n          </div>\n      </div>\n      \n      <div class="form-group">\n        <label for="techSpecs" class="col-sm-3 control-label">Technical Specifications</label>\n        <div class="col-sm-8">\n          <textarea class="form-control" rows="4"></textarea>\n        </div>\n      </div>\n      \n  </div>\n    \n  <div class="form-group">\n    <div class="col-sm-offset-4 col-sm-4">\n        <button class="btn btn-info btn" data-toggle="modal" data-target="#ImageLibrary">\n  \t\t\tProduct Image Library\n\t\t</button>\n\n\t\t\t\n        <button class="btn btn-default">Cancel</button>\n      <button type="submit" class="btn btn-success">Save</button>\n    </div>\n  </div>\n  \n  \n\n  </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


