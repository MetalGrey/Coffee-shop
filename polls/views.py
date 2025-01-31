from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Assortment, Order, OrderItem
from django.template import loader
from .forms import EmailForm, OrderForm
from decimal import Decimal
import json
import logging
import urllib.parse

logger = logging.getLogger(__name__)

def custom_404(request, exception):
    return render(request, '404.html', status=404)


def save_cart_to_cookies(response, cart_data):
    response.set_cookie('cart', json.dumps(cart_data), max_age=7*24*60*60)  # 7 days

def index(request):

    cart = request.COOKIES.get('cart', '{}')
    cart_items = []
    total_price = Decimal(0)

    decoded_data = urllib.parse.unquote(cart)

    try:
        cart_data = json.loads(decoded_data)
        for item in cart_data.get('items', []):
            item_total = Decimal(item['price'] * item['quantity'])
            total_price += item_total
            cart_items.append({
                'name': item['name'],
                'quantity': item['quantity'],
                'price': item['price'],
                'total': item_total
            })
    except (ValueError, KeyError):
        pass


    latest_assortment_list = Assortment.objects.filter(type=Assortment.COFFEE).order_by("-pub_date")[:6]
    latest_assortment_tools_list = Assortment.objects.filter(type=Assortment.TOOLS).order_by("-pub_date")[:6]


    alert_message = None 
    form = EmailForm(request.POST) if request.method == 'POST' else EmailForm()
    form_order = OrderForm(request.POST) if request.method == 'POST' else OrderForm()

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            alert_message = "Succsess!"

        if form_order.is_valid():
            order = form_order.save(commit=False)
            form_order.save()
            alert_message = "Succsess order!"
            
            try: 
                for item in cart_data.get('items', []):
                    product = Assortment.objects.get(id=item['id'])
                    order_item = OrderItem(
                                order=order,
                                assortment=product,
                                quantity=item['quantity'],
                                price=item['price']
                            )
                    order_item.save()
            except (ValueError, KeyError, Assortment.DoesNotExist):
                pass


    

    logger.debug("Cart items: %s", cart_items)
    logger.debug("Total price: %s", total_price)
    context = {"latest_assortment_list": latest_assortment_list,
               "latest_assortment_tools_list": latest_assortment_tools_list,
               "form": form,
               "form_order": form_order,
               "alert_message": alert_message,  
                "cart_items": cart_items,
               "total_price": total_price,
               }
    return render(request, "index.html", context)


def detail(request, assortment_id):
    assortment = get_object_or_404(Assortment, pk=assortment_id)
    return render(request, "detail.html", {"assortment": assortment})




