from django.urls import include, path

from Residents import views

urlpatterns = [
    path('', views.residents_page, name='index'),
    path('CheckCost/', views.CheckCost, name='CheckCost'),
    # path('logout/', views.my_logout, name='logout'),
]
