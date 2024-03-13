from django.contrib import admin
from .models import Smp


# Register your models here.


class SmpAdmin(admin.ModelAdmin):

    list_display = (
        'from_to_year',
        'territorial_unit',
        'name_of_diseases',
        'value',
        'from_year_format',
        'to_year_format',
        'modified_at',
        'created_at',

    )
    list_editable = (

    )
    list_filter = ('from_to_year', 'territorial_unit')

    def from_year_format(self, obj):
        return obj.from_year.strftime('%m.%Y')

    from_year_format.short_description = 'Начальный год'

    def to_year_format(self, obj):
        return obj.to_year.strftime('%m.%Y')

    to_year_format.short_description = 'Последний год'


admin.site.register(Smp, SmpAdmin)
