from django.urls import path
from Application import views
#use this app_name you can access particular this app

app_name = 'basic_app'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('special/', views.special, name='special')
]
