# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397003247.669983
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
        

        # SOURCE LINE 99
        __M_writer('  \r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 101
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
        __M_writer('\r\n\r\n\r\n\r\n\r\n<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\r\n  <!-- Indicators -->\r\n  <ol class="carousel-indicators">\r\n    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\r\n    <li data-target="#carousel-example-generic" data-slide-to="1"></li>\r\n    <li data-target="#carousel-example-generic" data-slide-to="2"></li>\r\n  </ol>\r\n\r\n  <!-- Wrapper for slides -->\r\n  <div class="carousel-inner">\r\n\r\n    <div class="item active">\r\n      <img src="/static/homepage/images/e2.jpg" alt="Digital SLR">\r\n      <div class="carousel-caption">\r\n\r\n        <div class=\'box-semi\'>\r\n          <div class=\'vertical_spacer6\'></div>\r\n          <div class=\'jumbo\'>Digital SLR</div>\r\n          <h3>We have the largest selection of Nikon, Canon, Olympus, and other brands anywhere.</h3>\r\n          <br/>\r\n          <ul class=\'list list-inline\'>\r\n            <li><a href=\'/catalog/category/1/\' class=\'btn btn-primary btn-lg\'>Cameras</a></li>\r\n            <li><a href=\'/catalog/category/1/5/\' class=\'btn btn-success btn-lg\'>Accessories</a></li>\r\n          </ul>\r\n          <br/>\r\n        </div>\r\n        \r\n      </div>\r\n    </div>\r\n\r\n    <div class="item">\r\n      <img src="/static/homepage/images/e3.jpg" alt="Rentals">\r\n      <div class="carousel-caption">        \r\n\r\n        <div class=\'box-semi\'>\r\n          <div class=\'vertical_spacer6\'></div>\r\n          <div class=\'jumbo\'>Rentals</div>\r\n          <h3>Only need a camera for the weekend? Get a professional camera for a killer price.</h3>\r\n          <br/>\r\n          <ul class=\'list list-inline\'>\r\n            <li><button class=\'btn btn-primary btn-lg\'>Locations</button></li>\r\n            <li><a href=\'/catalog/category/\' class=\'btn btn-success btn-lg\'>Catalog</a></li>\r\n          </ul>\r\n          <br/>\r\n        </div>\r\n\r\n\r\n    </div>\r\n  </div>\r\n\r\n    <div class="item">\r\n      <img src="/static/homepage/images/e1.jpg" alt="Repairs">\r\n      <div class="carousel-caption">\r\n\r\n        <div class=\'box-semi\'>\r\n          <div class=\'vertical_spacer6\'></div>\r\n          <div class=\'jumbo\'>Repairs</div>\r\n          <h3>Our skilled technicians can handle anything from deep cleanings to broken lenses.</h3>\r\n          <br/>\r\n          <ul class=\'list list-inline\'>\r\n            <li><button class=\'btn btn-primary btn-lg\'>Locations</button></li>\r\n            <li><a href=\'/catalog/category/\' class=\'btn btn-success btn-lg\'>Catalog</a></li>\r\n          </ul>\r\n          <br/>\r\n        </div>\r\n\r\n      </div>\r\n    </div>\r\n\r\n  </div>\r\n\r\n</div>\r\n\r\n\r\n\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


