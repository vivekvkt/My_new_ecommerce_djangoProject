
from django.urls import path
from .views import (
     #product_list_view, 
     ProductListView,
     ProductDetailSlugView,
     #product_detail_view,
     #ProductDetailView,
     #ProductFeaturedListView,
     #ProductFeaturedDetailView,
     
)

app_name = "products"

urlpatterns = [
   
    path('', ProductListView.as_view(), name="list"),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('productlistfbv/', product_list_view, name = 'productlistfbv'),
    # path('productdetailfbv/<int:pk>', product_detail_view, name = 'productdetailfbv'),
    #path('productdetailcbv/<int:pk>', ProductDetailView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name="detail"),#slug
   
]


