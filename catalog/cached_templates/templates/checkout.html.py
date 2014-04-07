# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1396907153.38453
_enable_loop = True
_template_filename = '/Users/ecookson/Desktop/MyStuff/catalog/templates/checkout.html'
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
        isRepairEmpty = context.get('isRepairEmpty', UNDEFINED)
        cart_all = context.get('cart_all', UNDEFINED)
        skip_list = context.get('skip_list', UNDEFINED)
        isRentEmpty = context.get('isRentEmpty', UNDEFINED)
        isEmployee = context.get('isEmployee', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def main():
            return render_main(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        # SOURCE LINE 305
        __M_writer('\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        isRepairEmpty = context.get('isRepairEmpty', UNDEFINED)
        cart_all = context.get('cart_all', UNDEFINED)
        skip_list = context.get('skip_list', UNDEFINED)
        isRentEmpty = context.get('isRentEmpty', UNDEFINED)
        isEmployee = context.get('isEmployee', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\n')
        # SOURCE LINE 6
 

        __M_writer('\n\t<div class="container">\n\t\t<h1>Checkout</h1></br>\n\t\t<div class="row">\n\t\t\t<div class="col-md-3">\n\n')
        # SOURCE LINE 12
        if cart_all:
            # SOURCE LINE 13
            __M_writer('\n\t\t\t\t<div class="well">\n\t\t\t\t\t<h3>Your Items</h3>\n\t\t\t\t\t<hr/>\n')
            # SOURCE LINE 17
            for c in cart_all.cartItem_list:
                # SOURCE LINE 18
                __M_writer('\t\t\t\t\t<table>\n\t\t\t\t\t\t<h4><strong>')
                # SOURCE LINE 19
                __M_writer(str(c.item.manufacturer))
                __M_writer(' ')
                __M_writer(str(c.item.name))
                __M_writer('</strong></h4>\n\n')
                # SOURCE LINE 21
                if c.error !='':
                    # SOURCE LINE 22
                    __M_writer("\t\t\t\t\t\t\t<div class='alert alert-danger'><h5>")
                    __M_writer(str(c.error))
                    __M_writer('</h5></div>\n')
                # SOURCE LINE 24
                __M_writer("\t\t\n\t\t\t\t\t\t<ul class='list-inline'>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<img src='")
                # SOURCE LINE 27
                __M_writer(str(c.item.img))
                __M_writer('\' width=\'55px\' alt="')
                __M_writer(str(c.item.manufacturer))
                __M_writer(' ')
                __M_writer(str(c.item.name))
                __M_writer('">\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<ul class=\'list-unstyled\'>\n\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t\t<strong>Price:</strong> $')
                # SOURCE LINE 32
                __M_writer(str(c.item.listPrice))
                __M_writer('\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t\t<strong>Quantity:</strong> ')
                # SOURCE LINE 35
                __M_writer(str(c.qty))
                __M_writer('\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t\t<strong>Extended:</strong> ')
                # SOURCE LINE 38
                __M_writer(str(c.extended))
                __M_writer('\n\t\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t</ul>\n\n\t\t\t\t\t\t<hr/>\n')
            # SOURCE LINE 48
            __M_writer('\t\t\t\t\n\n\n\t\t\t\t\t<table>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td><b>Subtotal: </b></td>\n\t\t\t\t\t\t\t<td></td>\n\t\t\t\t\t\t\t<td></td>\n\t\t\t\t\t\t\t<td>&nbsp;$ ')
            # SOURCE LINE 56
            __M_writer(str(cart_all.extended_sum))
            __M_writer('</td>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td><b>Tax: </b></td>\n\t\t\t\t\t\t\t<td></td>\n\t\t\t\t\t\t\t<td></td>\n\t\t\t\t\t\t\t<td>&nbsp;$ ')
            # SOURCE LINE 62
            __M_writer(str(cart_all.tax))
            __M_writer('</td>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td><b>TOTAL: </b></td>\n\t\t\t\t\t\t\t<td></td>\n\t\t\t\t\t\t\t<td></td>\n\t\t\t\t\t\t\t<td>&nbsp;<u>$ ')
            # SOURCE LINE 68
            __M_writer(str(cart_all.total))
            __M_writer('</u></td>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t</table>\n\t\t\t\t\t<br>\n\t\t\t\t</div> <!--closes the "well" -->\n')
        # SOURCE LINE 74
        __M_writer('\n\t\t\t\t<div class="well">\n\t\t\t\t\t<div class="container">\n\t\t\t\t\t\t<table>\n\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t<td><img src="http://www.logostage.com/logos/american-express.jpg" width=40px alt="AmExpress Logo"></td>\n\t\t\t\t\t\t\t\t<td><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/MasterCard_logo.png/800px-MasterCard_logo.png" width=50px alt="MaCard Logo"></td>\n\t\t\t\t\t\t\t\t<td><img src="http://embroiderystitchbystitch.com/wp-content/uploads/2012/02/Visa-Credit-Card-Logo-5.jpg" width=50px alt="ViCard Logo"></td>\n\t\t\t\t\t\t\t\t<td><img src="http://www.credit-card-logos.com/images/discover_credit-card-logos/discover_network2.jpg" width=50px alt="DisCard Logo"></td>\n\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t</div>\n\t\t\t\t</div> <!--closes the "well" -->\n\n\t\t\t\t<div class=\'well\'>\n\t\t\t\t\t<div class=\'container\'>\n\t\t\t\t\t\t<strong>Promo Code</strong> \n\t\t\t\t\t\t</br>\n\t\t\t\t\t\t<input type="name" class="col-md-2" id="fName" placeholder="Promo Code">\n\t\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\n\n\n\t\t\t\t\t\n\n<!-- MAIN PART -->\n\n\n\t\t\t\t<div class="col-md-9">\n\n\t\t\t\t\t')
        # SOURCE LINE 107
        bSide = True
                                               
        
        # SOURCE LINE 108
        __M_writer('\n\t\t\t\t\t')
        # SOURCE LINE 109
        spacer = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' 
        
        __M_writer('\n\t\t\t\t\t<!-- ######################## -->\n\t\t\t\t\t<!-- ## CREATE PANEL SECTION #-->\n\t\t\t\t\t<!-- ######################## -->\n\n\t\t\t\t\t<div class="panel-group" id="accordion">\n\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\n\t\t\t\t\t\t\t\t\tBilling Address\n\t\t\t\t\t\t\t\t</h4>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="panel-body">\n\t\t\t\t\t\t\t\t<form class ="form-horizontal" role="form" method ="POST">\n\t\t\t\t\t\t\t\t<table>\n\n\n')
        # SOURCE LINE 128
        for f in form:
            # SOURCE LINE 129
            __M_writer('\n<!-- IF Logic to only make this if its a user doing the checkout -->\n')
            # SOURCE LINE 131
            if isEmployee == False:
                # SOURCE LINE 132
                if f.label == 'Same as Billing':
                    # SOURCE LINE 133
                    __M_writer('\t\t\t\t\t\t')
                    print('SAME AS BILLING!!!')
                    
                    __M_writer('\n\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t<!-- end the table -->\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<!-- end the panel -->\n\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\n\t\t\t\t\t\t\t\t\tShipping Address\n\t\t\t\t\t\t\t\t</h4>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="panel-body">\n\n\t\t\t\t\t\t\t\t<table>\n\n\t\t\t\t\t\t<!-- create the next panel -->\n\t\t\t\t\t\t\n\t\t\t\t\t\t')
                    # SOURCE LINE 154
                    bSide = True
                                                                   
                    
                    # SOURCE LINE 155
                    __M_writer('\n')
            # SOURCE LINE 158
            __M_writer("\n<!-- IF Logic to only make this if the RENT cart isn't empty -->\n")
            # SOURCE LINE 160
            if isRentEmpty == False:
                # SOURCE LINE 161
                if f.label == 'Days to Rent':
                    # SOURCE LINE 162
                    __M_writer('\t\t\t\t\t\t')
                    print('days to rent')
                    
                    __M_writer('\n\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t<!-- end the table -->\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<!-- end the panel -->\n\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\n\t\t\t\t\t\t\t\t\tRental Info\n\t\t\t\t\t\t\t\t</h4>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="panel-body">\n\n\t\t\t\t\t\t\t\t<table>\n\n\t\t\t\t\t\t<!-- create the next panel -->\n\n\t\t\t\t\t\t')
                    # SOURCE LINE 183
                    bSide = True
                                                                   
                    
                    # SOURCE LINE 184
                    __M_writer('\n')
            # SOURCE LINE 187
            __M_writer("\n<!-- IF Logic to only make this if the REPAIR cart isn't empty -->\n\n")
            # SOURCE LINE 190
            if isRepairEmpty == False:
                # SOURCE LINE 191
                if f.label == 'Date Complete':
                    # SOURCE LINE 192
                    __M_writer('\t\t\t\t\t\t')
                    print('Date Complete')
                    
                    __M_writer('\n\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t<!-- end the table -->\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<!-- end the panel -->\n\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\n\t\t\t\t\t\t\t\t\tRepair Info\n\t\t\t\t\t\t\t\t</h4>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="panel-body">\n\n\t\t\t\t\t\t\t\t<table>\n\n\t\t\t\t\t\t<!-- create the next panel -->\n\n\t\t\t\t\t\t')
                    # SOURCE LINE 213
                    bSide = True
                                                                   
                    
                    # SOURCE LINE 214
                    __M_writer('\n')
            # SOURCE LINE 217
            __M_writer('\n')
            # SOURCE LINE 218
            if f.label == 'Credit Card':
                # SOURCE LINE 219
                __M_writer('\t\t\t\t\t\t')
                print('Credit Card')
                
                __M_writer('\n\n\t\t\t\t\t\t</table>\n\t\t\t\t\t\t<!-- end the table -->\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<!-- end the panel -->\n\n\t\t\t\t\t\t<div class="panel panel-default">\n\t\t\t\t\t\t\t<div class="panel-heading">\n\t\t\t\t\t\t\t\t<h4 class="panel-title">\n\t\t\t\t\t\t\t\t\tPayment Info\n\t\t\t\t\t\t\t\t</h4>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="panel-body">\n\n\t\t\t\t\t\t\t\t<table>\n\n\t\t\t\t\t\t<!-- create the next panel -->\n\t\t\t\t\t\t\n\t\t\t\t\t\t')
                # SOURCE LINE 240
                bSide = True
                                                               
                
                # SOURCE LINE 241
                __M_writer('\n')
            # SOURCE LINE 243
            __M_writer('\n\t\t\t\t\t\t<!-- ######################## -->\n\t\t\t\t\t\t<!-- END CREATE PANEL SECTION -->\n\t\t\t\t\t\t<!-- ######################## -->\n\n\t\t\t\t\t')
            # SOURCE LINE 248
            td1 = 'style="width:15%"' 
            
            __M_writer('\n\t\t\t\t\t')
            # SOURCE LINE 249
            td2 = 'style="width:30%"' 
            
            __M_writer('\n\t\t\t\t\t')
            # SOURCE LINE 250
            td3 = 'style="width:2%"' 
            
            __M_writer('\n\t\t\t\t\t')
            # SOURCE LINE 251
            td4 = 'style="width:7%"' 
            
            __M_writer('\n\n\n\n')
            # SOURCE LINE 255
            if f.name in skip_list:
                # SOURCE LINE 256
                __M_writer('\t\t\t\t\t\t')
                print('!!!!SKIPPED!!!')
                
                __M_writer('\n\t\t\t\t\t\t')
                # SOURCE LINE 257
                continue
                
                __M_writer('\n')
                # SOURCE LINE 258
            else:
                # SOURCE LINE 259
                __M_writer('\t\t\t\t\t')
                print('!!!!NOT SKIPPED!!!')
                
                __M_writer('\n')
                # SOURCE LINE 260
                if bSide: 
                    # SOURCE LINE 261
                    __M_writer("\t\t\t\t      \t<!-- Left side -->\n\t\t\t\t    \t<tr>\n\t\t\t\t    \t  <td></td>\n\t\t\t\t          <td class='text-right' ")
                    # SOURCE LINE 264
                    __M_writer(str(td1))
                    __M_writer('><strong>')
                    __M_writer(str( f.label ))
                    __M_writer('</strong></td>\n\t\t\t\t          <td ')
                    # SOURCE LINE 265
                    __M_writer(str(td3))
                    __M_writer('>&nbsp;</td>\n\t\t\t\t          <td ')
                    # SOURCE LINE 266
                    __M_writer(str(td2))
                    __M_writer('>')
                    __M_writer(str(f))
                    __M_writer(' ')
                    __M_writer(str(f.errors))
                    __M_writer('</td>  \n\t\t\t\t          <td ')
                    # SOURCE LINE 267
                    __M_writer(str(td4))
                    __M_writer('></td>\n')
                    # SOURCE LINE 268
                else: 
                    # SOURCE LINE 269
                    __M_writer("\t\t\t\t    \t<!-- Right side -->\n\t\t\t\t    \t\t<td></td>\n\t\t\t\t    \t\t<td class='text-right' ")
                    # SOURCE LINE 271
                    __M_writer(str(td1))
                    __M_writer('><strong>')
                    __M_writer(str( f.label ))
                    __M_writer('</strong></td>\n\t\t\t\t    \t\t<td ')
                    # SOURCE LINE 272
                    __M_writer(str(td3))
                    __M_writer('>&nbsp;</td>\n\t\t\t\t    \t\t<td ')
                    # SOURCE LINE 273
                    __M_writer(str(td2))
                    __M_writer('>')
                    __M_writer(str(f))
                    __M_writer(' ')
                    __M_writer(str(f.errors))
                    __M_writer('</td>  \n\t\t\t\t    \t\t<td></td>\n\t\t\t\t    \t</tr>\n\t\t\t\t    \t<tr>\n\t\t\t\t    \t\t<td>&nbsp;</td>\n\t\t\t\t    \t</tr>\n')
                # SOURCE LINE 280
                __M_writer('\n\t\t\t\t\t\t<!-- Swap from left to right or from right to left -->\n\t\t\t\t\t\t')
                # SOURCE LINE 282
                bSide = not bSide 
                
                __M_writer(' \n\n')
            # SOURCE LINE 285
            __M_writer('\t\t\t\t\t\n')
        # SOURCE LINE 287
        __M_writer('\n\t\t\t\t\t</table>\n\t\t\t\t\t  <div class="form-group">\n\t\t\t\t\t    <div class="col-sm-offset-4 col-sm-4">\n\t\t\t\t\t      <input class="btn btn-success" type="submit" value="Finish Transaction">\n\t\t\t\t\t    </div>\n\t\t\t\t\t  </div>\n\t\t\t\t\t</form>\n\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t</div>\n\n\t</div>\n</div>\n\n\t</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


