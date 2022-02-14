from django.views.generic import TemplateView



# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        header_classes = {"home": "current", "right_sidebar": "current", "dropdown": "current"}
        context['header_classes'] = header_classes
        return context