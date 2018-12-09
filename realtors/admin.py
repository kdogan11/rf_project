from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hire_date')
    search_fields = ('name',)


admin.site.register(Realtor,RealtorAdmin)
