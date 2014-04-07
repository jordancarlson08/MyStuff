# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396902101.647305
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/checkout.html'
_template_uri = 'checkout.html'
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
        isEmployee = context.get('isEmployee', UNDEFINED)
        cart_all = context.get('cart_all', UNDEFINED)
        isRepairEmpty = context.get('isRepairEmpty', UNDEFINED)
        skip_list = context.get('skip_list', UNDEFINED)
        def main():
            return render_main(context._locals(__M_locals))
        isRentEmpty = context.get('isRentEmpty', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 303
        __M_writer('\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        isEmployee = context.get('isEmployee', UNDEFINED)
        cart_all = context.get('cart_all', UNDEFINED)
        isRepairEmpty = context.get('isRepairEmpty', UNDEFINED)
        skip_list = context.get('skip_list', UNDEFINED)
        def main():
            return render_main(context)
        isRentEmpty = context.get('isRentEmpty', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\r\n')
        # SOURCE LINE 6
 

        __M_writer('\r\n\t<div class="container">\r\n\t\t<h1>Checkout</h1></br>\r\n\t\t<div class="row">\r\n\t\t\t<div class="col-md-3">\r\n\t\t\t\t<div class="well">\r\n\t\t\t\t\t<h3>Your Items</h3>\r\n\t\t\t\t\t<hr/>\r\n\r\n\r\n')
        # SOURCE LINE 16
        for c in cart_all.cartItem_list:
            # SOURCE LINE 17
            __M_writer('\t\t\t\t\t<table>\r\n\t\t\t\t\t\t<h4><strong>')
            # SOURCE LINE 18
            __M_writer(str(c.item.manufacturer))
            __M_writer(' ')
            __M_writer(str(c.item.name))
            __M_writer('</strong></h4>\r\n\r\n')
            # SOURCE LINE 20
            if c.error !='':
                # SOURCE LINE 21
                __M_writer("\t\t\t\t\t\t\t<div class='alert alert-danger'><h5>")
                __M_writer(str(c.error))
                __M_writer('</h5></div>\r\n')
            # SOURCE LINE 23
            __M_writer("\t\t\r\n\t\t\t\t\t\t<ul class='list-inline'>\r\n\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t<img src='")
            # SOURCE LINE 26
            __M_writer(str(c.item.img))
            __M_writer('\' width=\'55px\' alt="')
            __M_writer(str(c.item.manufacturer))
            __M_writer(' ')
            __M_writer(str(c.item.name))
            __M_writer('">\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t<ul class=\'list-unstyled\'>\r\n\t\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t\t<strong>Price:</strong> $')
            # SOURCE LINE 31
            __M_writer(str(c.item.listPrice))
            __M_writer('\r\n\t\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t\t<strong>Quantity:</strong> ')
            # SOURCE LINE 34
            __M_writer(str(c.qty))
            __M_writer('\r\n\t\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t\t<strong>Extended:</strong> ')
            # SOURCE LINE 37
            __M_writer(str(c.extended))
            __M_writer('\r\n\t\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t\t\t</li>\r\n\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t</ul>\r\n\r\n\t\t\t\t\t\t<hr/>\r\n')
        # SOURCE LINE 47
        __M_writer('\r\n\r\n\r\n\t\t\t\t\t<table>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td><b>Subtotal: </b></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td>&nbsp;$ ')
        # SOURCE LINE 55
        __M_writer(str(cart_all.extended_sum))
        __M_writer('</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td><b>Tax: </b></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td>&nbsp;$ ')
        # SOURCE LINE 61
        __M_writer(str(cart_all.tax))
        __M_writer('</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td><b>TOTAL: </b></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td></td>\r\n\t\t\t\t\t\t\t<td>&nbsp;<u>$ ')
        # SOURCE LINE 67
        __M_writer(str(cart_all.total))
        __M_writer('</u></td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t</table>\r\n\t\t\t\t\t<br>\r\n\t\t\t\t</div> <!--closes the "well" -->\r\n\r\n\t\t\t\t<div class="well">\r\n\t\t\t\t\t<div class="container">\r\n\t\t\t\t\t\t<table>\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t<td><img src="http://www.logostage.com/logos/american-express.jpg" width=40px alt="AmExpress Logo"></td>\r\n\t\t\t\t\t\t\t\t<td><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/MasterCard_logo.png/800px-MasterCard_logo.png" width=50px alt="MaCard Logo"></td>\r\n\t\t\t\t\t\t\t\t<td><img src="http://embroiderystitchbystitch.com/wp-content/uploads/2012/02/Visa-Credit-Card-Logo-5.jpg" width=50px alt="ViCard Logo"></td>\r\n\t\t\t\t\t\t\t\t<td><img src="http://www.credit-card-logos.com/images/discover_credit-card-logos/discover_network2.jpg" width=50px alt="DisCard Logo"></td>\r\n\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t</table>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div> <!--closes the "well" -->\r\n\r\n\t\t\t\t<div class=\'well\'>\r\n\t\t\t\t\t<div class=\'container\'>\r\n\t\t\t\t\t\t<strong>Promo Code</strong> \r\n\t\t\t\t\t\t</br>\r\n\t\t\t\t\t\t<input type="name" class="col-md-2" id="fName" placeholder="Promo Code">\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\r\n\r\n\r\n\t\t\t\t\t\r\n\r\n<!-- MAIN PART -->\r\n\r\n\r\n\t\t\t\t<div class="col-md-9">\r\n\r\n\t\t\t\t\t')
        # SOURCE LINE 105
        bSide = True
                                               
        
        # SOURCE LINE 106
        __M_writer('\r\n\t\t\t\t\t')
        # SOURCE LINE 107
        spacer = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' 
        
        __M_writer('\r\n\t\t\t\t\t<!-- ######################## -->\r\n\t\t\t\t\t<!-- ## CREATE PANEL SECTION #-->\r\n\t\t\t\t\t<!-- ######################## -->\r\n\r\n\t\t\t\t\t<div class="panel-group" id="accordion">\r\n\r\n\t\t\t\t\t\t<div class="panel panel-default">\r\n\t\t\t\t\t\t\t<div class="panel-heading">\r\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\r\n\t\t\t\t\t\t\t\t\tBilling Address\r\n\t\t\t\t\t\t\t\t</h4>\r\n\t\t\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t\t\t<div class="panel-body">\r\n\t\t\t\t\t\t\t\t<form class ="form-horizontal" role="form" method ="POST">\r\n\t\t\t\t\t\t\t\t<table>\r\n\r\n\r\n')
        # SOURCE LINE 126
        for f in form:
            # SOURCE LINE 127
            __M_writer('\r\n<!-- IF Logic to only make this if its a user doing the checkout -->\r\n')
            # SOURCE LINE 129
            if isEmployee == False:
                # SOURCE LINE 130
                if f.label == 'Same as Billing':
                    # SOURCE LINE 131
                    __M_writer('\t\t\t\t\t\t')
                    print('SAME AS BILLING!!!')
                    
                    __M_writer('\r\n\r\n\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t<!-- end the table -->\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t<!-- end the panel -->\r\n\r\n\t\t\t\t\t\t<div class="panel panel-default">\r\n\t\t\t\t\t\t\t<div class="panel-heading">\r\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\r\n\t\t\t\t\t\t\t\t\tShipping Address\r\n\t\t\t\t\t\t\t\t</h4>\r\n\t\t\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t\t\t<div class="panel-body">\r\n\r\n\t\t\t\t\t\t\t\t<table>\r\n\r\n\t\t\t\t\t\t<!-- create the next panel -->\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t')
                    # SOURCE LINE 152
                    bSide = True
                                                                   
                    
                    # SOURCE LINE 153
                    __M_writer('\r\n')
            # SOURCE LINE 156
            __M_writer("\r\n<!-- IF Logic to only make this if the RENT cart isn't empty -->\r\n")
            # SOURCE LINE 158
            if isRentEmpty == False:
                # SOURCE LINE 159
                if f.label == 'Days to Rent':
                    # SOURCE LINE 160
                    __M_writer('\t\t\t\t\t\t')
                    print('days to rent')
                    
                    __M_writer('\r\n\r\n\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t<!-- end the table -->\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t<!-- end the panel -->\r\n\r\n\t\t\t\t\t\t<div class="panel panel-default">\r\n\t\t\t\t\t\t\t<div class="panel-heading">\r\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\r\n\t\t\t\t\t\t\t\t\tRental Info\r\n\t\t\t\t\t\t\t\t</h4>\r\n\t\t\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t\t\t<div class="panel-body">\r\n\r\n\t\t\t\t\t\t\t\t<table>\r\n\r\n\t\t\t\t\t\t<!-- create the next panel -->\r\n\r\n\t\t\t\t\t\t')
                    # SOURCE LINE 181
                    bSide = True
                                                                   
                    
                    # SOURCE LINE 182
                    __M_writer('\r\n')
            # SOURCE LINE 185
            __M_writer("\r\n<!-- IF Logic to only make this if the REPAIR cart isn't empty -->\r\n\r\n")
            # SOURCE LINE 188
            if isRepairEmpty == False:
                # SOURCE LINE 189
                if f.label == 'Date Complete':
                    # SOURCE LINE 190
                    __M_writer('\t\t\t\t\t\t')
                    print('Date Complete')
                    
                    __M_writer('\r\n\r\n\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t<!-- end the table -->\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t<!-- end the panel -->\r\n\r\n\t\t\t\t\t\t<div class="panel panel-default">\r\n\t\t\t\t\t\t\t<div class="panel-heading">\r\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\r\n\t\t\t\t\t\t\t\t\tRepair Info\r\n\t\t\t\t\t\t\t\t</h4>\r\n\t\t\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t\t\t<div class="panel-body">\r\n\r\n\t\t\t\t\t\t\t\t<table>\r\n\r\n\t\t\t\t\t\t<!-- create the next panel -->\r\n\r\n\t\t\t\t\t\t')
                    # SOURCE LINE 211
                    bSide = True
                                                                   
                    
                    # SOURCE LINE 212
                    __M_writer('\r\n')
            # SOURCE LINE 215
            __M_writer('\r\n')
            # SOURCE LINE 216
            if f.label == 'Credit Card':
                # SOURCE LINE 217
                __M_writer('\t\t\t\t\t\t')
                print('Credit Card')
                
                __M_writer('\r\n\r\n\t\t\t\t\t\t</table>\r\n\t\t\t\t\t\t<!-- end the table -->\r\n\t\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t\t<!-- end the panel -->\r\n\r\n\t\t\t\t\t\t<div class="panel panel-default">\r\n\t\t\t\t\t\t\t<div class="panel-heading">\r\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\r\n\t\t\t\t\t\t\t\t\tPayment Info\r\n\t\t\t\t\t\t\t\t</h4>\r\n\t\t\t\t\t\t\t</div>\r\n\r\n\t\t\t\t\t\t\t<div class="panel-body">\r\n\r\n\t\t\t\t\t\t\t\t<table>\r\n\r\n\t\t\t\t\t\t<!-- create the next panel -->\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t')
                # SOURCE LINE 238
                bSide = True
                                                               
                
                # SOURCE LINE 239
                __M_writer('\r\n')
            # SOURCE LINE 241
            __M_writer('\r\n\t\t\t\t\t\t<!-- ######################## -->\r\n\t\t\t\t\t\t<!-- END CREATE PANEL SECTION -->\r\n\t\t\t\t\t\t<!-- ######################## -->\r\n\r\n\t\t\t\t\t')
            # SOURCE LINE 246
            td1 = 'style="width:15%"' 
            
            __M_writer('\r\n\t\t\t\t\t')
            # SOURCE LINE 247
            td2 = 'style="width:30%"' 
            
            __M_writer('\r\n\t\t\t\t\t')
            # SOURCE LINE 248
            td3 = 'style="width:2%"' 
            
            __M_writer('\r\n\t\t\t\t\t')
            # SOURCE LINE 249
            td4 = 'style="width:7%"' 
            
            __M_writer('\r\n\r\n\r\n\r\n')
            # SOURCE LINE 253
            if f.name in skip_list:
                # SOURCE LINE 254
                __M_writer('\t\t\t\t\t\t')
                print('!!!!SKIPPED!!!')
                
                __M_writer('\r\n\t\t\t\t\t\t')
                # SOURCE LINE 255
                continue
                
                __M_writer('\r\n')
                # SOURCE LINE 256
            else:
                # SOURCE LINE 257
                __M_writer('\t\t\t\t\t')
                print('!!!!NOT SKIPPED!!!')
                
                __M_writer('\r\n')
                # SOURCE LINE 258
                if bSide: 
                    # SOURCE LINE 259
                    __M_writer("\t\t\t\t      \t<!-- Left side -->\r\n\t\t\t\t    \t<tr>\r\n\t\t\t\t    \t  <td></td>\r\n\t\t\t\t          <td class='text-right' ")
                    # SOURCE LINE 262
                    __M_writer(str(td1))
                    __M_writer('><strong>')
                    __M_writer(str( f.label ))
                    __M_writer('</strong></td>\r\n\t\t\t\t          <td ')
                    # SOURCE LINE 263
                    __M_writer(str(td3))
                    __M_writer('>&nbsp;</td>\r\n\t\t\t\t          <td ')
                    # SOURCE LINE 264
                    __M_writer(str(td2))
                    __M_writer('>')
                    __M_writer(str(f))
                    __M_writer(' ')
                    __M_writer(str(f.errors))
                    __M_writer('</td>  \r\n\t\t\t\t          <td ')
                    # SOURCE LINE 265
                    __M_writer(str(td4))
                    __M_writer('></td>\r\n')
                    # SOURCE LINE 266
                else: 
                    # SOURCE LINE 267
                    __M_writer("\t\t\t\t    \t<!-- Right side -->\r\n\t\t\t\t    \t\t<td></td>\r\n\t\t\t\t    \t\t<td class='text-right' ")
                    # SOURCE LINE 269
                    __M_writer(str(td1))
                    __M_writer('><strong>')
                    __M_writer(str( f.label ))
                    __M_writer('</strong></td>\r\n\t\t\t\t    \t\t<td ')
                    # SOURCE LINE 270
                    __M_writer(str(td3))
                    __M_writer('>&nbsp;</td>\r\n\t\t\t\t    \t\t<td ')
                    # SOURCE LINE 271
                    __M_writer(str(td2))
                    __M_writer('>')
                    __M_writer(str(f))
                    __M_writer(' ')
                    __M_writer(str(f.errors))
                    __M_writer('</td>  \r\n\t\t\t\t    \t\t<td></td>\r\n\t\t\t\t    \t</tr>\r\n\t\t\t\t    \t<tr>\r\n\t\t\t\t    \t\t<td>&nbsp;</td>\r\n\t\t\t\t    \t</tr>\r\n')
                # SOURCE LINE 278
                __M_writer('\r\n\t\t\t\t\t\t<!-- Swap from left to right or from right to left -->\r\n\t\t\t\t\t\t')
                # SOURCE LINE 280
                bSide = not bSide 
                
                __M_writer(' \r\n\r\n')
            # SOURCE LINE 283
            __M_writer('\t\t\t\t\t\r\n')
        # SOURCE LINE 285
        __M_writer('\r\n\t\t\t\t\t</table>\r\n\t\t\t\t\t  <div class="form-group">\r\n\t\t\t\t\t    <div class="col-sm-offset-4 col-sm-4">\r\n\t\t\t\t\t      <input class="btn btn-success" type="submit" value="Finish Transaction">\r\n\t\t\t\t\t    </div>\r\n\t\t\t\t\t  </div>\r\n\t\t\t\t\t</form>\r\n\r\n\t\t\t\t</div>\r\n\t\t\t\t\r\n\t\t\t</div>\r\n\r\n\t</div>\r\n</div>\r\n\r\n\t</div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


