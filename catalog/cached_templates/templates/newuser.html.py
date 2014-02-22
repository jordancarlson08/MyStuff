# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1391280541.708238
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/newuser.html'
_template_uri = 'newuser.html'
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
    return runtime._inherit_from(context, 'base_users.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        # SOURCE LINE 6
        __M_writer('\n')
        # SOURCE LINE 9
        __M_writer('\n')
        # SOURCE LINE 11
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 170
        __M_writer('   ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer('\n')
        # SOURCE LINE 14
 

        __M_writer('\n\n  <h2>New User Account</h2><hr/>\n\t</br>\n <form class="form-horizontal" role="form">\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">First Name</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="First Name">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputtext3" class="col-sm-4 control-label">Last Name</label>\n    <div class="col-sm-4">\n      <input type="text" class="form-control" id="inputtext3" placeholder="Last Name">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Email</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="Email">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputtext3" class="col-sm-4 control-label">Username</label>\n    <div class="col-sm-4">\n      <a id="popoverOption"  href="#" data-content="Valid Keys: A-Z, a-z, _, -, or 0-9" rel="popover" data-placement="right" data-original-title="Username Rules" data-trigger="hover"><input type="text" class="form-control" id="inputtext3" placeholder="Username">\n      </a>\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputPassword3" class="col-sm-4 control-label">Password</label>\n    <div class="col-sm-4">\n      <a id="popoverOption2"  href="#" data-content="Valid Keys: A-Z, a-z, or 0-9" rel="popover" data-placement="right" data-original-title="Password Rules" data-trigger="hover"><input type="password" class="form-control" id="inputPassword3" placeholder="Password">\n      </a>\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Address</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="Address">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputtext3" class="col-sm-4 control-label">City</label>\n    <div class="col-sm-4">\n      <input type="text" class="form-control" id="inputtext3" placeholder="City">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">State</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="State">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputtext3" class="col-sm-4 control-label">Postal Code</label>\n    <div class="col-sm-4">\n      <input type="text" class="form-control" id="inputtext3" placeholder="Postal Code">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Country</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="Country">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label">Phone Number</label>\n    <div class="col-sm-4">\n      <input type="email" class="form-control" id="inputEmail3" placeholder="Phone Number">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputtext3" class="col-sm-4 control-label">Security Question</label>\n    <div class="col-sm-4">\n      <input type="text" class="form-control" id="inputtext3" placeholder="Security Question">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputtext3" class="col-sm-4 control-label">Security Answer</label>\n    <div class="col-sm-4">\n      <input type="text" class="form-control" id="inputtext3" placeholder="Answer">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputEmail3" class="col-sm-4 control-label"><b>Role</b></label>\n    <div class="col-sm-4">\n  \t\t<select class="form-control">\n        <option>Select One</option>\n        <option>Customer</option>\n        <option>Employee</option>\n        <option>Manager</option>\n        <option>Admin</option>\n  \t\t</select>\n        <a id="popoverOption3"  href="#" data-content="Customer: User, 0 access rights Employee: Employee, 0 access         Manager: Employee, Limited access        Admin: Employee, Full access" rel="popover" data-placement="bottom" data-original-title="Roles" data-trigger="hover">Role Descriptions</a>\n\t  </div> \n  </div>\n\n\n  <div class="form-group">\n    <label for="inputtext3" class="col-sm-4 control-label">Hire Date</label>\n    <div class="col-sm-4">\n      <input type="text" class="form-control" id="inputtext3" placeholder="Hire Date">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputtext3" class="col-sm-4 control-label">Salary</label>\n    <div class="col-sm-4">\n      <input type="text" class="form-control" id="inputtext3" placeholder="Salary">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <label for="inputtext3" class="col-sm-4 control-label">Commission Rate</label>\n    <div class="col-sm-4">\n      <input type="text" class="form-control" id="inputtext3" placeholder="Commission Rate">\n    </div>\n  </div>\n\n  <div class="form-group">\n    <div class="col-sm-offset-4 col-sm-4">\n      <button type="submit" class="btn btn-primary">Submit</button>\n      <button class="btn btn-default">Cancel</button>\n    </div>\n  </div>\n\n\n  </form>\n\n  <script>\n    $(\'#popoverOption\').popover({ trigger: "hover"});\n  </script>\n\n  <script>\n    $(\'#popoverOption2\').popover({ trigger: "hover"});\n  </script>\n\n  <script>\n    $(\'#popoverOption3\').popover({ trigger: "hover"});\n  </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


