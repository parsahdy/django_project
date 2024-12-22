from django.urls import path

from subscriptions import views


urlpatterns = [
    path('packages/', views.PackageView.as_view()),
    path('subscription/', views.SubscriptinView.as_view())
]