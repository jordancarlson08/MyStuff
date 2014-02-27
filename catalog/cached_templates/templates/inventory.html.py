# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393465999.151415
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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 200
        __M_writer('   \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n')
        # SOURCE LINE 4
 

        __M_writer('\r\n\r\n<h1>')
        # SOURCE LINE 6
        __M_writer(str(item.manufacturer))
        __M_writer(' ')
        __M_writer(str(item.name))
        __M_writer('</h1><hr>\r\n\r\n    <div>\r\n      <div class="tab-content">\r\n\r\n\r\n        <div class="text-center">\r\n          <h3><strong>Catalog Details</strong></h3>\r\n        </div>\r\n        <hr>\r\n  \r\n        <table class="table table-hover">\r\n          <thead>\r\n            <tr>\r\n              <th>Category</th>\r\n              <th>SKU</th>\r\n              <th>List Price</th>\r\n\r\n\r\n            </tr>\r\n          </thead>\r\n\r\n          <tr onclick="input" data-toggle="modal" href="#catalog">\r\n\r\n            <td>\r\n              <label>')
        # SOURCE LINE 31
        __M_writer(str(item.categoryID.categoryName))
        __M_writer('</label>\r\n            </td>\r\n            <td>')
        # SOURCE LINE 33
        __M_writer(str(item.sku))
        __M_writer('</td>\r\n            <td>$ ')
        # SOURCE LINE 34
        __M_writer(str(item.listPrice))
        __M_writer('</td>\r\n\r\n\r\n          </tr>\r\n\r\n        </table>\r\n\r\n          <!-- Catalog Edit Button and Delete -->\r\n          <div class="modal fade bs-modal-lg" id="catalog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n            <div class="modal-dialog modal-lg">\r\n              <div class="modal-content">\r\n\r\n                <div class="modal-header">\r\n                  <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                  <h4 class="modal-title" id="myModalLabel">Edit Product Information</h4>\r\n                </div>\r\n\r\n                <div class="modal-body">\r\n\r\n\r\n                  <form class ="form-horizontal" role="form" method ="POST">\r\n\r\n')
        # SOURCE LINE 56
        for field in form:
            # SOURCE LINE 57
            __M_writer('\r\n                      <div class="form-group">\r\n                        <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 59
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\r\n                          <div class="col-sm-8">\r\n                            ')
            # SOURCE LINE 61
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\r\n                            <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 62
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\r\n                          </div>\r\n                      </div>\r\n\r\n')
        # SOURCE LINE 67
        __M_writer('                    \r\n                  </div>\r\n                  <div class ="modal-footer">\r\n                    <div class="form-group">\r\n                      <div class="col-sm-offset-7 col-sm-4">\r\n                        <input class="btn btn-success" type="submit" value="Save Changes">\r\n                      </div>\r\n                    </div>\r\n                  </form>\r\n\r\n                </div>\r\n\r\n\r\n              </div>\r\n              <!-- /.modal-content -->\r\n            </div>\r\n            <!-- /.modal-dialog -->\r\n          </div>\r\n          <!-- /.modal -->  \r\n\r\n\r\n\r\n\r\n\r\n        <ul class="nav nav-pills">\r\n\r\n          <li class="active">\r\n            <button class="btn btn-success btn" data-toggle="modal" data-target="#ImageLibrary">Image Library <span class="badge">1</span>\r\n            </button>\r\n          </li>\r\n\r\n\r\n        </ul>\r\n\r\n\r\n\r\n        <!-- Modal -->\r\n        <div class="modal fade" id="ImageLibrary" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n          <div class="modal-dialog">\r\n            <div class="modal-content">\r\n              <div class="modal-header">\r\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\r\n                <h4 class="modal-title" id="myModalLabel">Modal title</h4>\r\n              </div>\r\n              <div class="modal-body">\r\n\r\n                <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\r\n                  <!-- Indicators -->\r\n                  <ol class="carousel-indicators">\r\n                    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\r\n                    <li data-target="#carousel-example-generic" data-slide-to="1"></li>\r\n                    <li data-target="#carousel-example-generic" data-slide-to="2"></li>\r\n                  </ol>\r\n\r\n                  <!-- Wrapper for slides -->\r\n                  <div class="carousel-inner">\r\n                    <div class="item active">\r\n                      <img src="')
        # SOURCE LINE 124
        __M_writer(str( STATIC_URL))
        __M_writer('base_app/images/NikonCamera.jpg" alt="Nikon Camera 1 V2" class="img-rounded">\r\n                      <div class="carousel-caption">\r\n                        IMG1.jpg\r\n                      </div>\r\n                    </div>\r\n                    ...\r\n                  </div>\r\n\r\n                  <!-- Controls -->\r\n                  <a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">\r\n                    <span class="glyphicon glyphicon-chevron-left"></span>\r\n                  </a>\r\n                  <a class="right carousel-control" href="#carousel-example-generic" data-slide="next">\r\n                    <span class="glyphicon glyphicon-chevron-right"></span>\r\n                  </a>\r\n                </div>\r\n\r\n\r\n              </div>\r\n              <div class="modal-footer">\r\n                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n                <button type="button" class="btn btn-primary">Save changes</button>\r\n              </div>\r\n            </div>\r\n            <!-- /.modal-content -->\r\n          </div>\r\n          <!-- /.modal-dialog -->\r\n        </div>\r\n        <!-- /.modal -->\r\n\r\n\r\n\r\n        <br/>\r\n        <h3>Product Description</h3>\r\n        <hr>\r\n        <p>')
        # SOURCE LINE 159
        __M_writer(str(item.description))
        __M_writer('\r\n          <a href="http://www.nikonusa.com/en/Nikon-Products/Product/Nikon1/27602/Nikon-1-V2.html" class="btn btn-info btn-xs">Go to Nikon</a>\r\n        </p>\r\n\r\n\r\n        <p></p>\r\n\r\n\r\n\r\n        <br/>\r\n        <h3>Tech Specs</h3>\r\n        <hr/>')
        # SOURCE LINE 170
        __M_writer(str(item.techSpecs))
        __M_writer('\r\n\r\n\r\n\r\n        <hr>\r\n\r\n\r\n\r\n\r\n      </div>\r\n  \t</div>\r\n</div>\r\n\r\n\r\n <script>\r\n    $(\'#popoverData\').popover();\r\n\t$(\'#popoverOption\').popover({ trigger: "hover" });\r\n\r\n    $(function () {\r\n        $(\'#myTab a:last\').tab(\'show\')\r\n    })\r\n\r\n    jQuery(document).ready(function($) {\r\n          $(".clickableRow").click(function() {\r\n                window.document.location = $(this).attr("href");\r\n          });\r\n    });\r\n\r\n</script>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


