from django.urls import path
from .views import HomePageView, AboutPageView, SomsaPageView, MontiPageView


urlpatterns =[
    path('',HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('somsa/', SomsaPageView.as_view(), name='somsa'),
    path('monti', MontiPageView.as_view(),name='monti'),

]