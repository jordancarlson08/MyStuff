# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1390623116.603147
_enable_loop = True
_template_filename = 'D:\\Google Drive\\MyStuff Website\\MyStuff\\homepage\\templates/Storescopy.html'
_template_uri = 'Storescopy.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 100
        __M_writer('   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n\n\t<div class="media">\n\n\t\t<p class="lead"><strong>Provo, Utah - 123</strong><br/>\n\t\t<small>Manager: Nancy Ford</small></p>\n\t\t<hr/>\n\n\n   \t\t\t<img class="media-object" src ="')
        # SOURCE LINE 12
        __M_writer(str( STATIC_URL))
        __M_writer('homepage/images/Provo_store.png" alt=\'Provo\'>\n\n    \t</div class="media-body">\n\n\t\t<hr/>\n\t\t                         \t\t\n\n\t\t                         \t\t<address>\n\t\t\t\t\t\t\t\t\t        <strong>MyStuff, Inc.</strong><br>\n\t\t\t\t\t\t\t\t\t        1475 W. Center Street<br>\n\t\t\t\t\t\t\t\t\t        Provo, UT 84057<br>\n\t\t\t\t\t\t\t\t\t     </address>\n\t\t                         \t</div>\n\t\t                         \t <button class="btn btn-success btn" data-toggle="modal" data-target="#CatalogItem">\n\t\t\t\t\t\t\t\t  \t\t\tView Image Library\n\t\t\t\t\t\t\t\t\t\t</button>\n\n\t\t\t\t\t\t\t<!-- Modal -->\n\t\t\t\t\t\t\t\t<div class="modal fade" id="CatalogItem" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n\t\t\t\t\t\t\t\t  <div class="modal-dialog">\n\t\t\t\t\t\t\t\t    <div class="modal-content">\n\t\t\t\t\t\t\t\t      <div class="modal-header">\n\t\t\t\t\t\t\t\t        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t\t\t\t\t\t\t        <h4 class="modal-title" id="myModalLabel">Image Library</h4>\n\t\t\t\t\t\t\t\t      </div>\n\t\t\t\t\t\t\t\t      <div class="modal-body">\n\n\t\t\t\t\t\t\t\t      <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">\n\t\t\t\t\t\t\t\t\t\t  <!-- Indicators -->\n\t\t\t\t\t\t\t\t\t\t  <ol class="carousel-indicators">\n\t\t\t\t\t\t\t\t\t\t    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>\n\t\t\t\t\t\t\t\t\t\t    <li data-target="#carousel-example-generic" data-slide-to="1"></li>\n\t\t\t\t\t\t\t\t\t\t    <li data-target="#carousel-example-generic" data-slide-to="2"></li>\n\t\t\t\t\t\t\t\t\t\t  </ol>\n\n\t\t\t\t\t\t\t\t\t\t  <!-- Wrapper for slides -->\n\t\t\t\t\t\t\t\t\t\t  <div class="carousel-inner">\n\t\t\t\t\t\t\t\t\t\t    <div class="item active">\n\t\t\t\t\t\t\t\t\t\t      <img src="')
        # SOURCE LINE 50
        __M_writer(str( STATIC_URL))
        __M_writer('homepage/images/NikonCamera.jpg" alt="Nikon Camera 1 V2" class="img-rounded">\n\t\t\t\t\t\t\t\t\t\t      <div class="carousel-caption">\n\t\t\t\t\t\t\t\t\t\t        IMG1.jpg\n\t\t\t\t\t\t\t\t\t\t      </div>\n\t\t\t\t\t\t\t\t\t\t    </div>\n\t\t\t\t\t\t\t\t\t\t    ...\n\t\t\t\t\t\t\t\t\t\t  </div>\n\n\t\t\t\t\t\t\t\t\t\t  <!-- Controls -->\n\t\t\t\t\t\t\t\t\t\t  <a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">\n\t\t\t\t\t\t\t\t\t\t    <span class="glyphicon glyphicon-chevron-left"></span>\n\t\t\t\t\t\t\t\t\t\t  </a>\n\t\t\t\t\t\t\t\t\t\t  <a class="right carousel-control" href="#carousel-example-generic" data-slide="next">\n\t\t\t\t\t\t\t\t\t\t    <span class="glyphicon glyphicon-chevron-right"></span>\n\t\t\t\t\t\t\t\t\t\t  </a>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t        \n\t\t\t\t\t\t\t\t      </div>\n\t\t\t\t\t\t\t\t      <div class="modal-footer">\n\t\t\t\t\t\t\t\t      <button type="button" class="btn btn-success">Add</button>\n\n\t\t\t\t\t\t\t\t      <!-- Provides extra visual weight and identifies the primary action in a set of buttons -->\n\t\t\t\t\t\t\t\t\t\t<button type="button" class="btn btn-success">Edit</button>\n\t\t\t\t\t\t\t\t\t\t<!-- Delete Rental Item -->\n\t\t\t\t\t\t\t\t\t\t<button type="button" class="btn btn-success">Delete</button>\n\t\t\t\t\t\t\t\t\t\t<button type="button" class="btn btn-success">Save</button>\n\n\t\t\t\t\t\t\t\t        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t      </div>\n\t\t\t\t\t\t\t\t    </div><!-- /.modal-content -->\n\t\t\t\t\t\t\t\t  </div><!-- /.modal-dialog -->\n\t\t\t\t\t\t\t\t</div><!-- /.modal -->\n\n\t\t                         \t<button type="button" class="btn btn-info">Edit</button>\n  <button type="button" class="btn btn-danger">Delete</button>\n\t\t                         <div>\t\t\n\n\n\n\t<script>\n        $(function () {\n        $(\'#myTab a:last\').tab(\'show\')\n    \t})\n      jQuery(document).ready(function($) {\n    \t$(".clickableRow").click(function() {\n            window.document.location = $(this).attr("href");\n        });\n     \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


