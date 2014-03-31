# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1395968388.844325
_enable_loop = True
_template_filename = 'C:\\Users\\Jordan Carlson\\Desktop\\MyStuff\\catalog\\templates/cart.html'
_template_uri = 'cart.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        cart_all = context.get('cart_all', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 84
        __M_writer('  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        cart_all = context.get('cart_all', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n')
        # SOURCE LINE 5
 

        __M_writer('\r\n')
        # SOURCE LINE 6
        if cart_all:
            # SOURCE LINE 7
            __M_writer('\r\n')
            # SOURCE LINE 8
            for c in cart_all.cartItem_list:
                # SOURCE LINE 9
                if c.error !='':
                    # SOURCE LINE 10
                    __M_writer("\t\t\t<div class='alert alert-danger'>")
                    __M_writer(str(c.error))
                    __M_writer('</div>\r\n')
            # SOURCE LINE 13
            __M_writer('\r\n')
            # SOURCE LINE 14
            if cart_all.cartItem_list:
                # SOURCE LINE 15
                __M_writer("\t<table class='table table-striped'>\r\n\t\t<thead>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Price</th>\r\n\t\t\t<th>Quantity</th>\r\n\t\t\t<th></th>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\t\t\t<!-- Shopping Cart Items -->\r\n")
                # SOURCE LINE 24
                for c in cart_all.cartItem_list:
                    # SOURCE LINE 25
                    __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
                    # SOURCE LINE 26
                    __M_writer(str(c.item.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(c.item.name))
                    __M_writer('</td>\r\n\t\t\t\t<td>')
                    # SOURCE LINE 27
                    __M_writer(str(c.item.listPrice))
                    __M_writer('</td>\r\n\t\t\t\t<td>')
                    # SOURCE LINE 28
                    __M_writer(str(c.qty))
                    __M_writer("</td>\r\n\t\t\t\t<td><a href='/catalog/cart__delete/")
                    # SOURCE LINE 29
                    __M_writer(str(c.item.id))
                    __M_writer("'><button class='btn btn-danger btn-sm'><span class='glyphicon glyphicon-remove'></span></button></a></td>\r\n\t\t\t</tr>\r\n")
                # SOURCE LINE 32
                __M_writer('\t\t\t<tr>\r\n\t\t\t<!-- \t<td>&nbsp;</td> -->\r\n\t\t\t\t<td>&nbsp;</td>\r\n\t\t\t\t<td>&nbsp;</td>\r\n\t\t\t\t<td>&nbsp;</td>\r\n\t\t\t\t<td>&nbsp;</td>\r\n\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\r\n\t\t\t\t<td></td>\r\n\t\t\t\t<td><strong>Subtotal:</strong></td>\r\n\t\t\t\t<td>$</td>\r\n\t\t\t\t<td>')
                # SOURCE LINE 45
                __M_writer(str(cart_all.extended_sum))
                __M_writer('</td>\r\n\t\t\t</tr>\r\n\t\t</tbody>\r\n\t</table>\r\n\t<br/>\r\n')
            # SOURCE LINE 51
            __M_writer('\r\n')
            # SOURCE LINE 52
            if cart_all.rentalItem_list:
                # SOURCE LINE 53
                __M_writer("\t<h3>Rentals</h3>\r\n\t<table class='table table-striped'>\r\n\t\t<thead>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Price/Day</th>\r\n\t\t\t<th></th>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\t\t\t<!-- Rental Items -->\r\n")
                # SOURCE LINE 62
                for c in cart_all.rentalItem_list:
                    # SOURCE LINE 63
                    __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
                    # SOURCE LINE 64
                    __M_writer(str(c.item.catalogItem.manufacturer))
                    __M_writer(' ')
                    __M_writer(str(c.item.catalogItem.name))
                    __M_writer('</td>\r\n\t\t\t\t<td>')
                    # SOURCE LINE 65
                    __M_writer(str(c.item.pricePerDay))
                    __M_writer("</td>\r\n\t\t\t\t<td><a href='/catalog/cart__delete/")
                    # SOURCE LINE 66
                    __M_writer(str(c.item.id))
                    __M_writer("/rental/'><button class='btn btn-danger btn-sm'><span class='glyphicon glyphicon-remove'></span></button></a></td>\r\n\t\t\t</tr>\r\n")
                # SOURCE LINE 69
                __M_writer('\t\t</tbody>\r\n\t</table>\r\n\t<br/>\r\n')
            # SOURCE LINE 73
            __M_writer("\r\n\t<a href='/catalog/checkout/' class='btn btn-primary'>Checkout</a>\r\n\r\n")
            # SOURCE LINE 76
        else:
            # SOURCE LINE 77
            __M_writer('\tThere are no items in your shopping cart. Check out our catalog to find the hottest new items.\r\n\t<br/>\r\n\t<br/>\r\n\t<a href="/catalog/category/" class=\'btn btn-primary\'>Go to Catalog</a>\r\n\r\n')
        # SOURCE LINE 83
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


