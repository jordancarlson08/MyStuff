# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396840300.233106
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\scripts/inventory.jsm'
_template_uri = 'inventory.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n\r\n$(function () {\r\n    $(\'#myTab a:last\').tab(\'show\');\r\n});\r\n\r\njQuery(document).ready(function($) {\r\n      $(".clickableRow").click(function() {\r\n            window.document.location = $(this).attr("href");\r\n      });\r\n});\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


