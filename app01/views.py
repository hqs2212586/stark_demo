from django.shortcuts import render, HttpResponse

# Create your views here.

from .models import *

def test(request):
    from django.db.models import Q
    # Q查询普通写法：
    ret = Book.objects.all().filter(Q(title="go")|Q(price=103))
    print("ret", ret)    # ret <QuerySet [<Book: go>]>
    # Q查询特殊用法：
    q = Q()
    q.connectiion = "or"
    q.children.append(("title", "go"))
    q.children.append(("price", 103))
    print("q", q)   # q (AND: ('title', 'yuan'), ('price', 123))
    return HttpResponse(ret, q)
