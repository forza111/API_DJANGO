from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:choice_id>/question/', views.change_sale_eur, name='change_sale_eur'),

]