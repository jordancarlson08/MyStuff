# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394169682.147716
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
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        category_list = context.get('category_list', UNDEFINED)
        form = context.get('form', UNDEFINED)
        category = context.get('category', UNDEFINED)
        subCategory = context.get('subCategory', UNDEFINED)
        message = context.get('message', UNDEFINED)
        def left_side():
            return render_left_side(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 71
        __M_writer('  \r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 149
        __M_writer('  \r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_side():
            return render_left_side(context)
        category_list = context.get('category_list', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
            __M_writer('\r\n            <button class="btn btn-default btn-block" type="submit"><span class="glyphicon glyphicon-search"></span>&nbsp;Search</button>\r\n          </div>\r\n          \r\n        </div>\r\n        </div>\r\n      </div>\r\n\r\n\r\n    </div>\r\n')
        # SOURCE LINE 28
        __M_writer('\r\n\r\n</form>\r\n\r\n\r\n\r\n\r\n\r\n<div class="panel-group" id="accordion">\r\n\r\n\r\n')
        # SOURCE LINE 39
        for c in category_list:
            # SOURCE LINE 40
            __M_writer('  <div class="panel panel-default">\r\n    <div class="panel-heading" data-toggle="collapse" data-parent="#accordion" href="#collapse')
            # SOURCE LINE 41
            __M_writer(str(c.id))
            __M_writer('">\r\n      <h4 class="panel-title">\r\n          ')
            # SOURCE LINE 43
            __M_writer(str(c.categoryName))
            __M_writer('\r\n      </h4>\r\n    </div>\r\n    <div id="collapse')
            # SOURCE LINE 46
            __M_writer(str(c.id))
            __M_writer('" class="panel-collapse collapse">\r\n      <div class="panel-body">\r\n\t\t<ul class=\'list-unstyled\'>\r\n\r\n      ')
            # SOURCE LINE 50

            from manager import models as mmod
            subs_list = mmod.SubCategory.objects.filter(category=c)
            
            
            # SOURCE LINE 53
            __M_writer("\r\n      <li><a class='btn btn-default btn-block' href='/catalog/category/")
            # SOURCE LINE 54
            __M_writer(str(c.id))
            __M_writer("/'>All</a></li>\r\n")
            # SOURCE LINE 55
            for s in subs_list:
                # SOURCE LINE 56
                __M_writer("\t\t\t<li><a class='btn btn-default btn-block' href='/catalog/category/")
                __M_writer(str(c.id))
                __M_writer('/')
                __M_writer(str(s.id))
                __M_writer("'>")
                __M_writer(str(s.subName))
                __M_writer('</a></li>\r\n')
            # SOURCE LINE 58
            __M_writer('\r\n\r\n\r\n\t\t</ul>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n')
        # SOURCE LINE 67
        __M_writer('</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        message = context.get('message', UNDEFINED)
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        category = context.get('category', UNDEFINED)
        subCategory = context.get('subCategory', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 74
        __M_writer('\r\n')
        # SOURCE LINE 75
 

        __M_writer('\r\n\r\n\r\n<h2>Catalog</h2><hr/>\r\n')
        # SOURCE LINE 79
        if category != '':
            # SOURCE LINE 80
            __M_writer('<ol class="breadcrumb">\r\n  <li><a href=\'/catalog/category/\'>Catalog</a></li>\r\n')
            # SOURCE LINE 82
            if subCategory == '':
                # SOURCE LINE 83
                __M_writer("  <li class='active'>")
                __M_writer(str(category.categoryName))
                __M_writer('</li>\r\n')
            # SOURCE LINE 85
            if subCategory != '':
                # SOURCE LINE 86
                __M_writer("  <li><a href='/catalog/category/")
                __M_writer(str(category.id))
                __M_writer("'>")
                __M_writer(str(category.categoryName))
                __M_writer('</a></li>\r\n  <li class="active">')
                # SOURCE LINE 87
                __M_writer(str(subCategory.subName))
                __M_writer('</li>\r\n')
            # SOURCE LINE 89
            __M_writer('</ol>\r\n')
        # SOURCE LINE 91
        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
        # SOURCE LINE 98
        __M_writer(str(message))
        __M_writer('\r\n\r\n<div class=\'text-left\'>\r\n\t<ul class="list-inline">\r\n\r\n\t\t\r\n')
        # SOURCE LINE 104
        for i in items:
            # SOURCE LINE 105
            __M_writer("\r\n      <li class='clickable'>\r\n        <a href='/catalog/inventory/")
            # SOURCE LINE 107
            __M_writer(str(i.id))
            __M_writer('\'>\r\n        <div class="panel panel-primary" >\r\n          <div class=\'panel-heading\'><h3><strong>')
            # SOURCE LINE 109
            __M_writer(str(i.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.name))
            __M_writer("</strong></h3></div>\r\n\r\n          <div class='panel-body'> <!-- panel body starts -->\r\n            \r\n            <ul class='list-inline'>\r\n\r\n              <li>\r\n\r\n                <img src='")
            # SOURCE LINE 117
            __M_writer(str(i.img))
            __M_writer("' width='200px'/>\r\n\r\n              </li>\r\n              <li>\r\n                <ul class='list-unstyled'>\r\n                  <li>\r\n                    <strong>Price: $ ")
            # SOURCE LINE 123
            __M_writer(str(i.listPrice))
            __M_writer('</strong>\r\n                  </li> \r\n                  <li>\r\n                    SKU: ')
            # SOURCE LINE 126
            __M_writer(str(i.sku))
            __M_writer('\r\n                  </li>\r\n\r\n                </ul>\r\n\r\n                \r\n              </li>\r\n            </ul>\r\n\r\n          </div> <!-- panel body ends -->\r\n        </div> <!-- panel ends -->\r\n      </a>\r\n      </li> <!-- list item ends -->\r\n\r\n')
        # SOURCE LINE 141
        __M_writer('\r\n\t</ul>\r\n</div>\r\n\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


