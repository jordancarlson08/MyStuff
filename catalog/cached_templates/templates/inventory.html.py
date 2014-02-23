# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393125771.863954
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/inventory.html'
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
        item = context.get('item', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 201
        __M_writer('   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n<h1>')
        # SOURCE LINE 6
        __M_writer(str(item.manufacturer))
        __M_writer(' ')
        __M_writer(str(item.name))
        __M_writer('</h1><hr>\n\n\n    <div>\n      <div class="tab-content">\n\n\n        <div class="text-center">\n          <h3><strong>Catalog Details</strong></h3>\n        </div>\n        <hr>\n\n        <table class="table table-hover">\n          <thead>\n            <tr>\n              <th>Category</th>\n              <th>SKU</th>\n              <th>List Price</th>\n\n\n            </tr>\n          </thead>\n\n          <tr onclick="input" data-toggle="modal" href="#catalog">\n\n            <td>\n              <label>')
        # SOURCE LINE 32
        __M_writer(str(item.categoryID.categoryName))
        __M_writer('</label>\n            </td>\n            <td>')
        # SOURCE LINE 34
        __M_writer(str(item.sku))
        __M_writer('</td>\n            <td>$ ')
        # SOURCE LINE 35
        __M_writer(str(item.listPrice))
        __M_writer('</td>\n\n\n          </tr>\n\n        </table>\n\n          <!-- Catalog Edit Button and Delete -->\n          <div class="modal fade bs-modal-lg" id="catalog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n            <div class="modal-dialog modal-lg">\n              <div class="modal-content">\n\n                <div class="modal-header">\n                  <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                  <h4 class="modal-title" id="myModalLabel">Edit Product Information</h4>\n                </div>\n\n                <div class="modal-body">\n\n\n                  <form class ="form-horizontal" role="form" method ="POST">\n\n')
        # SOURCE LINE 57
        for field in form:
            # SOURCE LINE 58
            __M_writer('\n                      <div class="form-group">\n                        <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 60
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n                          <div class="col-sm-8">\n                            ')
            # SOURCE LINE 62
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\n                            <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 63
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\n                          </div>\n                      </div>\n\n')
        # SOURCE LINE 68
        __M_writer('                    \n                  </div>\n                  <div class ="modal-footer">\n                    <div class="form-group">\n                      <div class="col-sm-offset-7 col-sm-4">\n                        <input class="btn btn-success" type="submit" value="Save Changes">\n                      </div>\n                    </div>\n                  </form>\n\n                </div>\n\n\n              </div>\n              <!-- /.modal-content -->\n            </div>\n            <!-- /.modal-dialog -->\n          </div>\n          <!-- /.modal -->  \n\n\n\n\n\n        <ul class="nav nav-pills">\n\n          <li class="active">\n            <button class="btn btn-success btn" data-toggle="modal" data-target="#ImageLibrary">Image Library <span class="badge">1</span>\n            </button>\n          </li>\n\n\n        </ul>\n\n\n\n        <!-- Modal -->\n        <div class="modal fade" id="ImageLibrary" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n          <div class="modal-dialog">\n            <div class="modal-content">\n              <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                <h4 class="modal-title" id="myModalLabel">Modal title</h4>\n              </div>\n              <div class="modal-body">\n\n                <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\n                  <!-- Indicators -->\n                  <ol class="carousel-indicators">\n                    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\n                    <li data-target="#carousel-example-generic" data-slide-to="1"></li>\n                    <li data-target="#carousel-example-generic" data-slide-to="2"></li>\n                  </ol>\n\n                  <!-- Wrapper for slides -->\n                  <div class="carousel-inner">\n                    <div class="item active">\n                      <img src="')
        # SOURCE LINE 125
        __M_writer(str( STATIC_URL))
        __M_writer('base_app/images/NikonCamera.jpg" alt="Nikon Camera 1 V2" class="img-rounded">\n                      <div class="carousel-caption">\n                        IMG1.jpg\n                      </div>\n                    </div>\n                    ...\n                  </div>\n\n                  <!-- Controls -->\n                  <a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">\n                    <span class="glyphicon glyphicon-chevron-left"></span>\n                  </a>\n                  <a class="right carousel-control" href="#carousel-example-generic" data-slide="next">\n                    <span class="glyphicon glyphicon-chevron-right"></span>\n                  </a>\n                </div>\n\n\n              </div>\n              <div class="modal-footer">\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n                <button type="button" class="btn btn-primary">Save changes</button>\n              </div>\n            </div>\n            <!-- /.modal-content -->\n          </div>\n          <!-- /.modal-dialog -->\n        </div>\n        <!-- /.modal -->\n\n\n\n        <br/>\n        <h3>Product Description</h3>\n        <hr>\n        <p>')
        # SOURCE LINE 160
        __M_writer(str(item.description))
        __M_writer('\n          <a href="http://www.nikonusa.com/en/Nikon-Products/Product/Nikon1/27602/Nikon-1-V2.html" class="btn btn-info btn-xs">Go to Nikon</a>\n        </p>\n\n\n        <p></p>\n\n\n\n        <br/>\n        <h3>Tech Specs</h3>\n        <hr/>')
        # SOURCE LINE 171
        __M_writer(str(item.techSpecs))
        __M_writer('\n\n\n\n        <hr>\n\n\n\n\n      </div>\n  \t</div>\n</div>\n\n\n <script>\n    $(\'#popoverData\').popover();\n\t$(\'#popoverOption\').popover({ trigger: "hover" });\n\n    $(function () {\n        $(\'#myTab a:last\').tab(\'show\')\n    })\n\n    jQuery(document).ready(function($) {\n          $(".clickableRow").click(function() {\n                window.document.location = $(this).attr("href");\n          });\n    });\n\n</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


