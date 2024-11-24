from django.conf.urls.static import static
from django.urls import path
from app_product import views
from conf import settings

urlpatterns = [
    path('', views.CategoryView.as_view(), name='categories'),

    path('product?#//<int:category_id>/', views.ProductView.as_view(), name='products'),
    path('product-detail?/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('cart/', views.cart, name='card')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
