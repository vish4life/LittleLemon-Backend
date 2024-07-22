from django.urls import path
from . import views
urlpatterns=[
    path('users',views.UserDetails.as_view()),
    path('users/users/me/',views.UserSepcificDetails.as_view()),
    path('category',views.CategoryView),
    path('category/<int:pk>',views.CategoryUpdate),
    path('menu-items',views.MenuItemView.as_view()),
    path('menu-items/<int:pk>',views.MenuItemUpdate.as_view(),name='menu-items-details'),
    path('groups/manager/users',views.ManagerCreation.as_view(),name='group-managers-users'),
    path('groups/manager/users/<int:pk>',views.ManagerDeletion.as_view(),name='group-managers-users-delete'),
    path('groups/delivery-crew/users',views.DCrewCreation.as_view(),name='group-delivery-crew-users'),
    path('groups/delivery-crew/users/<int:pk>',views.DCrewDeletion.as_view(),name='group-delivery-crew-users-delete'),
    path('cart/menu-items',views.CartAddFetchDelete,name='cart-items-details'),
    path('orders/',views.OrderFetchCreate.as_view(),name='orders'),
    path('orders/<int:pk>',views.OrderUpdates,name='order-updates'),
]