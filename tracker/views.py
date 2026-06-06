from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from events.models import Event
from .models import VehicleCount


@login_required
def dashboard(request):

    event = Event.objects.filter(
        active=True
    ).first()

    buses = VehicleCount.objects.filter(
        event=event,
        user=request.user,
        vehicle_type='BUS'
    ).first()

    costers = VehicleCount.objects.filter(
        event=event,
        user=request.user,
        vehicle_type='COSTER'
    ).first()

    taxis = VehicleCount.objects.filter(
        event=event,
        user=request.user,
        vehicle_type='TAXI'
    ).first()

    return render(
        request,
        'tracker/dashboard.html',
        {
            'event':event,
            'buses':buses,
            'costers':costers,
            'taxis':taxis
        }
    )
from django.shortcuts import redirect

def add_bus(request):

    event = Event.objects.get(active=True)

    obj, created = VehicleCount.objects.get_or_create(
        event=event,
        user=request.user,
        vehicle_type='BUS'
    )

    obj.count += 1

    obj.save()

    return redirect('dashboard')
def subtract_bus(request):

    event = Event.objects.get(
        active=True
    )

    obj = VehicleCount.objects.get(
        event=event,
        user=request.user,
        vehicle_type='BUS'
    )

    if obj.count > 0:
        obj.count -= 1
        obj.save()

    return redirect('dashboard')

def add_coster(request):

    event = Event.objects.get(active=True)

    obj, created = VehicleCount.objects.get_or_create(
        event=event,
        user=request.user,
        vehicle_type='COSTER'
    )

    obj.count += 1

    obj.save()

    return redirect('dashboard')

def subtract_coster(request):

    event = Event.objects.get(
        active=True
    )

    obj = VehicleCount.objects.get(
        event=event,
        user=request.user,
        vehicle_type='COSTER'
    )

    if obj.count > 0:
        obj.count -= 1
        obj.save()

    return redirect('dashboard')

def add_taxi(request):

    event = Event.objects.get(active=True)

    obj, created = VehicleCount.objects.get_or_create(
        event=event,
        user=request.user,
        vehicle_type='TAXI'
    )

    obj.count += 1

    obj.save()

    return redirect('dashboard')

def subtract_taxi(request):

    event = Event.objects.get(
        active=True
    )

    obj = VehicleCount.objects.get(
        event=event,
        user=request.user,
        vehicle_type='TAXI'
    )

    if obj.count > 0:
        obj.count -= 1
        obj.save()

    return redirect('dashboard')