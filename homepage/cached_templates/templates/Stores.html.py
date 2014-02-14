# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391135349.698461
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/stores.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        urlStore = context.get('urlStore', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 179
        __M_writer('   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        urlStore = context.get('urlStore', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n\n')
        # SOURCE LINE 5
 

        __M_writer('\n\n\t<div class="media">\n\n\t  <p class="lead"><strong>')
        # SOURCE LINE 9
        __M_writer(str(urlStore.locationName))
        __M_writer(', ')
        __M_writer(str(urlStore.state))
        __M_writer('</strong>\n\t    <br/>\n\t    <small>Manager: Nancy Ford (this needs to change to be dynamic)</small>\n\t    <br/>\n\t    <small>Store: ')
        # SOURCE LINE 13
        __M_writer(str(urlStore.id))
        __M_writer('</small>\n\t  </p>\n\t  <hr/>\n\t  <img class="media-object" src="')
        # SOURCE LINE 16
        __M_writer(str( STATIC_URL))
        __M_writer('homepage/images/Provo_store.png" alt=\'Provo\'>\n\t  <hr/>\t\n\t</div>\n\t<div class="media-body">\t\n\t\n\t\n\t\n\n\t<address>\n\t\t<strong>MyStuff, Inc.</strong><br>\n\t\t')
        # SOURCE LINE 26
        __M_writer(str(urlStore.street1))
        __M_writer('<br>\n\t\t')
        # SOURCE LINE 27
        __M_writer(str(urlStore.street2))
        __M_writer('<br>\n\t\t')
        # SOURCE LINE 28
        __M_writer(str(urlStore.city))
        __M_writer(', ')
        __M_writer(str(urlStore.state))
        __M_writer(' ')
        __M_writer(str(urlStore.zipCode))
        __M_writer('<br>\n\t</address>\n\t</div>\n\n\t<button class="btn btn-success btn" data-toggle="modal" data-target="#ImageLibray">View Image Library</button>\n\n\t\t<!-- Modal -->\n\t\t<div class="modal fade" id="ImageLibray" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n\t\t  <div class="modal-dialog">\n\t\t    <div class="modal-content">\n\t\t      <div class="modal-header">\n\t\t        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t        <h4 class="modal-title" id="myModalLabel">Image Library</h4>\n\t\t      </div>\n\t\t      <div class="modal-body">\n\t\t        <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\n\t\t          <!-- Indicators -->\n\t\t          <ol class="carousel-indicators">\n\t\t            <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\n\t\t            <li data-target="#carousel-example-generic" data-slide-to="1"></li>\n\t\t            <li data-target="#carousel-example-generic" data-slide-to="2"></li>\n\t\t          </ol>\n\t\t          <!-- Wrapper for slides -->\n\t\t          <div class="carousel-inner">\n\t\t            <div class="item active">\n\t\t              <img src="')
        # SOURCE LINE 53
        __M_writer(str( STATIC_URL))
        __M_writer('homepage/images/NikonCamera.jpg" alt="Nikon Camera 1 V2" class="img-rounded">\n\t\t              <div class="carousel-caption">\n\t\t                IMG1.jpg\n\t\t              </div>\n\t\t            </div>\n\t\t            ...\n\t\t          </div>\n\t\t          <!-- Controls -->\n\t\t          <a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">\n\t\t            <span class="glyphicon glyphicon-chevron-left"></span>\n\t\t          </a>\n\t\t          <a class="right carousel-control" href="#carousel-example-generic" data-slide="next">\n\t\t            <span class="glyphicon glyphicon-chevron-right"></span>\n\t\t          </a>\n\t\t        </div>\t\t\n\n\t\t      </div>\n\t\t      <div class="modal-footer">\n\t\t        <button type="button" class="btn btn-primary">Add</button>\n\t\t        <!-- Provides extra visual weight and identifies the primary action in a set of buttons -->\n\t\t        <button type="button" class="btn btn-warning">Edit</button>\n\t\t        <!-- Delete Rental Item -->\n\t\t        <button type="button" class="btn btn-danger">Delete</button>\n\t\t        <button type="button" class="btn btn-success">Save</button>\n\t\t        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\t\t\n\n\t\t      </div>\n\t\t    </div>\n\t\t    <!-- /.modal-content -->\n\t\t  </div>\n\t\t  <!-- /.modal-dialog -->\n\t\t</div>\n\t\t<!-- /.modal -->\t\n\n\n\n\n\t<button class="btn btn-warning btn" data-toggle="modal" data-target="#Edit">Edit</button>\n\n\n\t\t<!-- Modal -->\n\t\t<div class="modal fade" id="Edit" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n\t\t  <div class="modal-dialog">\n\t\t    <div class="modal-content">\n\n\t\t      <div class="modal-header">\n\t\t        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t        <h4 class="modal-title" id="myModalLabel">Edit Store Information</h4>\n\t\t      </div>\n\n\t\t      <div class="modal-body">\n\n\n\t\t\t      <form class ="form-horizontal" role="form" method ="POST">\n\n')
        # SOURCE LINE 108
        for field in form:
            # SOURCE LINE 109
            __M_writer('\n\t\t\t          <div class="form-group">\n\t\t\t            <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 111
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n\t\t\t              <div class="col-sm-4">\n\t\t\t              \t')
            # SOURCE LINE 113
            __M_writer(str(field))
            __M_writer('\n\t\t\t                <!-- <input type="text" class="form-control" name="')
            # SOURCE LINE 114
            __M_writer(str( field.name ))
            __M_writer('" id="id_')
            __M_writer(str( field.name ))
            __M_writer('"> -->\n\t\t\t              </div>\n\t\t\t          </div>\n\n')
        # SOURCE LINE 119
        __M_writer('\n\t\t\t        <div class="form-group">\n\t\t\t          <div class="col-sm-offset-4 col-sm-4">\n\t\t\t            <input class="btn btn-success" type="submit" value="Save">\n\t\t\t          </div>\n\t\t\t        </div>\n\t\t\t      </form>\n\n\t\t      </div>\n\n\n\t\t    </div>\n\t\t    <!-- /.modal-content -->\n\t\t  </div>\n\t\t  <!-- /.modal-dialog -->\n\t\t</div>\n\t\t<!-- /.modal -->\t\n\n\n\t<button class="btn btn-danger" data-toggle="modal" data-target="#Delete">Delete</button>\n\n\t<!-- Modal -->\n\t<div class="modal fade" id="Delete" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n\t  <div class="modal-dialog">\n\t    <div class="modal-content">\n\n\t      <div class="modal-header">\n\t        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t        <h4 class="modal-title" id="myModalLabel">Delete Store</h4>\n\t      </div>\n\n\t      <div class="modal-body">\n\t\t      <h3>Are you sure you want to delete this store? \n\t\t      <br/>\n\t\t      You will not be able to undo this action.</h3>\n\t      </div>\n\n\t      <div class="modal-footer">\n\t      \t<a href="/homepage/stores/')
        # SOURCE LINE 157
        __M_writer(str(urlStore.id))
        __M_writer('/delete" class="btn btn-success">Yes</a>\n\t        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t      </div>\n\t    </div>\n\t    <!-- /.modal-content -->\n\t  </div>\n\t  <!-- /.modal-dialog -->\n\t</div>\n\t<!-- /.modal -->\n\n\t<div class="vertical_spacer6"></div>\n\n\t<script>\n        $(function () {\n        $(\'#myTab a:last\').tab(\'show\')\n    \t})\n      jQuery(document).ready(function($) {\n    \t$(".clickableRow").click(function() {\n            window.document.location = $(this).attr("href");\n        });\n     \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


