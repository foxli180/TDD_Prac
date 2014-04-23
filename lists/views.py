from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
#home_page = None

def home_page(request):
    
    
    #items = Item.objects.all()
    
    return render(request,'home.html')
    #else:
    #    new_item_text = ''
        #return HttpResponse(request.POST['item_text'])
        
    
    #return render(request, 'home.html',{
    #            'new_item_text': new_item_text, })
    
def view_list(request,list_id):
    list_ = List.objects.get(id=list_id)
    #items = Item.objects.filter(list=list_)
    return render(request, 'list.html',{'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request,list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/' % (list_.id,))