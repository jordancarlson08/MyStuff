# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389337397.260977
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\base_app\\templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


# SOURCE LINE 5
from base_app import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <link href=\'http://fonts.googleapis.com/css?family=Poiret+One\' rel=\'stylesheet\' type=\'text/css\'>\n    <meta content="/homepage/images/camera_icon_75.png" itemprop="image">\n    <title>MyStuff</title>\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>\n  \n')
        # SOURCE LINE 18
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body><div id="container">\n\n  <!-- #################### HEADER ####################################### -->\n  <div id="header">\n    <h1>\n      <a href="../" title="Home"><img src="')
        # SOURCE LINE 26
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/images/camera_icon_75.png" width="75" height="75" alt="My Stuff" /></a>\n    </h1>\n    <h5>My Stuff - Digital Life My Way</h5>\n    <div id="nav">\n      <ul>\n        \n        <li><a href="../homepage/index" title="Home">Home</a></li>\n        <li><a href="../homepage/about" title="About Us">About</a></li>\n        <li><a href="../homepage/contact" title="Get in Touch">Contact Us</a></li>\n        <li><a href="../homepage/terms" title="Terms">Terms</a></li>\n      </ul>\n    </div>\n    \n  </div>\n  \n\n    \n\n\n  \n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 48
        __M_writer('  \n  \n')
        # SOURCE LINE 51
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 46
        __M_writer('\n      Site content goes here in sub-templates.\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


