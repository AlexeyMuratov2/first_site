from django.shortcuts import render, redirect
from .models import Task
from .models import FreeServices
from .forms import TaskForm


# Create your views here.
def index(request):
    #tasks = Task.objects.all()
    services_free = FreeServices.objects.filter()[:1].get()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'services': services_free})


def about_us(reqest):
    return render(reqest, 'main/about_us.html')

def create(reqest):
    error = ''
    if reqest.method == 'POST':
        form = TaskForm(reqest.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма введена неверно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(reqest, 'main/create.html', context)