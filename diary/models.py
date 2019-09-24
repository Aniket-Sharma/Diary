from django.db import models
from datetime import datetime, timedelta
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import reverse


class DailyEvent(models.Model):
    date = models.DateField(editable=True, default=datetime.now, unique=True)
    bg_img = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(str(self.date)+': '+str(self.title))


class PostPermission(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    message = models.CharField(max_length=200)

    permission_asked = models.BooleanField(default=False)
    permission_granted = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=10)
    comment = models.CharField(max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name


class PublicPageLongPost(models.Model):
    date_id = models.ForeignKey(DailyEvent, unique=False, on_delete=models.CASCADE)

    comment = GenericRelation(Comment)

    CATEGORIES = (
        ('project_update', 'Project Update'),
        ('technical', 'Technical'),
        ('dream', 'Dream'),
        ('political', 'Political'),
        ('plan', 'Plan'),
        ('goal', 'Goal'),
        ('super-optimistic-dream', 'Super Optimistic Dream'),
        ('story', 'Story'),
        ('real-story', 'Real Story'),
        ('bizarre_idea', 'Bizarre Idea'),
        ('other', 'Other'),
    )
    category = models.CharField(max_length=50, choices=CATEGORIES, default='technical')
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    post = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HiddenPageLongPost(models.Model):
    date_id = models.ForeignKey(DailyEvent, unique=False, on_delete=models.CASCADE)

    permission = GenericRelation(PostPermission)
    comment = GenericRelation(Comment)

    CATEGORIES = (
        ('project_update', 'Project Update'),
        ('technical', 'Technical'),
        ('dream', 'Dream'),
        ('political', 'Political'),
        ('plan', 'Plan'),
        ('goal', 'Goal'),
        ('super-optimistic-dream', 'Super Optimistic Dream'),
        ('story', 'Story'),
        ('real-story', 'Real Story'),
        ('bizarre_idea', 'Bizarre Idea'),
        ('other', 'Other'),
    )
    category = models.CharField(max_length=50, choices=CATEGORIES, default='technical')
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    post = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OnPermissionPageLongPost(models.Model):
    date_id = models.ForeignKey(DailyEvent, unique=False, on_delete=models.CASCADE)

    comment = GenericRelation(Comment)
    permission = GenericRelation(PostPermission)

    CATEGORIES = (
        ('project_update', 'Project Update'),
        ('technical', 'Technical'),
        ('dream', 'Dream'),
        ('political', 'Political'),
        ('plan', 'Plan'),
        ('goal', 'Goal'),
        ('super-optimistic-dream', 'Super Optimistic Dream'),
        ('story', 'Story'),
        ('real-story', 'Real Story'),
        ('bizarre_idea', 'Bizarre Idea'),
        ('other', 'Other'),
    )
    category = models.CharField(max_length=50, choices=CATEGORIES, default='technical')
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    post = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PrivatePageLongPost(models.Model):
    date_id = models.ForeignKey(DailyEvent, unique=False, on_delete=models.CASCADE)

    comment = GenericRelation(Comment)
    permission = GenericRelation(PostPermission)

    CATEGORIES = (
        ('project_update', 'Project Update'),
        ('technical', 'Technical'),
        ('dream', 'Dream'),
        ('political', 'Political'),
        ('plan', 'Plan'),
        ('goal', 'Goal'),
        ('super-optimistic-dream', 'Super Optimistic Dream'),
        ('story', 'Story'),
        ('real-story', 'Real Story'),
        ('bizarre_idea', 'Bizarre Idea'),
        ('other', 'Other'),
    )
    category = models.CharField(max_length=50, choices=CATEGORIES, default='technical')
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    post = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PublicShortPost(models.Model):
    date_id = models.ForeignKey(DailyEvent, unique=False, on_delete=models.CASCADE)

    comment = GenericRelation(Comment)

    CATEGORIES = (
        ('project_update', 'Project Update'),
        ('thought', 'Thought'),
        ('update', 'Update'),
    )
    category = models.CharField(max_length=200, choices=CATEGORIES, default='update')
    post = models.CharField(max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post


class HiddenShortPost(models.Model):
    date_id = models.ForeignKey(DailyEvent, unique=False, on_delete=models.CASCADE)

    comment = GenericRelation(Comment)
    permission = GenericRelation(PostPermission)

    CATEGORIES = (
        ('project_update', 'Project Update'),
        ('thought', 'Thought'),
        ('update', 'Update'),
    )
    category = models.CharField(max_length=200, choices=CATEGORIES, default='update')
    post = models.CharField(max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post


class OnPermissionShortPost(models.Model):
    date_id = models.ForeignKey(DailyEvent, unique=False, on_delete=models.CASCADE)

    permission = GenericRelation(PostPermission)
    comment = GenericRelation(Comment)

    CATEGORIES = (
        ('project_update', 'Project Update'),
        ('thought', 'Thought'),
        ('update', 'Update'),
    )
    category = models.CharField(max_length=200, choices=CATEGORIES, default='update')
    post = models.CharField(max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post


class PrivateShortPost(models.Model):
    date_id = models.ForeignKey(DailyEvent, unique=False, on_delete=models.CASCADE)

    permission = GenericRelation(PostPermission)
    comment = GenericRelation(Comment)

    CATEGORIES = (
        ('project_update', 'Project Update'),
        ('thought', 'Thought'),
        ('update', 'Update'),
    )
    category = models.CharField(max_length=200, choices=CATEGORIES, default='update')
    post = models.CharField(max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post


class Image(models.Model):
    CATEGORY = (
        (PrivatePageLongPost, 'Private Page Long Post'),
        (PublicPageLongPost, 'Public Page Long Post'),
        (HiddenPageLongPost, 'Hidden Page Long Post'),
        (OnPermissionPageLongPost, 'On Permission Page Long Post'),
    )
    date_id = models.ForeignKey(DailyEvent, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY, null=True, blank=True, max_length=50)
    img1 = models.ImageField(upload_to='content/images/posted/', null=True, blank=True)
    img2 = models.ImageField(upload_to='content/images/posted/', null=True, blank=True)
    img3 = models.ImageField(upload_to='content/images/posted/', null=True, blank=True)
    img4 = models.ImageField(upload_to='content/images/posted/', null=True, blank=True)
    img5 = models.ImageField(upload_to='content/images/posted/', null=True, blank=True)
    img6 = models.ImageField(upload_to='content/images/posted/', null=True, blank=True)

    def __str__(self):
        return str(self.date_id.date)+' : '+str(self.category)


class HourlyUpdates(models.Model):
    date_id = models.ForeignKey(DailyEvent, on_delete=models.CASCADE)
    sender = models.CharField(max_length=10)
    message = models.CharField(max_length=200)
    expiry = models.DateTimeField(default=(datetime.now() + timedelta(hours=24)))
    attachment = models.FileField(upload_to='content/files/hourly/', null=True, blank=True)

    def __str__(self):
        return str(self.expiry)+' : '+str(self.message)

# class Video(models.Model):
#     CATEGORY = (
#         (PrivatePageLongPost, 'Private Page Long Post'),
#         (PublicPageLongPost, 'Public Page Long Post'),
#         (HiddenPageLongPost, 'Hidden Page Long Post'),
#         (OnPermissionPageLongPost, 'On Permission Page Long Post'),
#     )
#     date_id = models.ForeignKey(DailyEvent, on_delete=models.CASCADE)
#     category = models.ForeignKey(choices=CATEGORY, null=True, blank=True)
#     img1 = models.FileField(upload_to='content/images/posted/', null=True)
#     img2 = models.FileField(upload_to='content/images/posted/', null=True)
#     img3 = models.FileField(upload_to='content/images/posted/', null=True)
#     img4 = models.FileField(upload_to='content/images/posted/', null=True)
#     img5 = models.FileField(upload_to='content/images/posted/', null=True)
#     img6 = models.FileField(upload_to='content/images/posted/', null=True)


# class DailyPost(models.Model):
#     PRIVACY_OPTIONS = (
#         ('Private', 'Only you can see the post'),
#         ('OnDemand', 'Viewer will have to ask for permissions to see the post'),
#         ('Hidden', 'You will know, who saw your post'),
#         ('Public', 'Everyone on Internet can see this'),
#     )
#     date_id = models.ForeignKey(DailyEvent, on_delete=models.CASCADE)
#     privacy = models.CharField(max_length=100, choices=PRIVACY_OPTIONS)
#

#
# class PageLongBlogPost(models.Model):
#     CATEGORIES = (
#         ('project_update', 'Project Update'),
#         ('technical', 'Technical'),
#         ('dream', 'Dream'),
#         ('political', 'Political'),
#         ('plan', 'Plan'),
#         ('goal', 'Goal'),
#         ('super-optimistic-dream', 'Super Optimistic Dream'),
#         ('story', 'Story'),
#         ('real-story', 'Real Story'),
#         ('bizarre_idea', 'Bizarre Idea'),
#         ('other', 'Other'),
#     )
#     category = models.CharField(max_length=200, choices=CATEGORIES, default='technical')
#     title = models.CharField(max_length=200)
#     summary = models.TextField()
#     post = models.TextField()
#
#     def __str__(self):
#         return self.title
#
#
# class ShortBlogPost(models.Model):
#     CATEGORIES = (
#         ('project_update', 'Project Update'),
#         ('thought', 'Thought'),
#         ('update', 'Update'),
#     )
#     category = models.CharField(max_length=200, choices=CATEGORIES, default='update')
#     post = models.CharField(max_length=500)
#
#     def __str__(self):
#         return self.post

#
# class DateAndPostRelation(models.Model):
#     date_id = models.ForeignKey(DailyPost)
#     post_id = models.ForeignKey(PageLongBlogPost)
#     views = models.TextField(null=True, blank=True)
#     view_requests = models.TextField(null=True, blank=True)
#
#
# #
# class ProjectUpdate(models.Model):
#     post = models.TextField()
#
#     def __str__(self):
#         return self.post
#
#
# class PageLongBlogPost(models.Model):
#     title = models.CharField(max_length=200)
#     post = models.TextField()
#
#     def __str__(self):
#         return self.title
