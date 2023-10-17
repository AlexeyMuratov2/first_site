from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import FreeServices
from .models import SiteOrder
from .forms import SiteForm
from django.contrib import messages


# Create your views here.
def index(request):
    #tasks = Task.objects.all()
    services_free = FreeServices.objects.filter()[:1].get()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'services': services_free})


def about_us(request):
    return render(request, 'main/about_us.html')

def create_site(request):
    submitted = False
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_site?submitted=True')
    else:
        form = SiteForm(initial={'user': request.user})
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/create_site_request.html', {'form':form, 'submitted': submitted})

def order_list(request):
    orders = SiteOrder.objects.all()
    return render(request, 'main/order_list.html', {'orders': orders})

def my_orders(request, order_id):
    order = SiteOrder.objects.get(pk = order_id)
    return render(request, 'main/my_order.html', {'order': order})

def update_order(request, order_id):
    order = SiteOrder.objects.get(pk=order_id)
    form = SiteForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('orders')

    return render(request, 'main/update_order.html', {'order': order, 'form': form})

def delete_order(request, order_id):
    order = SiteOrder.objects.get(pk=order_id)
    messages.success(request, f'вы удалили заказ {order}')
    order.delete()
    return redirect('orders')
