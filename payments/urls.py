from django.urls import path

from payments import views


urlpatterns = [
    path('getways/', views.as_view()),
    path('pay/', views.PaymentView.as_view())
]