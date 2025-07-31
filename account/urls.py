from django.urls import path,include
from account import views
urlpatterns = [
    path('users/', views.user_list)
]
