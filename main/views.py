from django.shortcuts import render,get_object_or_404
from .models import WishList
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    context= {'title': 'Wishlist | about project'}
    return render(request,'about.html',context)

def base(request):
    return render(request,'base.html')

def list_page(request,pk):
    """
    FBV view основаны на функциях
    :param request:
    :return:
    """

    wishlist=get_object_or_404(WishList, pk=pk)
    context={'wishlist': 'wishlist'}
    return render(request,'wish_list.html',context)