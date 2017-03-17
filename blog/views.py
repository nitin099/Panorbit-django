from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Custom_User

def home(request):

    return render(request, "index.html", {})

#@login_required(login_url='/posts/login/')
def create(request):
    form = CustomForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return redirect('posts:create')
    context = {
    'form' : form
    }
    return render(request, 'welcome.html', context)

def details(request, id=None):
    instance = get_object_or_404(Custom_User, id=id)
    context={
    'instance':instance,
    }
    return render(request, 'details.html', context)


def update(request, id=None):
    instance = get_object_or_404(Custom_User, id=id)
    form = CustomForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request, 'edit.html', {'form':form})
