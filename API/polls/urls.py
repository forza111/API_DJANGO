from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:polls_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:polls_id>/info/<int:question_id>', views.detail_question, name='detail_question'),
    path('<int:polls_id>/info/<int:question_id>/vote/', views.vote, name='vote'),
]