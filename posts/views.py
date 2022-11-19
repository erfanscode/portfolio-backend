from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostListView(ListView):
    template_name = "panel/base.html"
    def get_queryset(self):
        return Post.objects.all()
