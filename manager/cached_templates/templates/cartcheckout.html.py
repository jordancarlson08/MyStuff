# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393126640.774541
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\manager\\templates/cartcheckout.html'
_template_uri = 'cartcheckout.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['main']


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
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 461
        __M_writer('\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\r\n')
        # SOURCE LINE 6
 

        __M_writer('\r\n\t<div class="container">\r\n\t\t<h1>Your Shopping Cart</h1></br>\r\n\t\t<div class="row">\r\n\t\t\t<div class="col-md-3">\r\n\t\t\t\t<div class="well">\r\n\t\t\t\t\t<h3>Your Items</h3>\r\n\t\t\t\t\t<table>\r\n\t\t\t\t\t\t<h5><b>Nikon Coolpix S8000c</b></h5>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td rowspan="2"><img src="http://lghttp.22373.nexcesscdn.net/80A650/Magento/media/catalog/product/cache/1/small_image/150x/9df78eab33525d08d6e5fb8d27136e95/n/i/nikon_1_s800c_front.jpg" width= 55px alt="Nikon Camera">&nbsp;&nbsp;</td>\r\n\t\t\t\t\t\t\t<td><b>Quantity: </b></td>\r\n\t\t\t\t\t\t\t<td>1</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td><b>Price: </b></td>\r\n\t\t\t\t\t\t\t<td>$189.99</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t</table>\r\n\t\t\t\t\t<hr>\r\n\t\t\t\t\t<table>\r\n\t\t\t\t\t\t<h5><b>Nikon 12-24mm f/4G ED-IF AF-S DX Lens</b></h5>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td rowspan="2"><img src="https://www.pictureline.com/media/catalog/product/cache/1/small_image/50x/9df78eab33525d08d6e5fb8d27136e95/n/i/nikon_2_12-24_side.jpg" alt="Lens"></td>\r\n\t\t\t\t\t\t\t<td><b>Quantity: </b></td>\r\n\t\t\t\t\t\t\t<td>1</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td><b>Price: </b></td>\r\n\t\t\t\t\t\t\t<td>$1,224.35</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t</table>\r\n\t\t\t\t\t<hr>\r\n\t\t\t\t\t<table>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td><b>Subtotal: </b></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td>$1,414.94</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td><b>Tax: </b></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td>35.00</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td><b>TOTAL: </b></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td><u>$1,449.94</u></td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t</table>\r\n\t\t\t\t\t<br>\r\n\t\t\t\t</div> <!--closes the "well" -->\r\n\r\n\t\t\t\t<div class="well">\r\n\t\t\t\t\t<div class="container">\r\n\t\t\t\t\t\t<table>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td><img src="http://www.logostage.com/logos/american-express.jpg" width=40px alt="AmExpress Logo"></td>\r\n\t\t\t\t\t\t\t\t<td><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/MasterCard_logo.png/800px-MasterCard_logo.png" width=50px alt="MaCard Logo"></td>\r\n\t\t\t\t\t\t\t\t<td><img src="http://embroiderystitchbystitch.com/wp-content/uploads/2012/02/Visa-Credit-Card-Logo-5.jpg" width=50px alt="ViCard Logo"></td>\r\n\t\t\t\t\t\t\t\t<td><img src="http://www.credit-card-logos.com/images/discover_credit-card-logos/discover_network2.jpg" width=50px alt="DisCard Logo"></td>\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t</table>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div> <!--closes the "well" -->\r\n\r\n\t\t\t\t<div class=\'well\'>\r\n\t\t\t\t\t<div class=\'container\'>\r\n\t\t\t\t\t\t<strong>Promo Code</strong> </br>\r\n\t\t\t\t\t\t\t<input type="name" class="col-md-2" id="fName" placeholder="Promo Code">\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t\t<div class="col-md-9">\r\n\t\t\t\t\t<div class="panel-group" id="accordion">\r\n\t\t\t\t\t\t<div class="panel panel-default">\r\n\t\t\t\t\t\t\t<div class="panel-heading">\r\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\r\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">Billing Address\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</h4>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t<div id="collapseOne" class="panel-collapse collapse in">\r\n\t\t\t\t\t\t\t\t<div class="panel-body">\r\n\t\t\t\t\t\t\t\t\t<div class="container">\r\n\t\t\t\t\t\t\t\t\t\t<form role="form">\r\n\t\t\t\t\t\t\t\t\t\t\t<div class="form-group">\r\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="col-md-4">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="BillFirstName">First Name</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="name" class="form-control" id="fName" placeholder="First">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr class="spacer"></tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr class="spacer"></tr> \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="BillLastName">Last Name</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="name" class="form-control" id="lName" placeholder="Last">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="BillNumber">Phone Number</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="phone" class="form-control" id="phone" placeholder="Phone">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="BillEm">Email</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="email" class="form-control" id="email" placeholder="Email">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="col-md-5">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="BillStreet">Street Address</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="address" class="form-control" id="sAdd" placeholder="Address">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="BillCity">City</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="address" class="form-control" id="city" placeholder="City">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="BillState">State</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<select class="form-control">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>Select One</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>AK</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>AL</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>AR</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>AZ</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>CA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>CO</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>DE</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>FL</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>GA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>HI</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>IA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>ID</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>IL</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>IN</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>KS</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>KY</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>LA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MD</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>ME</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MI</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MN</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MO</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MS</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MT</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NC</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>ND</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NE</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NH</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NJ</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NM</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NV</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NY</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>OH</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>OK</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>OR</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>PA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>RI</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>SC</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>SD</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>TN</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>TX</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>UT</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>VT</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>WA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>WI</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>WV</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>WY</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</select>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="BillZip">Zip Code</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="zip" class="form-control" id="zipcode" placeholder="Zip Code">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t</form>\r\n\t\t\t\t\t\t\t\t\t</div> <!--ends Billing container-->\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div> <!-- end of panel, panel-default --> \r\n\t\t\t\t\t\t<div class="panel panel-default">\r\n\t\t\t\t\t\t\t<div class="panel-heading">\r\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\r\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">Shipping Address\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</h4>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t<div id="collapseTwo" class="panel-collapse collapse in">\r\n\t\t\t\t\t\t\t\t<div class="panel-body">\r\n\t\t\t\t\t\t\t\t\t<div class="container">\r\n\t\t\t\t\t\t\t\t\t\t<form role="form">\r\n\t\t\t\t\t\t\t\t\t\t\t<div class="form-group">\r\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="col-md-4">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ShipFirstName">First Name</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="name" class="form-control" id="fName" placeholder="First">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr class="spacer"></tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr class="spacer"></tr> \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ShipLastName">Last Name</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="name" class="form-control" id="lName" placeholder="Last">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ShipNumber">Phone Number</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="phone" class="form-control" id="phone" placeholder="Phone">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ShipEm">Email</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="email" class="form-control" id="email" placeholder="Email">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="col-md-4">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ShipStreet">Street Address</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="address" class="form-control" id="sAdd" placeholder="Address">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ShipCity">City</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="address" class="form-control" id="city" placeholder="City">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ShipState">State</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<select class="form-control">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>Select One</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>AK</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>AL</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>AR</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>AZ</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>CA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>CO</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>DE</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>FL</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>GA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>HI</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>IA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>ID</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>IL</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>IN</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>KS</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>KY</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>LA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MD</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>ME</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MI</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MN</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MO</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MS</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>MT</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NC</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>ND</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NE</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NH</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NJ</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NM</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NV</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>NY</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>OH</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>OK</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>OR</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>PA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>RI</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>SC</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>SD</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>TN</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>TX</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>UT</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>VT</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>WA</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>WI</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>WV</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>WY</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</select>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ShipZip">Zip Code</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="zip" class="form-control" id="zipcode" placeholder="Zip Code">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<form>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="checkbox" name="SameAdd" value="Address">&nbsp;&nbsp;Check if shipping address and billing address are the same<br>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</form>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t</form>\r\n\t\t\t\t\t\t\t\t\t</div> <!--ends Shipping container-->\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div> <!-- end of panel, panel-default -->\r\n\t\t\t\t\t\t<div class="panel panel-default">\r\n\t\t\t\t\t\t\t<div class="panel-heading">\r\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\r\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">Shipping Method\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</h4>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t<div id="collapseThree" class="panel-collapse collapse in">\r\n\t\t\t\t\t\t\t\t<div class="panel-body">\r\n\t\t\t\t\t\t\t\t\t<div class="container">\r\n\t\t\t\t\t\t\t\t\t\t<form role="form">\r\n\t\t\t\t\t\t\t\t\t\t\t<div class="form-group">\r\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="col-md-6">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<h5><b>Choose a delivery method</b></h5>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<form>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="Standard" value="standard">&nbsp;&nbsp;4-7 business days ($4.00)<br>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="NextUp" value="nextUp">&nbsp;&nbsp;2-3 business days ($10.00)<br>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="Overnight" value="overnight">&nbsp;&nbsp;Overnight ($25.00)<br>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="SameDay" value="sameDay">&nbsp;&nbsp;Same-day ($40.00)*<br>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="InStore" value="sameDay">&nbsp;&nbsp;In-Store Pickup (Free)<br>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t</form>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t</br>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<p>* Same-day shipping applies only to locations within 3 hours of warehouse location</p>\r\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t</form>\r\n\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div> <!-- end of panel, panel-default -->\r\n\t\t\t\t\t\t<div class="panel panel-default">\r\n\t\t\t\t\t\t\t<div class="panel-heading">\r\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\r\n\t\t\t\t\t\t\t\t\t<a data-toggle="collapse" data-parent="#accordion" href="#collapseFour">Payment Information\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</h4>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t<div id="collapseFour" class="panel-collapse collapse in">\r\n\t\t\t\t\t\t\t\t<div class="panel-body">\r\n\t\t\t\t\t\t\t\t\t<div class="container">\r\n\t\t\t\t\t\t\t\t\t\t<form role="form">\r\n\t\t\t\t\t\t\t\t\t\t\t<div class="form-group">\r\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="col-md-4">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="CardNumber">Card Number</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="card" class="form-control" id="cardNum" placeholder="XXXX-XXXX-XXXX-XXXX">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ExpMonth">Expiration Month</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<select class="form-control">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>Select One</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>1</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>2</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>3</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>4</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>5</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>6</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>7</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>8</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>9</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>10</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>11</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>12</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</select>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="col-md-4">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t<table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="SecurityCode">Security Code</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="SecCode" class="form-control" id="sCard" placeholder="XXX">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="glyphicon glyphicon-question-sign"></span>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<td> \r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="ExpYr">Expiration Year</label>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<select class="form-control">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>Select One</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>2020</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>2019</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>2018</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>2017</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>2016</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>2015</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<option>2014</option>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</select>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t</br>\r\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t\t\t</form>\r\n\t\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div> <!-- end of panel, panel-default -->\r\n\t\t\t\t\t</div> <!--end accordion-->\r\n\t\t\t\t\t</br>\r\n\t\t\t\t\t<a class="btn btn-warning" button type="button"><span class="glyphicon glyphicon-shopping-cart">&nbsp;&nbsp;Confirm</span></a>\r\n\r\n\t\t\t\t</div> <!--ends col-md-9 --> \r\n\t\t\t</div>\r\n\t\t</div> <!--ends container-->\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


