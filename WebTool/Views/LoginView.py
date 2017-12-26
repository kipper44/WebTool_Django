from django.shortcuts import render
from django.http import HttpResponse


#from django.contrib.auth.models import User
#from django.contrib.auth import login

def Index(request):
    if request.method =='POST' :
        print(request.POST.get('id'))
        print(request.POST.get('userpass'))
    #new_user = User.objects.create_user()
    #print(new_user)
    #login(request, new_user)
    return render(request,'WebTool/Index.html')

