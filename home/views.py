from django.shortcuts import render, redirect
from asyncio.log import logger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


@login_required(login_url='/kirish/')
def homeView(request):
    if request.user.is_authenticated:
        return switcher(request.user)
    else:
        return redirect('kirish')


def switcher(user):
    try:
        if user.type == 1:
            return redirect('driver')
        elif user.type == 2:
            return redirect('driver')
        elif user.type == 3:
            return redirect('customer')
        else:
            return redirect('logout')
    except Exception as e:
        logger.error(f"{e}")
        return redirect('logout')


def customer_register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.type = 3
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/customer/register.html", context={"form": form})


def customer_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    form = AuthenticationForm()
    context = {'login_form': form}
    return render(request, 'registration/customer/login.html', context)


def driver_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    form = AuthenticationForm()
    context = {'login_form': form}
    return render(request, 'registration/driver/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('kirish')


def kirish(request):
    return render(request, 'registration/kirish.html')
