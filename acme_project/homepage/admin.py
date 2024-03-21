from django.contrib import admin

# Register your models here.
from .models import DistrictName, TerritorialUnit, GeoCategory, StatForm
from .models import TableForm, PeriodMonth, PeriodYear, NameOfDiseases, Units, \
    Contingents

admin.site.register(GeoCategory)

admin.site.register(PeriodYear)


class DistrictNameAdmin(admin.ModelAdmin):
    list_display = (
        'title_ru',
        'short_ru'
    )


admin.site.register(DistrictName, DistrictNameAdmin)


class TerritorialUnitAdmin(admin.ModelAdmin):
    list_display = (
        'title_ru',
        'district',
        'geo_category',
    )

    list_editable = (
        'district',
        'geo_category',

    )

    list_filter = ('district', 'geo_category')
    list_display_links = ('title_ru',)
    empty_value_display = 'Не задано'


admin.site.register(TerritorialUnit, TerritorialUnitAdmin)


class StatFormAdmin(admin.ModelAdmin):
    list_display = (
        'num_form',
        'title_ru',
        'count_table',

    )

    list_editable = (

    )


admin.site.register(StatForm, StatFormAdmin)


class TableFormAdmin(admin.ModelAdmin):
    list_display = (
        'form',
        'title_ru',
        'table_number',

    )

    list_editable = (

    )


admin.site.register(TableForm, TableFormAdmin)


class NameOfDiseasesAdmin(admin.ModelAdmin):
    list_display = (
        'title_ru',
    )


admin.site.register(NameOfDiseases, NameOfDiseasesAdmin)


class UnitsAdmin(admin.ModelAdmin):
    list_display = (
        'title_ru',
    )


admin.site.register(Units, UnitsAdmin)


class ContingentsAdmin(admin.ModelAdmin):
    list_display = (
        'title_ru',
    )


admin.site.register(Contingents)


class PeriodMonthAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title_ru',
    )


admin.site.register(PeriodMonth, PeriodMonthAdmin)
