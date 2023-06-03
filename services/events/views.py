from django.shortcuts import render
from django.views import generic

from events.forms import RegisterForm
from events.models import Event


class IndexView(generic.ListView):
    template_name = "events/index.html"
    context_object_name = "latest_events"

    def get_queryset(self):
        return Event.objects.order_by("start_date")[:5]


class DetailView(generic.DetailView):
    model = Event
    template_name = "events/event.html"


class RegisterView(generic.FormView):
    template_name = "events/register.html"
    form_class = RegisterForm
    success_url = "/cart/"

    def form_valid(self, form):
        return super(RegisterView, self).form_valid(form)


def event_times_view(request):
    event_id = request.GET.get("event")
    event = Event.objects.get(id=event_id)
    return render(request, "events/event_time_dropdown_list_options.html", {"times": event.times.all()})
