# from django.shortcuts import render
# from calendar import HTMLCalendar
# from datetime import datetime, date
# from .utils import get_stored_status

# class StatusCalendar(HTMLCalendar):
#     def formatday(self, day, weekday):
#         if day == 0:
#             return '<td class="noday">&nbsp;</td>'

#         this_date = date(self.year, self.month, day)
#         status = get_stored_status(this_date)

#         if status == "success":
#             color = "green"
#         elif status == "failure":
#             color = "red"
#         else:
#             return f'<td style="padding:10px;">{day}</td>'  # no color

#         return f'<td style="background-color:{color}; padding:10px;">{day}</td>'

#     def formatmonth(self, year, month, withyear=True):
#         self.year, self.month = year, month
#         return super().formatmonth(year, month, withyear)

# def calendar_view(request):
#     now = datetime.now()
#     year = now.year
#     month = now.month

#     cal = StatusCalendar()
#     html_calendar = cal.formatmonth(year, month)

#     return render(request, 'calendar_app/calendar.html', {
#         'calendar': html_calendar,
#         'month': month,
#         'year': year
#     })




# =============================================================



# from django.shortcuts import render
# from calendar import HTMLCalendar
# from datetime import datetime, date
# from .utils import load_status_data

# class StatusCalendar(HTMLCalendar):
#     def __init__(self, data):
#         super().__init__()
#         self.data = data

#     def formatday(self, day, weekday):
#         if day == 0:
#             return '<td class="noday">&nbsp;</td>'

#         this_date = date(self.year, self.month, day).isoformat()
#         status_data = self.data.get(this_date, {})
#         color = "green" if status_data else "white"

#         return f'<td style="background-color:{color}; padding:10px;" class="calendar-cell" data-date="{this_date}">{day}</td>'

#     def formatmonth(self, year, month, withyear=True):
#         self.year, self.month = year, month
#         return super().formatmonth(year, month, withyear)

# def calendar_view(request):
#     now = datetime.now()
#     year = now.year
#     month = now.month
#     data = load_status_data()

#     cal = StatusCalendar(data)
#     html_calendar = cal.formatmonth(year, month)

#     return render(request, 'calendar_app/calendar.html', {
#         'calendar': html_calendar,
#         'status_data': data,
#         'month': month,
#         'year': year
#     })




# =================================================================================



from django.shortcuts import render
from calendar import HTMLCalendar
from datetime import datetime, date
from .utils import load_status_data

class StatusCalendar(HTMLCalendar):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def formatday(self, day, weekday):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'

        this_date = date(self.year, self.month, day).isoformat()
        status_info = self.data.get(this_date, {})
        status = status_info.get("status", "").lower()

        # Determine background color
        if status == "success":
            color = "lightgreen"
        elif status == "failure":
            color = "lightcoral"
        else:
            color = "white"

        return f'<td style="background-color:{color}; padding:10px;" class="calendar-cell" data-date="{this_date}">{day}</td>'

    def formatmonth(self, year, month, withyear=True):
        self.year, self.month = year, month
        return super().formatmonth(year, month, withyear)

def calendar_view(request):
    now = datetime.now()
    year = now.year
    month = now.month
    data = load_status_data()

    cal = StatusCalendar(data)
    html_calendar = cal.formatmonth(year, month)

    return render(request, 'calendar_app/calendar.html', {
        'calendar': html_calendar,
        'status_data': data,
        'month': month,
        'year': year
    })