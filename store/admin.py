from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from store.models import Category

# Register your models here.
admin.site.register([Category])
