from django.conf.urls import url

from . import views

app_name = 'finance'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customer/', views.CustomerView.as_view(), name='customer'),
    url(r'^taken/', views.TakenView.as_view(), name='taken'),
    url(r'^given/', views.GivenView.as_view(), name='given'),
    url(r'^provided/', views.ProvidedView.as_view(), name='provided'),
]
