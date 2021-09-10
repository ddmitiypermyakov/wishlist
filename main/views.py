from django.shortcuts import render,get_object_or_404
from .models import WishList
# Create your views here.
from  datetime import datetime
from .forms import ProductForm
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
    wishlist = get_object_or_404(WishList, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        product=form.save()
        wishlist.product.add(product)
        wishlist.save()

    else:


        form = ProductForm()

    context={'wishlist': wishlist , 'form': form , 'is_owner_list': wishlist.owner ==request.user}
    return render(request,'wish_list.html',context)