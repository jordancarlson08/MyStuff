# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397156441.037258
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/employee.html'
_template_uri = 'employee.html'
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
        passwordForm = context.get('passwordForm', UNDEFINED)
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        passwordForm = context.get('passwordForm', UNDEFINED)
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\n')
        # SOURCE LINE 4
 

        __M_writer('\n\n<div class=\'content\'>\n\n  <h2> Employee Profile Information </h2><hr/>\n\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Username: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 16
        __M_writer(str(user.username))
        __M_writer(' </label>\n    </div>\n  </div>\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Name: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 25
        __M_writer(str(user.first_name))
        __M_writer(' ')
        __M_writer(str(user.last_name))
        __M_writer(' </label>\n    </div>\n  </div>\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Email: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 34
        __M_writer(str(user.email))
        __M_writer('</label>\n    </div>\n  </div>\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Address: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 43
        __M_writer(str(user.street1))
        __M_writer('</label>\n    </div>\n  </div>\n')
        # SOURCE LINE 46
        if user.street2!='':
            # SOURCE LINE 47
            __M_writer('  <div class="row">\n    <div class="col-md-2" align="right">\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
            # SOURCE LINE 51
            __M_writer(str(user.street2))
            __M_writer('</label>\n    </div>\n  </div>\n')
        # SOURCE LINE 55
        __M_writer('\n  <div class="row">\n    <div class="col-md-2" align="right">\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 60
        __M_writer(str(user.city))
        __M_writer(', ')
        __M_writer(str(user.state))
        __M_writer(' ')
        __M_writer(str(user.zipCode))
        __M_writer('</label>\n    </div>\n  </div>\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Phone Number: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 69
        __M_writer(str(user.phone))
        __M_writer('</label>\n    </div>\n  </div>\n\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Role: </label>\n    </div>\n')
        # SOURCE LINE 78
        if user.is_superuser==True:
            # SOURCE LINE 79
            __M_writer('    <div class="col-md-2" align="left">\n      <label for="inputEmail3">Admin</label>\n    </div>\n')
            # SOURCE LINE 82
        elif user.is_staff==True:
            # SOURCE LINE 83
            __M_writer('    <div class="col-md-2" align="left">\n      <label for="inputEmail3">Manager</label>\n    </div>\n')
            # SOURCE LINE 86
        else:
            # SOURCE LINE 87
            __M_writer('    <div class="col-md-2" align="left">\n      <label for="inputEmail3">Employee</label>\n    </div>\n')
        # SOURCE LINE 91
        __M_writer('  </div>\n\n\n  <hr/>\n\n  <button class="btn btn-primary" data-toggle="modal" data-target="#changePassword">Change Password</button>\n\n  <!--####### CHANGE PASSWORD MODAL WINDOW ########-->\n\n  <div class="modal fade" id="changePassword" tabindex="-1" role="dialog" aria-labelledby="changePasswordModalLabel" aria-hidden="true">\n    <div class="modal-dialog">\n      <div class="modal-content">\n        <div class="modal-header">\n          Change Password\n        </div>\n        <div class="modal-body">\n            <form class ="form-horizontal" role="form" method ="POST">\n\n')
        # SOURCE LINE 109
        for field in passwordForm:
            # SOURCE LINE 110
            __M_writer('              \n                <div class="form-group">\n                  <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 112
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n                    <div class="col-sm-4">\n                      ')
            # SOURCE LINE 114
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\n                    </div>\n                </div>\n                \n')
        # SOURCE LINE 119
        __M_writer('              ')
        __M_writer(str(form.non_field_errors()))
        __M_writer('\n          </div>\n          <div class=\'modal-footer\'>\n            <div class="form-group">\n              <div class="col-sm-offset-4 col-sm-4">\n                <input class="btn btn-success" type="submit" value="Save Changes">\n              </div>\n            </div>\n          </div>\n\n          </form>\n      </div><!-- /.modal-content -->\n    </div><!-- /.modal-dialog -->\n  </div><!-- /.modal -->\n  <!--####### END CHANGE PASSWORD MODAL WINDOW ########-->\n\n\n\n\n  <button class="btn btn-warning" data-toggle="modal" data-target="#editUser">Edit</button>\n\n\n  <!--####### EDIT USER MODAL WINDOW ########-->\n\n  <div class="modal fade" id="editUser" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true">\n    <div class="modal-dialog">\n      <div class="modal-content">\n        <div class="modal-header">\n          Edit User Information\n        </div>\n        <div class="modal-body">\n\n          <form class ="form-horizontal" role="form" method ="POST">\n\n')
        # SOURCE LINE 153
        for field in form:
            # SOURCE LINE 154
            __M_writer('            \n              <div class="form-group">\n                <label class="col-sm-4 control-label" for="id_')
            # SOURCE LINE 156
            __M_writer(str( field.name ))
            __M_writer('">')
            __M_writer(str( field.label ))
            __M_writer('</label>\n                  <div class="col-sm-4">\n                    ')
            # SOURCE LINE 158
            __M_writer(str(field))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('\n                  </div>\n              </div>\n\n')
        # SOURCE LINE 163
        __M_writer('\n        </div>\n        <div class=\'modal-footer\'>\n            <div class="form-group">\n              <div class="col-sm-offset-4 col-sm-4">\n                <input class="btn btn-success" type="submit" value="Save Changes">\n              </div>\n            </div>\n\n          </form>\n        </div>\n      </div><!-- /.modal-content -->\n    </div><!-- /.modal-dialog -->\n  </div><!-- /.modal -->\n  <!--####### END EDIT USER MODAL WINDOW ########-->\n\n\n\n\n  <button class="btn btn-danger" data-toggle="modal" data-target="#deleteUser">Delete</button>\n\n\n  <!--####### DELETE USER MODAL WINDOW ########-->\n\n  <div class="modal fade" id="deleteUser" tabindex="-1" role="dialog" aria-labelledby="deleteModalLabel" aria-hidden="true">\n    <div class="modal-dialog">\n      <div class="modal-content">\n        <div class="modal-header">\n          Delete Account\n        </div>\n        <div class="modal-body">\n          Are you sure you want to delete this account?\n        </div>\n        <div class="modal-footer">\n          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n          <a href="/manager/users/')
        # SOURCE LINE 198
        __M_writer(str(user.id))
        __M_writer('/delete" class="btn btn-primary">Yes</a>\n        </div>\n      </div><!-- /.modal-content -->\n    </div><!-- /.modal-dialog -->\n  </div><!-- /.modal -->\n  <!--####### DELETE USER MODAL WINDOW ########-->\n\n\n\n  <div class=\'vertical_spacer6\'></div>\n\n</div>\n\n\n\n\n\n        \n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


