from django.urls import path,include
from .views import (
    home,
    contact,
    index,
    PostList,
    PostDetail,
    AskQuestionView,
)

urlpatterns = [

    path('contact/',contact, name="contact"),

    path('', PostList.as_view(), name='article_list'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='article_detail'),

    path('ask-question/',AskQuestionView,name="AskQuestionView"),

]