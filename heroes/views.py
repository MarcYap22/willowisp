from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'home.html')
def cloud_page(request):
    return render(request, 'detail_cloud.html')
def jester_page(request):
    return render(request, 'detail_jester.html')
def flowey_page(request):
    return render(request, 'detail_sunflowey.html')
