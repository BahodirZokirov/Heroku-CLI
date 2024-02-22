from .views import HomePageView, HowAreYou
from django.urls import path


urlpatterns = [
    path("", HomePageView.as_view(), name="HomePageView"),
    path("how", HowAreYou.as_view(), name="HowAreYou")
]