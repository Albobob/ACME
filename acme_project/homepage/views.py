from django.shortcuts import render
from .models import TerritorialUnit, DistrictName

TABLE_NAME = 'Регионы Российской Федерации'
FIRST_COLUMN = 'Регион'
SECOND_COLUMN = 'Округ'

# tu = TerritorialUnit.objects.select_related('district').values('id',
#                                                                'name_ru',
#                                                                'district_id',
#                                                                'district__short_ru',
#                                                                'geo_category_id',
#                                                                'created_at',
#                                                                'modified_at')

# for i in tu:
#     print(i['district__short_ru'])

tu = None


# Create your views here.
def homepage(request):
    context = {'table_name': TABLE_NAME,
               'first_column': FIRST_COLUMN,
               'second_column': SECOND_COLUMN,
               'regions': tu}
    template = 'homepage/index.html'
    return render(request, template, context)
