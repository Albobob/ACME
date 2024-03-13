from django.contrib import admin
from .models import FirstForm


# Register your models here.


class FirstFormAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_diseases',
        'territory',
        'period_year',
        'period_month',
        'contingents',
        'value',
        'unit',
    )
    pass


admin.site.register(FirstForm, FirstFormAdmin)
