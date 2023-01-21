from django.urls import path,include

from . import views




urlpatterns = [
    path('categories/', views.get_category),
    path('createcategory/', views.create_category),

    path('drones/', views.get_drones),
    path('drone/<slug:slug>/', views.get_drone),
    path('createdrone/', views.create_drone),
    path('updatedrone/<slug:slug>/', views.update_drone),
    path('deletedrone/<slug:slug>/', views.delete_drone),

    path('orders/', views.get_orders),
    path('ordersuser/', views.get_order_user),
    path('order/<int:id>/', views.get_order),
    path('createorder/', views.create_order),
    path('postorderstatus/<int:id>/', views.PostStatusAPIView.as_view()),

    path('feature/<slug:slug>/', views.get_feature),
    path('features/', views.get_features),
    path('createfeature/', views.create_feature),

    path('search/', views.DroneSearchListView.as_view()),

    ]