from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    # Retrieve the theme value from cookies
    theme = request.COOKIES.get('dark', 'light')
    print("theme", theme)
    return render(request, "Home/home.html",)
