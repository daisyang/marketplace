from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from marketplace_app.models import Provider,School
from django import forms
from django.shortcuts import get_object_or_404,get_list_or_404
# Create your views here.

# this is our default view



class Provider_form(forms.ModelForm):
    class Meta:
        model = Provider
        widgets = {'name':forms.TextInput(attrs={'id':'first_name'}),
                   'address':forms.TextInput(attrs={'id':'last_name'}),
                   'website':forms.TextInput(attrs={'id':'email'}),
                   'target_school':forms.TextInput(attrs={'id':'country'}),
                   'perception':forms.TextInput(attrs={'id':'affiliations'}),
                   'contact':forms.TextInput(attrs={'id':'cat_name'}),
                   'time_start':forms.TextInput(attrs={'id':'cat_name'}),
                   'time_end':forms.TextInput(attrs={'id':'gagdet'}),

                   }


def provider_money(request):
    # fields = list(Provider_form())
    return render(request, 'provider/money.html',{'form':Provider_form()})

def provider_submit(request):
    f= Provider_form(request.POST)
    if f.is_valid():
        f.save()
        return render(request, 'base.html', {'title': 'provider', 'success_msg': 'Success'})
    else :
        return render(request, 'provider/money.html',{'form':f})
        # return HttpResponseRedirect (reverse('school:school_index'))

def school_index(request):
    p=Provider.objects.all()
    return render(request, 'school/school_index.html', {'providers':p})


def provider_index(request):

    return render(request, 'provider/provider_index.html', {'form':Provider_form()})


def provider_show(request,id):
    p=get_object_or_404(Provider,pk=id)
    form = Provider_form(instance=p)
    return render(request, 'provider/show.html',{'form':form,'is_submit':False})