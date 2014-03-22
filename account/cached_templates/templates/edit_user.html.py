# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393567612.631158
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/edit_user.html'
_template_uri = 'edit_user.html'
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
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        c = context.get('c', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        c = context.get('c', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n')
        # SOURCE LINE 6
        if c != '':
            # SOURCE LINE 7
            __M_writer('<div class=\'text-center\'>\n  <div class="alert alert-success">\n    <h3>')
            # SOURCE LINE 9
            __M_writer(str(c))
            __M_writer('</h3>\n  </div>\n</div>\n<br/>\n')
        # SOURCE LINE 14
        __M_writer('\n<form class ="form-horizontal" role="form" method ="POST" action=\'/account/user__edit/')
        # SOURCE LINE 15
        __M_writer(str(user.id))
        __M_writer("/'>\n\n")
        # SOURCE LINE 17
        for field in form:
            # SOURCE LINE 18
            __M_writer('  \n    <div class="form-group">\n      <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 20
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n        <div class="col-sm-6">\n          ')
            # SOURCE LINE 22
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\n        </div>\n    </div>\n\n')
        # SOURCE LINE 27
        __M_writer('\n\n  <div class="form-group">\n    <div class="col-sm-offset-4 col-sm-4">\n      <input class="btn btn-success" type="submit" value="Save Changes">\n    </div>\n  </div>\n\n</form>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


