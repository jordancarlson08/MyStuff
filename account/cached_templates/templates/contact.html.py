# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389742124.613429
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\homepage\\templates/contact.html'
_template_uri = 'contact.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 46
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\t\n\n\t  <h2>Contact Us</h2>\n\n\t  <p>We are here to answer any questions you have about MyStuff and digital photography in general.</p>\n\t  <p>If there is something you want or need even if you can not find it on our website, let us know and we will do everything we can to help you find it.</p>\n\t  <div class="vertical_spacer6"></div>\n\t  <form class="form-horizontal" role="form">\n\t  \t<div class="form-group">\n\t  \t\t<label for="inputName" class="col-sm-2 control-label">Name</label>\n\t  \t\t<div class="col-sm-5">\n\t  \t\t\t<input type="text" class="form-control" id="inputName" placeholder="Name">\n\t  \t\t</div>\n\t  \t</div>\n\t  \t<div class="form-group">\n\t  \t\t<label for="inputEmail" class="col-sm-2 control-label">Email</label>\n\t  \t\t<div class="col-sm-5">\n\t  \t\t\t<input type="email" class="form-control" id="inputEmail" placeholder="Email">\n\t  \t\t</div>\n\t  \t</div>\n\t  \t<div class="form-group">\n\t  \t\t<label for="inputSubject" class="col-sm-2 control-label">Subject</label>\n\t  \t\t<div class="col-sm-5">\n\t  \t\t\t<input type="text" class="form-control" id="inputSubject" placeholder="Subject">\n\t  \t\t</div>\n\t  \t</div>\n\t  \t<div class="form-group">\n\t  \t\t<label for="inputMessage" class="col-sm-2 control-label">Message</label>\n\t  \t\t<div class="col-sm-5">\n\t  \t\t\t<textarea class="form-control" rows="6" id="inputMessage" placeholder="Message"></textarea>\n\t  \t\t</div>\n\t  \t</div>\n\t  \t<div class="form-group">\n\t  \t\t<label class="col-sm-2 control-label"></label>\n\t  \t\t<div class="col-sm-5">\n\t  \t\t\t<button type="submit" class="btn btn-primary">Send</button>\n\t  \t\t</div>\n\t  \t</div>\n\t  </form>\t\t\n\t  <div class="vertical_spacer6"></div>\t\t\n\n\t\t\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


