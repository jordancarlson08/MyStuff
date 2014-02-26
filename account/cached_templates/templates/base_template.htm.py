# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393378119.31501
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\base_app\\templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main', 'top']


# SOURCE LINE 6
from base_app import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main():
            return render_main(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top():
            return render_top(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
        __M_writer('\n')
        # SOURCE LINE 7
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <title>MyStuff</title>\n    <link href=\'http://fonts.googleapis.com/css?family=Poiret+One\' rel=\'stylesheet\' type=\'text/css\'>\n    <link rel="icon" type="image/x-icon"  href="/static/base_app/images/favicon.ico">   \n    <meta content="/homepage/images/camera_icon_75.png" itemprop="image">\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>\n    \n    <!-- Bootstrap stuff\n    <link rel="stylesheet" href="/static/base_app/styles/bootstrap.css"/>\n    <script src="/static/base_app/scripts/bootstrap.js"></script> -->\n\n    <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css" rel="stylesheet">\n    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>\n\n\n')
        # SOURCE LINE 28
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body>\n\n\n  <nav class="navbar navbar-default" role="navigation">\n  <!-- Brand and toggle get grouped for better mobile display -->\n  <div class="navbar-header">\n    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n      <span class="sr-only">Toggle navigation</span>\n      <span class="icon-bar"></span>\n      <span class="icon-bar"></span>\n      <span class="icon-bar"></span>\n    </button>\n    <a class="navbar-brand" href="/index/" title="Home"><img src="')
        # SOURCE LINE 43
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/images/camera_icon.png" width="90" /></a>\n    <a class="navbar-brand-custom" href="/index/">My Stuff - Digital Life My Way</a>\n\n  </div>\n\n  <!-- Collect the nav links, forms, and other content for toggling -->\n  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n    \n    <ul class="nav navbar-nav navbar-right">\n      \n      <li><a href="/"><span class="glyphicon glyphicon-camera"></span></a></li>\n      <!--<li><a href="/account/login/">Log In</a></li>\n      <li><a href="/account/logout/">Log Out</a></li>-->\n      <li><a href="#">Stores</a></li>\n      <li><a href="/catalog/search/">Catalog</a></li>\n      <li class="dropdown">\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Contact Us<b class="caret"></b></a>\n        <ul class="dropdown-menu">\n          <li><a href="/phone/">Call</a></li>\n          <li><a href="/contact/">Email</a></li>\n          <li><a href="http://www.facebook.com">Facebook</a></li>\n        </ul>\n      </li>\n        \n')
        # SOURCE LINE 67
        if request.user.is_anonymous() == True:
            # SOURCE LINE 68
            __M_writer('      <li>\n      <a href=\'/account/login/\'>\n      Log In\n      </a></li>\n<!--     %elif request.user.is_staff == True:\n      <li class="dropdown">\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Manage<b class="caret"></b></a>\n        <ul class="dropdown-menu">\n          <li><a href="/manageinventory/">Inventory</a></li>\n          <li><a href="/managestores/">Stores</a></li>\n          <li><a href="/manageusers/">Users</a></li>\n        </ul>\n      </li>\n  \n      <li>\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">')
            # SOURCE LINE 83
            __M_writer(str(request.user))
            __M_writer(' <b class="caret"></b></a>\n        <ul class="dropdown-menu">\n          <li><a href="/manageinventory/">Dashboard</a></li>\n          <li><a href="/manager/users/')
            # SOURCE LINE 86
            __M_writer(str(request.user.id))
            __M_writer('">Edit Profile</a></li>\n          <li><a href="/account/logout/">Logout</a></li>\n        </ul>\n\n      </li> -->\n\n')
            # SOURCE LINE 92
        else:
            # SOURCE LINE 93
            __M_writer('      <li>\n        <a href="#" class="dropdown-toggle" data-toggle="dropdown">')
            # SOURCE LINE 94
            __M_writer(str(request.user))
            __M_writer(' <b class="caret"></b></a>\n        <ul class="dropdown-menu">\n          <li><a href="/dash/">Dashboard</a></li>\n\n')
            # SOURCE LINE 98
            if request.user.is_staff == False:
                # SOURCE LINE 99
                __M_writer('          <li><a href="/account/user/')
                __M_writer(str(request.user.id))
                __M_writer('">Edit Profile</a></li>\n')
                # SOURCE LINE 100
            else:
                # SOURCE LINE 101
                __M_writer('          <li><a href="/manager/employee/')
                __M_writer(str(request.user.id))
                __M_writer('">Edit Profile</a></li>\n')
            # SOURCE LINE 103
            __M_writer('          <li><a href="/account/logout/">Logout</a></li>\n        </ul>\n\n      </li>\n\n')
        # SOURCE LINE 109
        __M_writer('\n    </ul>\n\n    \n  </div><!-- /.navbar-collapse -->\n</nav>\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top'):
            context['self'].top(**pageargs)
        

        # SOURCE LINE 160
        __M_writer('\n\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 167
        __M_writer('  \n\n')
        # SOURCE LINE 169
 

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n\n\n<!-- Footer-->\n\n<footer>\n      \n\n  <div class="container">\n    <div class="row">\n      <div class="col-md-4">\n        <ul class="list-unstyled">\n          <li class="title">Home</li>\n          <li><a href="/account/login/">Login / Signup</a></li>\n        </ul>\n      </div>\n      <div class="col-md-4">\n        <ul class="list-unstyled">\n          <li class="title">About</li>\n          <li><a href="/about/">About Us</a></li>\n        </ul>\n      </div>\n      <div class="col-md-3">\n        <ul class="list-unstyled">\n          <li class="title">Help</li>\n          <li><a href="/contact/">Contact Us</a></li>\n          <li><a href="/terms/">Terms</a></li>\n\n        </ul>\n      </div>\n\n      <div class="col-md-1">\n        <ul class="list-unstyled">\n          <li><a href="https://www.facebook.com/"><img src="/static/homepage/images/facebook.png" /></a></li>\n          <li><a href="https://plus.google.com/"><img src="/static/homepage/images/google.png" /></a></li>\n          <li><a href="https://www.twitter.com/"><img src="/static/homepage/images/twitter.png" /></a></li>\n        </ul>\n      </div>\n\n\n    </div>\n  </div>\n\n</footer> \n    \n\n\n  \n\n  \n')
        # SOURCE LINE 221
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
        # SOURCE LINE 165
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
        # SOURCE LINE 116
        __M_writer('\n')
        # SOURCE LINE 117
        if request.user.is_staff == True:
            # SOURCE LINE 118
            __M_writer('\n\n  <!-- The Manager Nav Bar -->\n  <ul class="nav nav-tabs navbar-right">\n\n    <li class="dropdown">\n      <a class="btn btn-primary" data-toggle="dropdown" href="#">\n        <span class="glyphicon glyphicon-tags"></span>&nbsp; Inventory <span class="caret"></span>\n      </a>\n      <ul class="dropdown-menu">\n        <li><a href="/manager/searchinventory/"><span class="glyphicon glyphicon-search"></span> Search</a></li>\n        <li><a href="/manager/newcatalogitem/"><span class="glyphicon glyphicon-new-window"></span> New Catalog Item</a></li>\n        <li><a href="/manager/newinventoryitem/"><span class="glyphicon glyphicon-new-window"></span> New Serialized Item</a></li>\n      </ul>\n    </li>\n\n    <li class="dropdown">\n      <a class="btn btn-success" data-toggle="dropdown" href="#">\n        <span class="glyphicon glyphicon-star"></span> Stores <span class="caret"></span>\n      </a>\n      <ul class="dropdown-menu">\n        <li><a href="/manager/searchstores/"><span class="glyphicon glyphicon-search"></span> Search</a></li>\n        <li><a href="/manager/newstore/"><span class="glyphicon glyphicon-new-window"></span> New Store</a></li>\n      </ul>\n    </li>\n\n    <li class="dropdown">\n      <a class="btn btn-danger" data-toggle="dropdown" href="#">\n        <span class="glyphicon glyphicon-user"></span> Users <span class="caret"></span>\n      </a>\n      <ul class="dropdown-menu">\n        <li><a href=""><span class="glyphicon glyphicon-search"></span> Search Users</a></li>\n        <li><a href="/manager/searchusers/"><span class="glyphicon glyphicon-search"></span> Search Employees</a></li>\n        <li><a href="/account/newemployee/"><span class="glyphicon glyphicon-new-window"></span> New Employee</a></li>\n      </ul>\n    </li>\n  </ul>\n  <!-- End Nav Bar -->\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


