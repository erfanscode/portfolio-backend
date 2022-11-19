from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail

urlpatterns = [
    path("", PostList.as_view(), name="api_list"),
    path("<int:pk>", PostDetail.as_view(), name="api_detail"),
    path("user/", UserList.as_view(), name="api_userlist"),
    path("user/<int:pk>", UserDetail.as_view(), name="api_userdetail"),
]