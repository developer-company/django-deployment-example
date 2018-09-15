from django.shortcuts import render
from app3.models import topic
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request,"app3/index.html")

def topic(request):
    esmha=topic.objects.order_by("name")

    name_dict={'sex':esmha}
    return render(request,"app3/vorode3.html",context=name_dict)
