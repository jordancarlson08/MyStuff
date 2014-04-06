# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396797998.030418
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\scripts/repairs.jsm'
_template_uri = 'repairs.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        repairs = context.get('repairs', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\njQuery(document).ready(function($) {\r\n    $(".clickableRow").click(function() {\r\n          window.document.location = $(this).attr("href");\r\n    });\r\n});\r\n\r\n\r\n\r\n')
        # SOURCE LINE 11
        for r in repairs:
            # SOURCE LINE 12
            __M_writer("$(function() {\r\n\r\n  $('#add_button_")
            # SOURCE LINE 14
            __M_writer(str(r.id))
            __M_writer("').off('click.add').on('click.add', function(){\r\n\r\n\t$('#add_button_")
            # SOURCE LINE 16
            __M_writer(str(r.id))
            __M_writer("').animate({\r\n\t\t'left':'0px',\r\n\t\twidth: '141px',\r\n\t\theight:'34px',\r\n\t});\r\n\t$('#add_button_")
            # SOURCE LINE 21
            __M_writer(str(r.id))
            __M_writer('\').html(\'<span class="glyphicon glyphicon-ok"></span>&nbsp; Added to Cart!\');\r\n\r\n\t//Add the rental to the cart\r\n\r\n\tconsole.log(\'/catalog/cart__add/')
            # SOURCE LINE 25
            __M_writer(str(r.id))
            __M_writer('/1/repair/\');\r\n\t$.ajax({\r\n\t\ttype: "POST",\r\n\t\turl: \'/catalog/cart__add/')
            # SOURCE LINE 28
            __M_writer(str(r.id))
            __M_writer("/1/repair/',\r\n\t\t\r\n\t});\r\n  });\r\n\r\n  $('#complete_button_")
            # SOURCE LINE 33
            __M_writer(str(r.id))
            __M_writer("').off('click.add').on('click.add', function(){\r\n\r\n\t$('#complete_button_")
            # SOURCE LINE 35
            __M_writer(str(r.id))
            __M_writer('\').html(\'<span class="glyphicon glyphicon-check"></span>\');\r\n\tconsole.log(\'/manager/repairs__complete/')
            # SOURCE LINE 36
            __M_writer(str(r.id))
            __M_writer('/\');\r\n\t$.ajax({\r\n\t\ttype: "POST",\r\n\t\turl: \'/manager/repairs__complete/')
            # SOURCE LINE 39
            __M_writer(str(r.id))
            __M_writer("/',\r\n\t\t\r\n\t});\r\n  });\r\n\r\n\r\n});\r\n")
        # SOURCE LINE 47
        __M_writer('\r\n$(function() {\r\n\r\n\r\n\r\n});')
        return ''
    finally:
        context.caller_stack._pop_frame()


