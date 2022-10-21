from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url='/kirish/')
def index(request):
    orders_all = Order.objects.filter(status='yangi').order_by('-id')

    context = {
        'orders': orders_all
    }
    return render(request, 'driver/orders.html', context)


@login_required(login_url='/kirish/')
def myorders(request):
    myorder = Order.objects.filter(driver=request.user).order_by('-id')

    context = {
        'myorder': myorder
    }
    return render(request, 'driver/myorders.html', context)


@login_required(login_url='/kirish/')
def order_detail(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'POST':
        data = order
        data.status = 'olindi'
        data.driver = request.user
        data.save()
        messages.success(request, 'Buyurtma qabul qilindi!')
        return redirect('home')
    context = {
        'order': order
    }
    return render(request, 'driver/order_detail.html', context)


@login_required(login_url='/kirish/')
def success_order(request, id):
    order = Order.objects.get(id=id)
    arch = ArchiveOrder()
    arch.status = 'yetkazildi'
    arch.qayerdan = order.qayerdan
    arch.qayerga = order.qayerga
    arch.person_count = order.person_count
    arch.price = order.price
    arch.client_phone = order.client_phone
    arch.client_name = order.client_name
    arch.customer = order.customer
    arch.driver = order.driver
    arch.save()
    order.delete()
    return redirect('driver-myorders')


def getOrders(request):
    queryset = Order.objects.all().order_by('-id')
    return JsonResponse({'orders': list(queryset.values())})
