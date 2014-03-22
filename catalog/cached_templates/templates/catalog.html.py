# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393723949.452132
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/catalog.html'
_template_uri = 'catalog.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'left_side']


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
        def left_side():
            return render_left_side(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 103
        __M_writer('  \r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 126
        __M_writer('  \r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 106
        __M_writer('\r\n')
        # SOURCE LINE 107
 

        __M_writer('\r\n\r\n\r\n<h2>Catalog</h2>\r\n<hr/>\r\n\r\n\r\n<div class=\'text-left\'>\r\n\t<ul class="list-inline">\r\n\r\n\t\t<!-- The Ajax goes here -->\r\n\r\n\t</ul>\r\n</div>\r\n\r\n\r\n<div class="vertical_spacer6"></div>\r\n<div class="vertical_spacer6"></div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n')
        # SOURCE LINE 5
 

        __M_writer('\r\n\r\n<div class="panel-group" id="accordion">\r\n\r\n  <div class="panel panel-default" data-toggle="collapse" data-parent="#accordion" href="#collapseOne">\r\n    <div class="panel-heading">\r\n      <h4 class="panel-title">\r\n          Cameras\r\n      </h4>\r\n    </div>\r\n    <div id="collapseOne" class="panel-collapse collapse in">\r\n      <div class="panel-body">\r\n\t\t<ul class=\'list-unstyled\'>\r\n\t\t\t<li><button class=\'btn btn-default btn-block\'>Digital SLR</li></button>\r\n\t\t\t<li><button class=\'btn btn-default btn-block\'>Digital Compact</li></button>\r\n\t\t\t<li><button class=\'btn btn-default btn-block\'>Film</li></button>\r\n\t\t\t<li><button class=\'btn btn-default btn-block\'>Other</li></button>\r\n\t\t</ul>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <div class="panel panel-default" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">\r\n    <div class="panel-heading">\r\n      <h4 class="panel-title">\r\n          Lenses\r\n      </h4>\r\n    </div>\r\n    <div id="collapseTwo" class="panel-collapse collapse">\r\n      <div class="panel-body">\r\n      \t<ul class=\'list-unstyled\'>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Digital SLR</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Digital Compact</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Film</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Other</li></button>\r\n      \t</ul>\r\n      </div>\r\n    </div>\r\n  </div>\r\n  <div class="panel panel-default" data-toggle="collapse" data-parent="#accordion" href="#collapseThree">\r\n    <div class="panel-heading">\r\n      <h4 class="panel-title">\r\n\r\n          Flash\r\n\r\n      </h4>\r\n    </div>\r\n    <div id="collapseThree" class="panel-collapse collapse">\r\n      <div class="panel-body">\r\n      \t<ul class=\'list-unstyled\'>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Digital SLR</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Digital Compact</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Film</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Other</li></button>\r\n      \t</ul>\r\n      </div>\r\n    </div>\r\n  </div>\r\n  \r\n  <div class="panel panel-default" data-toggle="collapse" data-parent="#accordion" href="#collapseFour">\r\n    <div class="panel-heading">\r\n      <h4 class="panel-title">\r\n        Batteries\r\n\r\n      </h4>\r\n    </div>\r\n    <div id="collapseFour" class="panel-collapse collapse">\r\n      <div class="panel-body">\r\n      \t<ul class=\'list-unstyled\'>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Digital SLR</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Digital Compact</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Film</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Other</li></button>\r\n      \t</ul>\r\n      </div>\r\n    </div>\r\n  </div>\r\n  <div class="panel panel-default" data-toggle="collapse" data-parent="#accordion" href="#collapseFive">\r\n    <div class="panel-heading">\r\n      <h4 class="panel-title">\r\n          Other\r\n      </h4>\r\n    </div>\r\n    <div id="collapseFive" class="panel-collapse collapse">\r\n      <div class="panel-body">\r\n      \t<ul class=\'list-unstyled\'>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Digital SLR</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Digital Compact</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Film</li></button>\r\n      \t\t<li><button class=\'btn btn-default btn-block\'>Other</li></button>\r\n      \t</ul>\r\n      </div>\r\n    </div>\r\n  </div>\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


