from django.http import HttpResponse


# def hello(request):
#     return HttpResponse("hello world")
#
#
# def fenzu(request, num):
#     return HttpResponse("这是一个分组视图:%s" % (num))
#
#
# def zuming(request, city, year):
#     return HttpResponse("%s年在%s工作" % (year, city))
#
#
# def gethtml(request):
#     html = """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#     </head>
#     <body>
#         <h1>我是一个h1标签</h1>
#     </body>
#     </html>
#     """
#     return HttpResponse(html)
#
#
# from django.shortcuts import render
#
#
# def index(request):
#     name = '张三三'
#     return render(request, 'index.html', {'name': name})
#
#
# from django.shortcuts import render_to_response
#
#
# def index2(request):
#     name = '小二郎'
#     return render_to_response('index2.html', {'name': name})
#
#
# from django.template.loader import get_template
#
#
# def index3(request):
#     template = get_template("index3.html")
#     name = "哈哈哈"
#     result = template.render({'name': name})
#     return HttpResponse(result)
#
#
# def xinxi(request):
#     name = 'zhangsan'
#     age = 18
#     like = ['吃', '喝', '篮球']
#     score = {'语文': 88, '数学': 99}
#     return render(request, 'xinxi.html', locals())
#
#
#
#
# def kongzhi(request, age):
#     print(age)
#     print(type(age))  # <class 'str'>
#     name = 'zhangsan'
#     age = int(age)
#     like = ['吃', '喝', '篮球']
#     score = {'语文': 66, '数学': 77}
#
#     myjs="""
#     <script>
#         alert("你好啊")
#     </script>
#     """
#     return render(request, 'xinxi.html', locals())




