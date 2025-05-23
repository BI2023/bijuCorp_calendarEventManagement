# from django.shortcuts import render
# from calendar import HTMLCalendar
# from datetime import datetime, date
# from .utils import get_status_for_date

# class StatusCalendar(HTMLCalendar):
#     def formatday(self, day, weekday):
#         if day == 0:
#             return '<td class="noday">&nbsp;</td>'

#         current_date = date.today()
#         this_date = date(self.year, self.month, day)

#         if this_date < current_date:
#             # Color historical dates based on computed status
#             status = get_status_for_date(this_date)
#             color = 'green' if status == 'success' else 'red'
#             return f'<td style="background-color:{color}; padding:10px;">{day}</td>'
#         elif this_date == current_date:
#             # Color only current day based on status
#             status = get_status_for_date(this_date)
#             color = 'green' if status == 'success' else 'red'
#             return f'<td style="background-color:{color}; font-weight:bold; padding:10px;">{day}</td>'
#         else:
#             # Future dates remain uncolored
#             return f'<td style="padding:10px;">{day}</td>'

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






from django.shortcuts import render
from calendar import HTMLCalendar
from datetime import datetime, date
from .utils import get_stored_status

class StatusCalendar(HTMLCalendar):
    def formatday(self, day, weekday):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'

        this_date = date(self.year, self.month, day)
        status = get_stored_status(this_date)

        if status == "success":
            color = "green"
        elif status == "failure":
            color = "red"
        else:
            return f'<td style="padding:10px;">{day}</td>'  # no color

        return f'<td style="background-color:{color}; padding:10px;">{day}</td>'

    def formatmonth(self, year, month, withyear=True):
        self.year, self.month = year, month
        return super().formatmonth(year, month, withyear)

def calendar_view(request):
    now = datetime.now()
    year = now.year
    month = now.month

    cal = StatusCalendar()
    html_calendar = cal.formatmonth(year, month)

    return render(request, 'calendar_app/calendar.html', {
        'calendar': html_calendar,
        'month': month,
        'year': year
    })
