from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

def about(request):
    return HttpResponse('这是一个about页面')


def gethtml(request):
    
    html="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    </head>
    <body>
        <h1>我是一个h1标签</h1>
    </body>
    </html>
    """
    # return HttpResponse(html)
from django.shortcuts import render
def indextemp(request):
    name='哈士奇'
    return render(request,'index.html',{'name':name})

from django.shortcuts import render_to_response
def abc(request):
    return render_to_response('abc.html')


def tpl(request,age):
    print(age)
    print(type(age))
    name='zhangsan'
    age=int(age)
    like=['吃','喝','玩']
    score={'语文':66,'数学':77}

    return render(request,'tpl.html',locals())



