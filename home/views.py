from django.views.generic import ListView
from django.utils import timezone

from .models import Post


class HomeView(ListView):

    template_name = 'home.html'
    model = Post
    paginate_by = 5
    paginate_orphans = 3
    ordering = 'created'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context['now'] = now
        return context
