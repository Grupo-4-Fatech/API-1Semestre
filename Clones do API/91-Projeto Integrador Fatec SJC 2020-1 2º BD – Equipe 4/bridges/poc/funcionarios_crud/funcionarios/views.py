from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def main(request):
    return render(request, "main.html")

