from django.conf.urls import url
from . import views

# 告诉django对于某段url应该调用哪段代码
# url ( 正则表达式，view函数，传递给视图的参数， 别名（命名空间），前缀 ),
urlpatterns = [
    url('create/', views.create, name='create'),
    url('create_dimension/', views.create_dimension, name='create_dimension'),
    url('search_all_atest/', views.search_all_atest, name='search_all_atest'),
    url('create_judge/', views.create_judge, name='create_judge'),
]  # 正则表达式表示url
