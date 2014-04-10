# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397112389.251152
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
        serial = context.get('serial', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n\r\n$(function () {\r\n    $(\'#myTab a:last\').tab(\'show\');\r\n});\r\n\r\njQuery(document).ready(function($) {\r\n      $(".clickableRow").click(function() {\r\n            window.document.location = $(this).attr("href");\r\n      });\r\n});\r\n\r\n//Ajax call, basic example\r\n$(function() {\r\n')
        # SOURCE LINE 16
        for s in serial:
            # SOURCE LINE 17
            __M_writer("\t$('#item_button_")
            __M_writer(str(s.id))
            __M_writer("').off('click.item').on('click.item', function(){\r\n\r\n\t\t$('#item_button_")
            # SOURCE LINE 19
            __M_writer(str(s.id))
            __M_writer("').loadmodal({\r\n\t\t\turl: '/manager/item/")
            # SOURCE LINE 20
            __M_writer(str(s.id))
            __M_writer("',\r\n\t\t\tid: 'item_modal_")
            # SOURCE LINE 21
            __M_writer(str(s.id))
            __M_writer("',\r\n\t\t\ttitle: '<h2>Edit ")
            # SOURCE LINE 22
            __M_writer(str(s.catalogItem.manufacturer))
            __M_writer(' ')
            __M_writer(str(s.catalogItem.name))
            __M_writer(' - ')
            __M_writer(str(s.serialNum))
            __M_writer("</h2>',\r\n\t\t\twidth: '800px',\r\n\t\t\tajax: {\r\n\t\t\t\tdataType: 'html',\r\n\t\t\t\tmethod: 'POST',\r\n\t\t\t\tsuccess: function(data, status, xhr) {\r\n\t\t\t\t\tconsole.log($('#item_modal_")
            # SOURCE LINE 28
            __M_writer(str(s.id))
            __M_writer("'));\r\n\t\t\t\t},//\r\n\t\t\t// any other options from the regular $.ajax call (see JQuery docs)\r\n\t\t\t\r\n\t\t\t},\r\n\t\t});\r\n\t});\r\n")
        # SOURCE LINE 36
        __M_writer('});\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


