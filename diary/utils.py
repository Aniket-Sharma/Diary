from calendar import HTMLCalendar
from datetime import datetime, date, time
import datetime
from .models import DailyEvent, PublicPageLongPost, HiddenPageLongPost, OnPermissionPageLongPost, PrivatePageLongPost, \
    PublicShortPost, HiddenShortPost, OnPermissionShortPost, PrivateShortPost, Image
from django.db.models import Count


class EventCalendar(HTMLCalendar):
    def __init__(self):
        super(EventCalendar, self).__init__()

    def formatday(self, day, weekday, themonth, theyear):
        pub_posts, priv_posts, img_count, temp_key = 0, 0, 0, 0
        if day != 0:
            rel_date = str(theyear) + '-' + str(themonth) + '-' + str(day)
            events = DailyEvent.objects.annotate(Count('publicpagelongpost'), Count('hiddenpagelongpost'),
                                                 Count('onpermissionpagelongpost'), Count('privatepagelongpost'),
                                                 Count('publicshortpost'), Count('hiddenshortpost'),
                                                 Count('onpermissionshortpost'), Count('privateshortpost'),
                                                 Count('image')).filter(date=rel_date)

            for event in events:
                pub_posts += event.publicpagelongpost__count + event.hiddenpagelongpost__count + \
                            event.hiddenshortpost__count + event.publicshortpost__count
                priv_posts += event.privatepagelongpost__count + event.onpermissionpagelongpost__count+event.\
                    privateshortpost__count + event.onpermissionshortpost__count
                img_count += event.image__count

                temp_key = event.pk

        now = date.today()

        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        elif day == now.day and themonth == now.month and theyear == now.year:
            return '<td class="%s today">Today <br> %d Public Posts <br> %d Private Posts <br> %d Images </td>' \
                   % (self.cssclasses[weekday], pub_posts, priv_posts, img_count)
        elif (day > now.day and themonth >= now.month and theyear >= now.year) or (themonth > now.month and theyear >=
                                                                                   now.year) or (theyear > now.year):
            return '<td class="%s future-day">%d-yet to come</td>' % (self.cssclasses[weekday], day)
        else:
            if temp_key:
                return '''<td class="%s have-events"><a href='/calendar/day%d'> %d Public Posts <br> %d Private Posts <br> %d 
                Images </a></td>''' % (self.cssclasses[weekday], temp_key, pub_posts, priv_posts, img_count)
            else:
                return '''<td class="%s no-events">There\'s nothing here</td>''' % (self.cssclasses[weekday])

    def formatweek(self, theweek, themonth, theyear):
        s = ''.join(self.formatday(d, wd, themonth, theyear) for (d, wd) in theweek)
        return '<tr class="week">%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        v = []
        a = v.append
        a('<table border="1" cellpadding="2" cellspacing="2" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, themonth, theyear))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

