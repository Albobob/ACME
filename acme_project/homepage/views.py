from django.shortcuts import render
from .models import TerritorialUnit

TABLE_NAME = 'Регионы Российской Федерации'
FIRST_COLUMN = 'Регион'
SECOND_COLUMN = 'Округ'

tu = TerritorialUnit.objects.values('title_ru', 'district__short_ru')


# Create your views here.
def homepage(request):
    context = {'table_name': TABLE_NAME,
               'first_column': FIRST_COLUMN,
               'second_column': SECOND_COLUMN,
               'regions': tu}
    template = 'homepage/index.html'
    return render(request, template, context)
