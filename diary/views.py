from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from datetime import date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
import calendar
from django.db.models import Count
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe

from .models import DailyEvent, PublicPageLongPost, HiddenPageLongPost, OnPermissionPageLongPost, PrivatePageLongPost, \
    PublicShortPost, HiddenShortPost, OnPermissionShortPost, PrivateShortPost, Image

from rest_framework import serializers, viewsets
from .utils import EventCalendar
#
#
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DailyEvent
#         fields = '__all__'
#
#
# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = DailyEvent.objects.all()
#     serializer_class = ArticleSerializer


class DailyEventView(TemplateView):

    template_name = 'diary/calendar.html'

    def get(self, request):

        dates = DailyEvent.objects.all()
        after_day = request.GET.get('day__gte', None)
        if not after_day:
            d = date.today()
        else:
            try:
                split_after_day = after_day.split('-')
                d = date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                d = date.today()

        previous_month = date(year=d.year, month=d.month, day=1)  # find first day of current month
        previous_month = previous_month - timedelta(days=1)  # backs up a single day
        previous_month = date(year=previous_month.year, month=previous_month.month, day=1)

        last_day = calendar.monthrange(d.year, d.month)

        next_month = date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
        next_month = next_month + timedelta(days=1)  # forward a single day
        next_month = date(year=next_month.year, month=next_month.month, day=1)  # find first day of next month

        previous_month = reverse('calendar') + '?day__gte=' + str(previous_month)
        next_month = reverse('calendar') + '?day__gte=' + str(next_month)
        current_month = reverse('calendar') + '?day__gte'+str(d)

        cal = EventCalendar()
        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace('<td ', '<td class ="Row" ')
        args = {'dates': dates, 'calendar': mark_safe(html_calendar), 'previous_month': previous_month,
                'next_month': next_month, 'current_month': current_month}

        return render(request, self.template_name, args)


class SingleDayView(TemplateView):
    template_name = 'diary/day.html'

    def get(self, request, date):

        public_long_posts = PublicPageLongPost.objects.filter(date_id=date)
        hidden_long_posts = HiddenPageLongPost.objects.filter(date_id=date)
        on_permission_long_posts = OnPermissionPageLongPost.objects.filter(date_id=date)
        private_long_posts = PrivatePageLongPost.objects.filter(date_id=date)

        public_short_posts = PublicShortPost.objects.filter(date_id=date)
        hidden_short_posts = HiddenShortPost.objects.filter(date_id=date)
        on_permission_short_posts = OnPermissionShortPost.objects.filter(date_id=date)
        private_short_posts = PrivateShortPost.objects.filter(date_id=date)

        images = Image.objects.filter(date_id=date)

        args = {'public_long_posts': public_long_posts, 'hidden_long_posts': hidden_long_posts,
                'on_permission_long_posts': on_permission_long_posts, 'private_long_posts': private_long_posts,
                'public_short_posts': public_short_posts, 'hidden_short_posts': hidden_short_posts,
                'on_permission_short_posts': on_permission_short_posts, 'private_short_posts': private_short_posts,
                'images': images}

        return render(request, self.template_name, args)

