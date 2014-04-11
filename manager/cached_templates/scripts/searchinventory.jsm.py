# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397244986.367499
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\scripts/searchinventory.jsm'
_template_uri = 'searchinventory.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\njQuery(document).ready(function($) {\r\n    $(".clickableRow").click(function() {\r\n          window.document.location = $(this).attr("href");\r\n    });\r\n});\r\n\r\n\r\n$(function() {\r\n    var hash = window.location.hash;\r\n    hash && $(\'ul.nav a[href="\' + hash + \'"]\').tab(\'show\');\r\n});\r\n\t\r\n\r\n\r\n\r\n')
        # SOURCE LINE 18
        for i in rental:
            # SOURCE LINE 19
            __M_writer("$(function() {\r\n\r\n  $('#rent_")
            # SOURCE LINE 21
            __M_writer(str(i.id))
            __M_writer("').off('click.add').on('click.add', function(){\r\n\r\n\t$('#rent_")
            # SOURCE LINE 23
            __M_writer(str(i.id))
            __M_writer("').animate({\r\n\t\t'left':'0px',\r\n\t\twidth: '141px',\r\n\t\theight:'34px',\r\n\t});\r\n\t$('#rent_")
            # SOURCE LINE 28
            __M_writer(str(i.id))
            __M_writer('\').html(\'<span class="glyphicon glyphicon-ok"></span>&nbsp; Added to Cart!\');\r\n\t$(\'#tr_')
            # SOURCE LINE 29
            __M_writer(str(i.id))
            __M_writer("').css('text-decoration','line-through');\r\n\r\n\r\n\t//Add the rental to the cart\r\n\r\n\tconsole.log('/catalog/cart__add/")
            # SOURCE LINE 34
            __M_writer(str(i.id))
            __M_writer('/1/rental/\');\r\n\t$.ajax({\r\n\t\ttype: "POST",\r\n\t\turl: \'/catalog/cart__add/')
            # SOURCE LINE 37
            __M_writer(str(i.id))
            __M_writer("/1/rental/',\r\n\t});\r\n\r\n  });\r\n\r\n\t// \tvar isClicked = false;\r\n\r\n\t// $('#title_")
            # SOURCE LINE 44
            __M_writer(str(i.id))
            __M_writer("').off('click.add').on('click.add', function(){\r\n\r\n\r\n\r\n\t// \tif (isClicked === false)\r\n\t// \t{\r\n\t// \t\t$('#title_")
            # SOURCE LINE 50
            __M_writer(str(i.id))
            __M_writer('\').html(\'<span class="glyphicon glyphicon-minus"></span>&nbsp;\');\r\n\t// \t\tisClicked= !isClicked;\r\n\t// \t\treturn isClicked;\r\n\t// \t}\r\n\t// \telse\r\n\t// \t{\r\n\t// \t\t$(\'#title_')
            # SOURCE LINE 56
            __M_writer(str(i.id))
            __M_writer('\').html(\'<span class="glyphicon glyphicon-plus"></span>&nbsp;\');\r\n\t// \t\tisClicked= !isClicked;\r\n\t// \t\treturn isClicked;\r\n\t// \t}\r\n\r\n\t// });\r\n\r\n\t// $(\'#collapse_')
            # SOURCE LINE 63
            __M_writer(str(i.id))
            __M_writer('\').on(\'hidden.bs.collapse\', function () {\r\n\t// \tconsole.log("hidden!!!");\r\n\t// });\r\n\t// $(\'#collapse_')
            # SOURCE LINE 66
            __M_writer(str(i.id))
            __M_writer('\').on(\'show.bs.collapse\', function () {\r\n\t// \tconsole.log("Show!!!");\r\n\t// });\r\n\r\n\r\n\r\n\r\n});\r\n')
        # SOURCE LINE 75
        __M_writer("\r\n$(function() {\r\n\r\n\t//This sorts the list by manufacturer\r\n\t$('#select_man').change(function(event) {\r\n\t\tvar url = '/manager/searchinventory/';\r\n\t\tvar value = ($('#select_man').val());\r\n\t\tvar url2;\r\n\t\tif (value === 'A - Z'){\r\n\t\t\turl2 = 'manufacturer/';\r\n\t\t} else if (value == 'Z - A') {\r\n\t\t\turl2 = 'manufacturer/-';\r\n\t\t} else {\r\n\t\t\turl2 = '';\r\n\t\t}\r\n\r\n\t\tvar newurl = url+url2;\r\n\t\twindow.location.href = newurl;\r\n\t});\r\n\r\n\r\n\t$('#select_name').change(function(event) {\r\n\t\tvar url = '/manager/searchinventory/';\r\n\t\tvar value = ($('#select_name').val());\r\n\t\tvar url2;\r\n\t\tif (value === 'A - Z'){\r\n\t\t\turl2 = 'name/';\r\n\t\t} else if (value == 'Z - A') {\r\n\t\t\turl2 = 'name/-';\r\n\t\t} else {\r\n\t\t\turl2 = '';\r\n\t\t}\r\n\r\n\t\tvar newurl = url+url2;\r\n\t\twindow.location.href = newurl;\r\n\t});\r\n\r\n\t$('#select_price').change(function(event) {\r\n\t\tvar url = '/manager/searchinventory/';\r\n\t\tvar value = ($('#select_price').val());\r\n\t\tvar url2;\r\n\t\tif (value === 'Low - High'){\r\n\t\t\turl2 = 'listPrice/';\r\n\t\t} else if (value == 'High - Low') {\r\n\t\t\turl2 = 'listPrice/-';\r\n\t\t} else {\r\n\t\t\turl2 = '';\r\n\t\t}\r\n\r\n\t\tvar newurl = url+url2;\r\n\t\twindow.location.href = newurl;\r\n\t});\r\n\r\n\t$('#select_cost').change(function(event) {\r\n\t\tvar url = '/manager/searchinventory/';\r\n\t\tvar value = ($('#select_cost').val());\r\n\t\tvar url2;\r\n\t\tif (value === 'Low - High'){\r\n\t\t\turl2 = 'cost/';\r\n\t\t} else if (value == 'High - Low') {\r\n\t\t\turl2 = 'cost/-';\r\n\t\t} else {\r\n\t\t\turl2 = '';\r\n\t\t}\r\n\r\n\t\tvar newurl = url+url2;\r\n\t\twindow.location.href = newurl;\r\n\t});\r\n\r\n\t$('#select_cat').change(function(event) {\r\n\t\tvar url = '/manager/searchinventory/';\r\n\t\tvar value = ($('#select_cat').val());\r\n\t\tvar url2;\r\n\t\tif (value === 'A - Z'){\r\n\t\t\turl2 = 'category/';\r\n\t\t} else if (value == 'Z - A') {\r\n\t\t\turl2 = 'category/-';\r\n\t\t} else {\r\n\t\t\turl2 = '';\r\n\t\t}\r\n\r\n\t\tvar newurl = url+url2;\r\n\t\twindow.location.href = newurl;\r\n\t});\r\n\r\n\t$('#select_views').change(function(event) {\r\n\t\tvar url = '/manager/searchinventory/';\r\n\t\tvar value = ($('#select_views').val());\r\n\t\tvar url2;\r\n\t\tif (value === 'Low - High'){\r\n\t\t\turl2 = 'views/';\r\n\t\t} else if (value == 'High - Low') {\r\n\t\t\turl2 = 'views/-';\r\n\t\t} else {\r\n\t\t\turl2 = '';\r\n\t\t}\r\n\r\n\t\tvar newurl = url+url2;\r\n\t\twindow.location.href = newurl;\r\n\t});\r\n\r\n});\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


