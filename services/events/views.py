from django.http import HttpResponse

from events.models import Event


def index(request):
    latest_events = Event.objects.order_by("created_timestamp")[:5]
    output = ", ".join([e.name for e in latest_events])
    return HttpResponse(output)


def detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    output = f"{event.name} - {event.cost}"
    return HttpResponse(output)
