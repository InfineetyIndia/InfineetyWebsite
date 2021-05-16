from django.urls import path

from  .import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name ='login'),
    #path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', views.register, name ='register'),
]