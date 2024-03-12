from django.contrib import admin

# Register your models here.
from .models import DistrictName, TerritorialUnit, GeoCategory

admin.site.register(GeoCategory)


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
        'geo_category'
    )

    list_editable = (
        'district',
        'geo_category',

    )

    list_filter = ('district', 'geo_category')
    list_display_links = ('title_ru',)
    empty_value_display = 'Не задано'


admin.site.register(TerritorialUnit, TerritorialUnitAdmin)
