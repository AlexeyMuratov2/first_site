from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import FreeServices
from .forms import SiteForm


# Create your views here.
def index(request):
    #tasks = Task.objects.all()
    services_free = FreeServices.objects.filter()[:1].get()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'services': services_free})


def about_us(reqest):
    return render(reqest, 'main/about_us.html')

def create_site(reqest):
    submitted = False
    if reqest.method == 'POST':
        form = SiteForm(reqest.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_site?submitted = True')
    else:
        form = SiteForm
        if 'submitted' in reqest.GET:
            submitted = True
    return render(reqest, 'main/create_site_request.html', {'form':form, 'submitted': submitted})
