# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1390363582.903372
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/users.html'
_template_uri = 'users.html'
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
    return runtime._inherit_from(context, 'base_users.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\t\t')
        __M_writer('\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 111
        __M_writer('   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n\n\t\t\t<!-- /Initializing Tab Names, ETC-->\n\t         \n\t          <ul class="nav nav-tabs">\n\t            <li class="active">\t\t                    \n\t            <a href="#Overview" data-toggle="tab"><strong>Overview</strong></a>\n\t            </li>\n\t            <li>\n\t            <a href="#Admin" data-toggle="tab"><strong>Administrators</strong></a>\n\t            </li>\n\t            <li>\n\t            <a href="#Mgr" data-toggle="tab"><strong>Managers</strong></a>\n\t            </li>\n\t            <li>\n\t            <a href="#accessrights" data-toggle="tab"><strong>Access Rights</strong></a>\n\t            </li>\n\t            \n\t          </ul>\n\n\t\t\t<!-- /Overview Tab Content-->\n\n            <div class="tab-content">\n\n\t             <div class="tab-pane active" id="Overview">\n\t\t                   \n\t                     <table class = "table table-hover">\n\t                    \t<thead>\n\t                    \t\t<tr>\n\t                    \t\t\t<th>ID</th>\n\t                    \t\t\t<th>Username</th>\n\t                    \t\t\t<th>Given Names</th>\n\t                    \t\t\t<th>Surnames</th>\n\t                    \t\t\t<th>Role</th>\n\t                    \t\t\n\t                    \t\t\t<th>Address</th>\n\t                    \t\t\t<th>Phone</th>\n\t                    \t\t\t<th>Email</th>\n\n\t                    \t\t</tr>\n\t                    \t</thead>\n\t\t\t                    \t<tr onclick="imput" data-toggle="modal" href="#ProductItem">\n\t\t\t\t                    \t<td>123</td>\n\t\t\t\t                    \t<td>monkey123</td>\n\t\t\t\t                    \t<td>Bob</td>\n\t\t\t\t                    \t<td>Reamer</td>\n\t\t\t\t                    \t<td>\n\t\t\t\t                    \t\t<span class="label label-warning">Admin</span>\n\t\t\t\t                    \t</td>\n\n\t\t\t\t                    \t<td>123 Sesame Street...</td>\n\t\t\t\t                    \t<td>123-4567</td>\n\t\t\t\t                    \t<td>bob_reamer@byu.edu</td>\n\t\t\t\t                    \t\n\t\t\t\t\t\t\t\t    </tr>\n\n\t\t\t\t\t\t\t\t    <tr onclick="imput" data-toggle="modal" href="#ProductItem">\n\t\t\t\t                    \t<td>321</td>\n\t\t\t\t                    \t<td>pickme123</td>\n\t\t\t\t                    \t<td>Nancy</td>\n\t\t\t\t                    \t<td>Ford</td>\n\t\t\t\t                    \t<td>\n\t\t\t\t                    \t\t<span class="label label-info">Manager</span>\n\t\t\t\t                    \t</td>\n\n\t\t\t\t                    \t<td>123 Sesame Street...</td>\n\t\t\t\t                    \t<td>123-4567</td>\n\t\t\t\t                    \t<td>nancy_ford@byu.edu</td>\n\t\t\t\t\t\t\t\t    </tr>\n\n\t\t\t\t\t\t\t\t     \n\t\t\t\n\t\t                    \t</table>\n\t\t                 </div>\n\n\t\t                \n\t             \t\t\t<div class="tab-pane active" id="Admin">\n\n\t             \t\t\t</div>\n\t             \t\n\n\t            \n\t             \t\t\t<div class="tab-pane active" id="Mgr">\n\n\t             \t\t\t</div>\n\t          \n\n\t      \n\t             \t\t\t<div class="tab-pane active" id="accessrights">\n\n\t             \t\t\t</div>\n\t             \t\t\n\n\t\t                    </div>\n\n\t\t                    \n\t\t                    </div>\n\t\t                    <script>\n\t\t                        $(function () {\n\t\t                            $(\'#myTab a:last\').tab(\'show\')\n\t\t                        })\n\n\t\t                        jQuery(document).ready(function($) {\n\t\t\t\t\t\t\t      $(".clickableRow").click(function() {\n\t\t\t\t\t\t\t            window.document.location = $(this).attr("href");\n\t\t\t\t\t\t\t     });\n\t\t\t\t\t\t\t     \n\t\t                    </script>\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


