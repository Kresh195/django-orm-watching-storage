from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


# def get_visit_duration(visit):
#     current_time = timezone.localtime().replace(microsecond=0)
#     visit_duration = (current_time - visit.entered_at)
#     return visit_duration


def storage_information_view(request):
    # Программируем здесь
    active_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = list()
    for visit in active_visits:
        visit_duration = visit.get_duration()
        visitor = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': visit_duration,
            'is_strange': visit.is_visit_long()
        }
        non_closed_visits.append(visitor)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
