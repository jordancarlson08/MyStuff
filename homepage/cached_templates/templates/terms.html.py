# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397176061.42151
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/homepage/templates/terms.html'
_template_uri = 'terms.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
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
        

        # SOURCE LINE 143
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
        __M_writer('\n \n  <h2>\n    Web Site Terms and Conditions of Use <span class="badge">Updated</span>\n  </h2>\n\n  <h3>\n    1. Terms\n  </h3>\n\n  <p>\n    By accessing this web site, you are agreeing to be bound by these \n    web site Terms and Conditions of Use, all applicable laws and regulations, \n    and agree that you are responsible for compliance with any applicable local \n    laws. If you do not agree with any of these terms, you are prohibited from \n    using or accessing this site. The materials contained in this web site are \n    protected by applicable copyright and trade mark law.\n  </p>\n\n  <h3>\n    2. Use License\n  </h3>\n\n  <ol type="a">\n    <li>\n      Permission is granted to temporarily download one copy of the materials \n      (information or software) on MyEducator Inc\'s web site for personal, \n      non-commercial transitory viewing only. This is the grant of a license, \n      not a transfer of title, and under this license you may not:\n      \n      <ol type="i">\n        <li>modify or copy the materials;</li>\n        <li>use the materials for any commercial purpose, or for any public display (commercial or non-commercial);</li>\n        <li>attempt to decompile or reverse engineer any software contained on MyEducator Inc\'s web site;</li>\n        <li>remove any copyright or other proprietary notations from the materials; or</li>\n        <li>transfer the materials to another person or "mirror" the materials on any other server.</li>\n      </ol>\n    </li>\n    <li>\n      This license shall automatically terminate if you violate any of these restrictions and may be terminated by MyEducator Inc at any time. Upon terminating your viewing of these materials or upon the termination of this license, you must destroy any downloaded materials in your possession whether in electronic or printed format.\n    </li>\n  </ol>\n\n  <h3>\n    3. Disclaimer\n  </h3>\n\n  <ol type="a">\n    <li>\n      The materials on MyEducator Inc\'s web site are provided "as is". MyEducator Inc makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties, including without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights. Further, MyEducator Inc does not warrant or make any representations concerning the accuracy, likely results, or reliability of the use of the materials on its Internet web site or otherwise relating to such materials or on any sites linked to this site.\n    </li>\n  </ol>\n\n  <h3>\n    4. Limitations\n  </h3>\n\n  <p>\n    In no event shall MyEducator Inc or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption,) arising out of the use or inability to use the materials on MyEducator Inc\'s Internet site, even if MyEducator Inc or a MyEducator Inc authorized representative has been notified orally or in writing of the possibility of such damage. Because some jurisdictions do not allow limitations on implied warranties, or limitations of liability for consequential or incidental damages, these limitations may not apply to you.\n  </p>\n        \n  <h3>\n    5. Revisions and Errata\n  </h3>\n\n  <p>\n    The materials appearing on MyEducator Inc\'s web site could include technical, typographical, or photographic errors. MyEducator Inc does not warrant that any of the materials on its web site are accurate, complete, or current. MyEducator Inc may make changes to the materials contained on its web site at any time without notice. MyEducator Inc does not, however, make any commitment to update the materials.\n  </p>\n\n  <h3>\n    6. Links\n  </h3>\n\n  <p>\n    MyEducator Inc has not reviewed all of the sites linked to its Internet web site and is not responsible for the contents of any such linked site. The inclusion of any link does not imply endorsement by MyEducator Inc of the site. Use of any such linked web site is at the user\'s own risk.\n  </p>\n\n  <h3>\n    7. Site Terms of Use Modifications\n  </h3>\n\n  <p>\n    MyEducator Inc may revise these terms of use for its web site at any time without notice. By using this web site you are agreeing to be bound by the then current version of these Terms and Conditions of Use.\n  </p>\n\n  <h3>\n    8. Governing Law\n  </h3>\n\n  <p>\n    Any claim relating to MyEducator Inc\'s web site shall be governed by the laws of the State of Utah without regard to its conflict of law provisions.\n  </p>\n\n  <p>\n    General Terms and Conditions applicable to Use of a Web Site.\n  </p>\n\n\n\n  <h2>\n    Privacy Policy\n  </h2>\n\n  <p>\n    Your privacy is very important to us. Accordingly, we have developed this Policy in order for you to understand how we collect, use, communicate and disclose and make use of personal information. The following outlines our privacy policy.\n  </p>\n\n  <ul>\n    <li>\n      Before or at the time of collecting personal information, we will identify the purposes for which information is being collected.\n    </li>\n    <li>\n      We will collect and use of personal information solely with the objective of fulfilling those purposes specified by us and for other compatible purposes, unless we obtain the consent of the individual concerned or as required by law.   \n    </li>\n    <li>\n      We will only retain personal information as long as necessary for the fulfillment of those purposes. \n    </li>\n    <li>\n      We will collect personal information by lawful and fair means and, where appropriate, with the knowledge or consent of the individual concerned. \n    </li>\n    <li>\n      Personal data should be relevant to the purposes for which it is to be used, and, to the extent necessary for those purposes, should be accurate, complete, and up-to-date. \n    </li>\n    <li>\n      We will protect personal information by reasonable security safeguards against loss or theft, as well as unauthorized access, disclosure, copying, use or modification.\n    </li>\n    <li>\n      We will make readily available to customers information about our policies and practices relating to the management of personal information. \n    </li>\n  </ul>\n\n  <p>\n    We are committed to conducting our business in accordance with these principles in order to ensure that the confidentiality of personal information is protected and maintained. \n  </p>\n\n  <div class="vertical_spacer6"></div>\n  <div class="vertical_spacer6"></div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


