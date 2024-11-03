from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'travelers'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/>', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('<int:pk>/giving/', views.giving, name='giving'),
    path('signup/', views.signup, name='signup'),
    path("signup_check/", views.signup_check, name="signup_check"),
    path('login/', views.signin, name='login'),
    path('log_verify/', views.signin_check, name='signin_check'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='travelers:home'), name='logout'),
    path('activate_email/<uidb64>/<token>/', views.activate_email, name='activate_email'),

]