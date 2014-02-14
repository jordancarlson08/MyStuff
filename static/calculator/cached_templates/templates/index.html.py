# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1388985594.593247
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Code\\django-mako-plus-master\\calculator\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 73
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n  <p>\n    Welcome to our home page!  This page explores the primary benefits of the base_app.controller in <a href="https://www.djangoproject.com/">Django</a>.\n  </p>\n  <h2><a href="http://www.makotemplates.org/">Mako</a> Templates - Ahhh, smell that strong sauce goodness!</h2>\n  <p>\n    A templating engine allows you to put code into HTML documents.  <a href="https://www.djangoproject.com/">Django</a> comes with a custom templating engine, but it\'s\n    weak; it provides only a few tags that limit your power (by design to encourage your template code to be minimal).\n    Method calls are different than regular python: they don\'t have parenthases and parameters are syntactically different.\n    When I first saw the templating syntax, I asked, "Why would I want to learn yet another syntax?  I\'m using Django\n    because I *like* Python!"\n  </p>    \n  <p>\n    In contrast, the <a href="http://www.makotemplates.org/">Mako</a> templating engine embeds standard Python into HTML pages.  For loops, if statements, method calls,\n    and everything else is standard and straightforward.  Fortunately, it\'s easy to use Mako with Django.  The base_app/controller.py \n    module provides a templating class that connects the two together. For example, see the "templater.render_to_response()" calls\n    in most of the views/ files.\n  </p>    \n\n  <h2>URL Matching by Convention - Sound Pythonic?</h2>\n  <p>\n    This file is just a simple HTML file.  There\'s no view function associated with it.  The controller\n    first looks for <tt>/calculator/views/index.py</tt> -> <tt>process_request()</tt>, and when it doesn\'t find the function, it\n    renders the <tt>/calculator/templates/index.html</tt> file directly.\n  </p>    \n  <p>\n    In other words, this index page is a great example of the base_app.controller.  Instead of putting an entry in urls.py\n    for every. single. page. on. your. site (the normal Django way), it uses a convention to know which pages can be\n    displayed.  The first url part (/calculator) takes it to the calculator app, the second url part (/index) takes it \n    to either index.py or index.html (if the first doesn\'t exist).\n  </p>\n\n  <h2>Automatic CSS and Javascript Inclusion</h2>\n  <p>\n    In addition, the parent template of this file (<tt>base_app/templates/base_template.htm</tt>) automatically includes styles and scripts\n    for each template in the inheritance chain.  For example, this index page has the following inheritance:\n    <ol>\n      <li>Base template: <tt>/base_app/templates/base_template.htm</tt></li>\n      <li>Child template: <tt>/calculator/templates/index.html</tt></li>\n    </ol>\n    Because of this chain, the following styles and scripts are automatically included in the rendered page:\n    <ol>\n      <li><tt>/base_app/styles/base.css</tt></li>\n      <li><tt>/base_app/styles/base.cssm</tt> (this one can contain dynamic Python code)</li>\n      <li><tt>/calculator/styles/index.css</tt></li>\n      <li><tt>/calculator/styles/index.cssm</tt> (this one can contain dynamic Python code)</li>\n      <li><tt>/base_app/scripts/base.js</tt></li>\n      <li><tt>/base_app/scripts/base.jsm</tt> (this one can contain dynamic Python code)</li>\n      <li><tt>/calculator/scripts/index.js</tt></li>\n      <li><tt>/calculator/scripts/index.jsm</tt> (yep, you guessed it, this one can contain dynamic Python code)</li>\n    </ol>\n    Of course, you\'d rarely create all the above files.  Just create the ones that you need.  For example, if you have \n    CSS that affects the dom elements in <tt>base.htm</tt>, place it in <tt>base.css</tt> or <tt>base.cssm</tt>.  If you have Javascript that affects \n    the dom elements in <tt>index.html</tt>, place it in <tt>index.js</tt> or <tt>index.jsm</tt>.\n  </p>\n  <p>\n    The above "automatic" inclusion of .css and .js files creates a nice separation of HTML, CSS, and JS code, and it \n    provies a place to attach styles and scripts at the same inheritance level as the HTML they affect.  It also \n    speeds up browser rendering because all the CSS and JS are included right in the HTML file - circumventing\n    further requests on your system (even though you\'re really keeping things separate on the coding side).\n  </p>\n\n  <h2>A More Complete Example</h2>\n  <p>\n    Try out the calculator app for a more complex example.\n  </p>\n  <ul>\n    <li><a href="/calculator/calc/">A calculator app</a></li>\n  </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


