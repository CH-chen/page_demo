from django.shortcuts import render,HttpResponse

# Create your views here.


from .models import *
def index(request):
    '''
    book_list=[]
    for  i in range(500):
        book_obj=Book(title="book_%s"%i,price=i*i)
        book_list.append(book_obj)
    Book.objects.bulk_create(book_list)

    :param request:
    :return:
    '''

    current_page=request.GET.get("page",1)

    all_count=Book.objects.all().count()
    base_url=request.path  # /index/
    from app01.utils.page import  Pagination


    pagination=Pagination(all_count,int(current_page),base_url,request.GET,per_page=10, max_show=11)


    print(pagination.start)
    print(pagination.end)

    book_list =Book.objects.all()[pagination.start:pagination.end]

    from django.http.request import QueryDict
    # dic = QueryDict(mutable=True)
    # dic["info"] = 123


    # print(type(request.GET))
    # request.GET["info"]=123


    import copy
    params=copy.deepcopy(request.GET)
    params["xxx"]=123







    return render(request,"index.html",locals())