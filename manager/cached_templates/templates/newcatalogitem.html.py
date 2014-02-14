# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1392324415.353532
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/newcatalogitem.html'
_template_uri = 'newcatalogitem.html'
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        # SOURCE LINE 3
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 66
        __M_writer('   ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
 

        __M_writer('\n\n<h2>New Catalog Item</h2><hr/>\n</br>\n\n<!-- Custom Form -->\n<form class ="form-horizontal" role="form" method ="POST">\n\n<!--   Loop through the fields of the form -->\n')
        # SOURCE LINE 15
        for f in form:
            # SOURCE LINE 16
            __M_writer('\n    <div class="form-group">\n      <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 18
            __M_writer(str( f.name ))
            __M_writer('">')
            __M_writer(str( f.label ))
            __M_writer('</label> <!-- the label -->\n        <div class="col-sm-8">\n          ')
            # SOURCE LINE 20
            __M_writer(str(f))
            __M_writer(' <!-- The input box -->\n          ')
            # SOURCE LINE 21
            __M_writer(str(f.errors))
            __M_writer('\n        </div>\n    </div>\n\n')
        # SOURCE LINE 26
        __M_writer('\n  <div class="form-group">\n    <div class="col-sm-offset-4 col-sm-4">\n      <input class="btn btn-success" type="submit" value="Save">\n    </div>\n  </div>\n</form>\n\n\n\n<!-- Trash that needs to be removed eventually -->\n<form>\n  <p class="lead">Approved Vendors</p>\n  <hr>\n  <div class="form-group">\n    <label for="avgCost" class="col-sm-3 control-label">\n    </label>\n    <div class="col-sm-8">\n      <select multiple class="form-control">\n        <option>EMEA</option>\n        <option>ABC</option>\n        <option>BestProductSupplier</option>\n      </select>\n    </div>\n  </div>\n  </div>\n  <div class="form-group">\n    <div class="col-sm-offset-4 col-sm-8">\n      <button class="btn btn-info btn" data-toggle="modal" data-target="#ImageLibrary">\n        Product Image Library\n      </button>\n      <button class="btn btn-warning">New Vendor</button>\n      <button class="btn btn-default">Cancel</button>\n      <button type="submit" class="btn btn-success">Save</button>\n    </div>\n  </div>\n</form>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


