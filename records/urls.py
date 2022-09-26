from django.urls import path

from . import views

app_name = 'records'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:record_id>/', views.detail, name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]