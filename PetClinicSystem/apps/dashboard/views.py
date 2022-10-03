from django.shortcuts import render

def dashbaord(request):
    return render(request, 'index.html')