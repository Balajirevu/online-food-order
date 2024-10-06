from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import *
from .models import *
from django.db.models import Q
# Create your views here.

#user registration
def user_register(request):
    if request.method=='POST':
        user=New_user.objects.filter(username=request.POST['username'])
        if user.exists():
            messages.info(request,'user already exists')
            return redirect('/register/')
        form=User_register_form(request.POST)
        if form.is_valid():
                form.save()
                return redirect('/login/')
    form=User_register_form()
    return render(request,'register.html',{'form':form})

#user login
def user_login(request):
    if request.method=='POST':
        form=User_login_form(request.POST)
        if form.is_valid():
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            if user:
                login(request,user)
                return redirect('/home/')
            else:
                messages.info(request,'username or password wrong')
                return redirect('/login/')
    return render(request,'login.html')

# homepage
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

#user logout
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('/login/')
    
#restaurents 
@login_required(login_url='login')
def restaurent_data(request):
    data=Restaurent.objects.all()
    return render(request,'hotels.html',{'data':data})

#menu"s
@login_required(login_url='login')
def menu(request,id):
    data=Menu.objects.filter(restaurent_id=id)
    print(data)
    return render(request,'menu.html',{'data':data})
#userinfo
@login_required(login_url='login')
def userinfo(request):
    if request.user:
        user=New_user.objects.filter(id=request.user.id)
        print(user)
    return render(request,'profile.html',{'data':user})

#view cart items
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.menu.item_price * item.quantity for item in cart_items)
    return render(request, 'cart1.html', {'cart_items': cart_items, 'total_price': total_price})

#addtocart items
def add_to_cart(request,id):
    menu = Menu.objects.get(menu_id=id)
    cart_item, created = CartItem.objects.get_or_create(menu=menu, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('/restaurents/')
#buy now items
def buy_now(request,id):
    menu = Menu.objects.get(menu_id=id)
    cart_item, created = CartItem.objects.get_or_create(menu=menu, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('/viewcart/')

#remove items
def remove_from_cart(request,id):
    cart_item = CartItem.objects.filter(menu_id=id)
    cart_item.delete()
    return redirect('tomato:viewcart')
 
#user orders 
def orders(request,id):
    data=CartItem.objects.filter(menu_id=id)
    total_price = sum(item.menu.item_price * item.quantity for item in data)
    return render(request,'order.html',{'data':data ,'total_price': total_price})
#hotels search
def search_view(request):
    query=request.GET.get('q')
    obj=Restaurent.objects.filter(restaurent_name__icontains=query)
    return render(request,'data.html',{'filter':obj})
#items search
def item_search_view(request):
     query1=request.GET.get('items')
     obj1=Menu.objects.filter(item_name__icontains=query1)
     return render(request,'itemsfilter.html',{'filter1':obj1})
                                               
#success 
def success(request):
    return render(request,'success.html')

