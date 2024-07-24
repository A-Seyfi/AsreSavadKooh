from django.views.generic import ListView
from .models import Gallery

class GalleryListView(ListView):
    template_name = 'news/gallery.html'
    model = Gallery
    context_object_name = 'images'
    ordering = ['created_at']

    def get_queryset(self):
        return Gallery.objects.all().order_by('-id')
