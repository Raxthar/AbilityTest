from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/', views.create, name='create'),
    url('create_dimension/', views.create_dimension, name='create_dimension'),
    url('add_question/', views.add_question, name='add_question'),
    url('search_all_atest/', views.search_all_atest, name='search_all_atest'),
    url('create_judge/', views.create_judge, name='create_judge'),
    url('set_dimension_page/', views.set_dimension_page, name='set_dimension_page'),
    url('set_deadline/', views.set_deadline, name='set_deadline'),
    url('search_all_questions/', views.search_all_questions, name='search_all_questions'),
    url('test_list', views.test_list, name='test_list'),
    url('search_dimensions', views.search_dimensions, name='search_dimensions'),

]  
