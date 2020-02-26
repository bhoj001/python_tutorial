from django.urls import path,include
from .views import (
    home,
    contact,
    index,
    PostList,
    PostDetail,
)

urlpatterns = [
    # path('',home,name="home"),
    
    path('contact/',contact, name="contact"),

    # path('index/',index, name="index"),

    path('', PostList.as_view(), name='article_list'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='article_detail'),
]