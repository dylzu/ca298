"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DylansShop import views, forms
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .forms import *
from .forms import UserSignupForm, UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('products/<int:prodid>', views.product_individual, name="individual_product"),
    path('register/', views.UserSignupView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
    path('logout/', views.logout_user, name="logout"),
    path('addbasket/<int:prodid>', views.add_to_basket, name="add_basket"),
    path('basket/', views.show_basket, name='show_basket'),
    path('removeitem/<int:sbi>', views.remove_item, name="removeitem"),
    path('order/', views.order, name="order"),
    path('orderhistory/', views.previous_orders, name="order_history"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
