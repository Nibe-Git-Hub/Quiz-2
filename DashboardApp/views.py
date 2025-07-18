from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def list(request):
    return render(request, 'list.html')