from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

def Topic1(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('<h1>data inserted in topic model successfully</h1>')
    return render(request,'Topic1.html')

def Webs(request):
    QST=Topic.objects.all()
    d={"topics":QST}
    if request.method=="POST":
        tn=request.POST['topic_name']
        n=request.POST['name']
        u=request.POST['url']
        T=Topic.objects.filter(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=n,url=u)[0]
        W.save()
        return HttpResponse('<h1>data inserted in webpage model successfully</h1>')
        
    return render(request,'Webs.html',d)


def access(request):
    QSW=Webpage.objects.all()
    d={"acces":QSW}
    if request.method=="POST":
        n=request.POST['name']
        dt=request.POST['date']
        W=Webpage.objects.filter(name=n)[0]
        W.save()
        a=AccessRecords.objects.get_or_create(name=W,date=dt)[0]
        a.save()
        return HttpResponse('h1>data inserted in AccessRecords model successfully</h1>')

    return render(request,'access.html',d)

