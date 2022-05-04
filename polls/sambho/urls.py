from django.urls import path
from .import views
from .views import index

app_name = 'sambho'
urlpatterns = [
    path('',views.modelPractice,name = 'modelPractice'),
    path('index/',views.index,name='index'),
    path('<int:question_id>/',views.details,name='details'),
    path('<int:question_id>/results/',views.results,name = 'results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
]
