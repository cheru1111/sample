from eco_app import views
from django.urls import path
from django.urls import include, path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('men/',views.men,name='men'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('login/',views.login,name="login"),
    path('regpage/',views.regpage,name='regpage'),
    path('customer_reg/',views.customer_reg,name="customer_reg"),
    
    path('addcart/<int:did>',views.addcart,name="addcart"),
    path('cart/<int:did>',views.cart,name="cart"),
    path('remove_cart/<int:did>',views.remove_cart,name="remove_cart"),

    path('ProductPage',views.ProductPage,name='ProductPage'),
    path('AddProduct',views.AddProduct,name='AddProduct'),
    path('categorypage',views.categorypage,name='categorypage'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('ProductDetails',views.ProductDetails,name='ProductDetails'),
    
    path('CustomerDetails',views.CustomerDetails,name='CustomerDetails'),
    
    path('delete_product/<int:pk>',views.delete_product,name='delete_product'),
    path('delete_customer/<int:pk>',views.delete_customer,name='delete_customer'),
    path('editcustomerpage/<int:did>',views.editcustomerpage,name="editcustomerpage"),
    path('edit_customerdetails/<int:did>',views.edit_customerdetails,name="edit_customerdetails"),
    path('editproductpage/<int:did>',views.editproductpage,name="editproductpage"),
    path('edit_products/<int:did>',views.edit_products,name="edit_products"),
    path('showproductpage/<int:did>',views.showproductpage,name="showproductpage"),
    path('orderproduct/<int:did>',views.orderproduct,name="orderproduct"),
    path('buynow/<int:did>',views.buynow,name="buynow"),
    path('success',views.success,name="success"),
    path('logout',views.logout,name='logout'),
    path('chomepage',views.chomepage,name='chomepage'),
    
    
]