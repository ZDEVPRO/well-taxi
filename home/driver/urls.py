from django.urls import path
from home.driver import views

urlpatterns = [
    path('', views.index, name='driver'),
    path('order/<int:id>/', views.order_detail, name='driver-order-detail'),
    path('myorders/', views.myorders, name='driver-myorders'),
    path('sucess/<int:id>/', views.success_order, name='driver-success-order'),

    path('ajax/getUsers', views.getOrders, name='getOrders'),
]
