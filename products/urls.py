from  django.urls import include,path
from .views import ProductListView,ProductDetailView,CatagoryDetailView,CatagorylistView,FileDetailView,FileListView

urlpatterns = [
    path('products/',ProductListView.as_view(),name='product-list'),
    path('products/<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
    path('catagory/',CatagorylistView.as_view(),name='catagory-list'),
    path('catagory/<int:pk>',CatagoryDetailView.as_view(),name='catagory-detail'),
    path('products/<int:product_id>/files/',FileListView.as_view(),name='file-list'),
    path('products/<int:product_id>/files/<int:pk>/',FileDetailView.as_view(),name='file-detail'),
]
