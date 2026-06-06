from django.shortcuts import render
from tracker.models import VehicleCount


def report(request):

    records = VehicleCount.objects.all()

    return render(
        request,
        'reports/report.html',
        {
            'records':records
        }
    )