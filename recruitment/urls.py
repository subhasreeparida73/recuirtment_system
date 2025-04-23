from django.urls import path
from recruitment.views import *

urlpatterns = [
    path('add_job/',add_job, name='add_job'),
    path('add_candidate/',add_candidate, name='add_candidate'),
    path('candidate_list',candidate_list,name='candidate_list'),

]