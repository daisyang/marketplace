from django.shortcuts import render

# Create your views here.

# this is our default view
def provider_index(request):
    return render(request, 'base.html', {'title': 'provider'})


def school_index(request):
    return render(request, 'base.html', {'title': 'provider'})