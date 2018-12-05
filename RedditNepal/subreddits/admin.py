from django.contrib import admin
from . import models
# Register your models here.

class SubRedditMemberInLine(admin.TabularInline):
    model = models.SubRedditMember

admin.site.register(models.SubReddit)
