# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396989593.738431
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/category.html'
_template_uri = 'category.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left_side', 'content']


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
        form = context.get('form', UNDEFINED)
        def left_side():
            return render_left_side(context._locals(__M_locals))
        subCategory = context.get('subCategory', UNDEFINED)
        category = context.get('category', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        category_list = context.get('category_list', UNDEFINED)
        history = context.get('history', UNDEFINED)
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 62
        __M_writer('  \r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 185
        __M_writer('  \r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def left_side():
            return render_left_side(context)
        category_list = context.get('category_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n')
        # SOURCE LINE 5
 

        __M_writer('\r\n\r\n\r\n<!-- Custom Form -->\r\n<form class ="form-horizontal" role="form" method ="GET" action=\'/catalog/category/\'>\r\n<!--   Loop through the fields of the form -->\r\n')
        # SOURCE LINE 11
        for f in form:
            # SOURCE LINE 12
            __M_writer('    <div class="form-group">\r\n      <div class=\'text-center\'>\r\n        <div class=\'container\'>\r\n        <div class=\'row\'>\r\n          <div class=\'col-md-2\'>\r\n            ')
            # SOURCE LINE 17
            __M_writer(str(f))
            __M_writer('\r\n            <button class="btn btn-default btn-block" type="submit"><span class="glyphicon glyphicon-search"></span>&nbsp;Search</button>\r\n          </div>\r\n        </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n')
        # SOURCE LINE 25
        __M_writer('</form>\r\n\r\n\r\n<div class="panel-group" id="accordion">\r\n\r\n')
        # SOURCE LINE 30
        for c in category_list:
            # SOURCE LINE 31
            __M_writer('  <div class="panel panel-default">\r\n    <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse')
            # SOURCE LINE 32
            __M_writer(str(c.id))
            __M_writer('">\r\n      <h4 class="panel-title">\r\n          ')
            # SOURCE LINE 34
            __M_writer(str(c.categoryName))
            __M_writer('\r\n      </h4>\r\n    </div>\r\n    <div id="collapse')
            # SOURCE LINE 37
            __M_writer(str(c.id))
            __M_writer('" class="panel-collapse collapse">\r\n      <div class="panel-body">\r\n\t\t<ul class=\'list-unstyled\'>\r\n\r\n      ')
            # SOURCE LINE 41

            from manager import models as mmod
            subs_list = mmod.SubCategory.objects.filter(category=c)
            
            
            # SOURCE LINE 44
            __M_writer("\r\n      <li><a class='btn btn-default btn-block' href='/catalog/category/")
            # SOURCE LINE 45
            __M_writer(str(c.id))
            __M_writer("/'>All</a></li>\r\n")
            # SOURCE LINE 46
            for s in subs_list:
                # SOURCE LINE 47
                __M_writer("\t\t\t<li><a class='btn btn-default btn-block' href='/catalog/category/")
                __M_writer(str(c.id))
                __M_writer('/')
                __M_writer(str(s.id))
                __M_writer("'>")
                __M_writer(str(s.subName))
                __M_writer('</a></li>\r\n')
            # SOURCE LINE 49
            __M_writer('\r\n\r\n\r\n\t\t</ul>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n')
        # SOURCE LINE 58
        __M_writer('</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        subCategory = context.get('subCategory', UNDEFINED)
        category = context.get('category', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        history = context.get('history', UNDEFINED)
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 65
        __M_writer(' \r\n')
        # SOURCE LINE 66
 

        __M_writer('\r\n\r\n\r\n<h2>Catalog</h2><hr/>\r\n')
        # SOURCE LINE 70
        if category != '':
            # SOURCE LINE 71
            __M_writer('<ol class="breadcrumb">\r\n  <li><a href=\'/catalog/category/\'>Catalog</a></li>\r\n')
            # SOURCE LINE 73
            if subCategory == '':
                # SOURCE LINE 74
                __M_writer("  <li class='active'>")
                __M_writer(str(category.categoryName))
                __M_writer('</li>\r\n')
            # SOURCE LINE 76
            if subCategory != '':
                # SOURCE LINE 77
                __M_writer("  <li><a href='/catalog/category/")
                __M_writer(str(category.id))
                __M_writer("'>")
                __M_writer(str(category.categoryName))
                __M_writer('</a></li>\r\n  <li class="active">')
                # SOURCE LINE 78
                __M_writer(str(subCategory.subName))
                __M_writer('</li>\r\n')
            # SOURCE LINE 80
            __M_writer('</ol>\r\n')
        # SOURCE LINE 82
        __M_writer('\r\n')
        # SOURCE LINE 83
        __M_writer(str(message))
        __M_writer('\r\n\r\n')
        # SOURCE LINE 85
        if history:
            # SOURCE LINE 86
            __M_writer("  <h3>Recently Viewed Items</h3>\r\n\r\n  <div class='container-fluid'>\r\n    <div class='row'>\r\n")
            # SOURCE LINE 90
            if request.user.is_authenticated()==True:
                # SOURCE LINE 91
                for h in history:
                    # SOURCE LINE 92
                    __M_writer("          <div class='col-md-4 col-sm-6 col-xs-12'>\r\n            <a href='/catalog/inventory/")
                    # SOURCE LINE 93
                    __M_writer(str(h.catalogItem.id))
                    __M_writer('\'>\r\n              <div class="panel panel-primary" >\r\n                <div class=\'panel-heading lg-heading\'><h3><strong>')
                    # SOURCE LINE 95
                    __M_writer(str(h.catalogItem.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(h.catalogItem.name))
                    __M_writer("</strong></h3></div>\r\n                <div class='panel-body text-center'> <!-- panel body starts -->\r\n                  <ul class='list-inline'>\r\n                    <li>\r\n                      <img class='max-img' src='")
                    # SOURCE LINE 99
                    __M_writer(str(h.catalogItem.img))
                    __M_writer("' width='200px'/>\r\n                    </li>\r\n                    <li>\r\n                      <ul class='list-unstyled'>\r\n                        <li>\r\n                          <strong>Price: $ ")
                    # SOURCE LINE 104
                    __M_writer(str(h.catalogItem.listPrice))
                    __M_writer('</strong>\r\n                        </li> \r\n                        <li>\r\n                          SKU: ')
                    # SOURCE LINE 107
                    __M_writer(str(h.catalogItem.sku))
                    __M_writer('\r\n                        </li>\r\n                      </ul>\r\n                    </li>\r\n                  </ul>\r\n                </div> <!-- panel body ends -->\r\n              </div> <!-- panel ends -->\r\n            </a>\r\n          </div>\r\n')
                # SOURCE LINE 117
            else:
                # SOURCE LINE 118
                for h in history:
                    # SOURCE LINE 119
                    __M_writer("          <div class='col-md-4 col-sm-6 col-xs-12'>\r\n            <a href='/catalog/inventory/")
                    # SOURCE LINE 120
                    __M_writer(str(h.catalogItem.id))
                    __M_writer('\'>\r\n              <div class="panel panel-primary" >\r\n                <div class=\'panel-heading lg-heading\'><h3><strong>')
                    # SOURCE LINE 122
                    __M_writer(str(h.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(h.name))
                    __M_writer("</strong></h3></div>\r\n                <div class='panel-body text-center'> <!-- panel body starts -->\r\n                  <ul class='list-inline'>\r\n                    <li>\r\n                      <img class='max-img' src='")
                    # SOURCE LINE 126
                    __M_writer(str(h.catalogItem.img))
                    __M_writer("' width='200px'/>\r\n                    </li>\r\n                    <li>\r\n                      <ul class='list-unstyled'>\r\n                        <li>\r\n                          <strong>Price: $ ")
                    # SOURCE LINE 131
                    __M_writer(str(h.listPrice))
                    __M_writer('</strong>\r\n                        </li> \r\n                        <li>\r\n                          SKU: ')
                    # SOURCE LINE 134
                    __M_writer(str(h.sku))
                    __M_writer('\r\n                        </li>\r\n                      </ul>\r\n                    </li>\r\n                  </ul>\r\n                </div> <!-- panel body ends -->\r\n              </div> <!-- panel ends -->\r\n            </a>\r\n          </div>\r\n')
            # SOURCE LINE 145
            __M_writer('    </div>\r\n  </div>\r\n')
        # SOURCE LINE 148
        __M_writer("\r\n\r\n<div class='container-fluid'>\r\n  <div class='row'>\r\n")
        # SOURCE LINE 152
        for i in items:
            # SOURCE LINE 153
            __M_writer("      <div class='col-md-4 col-sm-6 col-xs-12'>\r\n        <a href='/catalog/inventory/")
            # SOURCE LINE 154
            __M_writer(str(i.id))
            __M_writer('\'>\r\n          <div class="panel panel-primary" >\r\n            <div class=\'panel-heading lg-heading\'><h3><strong>')
            # SOURCE LINE 156
            __M_writer(str(i.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.name))
            __M_writer("</strong></h3></div>\r\n            <div class='panel-body text-center'> <!-- panel body starts -->\r\n              <ul class='list-inline'>\r\n                <li>\r\n                  <img class='max-img' src='")
            # SOURCE LINE 160
            __M_writer(str(i.img))
            __M_writer("' width='200px'/>\r\n                </li>\r\n                <li>\r\n                  <ul class='list-unstyled'>\r\n                    <li>\r\n                      <strong>Price: $ ")
            # SOURCE LINE 165
            __M_writer(str(i.listPrice))
            __M_writer('</strong>\r\n                    </li> \r\n                    <li>\r\n                      SKU: ')
            # SOURCE LINE 168
            __M_writer(str(i.sku))
            __M_writer('\r\n                    </li>\r\n                  </ul>\r\n                </li>\r\n              </ul>\r\n            </div> <!-- panel body ends -->\r\n          </div> <!-- panel ends -->\r\n        </a>\r\n      </div>\r\n')
        # SOURCE LINE 178
        __M_writer('  </div>\r\n</div>\r\n\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


