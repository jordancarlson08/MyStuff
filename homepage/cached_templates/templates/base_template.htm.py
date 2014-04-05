# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396734001.625688
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\base_app\\templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main', 'top']


# SOURCE LINE 5
from base_app import static_files 

# SOURCE LINE 22
from base_app import global_static 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main():
            return render_main(context._locals(__M_locals))
        def top():
            return render_top(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n\n  <head>\n    <title>MyStuff Digital Life My Way</title>\n    <meta name="description" content="MyStuff Digital Life My Way offers the best digital cameras, film cameras, lenses, accessories, rentals and repairs."></meta>\n    <meta name="keywords" content="Camera, film, rental, repair, digital photography, film photography"></meta>\n\n    <link rel="icon" type="image/x-icon"  href="/static/base_app/images/favicon.ico">      \n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>\n\n  \n')
        # SOURCE LINE 22
        __M_writer('    ')
        __M_writer('\n    ')
        # SOURCE LINE 23
        __M_writer(str( global_static.SITE_WIDE_CSS ))
        __M_writer('\n    ')
        # SOURCE LINE 24
        __M_writer(str( global_static.SITE_WIDE_JS ))
        __M_writer('\n\n')
        # SOURCE LINE 27
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n  </head>\n\n  <body>\n     <div id="fb-root"></div>\n\n\n  <nav class="navbar navbar-default" role="navigation">\n  <!-- Brand and toggle get grouped for better mobile display -->\n  <div class="navbar-header">\n    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n      <span class="sr-only">Toggle navigation</span>\n      <span class="icon-bar"></span>\n      <span class="icon-bar"></span>\n      <span class="icon-bar"></span>\n    </button>\n    <a class="navbar-brand" href="/index/" title="Home"><img src="')
        # SOURCE LINE 44
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/images/camera_icon.png" width="90" /></a>\n    <a class="navbar-brand-custom" href="/index/">My Stuff - Digital Life My Way</a>\n\n  </div>\n\n  <!-- Collect the nav links, forms, and other content for toggling -->\n  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n    \n    <ul class="nav navbar-nav navbar-right">\n      \n      <li>\n        <a id=\'cart_button\' href="#">\n          <span class="glyphicon glyphicon-shopping-cart"></span>\n          &nbsp; Shopping Cart &nbsp;\n          ')
        # SOURCE LINE 58
 
        cart = request.session.get('cart', {})
        rent = request.session.get('rent', {})
        repair = request.session.get('repair', {})
        cart_length = len(cart.keys()) + len(rent.keys()) + len(repair.keys())
        isStaff = False
        if request.user.is_staff == True:
          isStaff = True
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['repair','isStaff','cart_length','rent','cart'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 66
        __M_writer('\n')
        # SOURCE LINE 67
        if cart_length !=0:
            # SOURCE LINE 68
            __M_writer('          <span class="badge">')
            __M_writer(str(cart_length))
            __M_writer('</span>\n')
        # SOURCE LINE 70
        __M_writer('        </a>\n      </li>\n      <!--<li><a href="/account/login/">Log In</a></li>\n      <li><a href="/account/logout/">Log Out</a></li>-->\n      <li><a href="/catalog/category/">Catalog</a></li>\n')
        # SOURCE LINE 75
        if isStaff == True:
            # SOURCE LINE 76
            __M_writer('      <li>\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Rentals<b class="caret"></b></a>\n        <ul class="dropdown-menu">\n          <li><a href="/manager/searchinventory/">New Rental</a></li>\n          <li><a href="/manager/returns/">Returns</a></li>\n          <li><a href="/manager/laterentals/">Late Rentals</a></li>\n        </ul>\n      </li>\n      <li>\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Repairs<b class="caret"></b></a>\n        <ul class="dropdown-menu">\n          <li><a href="/manager/newrepair/">New Repair</a></li>\n          <li><a href="/manager/repairs/">Checkout Repair</a></li>\n        </ul>\n      </li>\n')
            # SOURCE LINE 91
        else:
            # SOURCE LINE 92
            __M_writer('      <li class="dropdown">\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Contact Us<b class="caret"></b></a>\n        <ul class="dropdown-menu">\n          <li><a href="/phone/">Call</a></li>\n          <li><a href="/contact/">Email</a></li>\n          <li><a href="http://www.facebook.com">Facebook</a></li>\n        </ul>\n      </li>\n')
        # SOURCE LINE 101
        __M_writer('        \n')
        # SOURCE LINE 102
        if request.user.is_anonymous() == True:
            # SOURCE LINE 103
            __M_writer("      <li>\n      <a id='login_button' href='#'>\n      Log In\n      </a></li>\n\n")
            # SOURCE LINE 108
        else:
            # SOURCE LINE 109
            __M_writer('      <li>\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">')
            # SOURCE LINE 110
            __M_writer(str(request.user))
            __M_writer(' <b class="caret"></b></a>\n        <ul class="dropdown-menu">\n          <li><a href="/dash/">Dashboard</a></li>\n')
            # SOURCE LINE 113
            if request.user.is_staff == False:
                # SOURCE LINE 114
                __M_writer('          <li><a href="/index/not_implemented_yet">Rentals</a></li>\n          <li><a href="/account/repairstatus/">Repairs</a></li>\n          <li><a href="/account/user/')
                # SOURCE LINE 116
                __M_writer(str(request.user.id))
                __M_writer('">Edit Profile</a></li>\n')
                # SOURCE LINE 117
            else:
                # SOURCE LINE 118
                __M_writer('          <li><a href="/manager/employee/')
                __M_writer(str(request.user.id))
                __M_writer('">Edit Profile</a></li>\n')
            # SOURCE LINE 120
            __M_writer('          <li><a href="/account/logout/">Logout</a></li>\n        </ul>\n\n      </li>\n\n')
        # SOURCE LINE 126
        __M_writer('\n    </ul>\n\n    \n  </div><!-- /.navbar-collapse -->\n</nav>\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 178
        __M_writer('\n\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 185
        __M_writer('  \n\n')
        # SOURCE LINE 187
 

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n\n\n<!-- Footer-->\n\n<footer>\n      \n\n  <div class="container">\n    <div class="row">\n      <div class="col-md-4">\n        <ul class="list-unstyled">\n          <li class="title">Home</li>\n          <li><a href="/account/login/">Login / Signup</a></li>\n        </ul>\n      </div>\n      <div class="col-md-4">\n        <ul class="list-unstyled">\n          <li class="title">About</li>\n          <li><a href="/about/">About Us</a></li>\n        </ul>\n      </div>\n      <div class="col-md-3">\n        <ul class="list-unstyled">\n          <li class="title">Help</li>\n          <li><a href="/contact/">Contact Us</a></li>\n          <li><a href="/terms/">Terms</a></li>\n\n        </ul>\n      </div>\n\n      <div class="col-md-1">\n        <ul class="list-unstyled">\n          <li><a href="https://www.facebook.com/"><img src="/static/homepage/images/facebook.png" /></a></li>\n          <li><a href="https://plus.google.com/"><img src="/static/homepage/images/google.png" /></a></li>\n          <li><a href="https://www.twitter.com/"><img src="/static/homepage/images/twitter.png" /></a></li>\n        </ul>\n      </div>\n\n\n    </div>\n  </div>\n\n</footer> \n    \n\n\n  \n\n  \n')
        # SOURCE LINE 239
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 183
        __M_writer('\n  Site content goes here in sub-templates.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top():
            return render_top(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 133
        __M_writer('\n')
        # SOURCE LINE 134
 

        __M_writer('\n')
        # SOURCE LINE 135
        if request.user.is_staff == True:
            # SOURCE LINE 136
            __M_writer('\n\n  <!-- The Manager Nav Bar -->\n  <ul class="nav nav-tabs navbar-right">\n\n    <li class="dropdown">\n      <a class="btn btn-primary" data-toggle="dropdown" href="#">\n        <span class="glyphicon glyphicon-tags"></span>&nbsp; Inventory <span class="caret"></span>\n      </a>\n      <ul class="dropdown-menu">\n        <li><a href="/manager/searchinventory/"><span class="glyphicon glyphicon-search"></span> Search</a></li>\n        <li><a href="/manager/newcatalogitem/"><span class="glyphicon glyphicon-new-window"></span> New Catalog Item</a></li>\n        <li><a href="/manager/newserializeditem/"><span class="glyphicon glyphicon-new-window"></span> New Serialized Item</a></li>\n      </ul>\n    </li>\n\n    <li class="dropdown">\n      <a class="btn btn-success" data-toggle="dropdown" href="#">\n        <span class="glyphicon glyphicon-star"></span> Stores <span class="caret"></span>\n      </a>\n      <ul class="dropdown-menu">\n        <li><a href="/manager/searchstores/"><span class="glyphicon glyphicon-search"></span> Search</a></li>\n        <li><a href="/manager/newstore/"><span class="glyphicon glyphicon-new-window"></span> New Store</a></li>\n      </ul>\n    </li>\n\n    <li class="dropdown">\n      <a class="btn btn-danger" data-toggle="dropdown" href="#">\n        <span class="glyphicon glyphicon-user"></span> Users <span class="caret"></span>\n      </a>\n      <ul class="dropdown-menu">\n        <li><a href="/manager/searchusers/"><span class="glyphicon glyphicon-search"></span> Search Users</a></li>\n        <li><a href="/account/newuser/"><span class="glyphicon glyphicon-new-window"></span> New User</a></li>\n        <li><a href="/account/newemployee/"><span class="glyphicon glyphicon-new-window"></span> New Employee</a></li>\n      </ul>\n    </li>\n  </ul>\n  <!-- End Nav Bar -->\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


