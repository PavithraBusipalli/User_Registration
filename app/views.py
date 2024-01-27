from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def userregistration(request):
    ufo = UserForm()
    pfo = ProfileForm()
    d = {'ufo':ufo, 'pfo':pfo}
    if request.method == 'POST' and request.FILES :
        UF = UserForm(request.POST)
        PF = ProfileForm(request.POST,request.FILES)
        if UF.is_valid() and PF.is_valid():
            MUFO = UF.save(commit=False)
            pswd = UF.cleaned_data['password']
            MUFO.set_password(pswd)
            MUFO.save()
            UF.save()
            MPFO = PF.save(commit=False)
            MPFO.username = MUFO
            MPFO.save()
            return HttpResponse('Registered Successfully!!')
        else:
            return HttpResponse('Invalid Data')
    else:
        print('deactivate--------')

    return render(request, 'userregistration.html',d)

