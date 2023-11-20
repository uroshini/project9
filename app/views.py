from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='this is assumption'
    d={'assumption':data,'age':15}
    return render(request,'data_render.html',context=d)
def login(request):
    d={'username':'Harshad','age':26}
    return render(request,'login.html',context=d)
