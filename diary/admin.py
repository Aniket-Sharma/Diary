from django.contrib import admin
from .models import DailyEvent, PostPermission, PublicPageLongPost, HiddenPageLongPost, OnPermissionPageLongPost, \
    PrivatePageLongPost, PublicShortPost, HiddenShortPost, OnPermissionShortPost, PrivateShortPost, Image, HourlyUpdates

admin.site.register(DailyEvent)
admin.site.register(PostPermission)

admin.site.register(PublicPageLongPost)
admin.site.register(HiddenPageLongPost)
admin.site.register(OnPermissionPageLongPost)
admin.site.register(PrivatePageLongPost)

admin.site.register(PublicShortPost)
admin.site.register(HiddenShortPost)
admin.site.register(OnPermissionShortPost)
admin.site.register(PrivateShortPost)

admin.site.register(Image)
admin.site.register(HourlyUpdates)