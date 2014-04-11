# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397253762.868565
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top', 'main']


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
    return runtime._inherit_from(context, 'base_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top():
            return render_top(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 237
        __M_writer('  \r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 239
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n')
        # SOURCE LINE 4
 

        __M_writer('\r\n\r\n')
        # SOURCE LINE 6
 
        from base_app.user_util import manager_check, employee_check
        
        isEmployee = employee_check(request.user)
        isManager = manager_check(request.user)
        
        
        
        # SOURCE LINE 12
        __M_writer('\r\n\r\n\r\n\r\n\r\n<div id="carousel-example-generic" class="carousel slide " data-ride="carousel">\r\n  <!-- Indicators -->\r\n  <ol class="carousel-indicators">\r\n    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\r\n    <li data-target="#carousel-example-generic" data-slide-to="1"></li>\r\n    <li data-target="#carousel-example-generic" data-slide-to="2"></li>\r\n  </ol>\r\n\r\n  <!-- Wrapper for slides -->\r\n  <div class="carousel-inner "> <!-- Start Carousel Inner -->\r\n    <div class="item active"> <!-- Start Item -->\r\n      <img src="/static/homepage/images/e2.jpg" alt="Digital SLR">\r\n      <div class="carousel-caption">\r\n        <div class=\'box-semi\'>\r\n          <br>\r\n          <br>\r\n          <div class=\'jumbo\'>Welcome!</div>\r\n          <p class="lead">Serving you since 1990, we know how to serve our customers! MyStuff carries a large selection of cameras, accessories, lighting setups, bags and cases.</p>\r\n          <br/>\r\n          <ul class=\'list list-inline\'>\r\n            <li><a href=\'/locations/\' class=\'btn btn-primary btn-lg\'><span class="glyphicon glyphicon-home"></span>  Locations</a></li>\r\n            <li><a href=\'/catalog/category/\' class=\'btn btn-success btn-lg\'>Shop</a></li>\r\n          </ul>\r\n          <br/>\r\n        </div>\r\n      </div>\r\n    </div> <!-- End Item -->\r\n    <div class="item"> <!-- Start Item -->\r\n      <img src="/static/homepage/images/e3.jpg" alt="Rentals">\r\n      <div class="carousel-caption">        \r\n        <div class=\'box-semi\'>\r\n          <br>\r\n          <br>\r\n          <div class=\'jumbo\'>Rentals</div>\r\n\r\n          <p class="lead">Cameras, Lenses, Lighting and Accessories. <br/>\r\n            Come into one of our locations today to rent!</p>\r\n          <br/>\r\n          <ul class=\'list list-inline\'>\r\n            <li><a href=\'/locations/\' class=\'btn btn-primary btn-lg\'><span class="glyphicon glyphicon-home"></span> Locations</a></li>\r\n            <li><a href=\'/catalog/rentals/\' class=\'btn btn-success btn-lg\'>Rentals</a></li>\r\n          </ul>\r\n          <br/>\r\n        </div>\r\n      </div>\r\n    </div> <!-- End Item -->\r\n    <div class="item"> <!-- Start Item -->\r\n      <img src="/static/homepage/images/e1.jpg" alt="Repairs">\r\n      <div class="carousel-caption">\r\n        <div class=\'box-semi\'>\r\n          <br>\r\n          <br>\r\n          <div class=\'jumbo\'>Nikon 1 V2</div>\r\n            <p class="lead">For creativity that has no limits.<br/>\r\n            Exceptional speed. Exceptional performance. Exceptional price.</p>\r\n          <br/>\r\n          <ul class=\'list list-inline\'>\r\n            <li><a href=\'/catalog/inventory/100025\' class=\'btn btn-primary btn-lg\'>View</a></li>\r\n            <li><a href=\'/catalog/category/99991\' class=\'btn btn-success btn-lg\'>Cameras</a></li>\r\n          </ul>\r\n          <br/>\r\n        </div>\r\n      </div>\r\n    </div> <!-- End Item -->\r\n  </div> <!-- End Carousel Inner -->\r\n</div> <!-- End Carousel -->\r\n\r\n<br/>\r\n\r\n<div class=\'container-fluid\'>\r\n  <div class=\'row text-center\'>\r\n    <div class=\'col-md-1\'></div>\r\n\r\n    <div class=\'col-md-2\'>\r\n      <a href="/catalog/category/99991/">\r\n        <div class="panel panel-default">\r\n          <div class="panel-body">\r\n            <img src="/static/catalog/images/products/nikon1v2.jpg" alt="Cameras">\r\n            <br/><br/>\r\n            <p class="lead">Cameras</p>\r\n          </div>\r\n        </div>\r\n      </a>\r\n    </div>\r\n\r\n    <div class=\'col-md-2\'>\r\n      <a href="/catalog/category/99992/">\r\n        <div class="panel panel-default">\r\n          <div class="panel-body">\r\n            <img src="/static/catalog/images/products/nikonlens1.jpg" alt="Lenses">\r\n            <br/><br/>\r\n            <p class="lead">Lenses</p>\r\n          </div>\r\n        </div>\r\n      </a>\r\n    </div>\r\n\r\n    <div class=\'col-md-2\'>\r\n      <a href="/catalog/category/99993/">\r\n        <div class="panel panel-default">\r\n          <div class="panel-body">\r\n            <img src="/static/catalog/images/products/light1.png" alt="Lighting">\r\n            <br/><br/>\r\n            <p class="lead">Lighting</p>\r\n          </div>\r\n        </div>\r\n      </a>\r\n    </div>\r\n\r\n    <div class=\'col-md-2\'>\r\n      <a href="/catalog/category/99994/">\r\n        <div class="panel panel-default">\r\n          <div class="panel-body">\r\n            <img src="/static/catalog/images/products/tripod1.jpg" alt="Tripod">\r\n            <br/><br/>\r\n            <p class="lead">Tripods</p>\r\n          </div>\r\n        </div>\r\n      </a>\r\n    </div>\r\n\r\n    <div class=\'col-md-2\'>\r\n      <a href="/catalog/category/99995/">\r\n        <div class="panel panel-default">\r\n          <div class="panel-body">\r\n            <img src="/static/catalog/images/products/bag1.jpg" alt="Bags & Cases">\r\n            <br/><br/>\r\n            <p class="lead">Cases</p>\r\n          </div>\r\n        </div>\r\n      </a>\r\n    </div>\r\n\r\n    <div class=\'col-md-1\'></div>\r\n  </div>\r\n\r\n\r\n  <div class="vertical_spacer6"></div>\r\n\r\n<!-- START FEATURED PRODUCTS -->\r\n  <div class=\'row \'>\r\n    <div class=\'col-md-1\'></div>\r\n    <div class=\'col-md-10\'> <!-- Open Column -->\r\n      <div class="panel panel-primary"> <!-- Featured Products Panel -->\r\n        <div class="panel-heading"><strong>Featured Products</strong></div>\r\n        <div class="panel-body text-center"> <!-- Featured Products Panel Body -->\r\n          <br/>\r\n\r\n          <div class=\'container-fluid\'> <!-- Feat Products Container -->\r\n            <div class=\'row\'> <!-- Feat Products Row -->\r\n\r\n              <div class=\'col-md-3\'>\r\n                <a href="/catalog/inventory/100022/">\r\n                  <div class="panel panel-default">\r\n                    <div class="panel-body feat-product">\r\n                      <img src="/static/catalog/images/products/canont5.jpg" alt="Canon Eos T5">\r\n                      <br/><br/>\r\n                      <p class=\'lead\'>Canon Eos T5</p>\r\n                      <p class=\'black\'>The EOS Rebel T5 has an 18.0 Megapixel CMOS...</p>\r\n                    </div>\r\n                  </div>\r\n                </a>\r\n              </div>\r\n\r\n              <div class=\'col-md-3\'>\r\n                <a href="/catalog/inventory/100027/">\r\n                  <div class="panel panel-default">\r\n                    <div class="panel-body feat-product">\r\n                      <img class=\'xsimg\' src="/static/catalog/images/products/nikond4.jpg" alt="Bags & Cases">\r\n                      <br/><br/>\r\n                      <p class="lead">Nikon D4</p>\r\n                      This new flagship D-SLR offers speed and accuracy...\r\n                    </div>\r\n                  </div>\r\n                </a>  \r\n              </div>\r\n\r\n              <div class=\'col-md-3\'>\r\n                <a href="/catalog/inventory/100025/">\r\n                  <div class="panel panel-default">\r\n                    <div class="panel-body feat-product">\r\n                      <img src="/static/catalog/images/products/nikon1v2.jpg" alt="Nikon 1 v2">\r\n                      <br/><br/>\r\n                      <p class="lead">Nikon 1 v2</p>\r\n                      Introducing Nikon 1 V2, with the exceptional speed...\r\n                    </div>\r\n                  </div>\r\n                </a>\r\n              </div>\r\n\r\n              <div class=\'col-md-3\'>\r\n                <a href="/catalog/inventory/100026/">\r\n                  <div class="panel panel-default">\r\n                    <div class="panel-body feat-product">\r\n                      <img src="/static/catalog/images/products/nikond50.jpg" alt="Bags & Cases">\r\n                      <br/><br/>\r\n                      <p class="lead">Nikon D50</p>\r\n                      Nikon\'s D50 interchangeable-lens digital SLR camera...\r\n                    </div>\r\n                  </div>\r\n                </a>\r\n              </div>\r\n\r\n            </div> <!-- End Feat Products Row -->\r\n          </div> <!-- End Feat Products Container -->\r\n\r\n        </div> <!-- End Featured Products Panel Body -->\r\n      </div> <!-- End Featured Products Panel -->\r\n    </div> <!-- Close Column -->\r\n    <div class=\'col-md-1\'></div>\r\n</div>\r\n<!-- END FEATURED PRODUCTS -->\r\n\r\n\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


