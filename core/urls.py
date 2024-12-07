from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.authenticationPage, name='authentication'),  # Authentication page
    path('signup/', views.signup_view, name='signup'),          # Signup view
    path('login/', views.login_view, name='login'),              # Login view
    path('home/', views.home_view, name='home'),                  # Home page
    path('logout/', views.logout_view, name='logout'),
]
