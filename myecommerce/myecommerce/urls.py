"""myecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from products.views import (
#      product_list_view, 
#      ProductListView,
#      product_detail_view,
#      ProductDetailView,
#      ProductFeaturedListView,
#      ProductFeaturedDetailView,
#      ProductDetailSlugView
# )

from carts.views import cart_home
from .views import home_page, about, contact, loginuser,registration

urlpatterns = [
    path('', home_page, name = 'home'),
    path('login/', loginuser, name = 'login'),
    path('logout/', loginuser, name = 'logout'),
    path('registration/', registration, name = 'registration'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('cart/', cart_home, name = 'cart'),
    path('products/', include("products.urls", namespace='products')),
    path('search/', include("search.urls", namespace='search')),
    path('admin/', admin.site.urls)
    # path('productlistcbv/', ProductListView.as_view()),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('productlistfbv/', product_list_view, name = 'productlistfbv'),
    # path('productdetailfbv/<int:pk>', product_detail_view, name = 'productdetailfbv'),
    # #path('productdetailcbv/<int:pk>', ProductDetailView.as_view()),
    # path('productdetailcbv/<slug:slug>', ProductDetailSlugView.as_view()),#slug
    
]



if settings.DEBUG:
    urlpatterns =  urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns =  urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
