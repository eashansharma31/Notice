from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import Noticeform
from .models import Notice
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from urllib.request import urlopen
import json
# from .models import Object

# Create your views here.

def home(request):
    x=Notice.objects.all()
    response=urlopen("https://api.quotable.io/random")
    data=json.loads(response.read())
    quote=data['content']
    return render(request,"Noticeapp/index.html",{"x":x,"quote":quote})

def id():
    x=Notice.objects.all().count()
    return x+1

@login_required
@user_passes_test(lambda u: u.is_superuser)
def createnotice(request):
    if request.method=="GET":
        x=Notice.objects.all()
        y=id()
        initial_data = {'S_No': y}
        form=Noticeform(initial=initial_data)
        form.fields['S_No'].widget.attrs['readonly'] = True
        return render(request,"Noticeapp/createnotice.html",{"form":form,"x":x})
    else:
        form=Noticeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("createnotice")
        else:
            return HttpResponse("form not valid")

@login_required
@user_passes_test(lambda u: u.is_superuser)       
def deletenotice(request,i):
        notice_obj=get_object_or_404(Notice,pk=i)
        notice_obj.delete()
        return redirect("createnotice")


def count_objects(request):
        x=x=Notice.objects.all().count()
        data = {'count': x}
        return JsonResponse(data)
    
def quote(request):
    response=urlopen("https://api.quotable.io/random")
    data=json.loads(response.read())
    quote= {'quote': data['content']}
    return JsonResponse(quote)