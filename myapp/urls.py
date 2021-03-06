from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/', views.create, name='create'),
    url('create_dimension/', views.create_dimension, name='create_dimension'),
    url('add_question/', views.add_question, name='add_question'),
    url('search_all_atest/', views.search_all_atest, name='search_all_atest'),
    url('set_dimension_page/', views.set_dimension_page, name='set_dimension_page'),
    url('search_all_questions/', views.search_all_questions, name='search_all_questions'),
    url('test_list', views.test_list, name='test_list'),
    url('search_dimensions', views.search_dimensions, name='search_dimensions'),
    url('delete_question/', views.delete_question, name='delete_question'),
    url('edit_question', views.edit_question, name='edit_question'),
    url('update_question/', views.update_question, name='update_question'),
    url('delete_evaluation/', views.delete_evaluation, name='delete_evaluation'),
    url('search_atest_by', views.search_atest_by, name='search_atest_by'),
    url('update_atest/', views.update_atest, name='update_atest'),
    url('update_dimension/', views.update_dimension, name='update_dimension'),
    url('search_stat', views.search_stat, name='search_stat'),
    url('edit_judge/', views.edit_judge, name='edit_judge'),
    url('load_result', views.load_result, name='load_result'),
    url('question_chat/', views.question_chat, name='question_chat'),
    url('show_atest', views.show_atest, name='show_atest'),
    url('add_record/', views.add_record, name='add_record'),
    url('search_judge', views.search_judge, name='search_judge'),
]  
