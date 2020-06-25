from django.urls import path
from polls.views import (
    IndexView,
    DetailView,
    ResultsView,
    vote,
    CreatePollView,
)


app_name = 'polls'
urlpatterns = [
    path('',IndexView, name='index'),
    path('<int:question_id>/', DetailView, name='detail'),
    path('<int:question_id>/results/', ResultsView, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('create/',CreatePollView, name="create")
]
