from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse



# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        header_classes = {"home": "active", "about": "LAROU", "dropdown": "current"}
        context['header_classes'] = header_classes
        return context

def receive_contact_information(request: HttpRequest):
    print(request.POST['name'])
    return HttpResponse("OBRIGADO", 202)