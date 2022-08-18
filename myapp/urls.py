from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('steps',views.steps,name='steps'),
    path('query',views.query,name='query'),
    path('basicDetails',views.basicDetails,name='basicDetails'),
    path('selectTest',views.selectTest,name='selectTest'),
    path('psychomotor',views.psychomotor,name='psychomotor'),
    path('psychomotor1',views.psychomotor1,name='psychomotor1'),
    path('psychomotor2',views.psychomotor2,name='psychomotor2'),
    path('cognitive',views.cognitive,name='cognitive'),
    path('cognitive1',views.cognitive1,name='cognitive1'),
    path('result',views.result,name='result'),
    path('cognitive_result',views.cognitive_result,name='cognitive_result'),
    path('reset',views.reset,name='reset'),
]