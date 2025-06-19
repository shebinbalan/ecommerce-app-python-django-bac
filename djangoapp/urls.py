from django.urls import path
from . import views
from .views import LogoutView
from .views import CartItemListCreateView
urlpatterns = [

    path('users/register/', views.register, name='register'),
    path('users/login/', views.login, name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
  # existing product APIs...    

    # User APIs
    path('users/', views.getData),
    path('users/create', views.addUser),
    path('users/read/<str:pk>', views.getUser),
    path('users/update/<str:pk>', views.updateUser),
    path('users/delete/<str:pk>', views.deleteUser),

    # Product APIs
    path('products/', views.getProducts),
    path('products/create', views.addProduct),
    path('products/read/<str:pk>', views.getProduct),
    path('products/update/<str:pk>', views.updateProduct),
    path('products/delete/<str:pk>', views.deleteProduct),


    path('cart/', CartItemListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', views.CartItemDeleteView.as_view(), name='cart-delete'),

    # 💖 Wishlist URLs
    path('wishlist/', views.WishlistItemListCreateView.as_view(), name='wishlist-list-add'),
    path('wishlist/<int:pk>/', views.WishlistItemDeleteView.as_view(), name='wishlist-delete'),
]
