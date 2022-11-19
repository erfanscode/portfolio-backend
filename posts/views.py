from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    template_name = "panel/base.html"
    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(DetailView):
    template_name = "panel/base.html"
    def get_object(self):
        return get_object_or_404(Post.objects.all(), pk=self.kwargs.get("pk"))
