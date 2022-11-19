from rest_framework.generics import ListAPIView
from posts.models import Post
from .serializers import PostSerializers

# Create your views here.
class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers