# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397177093.28641
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/base_app/templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main', 'top', 'shopping_cart_navigation_option']


# SOURCE LINE 5
from base_app import static_files 

# SOURCE LINE 23
from base_app import global_static 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n\n  <head>\n    <title>MyStuff Digital Life My Way</title>\n    <meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'>\n    <meta name="description" content="MyStuff Digital Life My Way offers the best digital cameras, film cameras, lenses, accessories, rentals and repairs."></meta>\n    <meta name="keywords" content="Camera, film, rental, repair, digital photography, film photography"></meta>\n\n    <link rel="icon" type="image/x-icon"  href="/static/base_app/images/favicon.ico">      \n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>\n\n  \n')
        # SOURCE LINE 23
        __M_writer('    ')
        __M_writer('\n    ')
        # SOURCE LINE 24
        __M_writer(str( global_static.SITE_WIDE_CSS ))
        __M_writer('\n    ')
        # SOURCE LINE 25
        __M_writer(str( global_static.SITE_WIDE_JS ))
        __M_writer('\n\n')
        # SOURCE LINE 28
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n  </head>\n\n  <body>\n\n    ')
        # SOURCE LINE 34
 
        from base_app.user_util import manager_check, employee_check
        
        isEmployee = employee_check(request.user)
        isManager = manager_check(request.user)
        
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['employee_check','isEmployee','manager_check','isManager'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 40
        __M_writer('\n\n\n\n     <div id="fb-root"></div>\n\n  <nav class="navbar navbar-default" role="navigation">\n  <!-- Brand and toggle get grouped for better mobile display -->\n  <div class="navbar-header">\n    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n      <span class="sr-only">Toggle navigation</span>\n      <span class="icon-bar"></span>\n      <span class="icon-bar"></span>\n      <span class="icon-bar"></span>\n    </button>\n    <a class="navbar-brand" href="/index/" title="Home"><img src="/static/homepage/images/camera_icon.png" width="90" /></a>\n    <a class="navbar-brand-custom" href="/index/">My Stuff - Digital Life My Way</a>\n\n  </div>\n\n  <!-- Collect the nav links, forms, and other content for toggling -->\n<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n\n    <ul class="nav navbar-nav navbar-right">\n      <li>\n        <form class="navbar-form navbar-left" role="form" method ="GET" action=\'/catalog/category/\'>\n          <div class="form-group">\n            <input type="text" name=\'search\' class="form-control" placeholder="Search...">\n          </div>\n          <button type="submit" class="btn btn-default"><span class="glyphicon glyphicon-search"></span></button>\n        </form>\n      </li>\n      <!--placing most overhead options in a block prevents managers from seeing unnecessary items-->\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shopping_cart_navigation_option'):
            context['self'].shopping_cart_navigation_option(**pageargs)
        

        # SOURCE LINE 98
        __M_writer('\n\n')
        # SOURCE LINE 100
        if request.user.is_anonymous() == True:
            # SOURCE LINE 101
            __M_writer("      <li>\n      <a id='login_button' href='#'>\n      LOG IN\n      </a></li>\n\n")
            # SOURCE LINE 106
        else:
            # SOURCE LINE 107
            __M_writer('      <li>\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">')
            # SOURCE LINE 108
            __M_writer(str(request.user.username))
            __M_writer(' <b class="caret"></b></a>\n        <ul class="dropdown-menu">\n')
            # SOURCE LINE 110
            if isEmployee == True:
                # SOURCE LINE 111
                __M_writer('          <li><a href="/manager/dash/"><span class=\'glyphicon glyphicon-globe\'></span>&nbsp; DASHBOARD</a></li>\n          <li><a href="/manager/employee/')
                # SOURCE LINE 112
                __M_writer(str(request.user.id))
                __M_writer('"><span class=\'glyphicon glyphicon-edit\'></span>&nbsp; EDIT PROFILE</a></li>\n')
                # SOURCE LINE 113
            else:
                # SOURCE LINE 114
                __M_writer('          <li><a href="/account/myorders/"><span class=\'glyphicon glyphicon-inbox\'></span>&nbsp; MY ORDERS</a></li>\n          <li><a href="/index/not_implemented_yet"><span class=\'glyphicon glyphicon-camera\'></span>&nbsp; RENTALS</a></li>\n          <li><a href="/account/repairstatus/"><span class=\'glyphicon glyphicon-wrench\'></span>&nbsp; REPAIRS</a></li>\n          <li><a href="/account/user/')
                # SOURCE LINE 117
                __M_writer(str(request.user.id))
                __M_writer('"><span class=\'glyphicon glyphicon-edit\'></span>&nbsp; EDIT PROFILE</a></li>\n')
            # SOURCE LINE 119
            __M_writer('          <li><a href="/account/logout/"><span class=\'glyphicon glyphicon-log-out\'></span>&nbsp; LOGOUT</a></li>\n        </ul>\n\n      </li>\n\n')
        # SOURCE LINE 125
        __M_writer('\n    </ul>\n\n    \n  </div><!-- /.navbar-collapse -->\n</nav>\n  \n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 134
        __M_writer('\n\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 141
        __M_writer('  \n\n')
        # SOURCE LINE 143
 

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n\n\n\n<!-- Footer-->\n\n<footer>\n      \n\n  <div class="container">\n    <div class="row">\n      <div class="col-md-4">\n        <ul class="list-unstyled">\n          <li class="title">Home</li>\n          <li><a href="/account/newuser/">New Account</a></li>\n          <li><a href="/catalog/category">Search Products</a></li>\n        </ul>\n      </div>\n      <div class="col-md-4">\n        <ul class="list-unstyled">\n          <li class="title">About</li>\n          <li><a href="/about/">About Us</a></li>\n          <li><a href="/locations/">Locations</a></li>\n        </ul>\n      </div>\n      <div class="col-md-3">\n        <ul class="list-unstyled">\n          <li class="title">Help</li>\n          <li><a href="/contact/">Contact Us</a></li>\n          <li><a href="/terms/">Rental Policy</a></li>\n          <li><a href="/account/newuser/">Repair Terms</a></li>\n\n        </ul>\n      </div>\n\n      <div class="col-md-1">\n        <ul class="list-unstyled">\n          <li><a href="https://www.facebook.com/digitallifemyway"><img src="/static/homepage/images/facebook.png" /></a></li>\n          <li><a href="https://plus.google.com/"><img src="/static/homepage/images/google.png" /></a></li>\n          <li><a href="https://www.twitter.com/"><img src="/static/homepage/images/twitter.png" /></a></li>\n        </ul>\n      </div>\n\n\n    </div>\n  </div>\n\n</footer> \n    \n\n\n  \n\n  \n')
        # SOURCE LINE 199
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>\n')
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
        __M_writer('\n  Site content goes here in sub-templates.\n')
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
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shopping_cart_navigation_option(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def shopping_cart_navigation_option():
            return render_shopping_cart_navigation_option(context)
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(' ')
 

        __M_writer('\n\n      <li>\n        <a id=\'cart_button\' href="#">\n          <span class="glyphicon glyphicon-shopping-cart"></span>&nbsp; MY CART\n\n          ')
        # SOURCE LINE 79
 
        from base_app.user_util import manager_check, employee_check
        
        isEmployee = employee_check(request.user)
        isManager = manager_check(request.user)
        
        cart = request.session.get('cart', {})
        rent = request.session.get('rent', {})
        repair = request.session.get('repair', {})
        cart_length = len(cart.keys()) + len(rent.keys()) + len(repair.keys())
        
        
        
        # SOURCE LINE 90
        __M_writer('\n\n')
        # SOURCE LINE 92
        if cart_length !=0:
            # SOURCE LINE 93
            __M_writer('          <span id=\'cart_length\' class="badge alert-custom">')
            __M_writer(str(cart_length))
            __M_writer('</span>\n')
        # SOURCE LINE 95
        __M_writer('        </a>\n      </li>\n      \n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


