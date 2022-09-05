
from django.contrib import messages
from django.shortcuts import render
from App_Payment.models import BillingAddress
from App_Payment.forms import BillingForm
from django.contrib.auth.decorators import login_required
from App_Order.models  import Order,Cart
from django.shortcuts import redirect

# Create your views here.

@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST,instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request,f"Shipping Address Saved!")
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()
    return render(request,'App_Payment/checkout.html',context={'form':form,'order_items':order_items,'order_total':order_total,'saved_address':saved_address})

@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_filled():
        messages.info(request,f"Please complete shipping address!")
        return redirect('App_Payment:checkout')
    if not request.user.profile.is_fully_filled():
        messages.info(request,f"Please complete profile details!")
        return redirect('App_Login:change_profile')
    return redirect('App_Shop:home')