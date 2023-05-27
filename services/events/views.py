from django.views import generic

from events.forms import RegisterForm
from events.models import Event


class IndexView(generic.ListView):
    template_name = "events/index.html"
    context_object_name = "latest_events"

    def get_queryset(self):
        return Event.objects.order_by("-start_date")[:5]


class DetailView(generic.DetailView):
    model = Event
    template_name = "events/event.html"


class RegisterView(generic.FormView):
    template_name = "events/register.html"
    form_class = RegisterForm
    success_url = "/cart/"
    
    def form_valid(self, form):
        form.add_to_cart()
        return super(RegisterView, self).form_valid(form)