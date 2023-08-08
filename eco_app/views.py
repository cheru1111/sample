from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

def home(request):
    data=CategoryModel.objects.all()
    return render(request,"home.html",{'data':data})




def regpage(request):
    category=CategoryModel.objects.all()
    context={'category':category}
    return render(request,"signup.html",context)


def customer_reg(request):
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        email=request.POST['eid']
        usname=request.POST['uname']
        num=request.POST['ph']
        pswd=request.POST['pass']
        cpswd=request.POST['cpass']

        if pswd==cpswd:
            if User.objects.filter(username=usname).exists():
                return redirect('customer_reg')
            elif User.objects.filter(email=email).exists():
                return redirect('customer_reg')
            else:
                user=User.objects.create_user(first_name=fn,last_name=ln,email=email,username=usname,password=pswd)
                user.save()
                data=User.objects.get(id=user.id)
                teacher=CustomerModel(number=num,user=data)
                teacher.save()
                print("success")
                return redirect('login')

        else:
            print("password error")
            return redirect('customer_reg')

    else:
            print(" error")
            return redirect('customer_reg')
    
def loginpage(request):
    return render(request,'login.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)

            if request.user.is_staff==1:
                print("admin")
                return redirect('adminpage')
            else:
                print("thome")
                return redirect('chomepage')
        else:
            messages.info(request,"Invalid username or password.Try Again.")
            print("try again")
            return redirect('loginpage')
    else:
        print("try again")    
        return redirect('loginpage')  

def categorypage(request):
    return render(request,"category.html")

def addcategory(request):
    if request.method == 'POST':
        category=request.POST['categoryname']
        
        data = CategoryModel(Category_Name=category)
        data.save()
        return redirect('adminpage')

def adminpage(request):
        return render(request,"admin.html")

def ProductPage(request):
    categories=CategoryModel.objects.all()
    context={'categories':categories}
    return render(request,'product.html',context)


def AddProduct(request):
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        description=request.POST['description']
        quantity=request.POST['quantity']
        image=request.FILES.get('file')
        # joindate=request.POST['joindate']
        select=request.POST['select']
        category=CategoryModel.objects.get(id=select)
        data = product(name=name,price=price,description=description,quantity=quantity,image=image,category=category)
        data.save()
        return redirect('adminpage')


def ProductDetails(request):
    product_detail = product.objects.all()
    return render(request,'productdetails.html',{'product':product_detail})

def CustomerDetails(request):
    customer_detail = CustomerModel.objects.all()
    return render(request,'customerdetails.html',{'customer':customer_detail})

def addcart(request,did):
    data=product.objects.get(id=did)
    current_user=request.user
    uid=current_user.id
    
    user=CustomerModel.objects.get(user=uid)

    cart=CartModel(Customer=user,Product=data)
    cart.save()
    return redirect('chomepage')


def cart(request,did):
    data=CartModel.objects.filter(Customer=did)
    ca=CategoryModel.objects.all()
    
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=CustomerModel.objects.get(user=uid)
    return render(request,"cart.html",{'data':data,'user':user,'ca':ca})

def remove_cart(request,did):
    cart=CartModel.objects.get(id=did)
    cart.delete()
    print("remove cart")
    return redirect('chomepage')

def chomepage(request):
    cate=CategoryModel.objects.all()
    current_user=request.user
    uid=current_user.id

    user=CustomerModel.objects.get(user=uid)
    return render(request,'customerhome.html',{'category':cate,'user':user})

def men(request):
    return render(request,'men.html')

def customerpage(request):  
    data=CustomerModel.objects.all()
   
    return render(request,"customer.html",{'data':data}) 

def delete_product(request,pk):
    ptd=product.objects.get(id=pk)
    ptd.delete()
    return redirect('ProductDetails')

def delete_customer(request,pk):
    customer=CustomerModel.objects.get(id=pk)
    customer.delete()
    return redirect('CustomerDetails')

def editproductpage(request,did):
    ptd=product.objects.get(id=did)    
    return render(request,'editproduct.html',{'product':ptd})

def edit_products(request,did):
    if request.method=='POST':
        
        ptd=product.objects.get(id=did)
        old=ptd.image
        new=request.FILES.get('file')
        if old!=None and new==None:
            ptd.image=old
        else:
            ptd.image=new
        
        ptd.name=request.POST.get('prtname')
        ptd.description=request.POST.get('prtdispription')
        ptd.price=request.POST.get('prtprice')

        sselete=request.POST['select']
        category=CategoryModel.objects.get(id=sselete)
        ptd.category=category
        ptd.save()
        

        print("update success")
        return redirect('ProductDetails')
    print("else")
    return request(request,"editproduct.html")

def editcustomerpage(request,did):
    customer=CustomerModel.objects.get(id=did)    
    return render(request,'editcustomer.html',{'customer':customer})

def edit_customerdetails(request,did):
    if request.method=='POST':
        customer=CustomerModel.objects.get(id=did)
        
        customer.user.first_name=request.POST.get('fname')
        customer.user.last_name=request.POST.get('lname')
        customer.user.email=request.POST.get('email')
        #customer.number=request.POST.get('ph')
        #customer.user.username=request.POST.get('uname')
        customer.save()
        customer.user.save()

        print("update success")
        return redirect('CustomerDetails',)
    print("else")
    return request(request,"editcustomer.html")
    
def showproductpage(request,did):  
    data=product.objects.filter(category=did)
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=CustomerModel.objects.get(user=uid)
    return render(request,"showproduct.html",{'data':data,'user':user})   

def orderproduct(request,did):
    data=product.objects.get(id=did)
    ca=CategoryModel.objects.all()
    current_user=request.user
    uid=current_user.id
    user=CustomerModel.objects.get(user=uid)
    return render(request,"order.html",{'data':data,'ca':ca,'user':user})

def buynow(request,did):
    data=product.objects.get(id=did)
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=CustomerModel.objects.get(user=uid)
    

    ptd=OrderModel(Category=data.category,Customer=user,Product=data)
    ptd.save()
    print("shoping complited")
    return redirect('success')

def success(request):
    current_user=request.user
    uid=current_user.id
    print(uid)
    user=CustomerModel.objects.get(user=uid)
    return render(request,"confirmed.html",{'user':user})

def logout(request):
	auth.logout(request)
	return redirect('home')
