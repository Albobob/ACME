from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def smp(request):
    template = 'smp/base.html'
    return render(request, template)
