from django.shortcuts import render
# Create your views here. Методы которые будут вызваны при переходе пользователя на какую-то страницу

def index(request):
    return render(request, 'basic/index.html')

def about(request):
    return render(request, 'basic/about.html')

def auth(request):
    return render(request, 'basic/auth.html')