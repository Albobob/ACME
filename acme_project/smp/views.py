from django.shortcuts import render



# Create your views here.
def smp(request):
    template = 'smp/mean_morbidity.html'
    return render(request, template)
