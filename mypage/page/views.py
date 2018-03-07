from django.http import HttpResponse, Http404
from page.models import Category, Good

def index(request, cat_id):
    if cat_id == None:
      cat = Category.objects.first()
    else:
        try:
            cat = Category.objects.get(pk = cat_id)
        except Category.DoesNotExist:
            raise Http404
    goods = Good.objects.filter(category = cat).order_by("name")
    s = "Категория: " + cat.name + "<br><br>"
    for good in goods:
        s = s + "(" + str(good.pk) + ")" + good.name + "<br>"
    return HttpResponse(s)

def good(request, good_id):
    try:
        good = Good.objects.get(pk = good_id)
    except Good.DoesNotExist:
        raise Http404
    s = good.name + "<br><br>" + good.category.name + "<br><br>" + good.description
    if not good.in_stock:
        s = s + "<br><br>" + "Нет в наличии!"
    return HttpResponse(s)
    
    
def cattu(request):
    cattu = Category.objects.all().distinct()
    i = ["Категории: "]
    for cattup in cattu:
        s =  cattup.name + " " 
        i +=s
    return HttpResponse(i)
    
    
        
