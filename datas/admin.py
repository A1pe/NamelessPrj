from django.contrib import admin
from . import models


@admin.register(models.Data)
class DataAdmin(admin.ModelAdmin):
    pass
