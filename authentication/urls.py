from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# from .views import 
from . import views

urlpatterns = [
    path('register/', views.register, name="sign-up"),
    path('signout', views.signout, name='logout'),
    # path('login', views.login, name='login'),
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    # path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
