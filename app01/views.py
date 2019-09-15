from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def ss(request):
    return HttpResponse('okokokok!!!')


def add(request):
    # save 1 实例化后直接加参数
    # person = Person(name='张三', gender=1, age=18)
    # person.save()

    # save 2 先实例化，再利用属性赋值
    # person = Person()
    # person.name = '李四'
    # person.gender = 0
    # person.age = 20
    # person.save()

    # create
    # Person.objects.create(name='王五', gender=1, age=25)

    # data = dict(name='赵六', gender=1, age=22)
    # Person.objects.create(**data)
    return HttpResponse('添加成功')


def query(request):
    # all() 返回符合条件的所有数据
    # data = Person.objects.all()  # 返回一个QuerySet查询集，表示从数据库中获取的一个对象集合
    # print(data)
    # print(data[0].name)  # 可以使用索引，打印相关属性
    # print(data[0].gender)
    # print(data[0].age)
    # for one in data:  # 可以遍历
    #     print(one.name)

    # get() 返回单个满足条件的对象,get后面的条件常用主键
    # data=Person.objects.get(id=4)
    # print(data.name)

    # filter() 返回满足条件的数据,返回一个QuerySet,类似于sql中的 where
    # data=Person.objects.filter(name='赵六')  # 使用遍历或者下标提取属性的值
    # print(data[0].age)

    # first() 返回一个对象，返回符合条件的第一个对象
    # data=Person.objects.filter(name='张三').first()
    # print(data.age)

    # last() 返回一个对象，返回符合条件的最后一个对象
    # data=Person.objects.filter(name='张三').last()
    # print(data.age)

    # order_by()
    # data=Person.objects.order_by('age')  # 升序
    # data=Person.objects.order_by('-age')  # 降序
    # for one in data:
    #     print(one.age)

    # exclude() 排除，返回一个QuerySet，不符合限制条件的所有数据
    # data=Person.objects.exclude(name='张三')
    # for one in data:
    #     print(one.name)

    # values() 返回[对象，对象，对象]
    # data=Person.objects.filter(name='张三').values()
    # print(data)
    # <QuerySet [{'id': 1, 'age': 28, 'name': '张三', 'gender': 1}, {'id': 2, 'age': 18, 'name': '张三', 'gender': 1}]>
    # for one in data:
    #     print(one)
    # {'age': 28, 'id': 1, 'gender': 1, 'name': '张三'}
    # {'age': 18, 'id': 2, 'gender': 1, 'name': '张三'}

    # count() 返回的是符合当前条件的数据的条数
    # data=Person.objects.filter(name='张三').count()
    # print(data)

    # exists() 返回一个True或者False判断是否存在
    # data = Person.objects.filter(name="李白").exists()
    # print (data)

    # [m:n] 切片
    # id  1 2 3 4 5
    # 切片 0 1 2 3 4
    # data = Person.objects.order_by("id")[2:4]
    # print(data)
    # for one in data:
    #     print(one.name)
    return HttpResponse('查询成功')


def update(request):
    # update
    # Person.objects.filter(id=2).update(name="张666")
    return HttpResponse('修改成功')


def delete(request):
    # delete()
    # Person.objects.filter(id=2).delete()
    return HttpResponse('删除成功')

def scx(request):
    # __lt 小于(less than)
    # data = Person.objects.filter(id__lt=3)
    # print (data)

    # __gt 大于(greater than)
    # data = Person.objects.filter(id__gt=3)
    # print (data)

    # __gte 大于等于(great than or equal)
    # data = Person.objects.filter(id__gte=3)
    # print (data)

    # __lte 小于等于(less than or equal)
    # data = Person.objects.filter(id__lte=3)
    # print (data)

    # in 包含 相当于select * from stu where id in (1,2,3,4);
    # data = Person.objects.filter(id__in = [1,2,3])
    # print (data)

    # exclude 不包含

    # range 范围
    # data = Person.objects.filter(id__range = [1,5])
    # print (data)

    # startswith 像 like j% endswith 像 %j
    # data = Person.objects.filter(name__startswith="张")
    # print (data)

    # endswith

    # __contains 包含 大小写敏感
    # data = Person.objects.filter(name__contains="w")
    # print(data)

    # __icontains 包含，大小写不敏感
    # data = Person.objects.filter(name__icontains="w")
    # print(data)
    return HttpResponse('双查询成功')

def yddadd(request):
    # 增加出版社
    # Publish.objects.create(name='山东出版社',address = '山东')
    # Publish.objects.create(name='山西出版社',address = '山西')
    # Publish.objects.create(name='河南出版社',address = '河南')
    # Publish.objects.create(name='河北出版社',address = '河北')

    # 增加书
    # Book.objects.create(name='西游记',p_id = 1)
    # Book.objects.create(name='三国演义',p_id = 1)

    # 正向操作 从外键所在的表到主表
    # book = Book()
    # book.name = '聊斋'
    # book.p = Publish.objects.get(name='山西出版社')
    # book.save()

    # 反向操作 从主表到从表
    # p= Publish.objects.get(name="山东出版社")
    # p.book_set.create(name='唐诗')
    return HttpResponse('一对多增加成功')

def yddquery(request):
    # 查询的第一种方法
    # publish = Publish.objects.get(name="山东出版社")
    # book = Book.objects.filter(publish_id=publish.id)
    # for x in book:
    #     print (x.name)

    # 正向查询 从外键所在的表到主表
    # 查询 红楼梦 属于哪一个出版社
    # book = Book.objects.filter(name='红楼梦')
    # for one in book:
    #     print(one.publish.name)


    # 反向查询 从主表到从表 _set
    # publish = Publish.objects.get(name='山东出版社')
    # book = publish.book_set.all()
    # for one in book:
    #     print(one.name)
    return  HttpResponse('一对多查询成功')

def yddupdate(request):
    # save 把id=1的书改为河北出版社出版
    # book=Book.objects.get(id=1)
    # book.p=Publish.objects.get(name='河北出版社')
    # book.save()

    # update 把水浒传改为河北出版社出版
    # publish_obj=Publish.objects.get(name='河北出版社')
    # Book.objects.filter(name='水浒传').update(p=publish_obj)

    # set 反向 把id=3和id=4的书修改为河南出版社出版
    # publish_obj = Publish.objects.get(name='河南出版社')
    # book=Book.objects.get(id=3)
    # book1=Book.objects.get(id=4)
    # publish_obj.book_set.set([book,book1])
    return HttpResponse('一对多修改成功')

def ydddelete(request):
    # 一起使用同时删除,先删除外键所在的表，再删除关联表
    # Book.objects.get(id=7).delete()  # 单独使用删除书籍
    # Publish.objects.get(name='搜索').delete()  # 单独使用删除出版社
    return HttpResponse('一对多删除成功')

def dddadd(request):
    # Teacher.objects.create(name='赵老师',gender=1)
    # Teacher.objects.create(name='钱老师',gender=0)
    # Teacher.objects.create(name='孙老师',gender=0)
    # Teacher.objects.create(name='李老师',gender=1)

    # 新学员 田七 是 赵老师 的学生 正向
    # teacher_obj=Teacher.objects.filter(name='赵老师').first()
    # teacher_obj.person.create(name='田七',gender=0,age=16)

    # 老学员 李四 是 钱老师 的学生 正向
    # teacher_obj=Teacher.objects.filter(name='钱老师').first()
    # person_obj=Person.objects.filter(name='李四').first()
    # teacher_obj.person.add(person_obj)

    # 田七 还是 孙老师的学生 反向
    # person_obj=Person.objects.filter(name='田七').first()
    # teacher_obj=Teacher.objects.filter(name='孙老师').first()
    # person_obj.teacher_set.add(teacher_obj)
    return HttpResponse('多对多增加成功')

def dddquery(request):
    # 正向 查到老师信息，寻找这个老师所教的学生
    # teacher_obj=Teacher.objects.filter(name='赵老师').first()
    # person=teacher_obj.person.all()
    # print(person)

    # 反向 查到学生信息，寻找这个学生的老师
    # person_obj=Person.objects.filter(name='李四').first()
    # teacher_obj=person_obj.teacher_set.all()
    # print(teacher_obj)
    return HttpResponse('多对多查询成功')

def dddupdate(request):
    # 正向 从外键所在表到关联表   t-p
    # 孙老师教 赵六 和 田七
    # teacher_obj = Teacher.objects.filter(name='孙老师').first()
    # person1=Person.objects.filter(name='赵六').first()
    # person2=Person.objects.filter(name='田七').first()
    # set 后面放一个列表，列表中可以是id，可以是对象
    # teacher_obj.person.set([person1,person2])

    # 反向 张三老师变为除了赵老师之外的其他三个老师
    # person_obj=Person.objects.filter(name='张三').first()
    # teacher1=Teacher.objects.filter(id=2).first()
    # teacher2=Teacher.objects.filter(id=3).first()
    # teacher3=Teacher.objects.filter(id=4).first()
    # person_obj.teacher_set.set([teacher1,teacher2,teacher3])
    return HttpResponse('多对多修改成功')

def ddddelete(request):
    return HttpResponse('多对多删除成功')
