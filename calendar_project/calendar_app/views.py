from django.shortcuts import render

# Create your views here.
# calendar_app/views.py

from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
import calendar
from calendar import HTMLCalendar
from datetime import datetime, date

def calendar_view(request):
    now = datetime.now()
    year = now.year
    month = now.month
    cal = HTMLCalendar().formatmonth(year, month)

    events = Event.objects.filter(date__year=year, date__month=month)

    return render(request, 'calendar_app/calendar.html', {
        'calendar': cal,
        'events': events,
        'month': month,
        'year': year
    })

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = EventForm()
    return render(request, 'calendar_app/event_form.html', {'form': form})

def events_by_date(request, year, month, day):
    selected_date = date(year, month, day)
    events = Event.objects.filter(date=selected_date)
    return render(request, 'calendar_app/events_by_date.html', {
        'events': events,
        'date': selected_date
    })
