from django.urls import path
from . import views
from . views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('candidates/',views.candidate_list,name='candidate_list'),
    path('vote/<int:candidate_id>/', views.vote, name='vote'),

    
]
