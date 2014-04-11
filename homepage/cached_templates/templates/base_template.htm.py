# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397239780.938365
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\base_app\\templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['shopping_cart_navigation_option', 'top', 'main']


# SOURCE LINE 5
from base_app import static_files 

# SOURCE LINE 23
from base_app import global_static 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n')
        # SOURCE LINE 5
        __M_writer('\r\n')
        # SOURCE LINE 6
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n\r\n  <head>\r\n    <title>MyStuff Digital Life My Way</title>\r\n    <meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'>\r\n    <meta name="description" content="MyStuff Digital Life My Way offers the best digital cameras, film cameras, lenses, accessories, rentals and repairs."></meta>\r\n    <meta name="keywords" content="Camera, film, rental, repair, digital photography, film photography"></meta>\r\n\r\n    <link rel="icon" type="image/x-icon"  href="/static/base_app/images/favicon.ico">      \r\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>\r\n\r\n  \r\n')
        # SOURCE LINE 23
        __M_writer('    ')
        __M_writer('\r\n    ')
        # SOURCE LINE 24
        __M_writer(str( global_static.SITE_WIDE_CSS ))
        __M_writer('\r\n    ')
        # SOURCE LINE 25
        __M_writer(str( global_static.SITE_WIDE_JS ))
        __M_writer('\r\n\r\n')
        # SOURCE LINE 28
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n\r\n  <body>\r\n\r\n    ')
        # SOURCE LINE 34
 
        from base_app.user_util import manager_check, employee_check
        
        isEmployee = employee_check(request.user)
        isManager = manager_check(request.user)
        
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['isManager','isEmployee','manager_check','employee_check'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 40
        __M_writer('\r\n\r\n\r\n\r\n     <div id="fb-root"></div>\r\n\r\n  <nav class="navbar navbar-default" role="navigation">\r\n  <!-- Brand and toggle get grouped for better mobile display -->\r\n  <div class="navbar-header">\r\n    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n      <span class="sr-only">Toggle navigation</span>\r\n      <span class="icon-bar"></span>\r\n      <span class="icon-bar"></span>\r\n      <span class="icon-bar"></span>\r\n    </button>\r\n    <a class="navbar-brand" href="/index/" title="Home"><img src="/static/homepage/images/camera_icon.png" width="90" /></a>\r\n    <a class="navbar-brand-custom" href="/index/">My Stuff - Digital Life My Way</a>\r\n\r\n  </div>\r\n\r\n  <!-- Collect the nav links, forms, and other content for toggling -->\r\n<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n\r\n    <ul class="nav navbar-nav navbar-right">\r\n      <li>\r\n        <form class="navbar-form navbar-left" role="form" method ="GET" action=\'/catalog/category/\'>\r\n          <div class="form-group">\r\n            <input type="text" name=\'search\' class="form-control" placeholder="Search...">\r\n          </div>\r\n          <button type="submit" class="btn btn-default"><span class="glyphicon glyphicon-search"></span></button>\r\n        </form>\r\n      </li>\r\n      <!--placing most overhead options in a block prevents managers from seeing unnecessary items-->\r\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shopping_cart_navigation_option'):
            context['self'].shopping_cart_navigation_option(**pageargs)
        

        # SOURCE LINE 98
        __M_writer('\r\n\r\n')
        # SOURCE LINE 100
        if request.user.is_anonymous() == True:
            # SOURCE LINE 101
            __M_writer("      <li>\r\n      <a id='login_button' href='#'>\r\n      LOG IN\r\n      </a></li>\r\n\r\n")
            # SOURCE LINE 106
        else:
            # SOURCE LINE 107
            __M_writer('      <li>\r\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">')
            # SOURCE LINE 108
            __M_writer(str(request.user.username))
            __M_writer(' <b class="caret"></b></a>\r\n        <ul class="dropdown-menu">\r\n')
            # SOURCE LINE 110
            if isEmployee == True:
                # SOURCE LINE 111
                __M_writer('          <li><a href="/manager/dash/"><span class=\'glyphicon glyphicon-globe\'></span>&nbsp; DASHBOARD</a></li>\r\n          <li><a href="/manager/employee/')
                # SOURCE LINE 112
                __M_writer(str(request.user.id))
                __M_writer('"><span class=\'glyphicon glyphicon-edit\'></span>&nbsp; MY ACCOUNT</a></li>\r\n')
                # SOURCE LINE 113
            else:
                # SOURCE LINE 114
                __M_writer('          <li><a href="/account/myorders/"><span class=\'glyphicon glyphicon-inbox\'></span>&nbsp; MY ORDERS</a></li>\r\n          <li><a href="/account/myrentals/"><span class=\'glyphicon glyphicon-camera\'></span>&nbsp; MY RENTALS</a></li>\r\n          <li><a href="/account/myrepairs/"><span class=\'glyphicon glyphicon-wrench\'></span>&nbsp; MY REPAIRS</a></li>\r\n          <li><a href="/account/user/')
                # SOURCE LINE 117
                __M_writer(str(request.user.id))
                __M_writer('"><span class=\'glyphicon glyphicon-edit\'></span>&nbsp; MY ACCOUNT</a></li>\r\n')
            # SOURCE LINE 119
            __M_writer('          <li><a href="/account/logout/"><span class=\'glyphicon glyphicon-log-out\'></span>&nbsp; LOGOUT</a></li>\r\n        </ul>\r\n\r\n      </li>\r\n\r\n')
        # SOURCE LINE 125
        __M_writer('\r\n    </ul>\r\n\r\n    \r\n  </div><!-- /.navbar-collapse -->\r\n</nav>\r\n  \r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 134
        __M_writer('\r\n\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 141
        __M_writer('  \r\n\r\n')
        # SOURCE LINE 143
 

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n\r\n\r\n\r\n<!-- Footer-->\r\n\r\n<footer>\r\n      \r\n\r\n  <div class="container">\r\n    <div class="row">\r\n      <div class="col-md-4">\r\n        <ul class="list-unstyled">\r\n          <li class="title">Home</li>\r\n          <li><a href="/account/newuser/">New Account</a></li>\r\n          <li><a href="/catalog/category">Search Products</a></li>\r\n        </ul>\r\n      </div>\r\n      <div class="col-md-4">\r\n        <ul class="list-unstyled">\r\n          <li class="title">About</li>\r\n          <li><a href="/about/">About Us</a></li>\r\n          <li><a href="/locations/">Locations</a></li>\r\n        </ul>\r\n      </div>\r\n      <div class="col-md-3">\r\n        <ul class="list-unstyled">\r\n          <li class="title">Help</li>\r\n          <li><a href="/contact/">Contact Us</a></li>\r\n          <li><a href="/terms/">Rental Policy</a></li>\r\n          <li><a href="/account/newuser/">Repair Terms</a></li>\r\n\r\n        </ul>\r\n      </div>\r\n\r\n      <div class="col-md-1">\r\n        <ul class="list-unstyled">\r\n          <li><a href="https://www.facebook.com/digitallifemyway"><img src="/static/homepage/images/facebook.png" /></a></li>\r\n          <li><a href="https://plus.google.com/"><img src="/static/homepage/images/google.png" /></a></li>\r\n          <li><a href="https://www.twitter.com/"><img src="/static/homepage/images/twitter.png" /></a></li>\r\n        </ul>\r\n      </div>\r\n\r\n\r\n    </div>\r\n  </div>\r\n\r\n</footer> \r\n    \r\n\r\n\r\n  \r\n\r\n  \r\n')
        # SOURCE LINE 199
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n  \r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shopping_cart_navigation_option(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context)
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(' ')
 

        __M_writer('\r\n\r\n      <li>\r\n        <a id=\'cart_button\' href="#">\r\n          <span class="glyphicon glyphicon-shopping-cart"></span>&nbsp; MY CART\r\n\r\n          ')
        # SOURCE LINE 79
 
        from base_app.user_util import manager_check, employee_check
        
        isEmployee = employee_check(request.user)
        isManager = manager_check(request.user)
        
        cart = request.session.get('cart', {})
        rent = request.session.get('rent', {})
        repair = request.session.get('repair', {})
        cart_length = len(cart.keys()) + len(rent.keys()) + len(repair.keys())
        
        
        
        # SOURCE LINE 90
        __M_writer('\r\n\r\n')
        # SOURCE LINE 92
        if cart_length !=0:
            # SOURCE LINE 93
            __M_writer('          <span id=\'cart_length\' class="badge alert-custom">')
            __M_writer(str(cart_length))
            __M_writer('</span>\r\n')
        # SOURCE LINE 95
        __M_writer('        </a>\r\n      </li>\r\n      \r\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        __M_writer = context.writer()
        # SOURCE LINE 133
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 139
        __M_writer('\r\n  Site content goes here in sub-templates.\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


