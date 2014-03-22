# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1395522122.716086
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/oldcheckoutstuff.html'
_template_uri = 'oldcheckoutstuff.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\t\t\t\t<div class="col-md-9">\r\n\r\n\t\t\t\t\t\r\n\t\t\t\t\t<form class ="form-horizontal" role="form" method ="POST">\r\n\t\t\t\t\t\t<ul class=\'list-unstyled\'>\r\n\t\t\t\t\t<!--   Loop through the fields of the form -->\r\n\t\t\t\t\t')
        # SOURCE LINE 7
        bSide = True
                                               
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['bSide'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 8
        __M_writer('\r\n')
        # SOURCE LINE 9
        for f in form:
            # SOURCE LINE 10
            __M_writer('\t\t\t\t\t\t\r\n')
            # SOURCE LINE 11
            if bSide:
                # SOURCE LINE 12
                __M_writer('\t\t\t\t\t  \t<li>\r\n\t\t\t\t\t  \t<ul class=\'list-inline\'>\r\n\t\t\t\t\t\t<li>\r\n\t\t\t\t\t    <div class="form-group">\r\n\t\t\t\t\t      <label class="col-sm-5 control-label" for="id_')
                # SOURCE LINE 16
                __M_writer(str( f.name ))
                __M_writer('">')
                __M_writer(str( f.label ))
                __M_writer('</label> <!-- the label -->\r\n\t\t\t\t\t        <div class="col-sm-7">\r\n\t\t\t\t\t          ')
                # SOURCE LINE 18
                __M_writer(str(f))
                __M_writer(' <!-- The input box -->\r\n\t\t\t\t\t          ')
                # SOURCE LINE 19
                __M_writer(str(f.errors))
                __M_writer('\r\n\t\t\t\t\t        </div>\r\n\t\t\t\t\t    </div>\r\n\t\t\t\t\t\t</li>\r\n\r\n')
                # SOURCE LINE 24
            else:
                # SOURCE LINE 25
                __M_writer('\t\t\t\t\t\t<li>\r\n\t\t\t\t\t    <div class="form-group">\r\n\t\t\t\t\t      <label class="col-sm-5 control-label" for="id_')
                # SOURCE LINE 27
                __M_writer(str( f.name ))
                __M_writer('">')
                __M_writer(str( f.label ))
                __M_writer('</label> <!-- the label -->\r\n\t\t\t\t\t        <div class="col-sm-7">\r\n\t\t\t\t\t          ')
                # SOURCE LINE 29
                __M_writer(str(f))
                __M_writer(' <!-- The input box -->\r\n\t\t\t\t\t          ')
                # SOURCE LINE 30
                __M_writer(str(f.errors))
                __M_writer('\r\n\t\t\t\t\t        </div>\r\n\t\t\t\t\t    </div>\r\n\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t\t</li>\r\n')
            # SOURCE LINE 37
            __M_writer('\t\t\t\t\t\t\r\n\t\t\t\t\t\t')
            # SOURCE LINE 38
 
            print(bSide)
            bSide = not bSide
            print(bSide)
            print('--------------')
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['bSide'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 43
            __M_writer('\r\n')
        # SOURCE LINE 45
        __M_writer('\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t  <div class="form-group">\r\n\t\t\t\t\t    <div class="col-sm-offset-4 col-sm-4">\r\n\t\t\t\t\t      <input class="btn btn-success" type="submit" value="Save">\r\n\t\t\t\t\t    </div>\r\n\t\t\t\t\t  </div>\r\n\t\t\t\t\t</form>\r\n\r\n\r\n\r\n\t\t\t</div>\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\t\t\t\t<div class="col-md-9">\r\n\r\n\t\t\t\t\t\r\n\t\t\t\t<div class=\'container-fluid\'>\r\n\t\t\t\t\t<form class ="form-horizontal" role="form" method ="POST">\r\n\t\t\t\t\t<!--   Loop through the fields of the form -->\r\n\t\t\t\t\t')
        # SOURCE LINE 71
        bSide = True
                                               
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['bSide'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 72
        __M_writer('\r\n')
        # SOURCE LINE 73
        for f in form:
            # SOURCE LINE 74
            __M_writer('\r\n')
            # SOURCE LINE 75
            if bSide:
                # SOURCE LINE 76
                __M_writer('\t\t\t\t\t  \t<div class=\'row\'>\r\n\r\n\t\t\t\t\t    <div class="form-group">\r\n\t\t\t\t\t      <label class="col-sm-2 control-label" for="id_')
                # SOURCE LINE 79
                __M_writer(str( f.name ))
                __M_writer('">')
                __M_writer(str( f.label ))
                __M_writer('</label> <!-- the label -->\r\n\t\t\t\t\t        <div class="col-sm-3">\r\n\t\t\t\t\t          ')
                # SOURCE LINE 81
                __M_writer(str(f))
                __M_writer(' <!-- The input box -->\r\n\t\t\t\t\t          ')
                # SOURCE LINE 82
                __M_writer(str(f.errors))
                __M_writer('\r\n\t\t\t\t\t        </div>\r\n\t\t\t\t\t    </div>\r\n\r\n')
                # SOURCE LINE 86
            else:
                # SOURCE LINE 87
                __M_writer('\t\t\t\t\t    <div class="form-group">\r\n\t\t\t\t\t      <label class="col-sm-offset-5 col-sm-2 control-label" for="id_')
                # SOURCE LINE 88
                __M_writer(str( f.name ))
                __M_writer('">')
                __M_writer(str( f.label ))
                __M_writer('</label> <!-- the label -->\r\n\t\t\t\t\t        <div class="col-sm-3">\r\n\t\t\t\t\t          ')
                # SOURCE LINE 90
                __M_writer(str(f))
                __M_writer(' <!-- The input box -->\r\n\t\t\t\t\t          ')
                # SOURCE LINE 91
                __M_writer(str(f.errors))
                __M_writer('\r\n\t\t\t\t\t        </div>\r\n\t\t\t\t\t    </div>\r\n')
            # SOURCE LINE 95
            __M_writer('\t\t\t\t\t\t\r\n\t\t\t\t\t\t')
            # SOURCE LINE 96
 
            print(bSide)
            bSide = not bSide
            print(bSide)
            print('--------------')
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['bSide'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 101
            __M_writer('\r\n')
        # SOURCE LINE 103
        __M_writer('\t\t\t\t\t\t</div>\r\n\t\t\t\t\t  <div class="form-group">\r\n\t\t\t\t\t    <div class="col-sm-offset-4 col-sm-4">\r\n\t\t\t\t\t      <input class="btn btn-success" type="submit" value="Save">\r\n\t\t\t\t\t    </div>\r\n\t\t\t\t\t  </div>\r\n\t\t\t\t\t</form>\r\n\r\n\t\t\t\t</div>\r\n\t\t\t\t\r\n\t\t\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


