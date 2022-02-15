import http
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse

from apps.core.models.contact import Contact



# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        header_classes = {"home": "active", "about": "LAROU", "dropdown": "current"}
        context['header_classes'] = header_classes
        return context

def receive_contact_information(request: HttpRequest):
    message = {"message": request.POST['message'], "email": request.POST["email"], "name": request.POST["name"], "subject": request.POST["subject"]}
    Contact.objects.create(**message)
    response = HttpResponse("OK")
    response.status_code = http.HTTPStatus.OK
    return response
