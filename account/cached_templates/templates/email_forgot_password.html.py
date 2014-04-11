# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397169653.805318
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\account\\templates/email_forgot_password.html'
_template_uri = 'email_forgot_password.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<body style="margin:25px 50px;">\r\n\t<table>\r\n\t\t<tbody>\r\n\t\t\t<tr>\r\n\t\t\t\t<td><img alt="My Stuff" height="75" width="75" src="http://digitallifemyway.com/static/homepage/images/camera_icon_xs.png" /></td>\r\n\t\t\t\t<td>&nbsp;&nbsp;&nbsp;&nbsp;</td>\r\n\t\t\t\t<td><h1 style="font-family:sans-serif;">My Stuff - Digital Life My Way</h1></td>\r\n\t\t\t</tr>\r\n\t\t</tbody>\r\n\t</table>\r\n\r\n\t<br/>\r\n\t<h2 style="font-family:sans-serif;">Forgot Password</h2>\r\n\r\n\t<p \tstyle=\'font-family: sans-serif;\'>We recieved a request to reset your password.<br/> \r\n\tYou can use the following link to reset it.<br/><br/>\r\n\t<a href="')
        # SOURCE LINE 19
        __M_writer(str(url))
        __M_writer('" \r\n\tstyle=\r\n\t\'\r\n\tfont-family: sans-serif;\r\n\tcolor:#fff;\r\n\tbackground-color:#5cb85c;\r\n\tborder-color:#4cae4c;\r\n\ttext-decoration:none;\r\n\tdisplay: inline-block;\r\n\tpadding: 6px 12px;\r\n\tmargin-bottom: 0;\r\n\tfont-size: 14px;\r\n\tfont-weight: normal;\r\n\tline-height: 1.42857143;\r\n\ttext-align: center;\r\n\twhite-space: nowrap;\r\n\tvertical-align: middle;\r\n\tcursor: pointer;\r\n\t-webkit-user-select: none;\r\n\t   -moz-user-select: none;\r\n\t    -ms-user-select: none;\r\n\t        user-select: none;\r\n\tbackground-image: none;\r\n\tborder: 1px solid transparent;\r\n\tborder-radius: 4px;\r\n\t\'\r\n\t>Reset Password</a><br/><br/>\r\n\tFor security purposes, this link will only be active for 3 hours.</p>\r\n\t<br/>\r\n\t<br/>\r\n\tThank You!\r\n\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


