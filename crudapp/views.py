from collections import UserList
from django.shortcuts import redirect, render

from crudapp.forms import UserForm
from crudapp.models import userModel
from django.http import HttpResponseRedirect

# Create your views here.
def HomeView(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['Full_Name']
            em = fm.cleaned_data['Email']
            ad = fm.cleaned_data['Address']
            ph = fm.cleaned_data['Phone_Number']
            db = fm.cleaned_data['Birth_Date']
            reg = userModel(Full_Name=fn,Email=em,Address=ad,Phone_Number=ph,Birth_Date=db)
            reg.save()
            return redirect('homepage')
    else:
        fm = UserForm
    inf = userModel.objects.all()
    return render(request,'crudapp/home.html',{'form':fm,'infom':inf})
def Delete_Data(request,id):
    if request.method == 'POST':
        reg = userModel.objects.get(id=id)
        reg.delete()
        return redirect('homepage')

def Update_Data(request,id):
    if request.method =='POST':
        reg = userModel.objects.get(pk=id)
        fm = UserForm(request.POST, instance=reg )
        if fm.is_valid():
            reg.save() 
            return redirect('homepage')
    else:
        reg = userModel.objects.get(pk=id)
        fm = UserForm(instance=reg)
    return render(request,'crudapp/update.html',{'form':fm})

