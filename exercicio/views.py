from django.shortcuts import render

# Create your views here.
def exercicio(request):
    return render(request, 'index.html')