# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1390603162.172999
_enable_loop = True
_template_filename = 'D:\\Google Drive\\MyStuff Website\\MyStuff\\homepage\\templates/newinventoryitem.html'
_template_uri = 'newinventoryitem.html'
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
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 136
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
        # SOURCE LINE 13
        __M_writer('\n\n\n')
        # SOURCE LINE 16
        __M_writer('\n\n\n  <h2>New Store Item</h2>\n\t</br>\n <form class="form-horizontal" role="form">\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label"><b>Catalog Item</b></label>\n    <div class="col-sm-4">\n      <select class="form-control">\n        <option>Select One</option>\n\n        <option>Canon - PowerShot 150</option>\n        <option>Canon - PowerShot 200</option>\n        <option>Canon - PowerShot 550</option>\n        <option>Canon - PowerShot 3000</option>\n        <option>Canon - PowerShot 4500</option>\n\n        <option>Kodak - K45</option>\n        <option>Kodak - K45+</option>\n        <option>Kodak - K100</option>\n\n        <option>Nikon - D30</option>\n        <option>Nikon - D50</option>\n        <option>Nikon - D450</option>\n        <option>Nikon - D3000</option>\n        <option>Nikon - D4000</option>\n        <option>Nikon - D5000</option>\n         \n        <option>Olympus - S112</option>\n        <option>Olympus - StyleTough</option>\n      </select>\n    </div> \n  </div>\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Serial Number</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="042A000-66">\n    </div>\n  </div>\n  \n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label"></label>\n    <div class="col-sm-4">\n        <input type="email" class="form-control" id="inputEmail3" placeholder="042A000-66"><br/>\n        <input type="email" class="form-control" id="inputEmail3" placeholder="042A000-67"><br/>\n        <input type="email" class="form-control" id="inputEmail3" placeholder="042A000-68"><br/>\n        <input type="email" class="form-control" id="inputEmail3" placeholder="042A000-69"><br/>\n        <button class="btn btn-info btn-sm" data-toggle="modal" data-target="#MyModal">Add More</button>\n      \n    </div>\n  </div>\n  \n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label"><b>Store</b></label>\n    <div class="col-sm-4">\n      <select class="form-control">\n        <option>Select One</option>\n\n        <option>Ogden</option>\n        <option>Provo</option>\n        <option>Sandy</option>\n\n      </select>\n    </div> \n  </div>\n\n  <div class="form-group">\n    <label for="inputPassword3" class="col-sm-4 control-label">Cost</label>\n    <div class="col-sm-4">\n      <input type="text" class="form-control" id="inputPassword3" placeholder="$799.00">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Condition</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="New">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Rental Item</label>\n    <div class="col-sm-4">\n      <label class="btn btn-default">\n        <input type="radio" name="Rental" id="rentalNo" value="No"> <strong>No</strong></label>\n      <label class="btn btn-default">\n        <input type="radio" name="Rental" id="rentalYes" value="Yes"> <strong>Yes</strong></label>\n    </div>\n  </div>\n\n  <div class="form-group">\n    <div class="col-sm-offset-4 col-sm-4">\n      <button type="submit" class="btn btn-primary">Submit</button>\n      <a href="/manageinventory/" class="btn btn-success">Cancel</a>\n    </div>\n  </div>\n\n\n  </form>\n\n  <script>\n    $(\'#popoverOption\').popover({ trigger: "hover"});\n  </script>\n\n  <script>\n  $(\'.popover-markup\').popover({\n    html: true,\n    title: function () {\n        return $(this).parent().find(\'.head\').html();\n    },\n    content: function () {\n        return $(this).parent().find(\'.content\').html();\n    trigger: "hover"\n    }\n  }); \n  </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


