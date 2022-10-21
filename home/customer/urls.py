from django.urls import path
from home.customer import views

urlpatterns = [
    path('', views.customer, name='customer'),
    path('order/<int:id>/', views.order_detail, name='customer-order-detail'),
    path('kutish/<int:id>/', views.kutish, name='customer-kutish'),
    path('my-orders/', views.myorders, name='customer-my-orders'),
    path('delete-order/<int:id>/', views.delete_order, name='delete-order'),
    path('right-order/<int:id>/', views.right_order, name='right-order'),
]
