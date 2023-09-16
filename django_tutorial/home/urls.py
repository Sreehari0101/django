from django.urls import path,include 
from.import views
urlpatterns = [
path('',views.index,name='home'),
path('register',views.register,name="register"),
path('login',views.login_page,name="login"),
path('user',views.user,name='user'),
path('apply',views.apply,name='apply'),
path('status',views.status,name='status'),
path('department',views.departmentname,name='department'),
]