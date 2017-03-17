from django.shortcuts import render

# Create your views here.
from .models import Custom_User

def home(request):
    return render(request, "welcome.html", {})
