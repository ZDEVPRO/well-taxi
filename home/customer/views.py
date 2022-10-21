from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/kirish/')
def customer(request):
    if request.method == 'POST':
        data = TempOrder()
        data.qayerdan = request.POST.get('qayerdan')
        data.qayerga = request.POST.get('qayerga')
        data.client_name = 'Zikirillo'
        data.client_phone = '+998941600021'
        data.customer = request.user
        data.save()
        messages.success(request, 'Buyurtma qabul qilindi!')
        return redirect('customer-kutish', data.id)
    return render(request, 'customer/index.html')


@login_required(login_url='/kirish/')
def kutish(request, id):
    order = TempOrder.objects.get(id=id)

    context = {
        'order': order
    }
    return render(request, 'customer/kutish.html', context)


@login_required(login_url='/kirish/')
def delete_order(request, id):
    try:
        order = Order.objects.get(id=id)
    except Exception as e:
        print(e)
        order = TempOrder.objects.get(id=id)
    order.delete()
    messages.success(request, 'Muvoffaqiyatli o`chirildi!')
    return redirect('customer')


@login_required(login_url='/kirish/')
def right_order(request, id):
    temp_order = TempOrder.objects.get(id=id)

    data = Order()
    data.status = 'yangi'
    data.qayerdan = temp_order.qayerdan
    data.qayerga = temp_order.qayerga
    data.person_count = temp_order.person_count
    data.price = temp_order.price
    data.client_phone = temp_order.client_phone
    data.client_name = temp_order.client_name
    data.customer = request.user
    data.save()
    messages.success(request, 'Buyurtmangiz doskaga muffaqiyatli chiqarildi!')

    temp_order.delete()
    return redirect('customer')


@login_required(login_url='/kirish/')
def myorders(request):
    orders = Order.objects.all().order_by('-id')

    context = {
        'myorders': orders
    }
    return render(request, 'customer/myorders.html', context)


@login_required(login_url='/kirish/')
def order_detail(request, id):
    order = Order.objects.get(id=id)

    context = {
        'order': order
    }
    return render(request, 'customer/order_detail.html', context)
