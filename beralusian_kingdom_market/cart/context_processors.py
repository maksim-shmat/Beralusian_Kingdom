"""Add cart into a context of any templates."""

from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}
