from django.urls import path

from  .import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('testimonial',views.testimonial),
    path('videos',views.videos),
    path('syllabus',views.syllabus),
    path('features',views.features),
    path('subscription', views.subscription),
    # path('login/', views.login, name ='login'),
    #path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    # path('register/', views.register, name ='register'),
]



