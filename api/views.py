from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from accounts.models import CustomUser
from posts.models import Post
from .serializers import PostSerializers, UserSerializers

# Create your views here.
class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class UserList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers