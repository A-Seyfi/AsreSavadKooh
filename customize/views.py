from django.views.generic import TemplateView
from .models import AboutUs

class AboutUsView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        data: AboutUs = AboutUs.objects.all().order_by('id')
        context['data'] = data
        return context