# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396734092.603479
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/searchusers.htm'
_template_uri = 'searchusers.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'main']


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
        def content():
            return render_content(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 84
        __M_writer('\n        Site content goes here in sub-templates.\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n<div class="content">\n  <div class="row">\n    <div class="col-md-2">\n      <div class="bs-sidebar hidden-print" role="complementary">\n        <ul class="nav bs-sidenav">\n\n          <div class="btn-group">\n            <button class="btn btn-default btn dropdown-toggle" type="button" data-toggle="dropdown">\n              <span class="glyphicon glyphicon-user"></span><span class="lead"> Users</span> <span class="caret"></span>\n            </button>\n            <ul class="dropdown-menu">\n              <ul class="nav nav-pills nav-stacked">\n                  <li>\n                      <!--User Management-->\n                     \n                      <a href="/manager/searchusers/"><span class="glyphicon glyphicon-search"></span>\n                          <small>Search</small></a>\n                      <a href="/account/newemployee/"><span class="glyphicon glyphicon-new-window"></span>\n                          <small>New User</small></a>\n                      <a href="/manageusers/"><span class="glyphicon glyphicon-home"></span>\n                      <small>User Dashboard</small></a>\n\n                      <li class="divider"></li>\n\n                      <!--Overall Menu Items-->\n                      \n                      <li><a href="/managestores/"><span class="glyphicon glyphicon-search"></span> \n                      <span class="lead"><small>Stores</small></span></a></li>\n                      <li><a href="/manageinventory/"><span class="glyphicon glyphicon-tags"></span> \n                      <span class="lead"><small> Inventory</small></span></a></li>\n                      <li><a href="/"><span class="glyphicon glyphicon-star"></span>\n                          <span class="lead"><small>Dashboard</small></span></a></li>\n                  </li>\n              </ul>\n            </ul>\n          </div>\n\n          <br/>\n          <br/>\n\n\n          <li>\n          <form class="navbar-form" role="search">\n                  <div class="input-group">\n                      <input type="text" class="form-control" placeholder="Search" name="srch-term" id="srch-term">\n                      <div class="input-group-btn">\n                          <button class="btn btn-default" type="submit"><i class="glyphicon glyphicon-search"></i></button>\n                      </div>\n                  </div>\n                  </form>\n          </li>\n\n          <br/>\n          <li><p>\n            Role\n            <select class="form-control">\n              <option>All</option>\n              <option>Customer</option>\n              <option>Employee</option>\n              <option>Manager</option>\n              <option>Admin</option>\n            </select>\n          </p></li>\n          <li><p>\n            Store\n            <select class="form-control">\n              <option>All</option>\n              <option>Sandy</option>\n              <option>Provo</option>\n              <option>Ogden</option>\n            </select>\n          </p></li>\n        </ul>\n      </div>\n    </div>\n    <div class="col-md-10" role="main">\n\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 86
        __M_writer('   ')
 

        __M_writer('\n                  \n    </div>\n    </div>  \n    </div>\n    </div>\n    </div>  \n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


