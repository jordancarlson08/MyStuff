# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391660472.226304
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/stores.html'
_template_uri = 'stores.html'
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
    return runtime._inherit_from(context, 'base_store.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        urlStore = context.get('urlStore', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 183
        __M_writer('   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        urlStore = context.get('urlStore', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n\t<div class="media">\n\n\t  <p class="lead"><strong>')
        # SOURCE LINE 9
        __M_writer(str(urlStore.locationName))
        __M_writer(', ')
        __M_writer(str(urlStore.state))
        __M_writer('</strong>\n\t    <br/>\n\t    <small>Manager: ')
        # SOURCE LINE 11
        __M_writer(str(urlStore.manager.user.first_name))
        __M_writer(' ')
        __M_writer(str(urlStore.manager.user.last_name))
        __M_writer('</small>\n\t    <br/>\n\t    <small>Store: ')
        # SOURCE LINE 13
        __M_writer(str(urlStore.id))
        __M_writer('</small>\n\t  </p>\n\t  <hr/>\n\t  <img class="media-object" src="')
        # SOURCE LINE 16
        __M_writer(str( STATIC_URL))
        __M_writer('manager/images/Provo_store.png" alt=\'Provo\'>\n\t  <hr/>\t\n\t</div>\n\t<div class="media-body">\t\n\t\n\t\n\t\n\n\t<address>\n\t\t<strong>MyStuff, Inc.</strong><br>\n\t\t')
        # SOURCE LINE 26
        __M_writer(str(urlStore.street1))
        __M_writer('<br>\n')
        # SOURCE LINE 27
        if urlStore.street2 != '':
            # SOURCE LINE 28
            __M_writer('\t\t')
            __M_writer(str(urlStore.street2))
            __M_writer('<br>\n')
        # SOURCE LINE 30
        __M_writer('\t\t')
        __M_writer(str(urlStore.city))
        __M_writer(', ')
        __M_writer(str(urlStore.state))
        __M_writer(' ')
        __M_writer(str(urlStore.zipCode))
        __M_writer('<br>\n\t</address>\n\t</div>\n\n\n\t<button class="btn btn-success btn" data-toggle="modal" data-target="#InventoryModal">View Inventory</button>\n\n\t\t<!-- Modal -->\n\t\t<div class="modal fade" id="InventoryModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n\t\t  <div class="modal-dialog">\n\t\t    <div class="modal-content">\n\n\t\t      <div class="modal-header">\n\t\t        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t        <h4 class="modal-title" id="myModalLabel">Inventory - ')
        # SOURCE LINE 44
        __M_writer(str(urlStore.locationName))
        __M_writer('</h4>\n\t\t      </div>\n\n\t\t      <div class="modal-body">\n\t\t      \t<table class=\'table table-hover\'>\n\t\t      \t\t<thead>\n\t\t      \t\t\t<th>Name</th>\n\t\t      \t\t\t<th>List Price</th>\n\t\t      \t\t\t<th>QTY</th>\n\t\t      \t\t</thead>\n\t\t      \t\t<tbody>\n')
        # SOURCE LINE 55
        for i in items:
            # SOURCE LINE 56
            __M_writer('\t\t      \t\t\t<tr>\n\t\t      \t\t\t\t<td>')
            # SOURCE LINE 57
            __M_writer(str(i.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(i.catalogItem.name))
            __M_writer('</td>\n\t\t      \t\t\t\t<td>')
            # SOURCE LINE 58
            __M_writer(str(i.catalogItem.listPrice))
            __M_writer('</td>\n\t\t      \t\t\t\t<td>')
            # SOURCE LINE 59
            __M_writer(str(i.cost))
            __M_writer('</td>\n\n\t\t      \t\t\t</tr>\n')
        # SOURCE LINE 63
        __M_writer('\t\t      \t\t</tbody>\n\t\t      \t</table>\n\t\t      </div>\n\n\t\t      <div class="modal-footer">\n\t\t        <button type="button" class="btn btn-primary">New Catalog Item</button>\n\t\t        <button type="button" class="btn btn-warning">New Serialized Item</button>\n\t\t        <button type="button" class="btn btn-danger">Inventory Management</button>\n\t\t        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\t\t\n\t\t      </div>\n\n\t\t    </div>\n\t\t    <!-- /.modal-content -->\n\t\t  </div>\n\t\t  <!-- /.modal-dialog -->\n\t\t</div>\n\t\t<!-- /.modal -->\t\n\n\n\n\n\t<button class="btn btn-warning btn" data-toggle="modal" data-target="#Edit">Edit</button>\n\n\n\t\t<!-- Modal -->\n\t\t<div class="modal fade" id="Edit" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n\t\t  <div class="modal-dialog">\n\t\t    <div class="modal-content">\n\n\t\t      <div class="modal-header">\n\t\t        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t        <h4 class="modal-title" id="myModalLabel">Edit Store Information</h4>\n\t\t      </div>\n\n\t\t      <div class="modal-body">\n\n\n\t\t\t      <form class ="form-horizontal" role="form" method ="POST">\n\n')
        # SOURCE LINE 102
        for field in form:
            # SOURCE LINE 103
            __M_writer('\n\t\t\t          <div class="form-group">\n\t\t\t            <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 105
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n\t\t\t              <div class="col-sm-4">\n\t\t\t              \t')
            # SOURCE LINE 107
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\n\t\t\t                <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 108
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\n\t\t\t              </div>\n\t\t\t          </div>\n\n')
        # SOURCE LINE 113
        __M_writer('\n\n\n\t\t      </div>\n\t\t      <div class=\'modal-footer\'>\n\t\t      \t  <div class="form-group">\n\t\t      \t    <div class="col-sm-offset-4 col-sm-4">\n\t\t      \t      <input class="btn btn-success" type="submit" value="Save Changes">\n\t\t      \t    </div>\n\t\t      \t  </div>\n\t\t      \t</form>\n\t\t      </div>\n\n\t\t    </div>\n\t\t    <!-- /.modal-content -->\n\t\t  </div>\n\t\t  <!-- /.modal-dialog -->\n\t\t</div>\n\t\t<!-- /.modal -->\t\n\n\n\t<button class="btn btn-danger" data-toggle="modal" data-target="#Delete">Delete</button>\n\n\t<!-- Modal -->\n\t<div class="modal fade" id="Delete" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n\t  <div class="modal-dialog">\n\t    <div class="modal-content">\n\n\t      <div class="modal-header">\n\t        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t        <h4 class="modal-title" id="myModalLabel">Delete Store</h4>\n\t      </div>\n\n\t      <div class="modal-body">\n\t\t      <h3>Are you sure you want to delete this store? \n\t\t      <br/>\n\t\t      You will not be able to undo this action.</h3>\n\t      </div>\n\n\t      <div class="modal-footer">\n\t      \t<a href="/manager/stores/')
        # SOURCE LINE 153
        __M_writer(str(urlStore.id))
        __M_writer('/delete" class="btn btn-success">Yes</a>\n\t        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t      </div>\n\t    </div>\n\t    <!-- /.modal-content -->\n\t  </div>\n\t  <!-- /.modal-dialog -->\n\t</div>\n\t<!-- /.modal -->\n\n\t<div class="vertical_spacer6"></div>\n\t<div class="vertical_spacer6"></div>\n\n\n\n\n\n\n\n\n\t<script>\n        $(function () {\n        $(\'#myTab a:last\').tab(\'show\')\n    \t})\n      jQuery(document).ready(function($) {\n    \t$(".clickableRow").click(function() {\n            window.document.location = $(this).attr("href");\n        });\n     \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


