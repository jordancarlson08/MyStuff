# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397198936.876768
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main', 'top']


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
        request = context.get('request', UNDEFINED)
        def main():
            return render_main(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 241
        __M_writer('  \n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 243
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n')
        # SOURCE LINE 6
 
        from base_app.user_util import manager_check, employee_check
        
        isEmployee = employee_check(request.user)
        isManager = manager_check(request.user)
        
        
        
        # SOURCE LINE 12
        __M_writer('\n\n\n\n\n<div id="carousel-example-generic" class="carousel slide " data-ride="carousel">\n  <!-- Indicators -->\n  <ol class="carousel-indicators">\n    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\n    <li data-target="#carousel-example-generic" data-slide-to="1"></li>\n    <li data-target="#carousel-example-generic" data-slide-to="2"></li>\n  </ol>\n\n  <!-- Wrapper for slides -->\n  <div class="carousel-inner "> <!-- Start Carousel Inner -->\n    <div class="item active"> <!-- Start Item -->\n      <img src="/static/homepage/images/e2.jpg" alt="Digital SLR">\n      <div class="carousel-caption">\n        <div class=\'box-semi\'>\n          <br>\n          <br>\n          <div class=\'jumbo\'>Welcome!</div>\n          <p class="lead">In business since 1990, we know how to serve our customers! MyStuff carries a large selection of cameras, accessories, lighting setups, bags and cases. Premium service for rentals and repairs is available at all of our locations. Shop online or stop by one of our stores!</p>\n          <br/>\n          <ul class=\'list list-inline\'>\n            <li><a href=\'/locations/\' class=\'btn btn-primary btn\'><span class="glyphicon glyphicon-home"></span>  Locations</a></li>\n            <li><a href=\'/catalog/category/\' class=\'btn btn-success btn\'>Shop</a></li>\n          </ul>\n          <br/>\n        </div>\n      </div>\n    </div> <!-- End Item -->\n    <div class="item"> <!-- Start Item -->\n      <img src="/static/homepage/images/e3.jpg" alt="Rentals">\n      <div class="carousel-caption">        \n        <div class=\'box-semi\'>\n          <br>\n          <br>\n          <div class=\'jumbo\'>Rentals</div>\n\n          <p class="lead">We want everyone to have the best tools regardless of financial constraints. MyStuff offers the highest quality\n            equipment to best fit your specific needs. Rental selections include cameras, accessories, lighting, and bags. Come into one of our three locations today to rent!</p>\n          <br/>\n          <ul class=\'list list-inline\'>\n            <li><a href=\'/locations/\' class=\'btn btn-primary btn\'><span class="glyphicon glyphicon-home"></span>  Locations</a></li>\n            <li><a href=\'/rentalterms/\' class=\'btn btn-success btn\'>Rental Terms</a></li>\n          </ul>\n          <br/>\n        </div>\n      </div>\n    </div> <!-- End Item -->\n    <div class="item"> <!-- Start Item -->\n      <img src="/static/homepage/images/e1.jpg" alt="Repairs">\n      <div class="carousel-caption">\n        <div class=\'box-semi\'>\n          <br>\n          <br>\n          <div class=\'jumbo\'>Nikon 1 V2</div>\n          <h3>For creativity that has no limits</h3>\n          <p class="lead">Introducing the Nikon 1 V2, with \n            exceptional speed and performance of the Nikon 1 \n            system, plus pro-style enhancements for greater\n            creativity, flexibility, comfort and control.\n            </p>\n          <br/>\n          <ul class=\'list list-inline\'>\n            <li><a href=\'/locations/\' class=\'btn btn-primary btn\'>View</a></li>\n            <li><a href=\'/catalog/category/\' class=\'btn btn-success btn\'>Catalog</a></li>\n          </ul>\n          <br/>\n        </div>\n      </div>\n    </div> <!-- End Item -->\n  </div> <!-- End Carousel Inner -->\n</div> <!-- End Carousel -->\n\n<br/>\n\n<div class=\'container-fluid\'>\n  <div class=\'row text-center\'>\n    <div class=\'col-md-1\'></div>\n\n    <div class=\'col-md-2\'>\n      <a href="/catalog/category/1/">\n        <div class="panel panel-default">\n          <div class="panel-body">\n            <img src="/static/catalog/images/products/nikon1v2.jpg" alt="Cameras">\n            <br/><br/>\n            <p class="lead">Cameras</p>\n          </div>\n        </div>\n      </a>\n    </div>\n\n    <div class=\'col-md-2\'>\n      <a href="/catalog/category/2/">\n        <div class="panel panel-default">\n          <div class="panel-body">\n            <img src="/static/catalog/images/products/nikonlens1.jpg" alt="Lenses">\n            <br/><br/>\n            <p class="lead">Lenses</p>\n          </div>\n        </div>\n      </a>\n    </div>\n\n    <div class=\'col-md-2\'>\n      <a href="/catalog/category/3/">\n        <div class="panel panel-default">\n          <div class="panel-body">\n            <img src="/static/catalog/images/products/light1.png" alt="Lighting">\n            <br/><br/>\n            <p class="lead">Lighting</p>\n          </div>\n        </div>\n      </a>\n    </div>\n\n    <div class=\'col-md-2\'>\n      <a href="/catalog/category/4/">\n        <div class="panel panel-default">\n          <div class="panel-body">\n            <img src="/static/catalog/images/products/tripod1.jpg" alt="Tripod">\n            <br/><br/>\n            <p class="lead">Tripods</p>\n          </div>\n        </div>\n      </a>\n    </div>\n\n    <div class=\'col-md-2\'>\n      <a href="/catalog/category/5/">\n        <div class="panel panel-default">\n          <div class="panel-body">\n            <img src="/static/catalog/images/products/bag1.jpg" alt="Bags & Cases">\n            <br/><br/>\n            <p class="lead">Cases</p>\n          </div>\n        </div>\n      </a>\n    </div>\n\n    <div class=\'col-md-1\'></div>\n  </div>\n\n\n  <div class="vertical_spacer6"></div>\n\n<!-- START FEATURED PRODUCTS -->\n  <div class=\'row \'>\n    <div class=\'col-md-1\'></div>\n    <div class=\'col-md-10\'> <!-- Open Column -->\n      <div class="panel panel-primary"> <!-- Featured Products Panel -->\n        <div class="panel-heading"><strong>Featured Products</strong></div>\n        <div class="panel-body text-center"> <!-- Featured Products Panel Body -->\n          <br/>\n\n          <div class=\'container-fluid\'> <!-- Feat Products Container -->\n            <div class=\'row\'> <!-- Feat Products Row -->\n\n              <div class=\'col-md-3\'>\n                <a href="/catalog/inventory/10/">\n                  <div class="panel panel-default">\n                    <div class="panel-body feat-product">\n                      <img src="/static/catalog/images/products/canont5.jpg" alt="Canon Eos T5">\n                      <br/><br/>\n                      <p class=\'lead\'>Canon Eos T5</p>\n                      <p class=\'black\'>The EOS Rebel T5 has an 18.0 Megapixel CMOS...</p>\n                    </div>\n                  </div>\n                </a>\n              </div>\n\n              <div class=\'col-md-3\'>\n                <a href="/catalog/inventory/4/">\n                  <div class="panel panel-default">\n                    <div class="panel-body feat-product">\n                      <img class=\'xsimg\' src="/static/catalog/images/products/nikond4.jpg" alt="Bags & Cases">\n                      <br/><br/>\n                      <p class="lead">Nikon D4</p>\n                      This new flagship D-SLR offers speed and accuracy...\n                    </div>\n                  </div>\n                </a>  \n              </div>\n\n              <div class=\'col-md-3\'>\n                <a href="/catalog/inventory/1/">\n                  <div class="panel panel-default">\n                    <div class="panel-body feat-product">\n                      <img src="/static/catalog/images/products/nikon1v2.jpg" alt="Nikon 1 v2">\n                      <br/><br/>\n                      <p class="lead">Nikon 1 v2</p>\n                      Introducing Nikon 1 V2, with the exceptional speed...\n                    </div>\n                  </div>\n                </a>\n              </div>\n\n              <div class=\'col-md-3\'>\n                <a href="/catalog/inventory/3/">\n                  <div class="panel panel-default">\n                    <div class="panel-body feat-product">\n                      <img src="/static/catalog/images/products/nikond50.jpg" alt="Bags & Cases">\n                      <br/><br/>\n                      <p class="lead">Nikon D50</p>\n                      Nikon\'s D50 interchangeable-lens digital SLR camera...\n                    </div>\n                  </div>\n                </a>\n              </div>\n\n            </div> <!-- End Feat Products Row -->\n          </div> <!-- End Feat Products Container -->\n\n        </div> <!-- End Featured Products Panel Body -->\n      </div> <!-- End Featured Products Panel -->\n    </div> <!-- Close Column -->\n    <div class=\'col-md-1\'></div>\n</div>\n<!-- END FEATURED PRODUCTS -->\n\n\n\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n<div class="vertical_spacer6"></div>\n\n')
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


