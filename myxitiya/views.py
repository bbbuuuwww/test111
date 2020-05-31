from django.shortcuts import render
from django.http import HttpResponse, request, response
from myxitiya.models import Item, Spider
from django.template import loader, RequestContext
from django.shortcuts import render
from django.db import transaction, DatabaseError
import random
import datetime
# Create your views here.


def add(request):
    r = open("1.txt", "r")
    ts_list = r.read().split("https", )
    for i in ts_list:
        item = Item()
        item.url = "https"+i
        item.type = random.randint(1, 5)
        item.name = "t{}".format(random.randint(1, 5))
        item.create_time = str(datetime.datetime.now())
        item.save()
        # with transaction.atomic():
        #     item.save()
        #     raise DatabaseError


    return HttpResponse("hello")

def index(request):
    print(11111)
    item = Item.objects.filter(id__gte=1024).order_by("type")
    context =  {"title": "nimabi"}
    context["content"] = item[0].get_dict()
    # temp = loader.get_template("myxitiya/index.html")
    #return HttpResponse(temp.render())
    return render(request, "myxitiya/index.html", context=context)

def find(request):
    print()
    item = Item.objects.get(id=random.randint(1020, 1400))

    print(item.get_dict())
    return HttpResponse("htt2")