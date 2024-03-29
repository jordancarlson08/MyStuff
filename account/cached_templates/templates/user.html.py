# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1397180272.930124
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/account/templates/user.html'
_template_uri = 'user.html'
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
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer('\n')
        # SOURCE LINE 7
 

        __M_writer('\n\n\n  <h2> My Account </h2><hr/>\n\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Username: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 18
        __M_writer(str(user.username))
        __M_writer(' </label>\n    </div>\n  </div>\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Name: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 27
        __M_writer(str(user.first_name))
        __M_writer(' ')
        __M_writer(str(user.last_name))
        __M_writer(' </label>\n    </div>\n  </div>\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Email: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 36
        __M_writer(str(user.email))
        __M_writer('</label>\n    </div>\n  </div>\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Address: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 45
        __M_writer(str(user.street1))
        __M_writer('</label>\n    </div>\n  </div>\n')
        # SOURCE LINE 48
        if user.street2!='':
            # SOURCE LINE 49
            __M_writer('  <div class="row">\n    <div class="col-md-2" align="right">\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
            # SOURCE LINE 53
            __M_writer(str(user.street2))
            __M_writer('</label>\n    </div>\n  </div>\n')
        # SOURCE LINE 57
        __M_writer('\n  <div class="row">\n    <div class="col-md-2" align="right">\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 62
        __M_writer(str(user.city))
        __M_writer(', ')
        __M_writer(str(user.state))
        __M_writer(' ')
        __M_writer(str(user.zipCode))
        __M_writer('</label>\n    </div>\n  </div>\n\n  <div class="row">\n    <div class="col-md-2" align="right">\n      <label for="inputEmail3">Phone Number: </label>\n    </div>\n    <div class="col-md-2" align="left">\n      <label for="inputEmail3">')
        # SOURCE LINE 71
        __M_writer(str(user.phone))
        __M_writer('</label>\n    </div>\n  </div>\n\n  <hr/>\n\n  <button class="btn btn-primary" id=\'password_button\'>Change Password</button>\n  <button class="btn btn-success" id=\'edit_button\'>Edit Profile</button>\n  <button class="btn btn-danger" data-toggle="modal" data-target="#deleteUser">Cancel Account</button>\n\n  <!--####### DELETE USER MODAL WINDOW ########-->\n\n  <div class="modal fade" id="deleteUser" tabindex="-1" role="dialog" aria-labelledby="deleteModalLabel" aria-hidden="true">\n    <div class="modal-dialog">\n      <div class="modal-content">\n        <div class="modal-header">\n          Cancel Account\n        </div>\n        <div class="modal-body">\n          Are you sure you want to cancel your account?\n        </div>\n        <div class="modal-footer">\n          <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>\n          <a href="/manager/users/')
        # SOURCE LINE 94
        __M_writer(str(user.id))
        __M_writer('/delete" class="btn btn-primary">Yes</a>\n        </div>\n      </div><!-- /.modal-content -->\n    </div><!-- /.modal-dialog -->\n  </div><!-- /.modal -->\n  <!--####### DELETE USER MODAL WINDOW ########-->\n\n\n\n  <div class=\'vertical_spacer6\'></div>\n\n\n\n\n\n\n\n        \n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


