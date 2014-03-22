# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1395441656.238242
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/item.html'
_template_uri = 'item.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        s = context.get('s', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 61
        __M_writer('   \n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        s = context.get('s', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n<h1>')
        # SOURCE LINE 6
        __M_writer(str(s.catalogItem.manufacturer))
        __M_writer(' ')
        __M_writer(str(s.catalogItem.name))
        __M_writer(' - ')
        __M_writer(str(s.serialNum))
        __M_writer(' - Detail</h1><hr>\n\n\n  <form class ="form-horizontal" role="form" method ="POST">\n\n')
        # SOURCE LINE 11
        for field in form:
            # SOURCE LINE 12
            __M_writer('\n      <div class="form-group">\n        <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 14
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n          <div class="col-sm-4">\n            ')
            # SOURCE LINE 16
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\n            <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 17
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\n          </div>\n      </div>\n\n')
        # SOURCE LINE 22
        __M_writer('\n    <div class="form-group">\n      <div class="col-sm-offset-4 col-sm-4">\n        <input class="btn btn-success" type="submit" value="Save Changes">\n        <button class="btn btn-danger" data-toggle="modal" data-target="#Delete">Delete</button>\n\n      </div>\n    </div>\n  </form>\n\n\n\n  <!-- Modal -->\n  <div class="modal fade" id="Delete" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n    <div class="modal-dialog">\n      <div class="modal-content">\n\n        <div class="modal-header">\n          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n          <h4 class="modal-title" id="myModalLabel">Delete Serialized Item</h4>\n        </div>\n\n        <div class="modal-body">\n          <h4>Are you sure you want to delete this item?</h4>  \n          <br/>\n          You will not be able to undo this action.\n        </div>\n\n        <div class="modal-footer">\n          <a href=\'/manager/item/')
        # SOURCE LINE 51
        __M_writer(str(s.id))
        __M_writer('/delete\' class=\'btn btn-danger\'>Delete</a>\n          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n        </div>\n      </div>\n      <!-- /.modal-content -->\n    </div>\n    <!-- /.modal-dialog -->\n  </div>\n  <!-- /.modal -->\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


