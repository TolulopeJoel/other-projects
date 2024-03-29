import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse

from .models import Subscriber, Unsubscriber


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' 'filename={}.csv'.format(
        opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields(
    ) if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)

    return response


export_to_csv.short_description = 'Export to CSV'


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'confirmed']
    list_filter = ['confirmed', 'created_at']
    actions = [export_to_csv]
    search_fields = ['email', 'first_name', 'last_name']


class UnubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'created_at']
    list_filter = ['created_at']
    actions = [export_to_csv]


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Unsubscriber, UnubscriberAdmin)
