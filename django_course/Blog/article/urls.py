from django.urls import path,include
from .views import (
    home,
    article,
    index,
    PostList,
    PostDetail,
)

urlpatterns = [
    path('',home,name="home"),
    path('article/',article, name="article"),
    path('index/',index, name="index"),



    path('list/', PostList.as_view(), name='article_list'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='article_detail'),
]