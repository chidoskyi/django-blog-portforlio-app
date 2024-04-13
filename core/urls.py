from django.urls import path
from . import views
from .views import SubscribeView,NewsletterView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.service, name='service'),
    path('profile/<str:username>/', views.userProfile, name='profile'),
    path('profile/update', views.profileUpdate, name="update-profile"),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('newsletter/', NewsletterView.as_view(), name='newsletter'),
    # path('subscription-success/', SubscriptionSuccessView.as_view(), name='subscription_success'),
    # path('newletter-success/', NewsletterSuccessView.as_view(), name='newsletter_success'),
]