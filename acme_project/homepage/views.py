from django.shortcuts import render

reg = ['Белгородская область', 'Брянская область', 'Владимирская область',
       'Воронежская область', 'Ивановская область', 'Калужская область',
       'Костромская область', 'Курская область', 'Липецкая область',
       'Московская область', 'Орловская область', 'Рязанская область', 
       'Смоленская область', 'Тамбовская область', 'Тверская область',
       'Тверская область', 'Ярославска область', 'Москва',
       'Республика Карелия', 'Республика Коми', 
       'Архангельская область', 'Ненецкий автономный округ',
       'Вологодская область', 'Калининградская область', 
       'Ленинградская область', 'Мурманская область', 'Новгородская область', 
       'Псковская область', 'Санкт-Петербург', 'Республика Адыгея', 
       'Республика Калмыкия', 'Республика Крым', 'Краснодарский край', 
       'Астраханская область', 'Волгоградская область', 'Ростовская область', 
       'Севастополь', 'Республика Дагестан', 'Республика Ингушетия', 
       'Кабардино-Балкарская Республика', 'Карачаево-Черкесская Республика', 
       'Республика Северная Осетия — Алания', 'Чеченская Республика', 
       'Ставропольский край', 'Республика Башкортостан', 'Республика Марий Эл',
       'Республика Мордовия', 'Республика Татарстан', 'Удмуртская Республика',
       'Чувашская Республика', 'Пермский край', 'Кировская область',
       'Нижегородская область', 'Оренбургская область', 'Пензенская область',
       'Самарская область', 'Саратовская область', 'Ульяновская область',
       'Курганская область', 'Свердловская область', 'Тюменская область',
       'Ханты-Мансийский автономный округ — Югра',
       'Ямало-Ненецкий автономный округ',
       'Челябинская область', 'Республика Алтай', 'Республика Тыва',
       'Республика Хакасия', 'Алтайский край', 'Красноярский край',
       'Иркутская область', 'Кемеровская область', 'Новосибирская область',
       'Омская область', 'Томская область', 'Республика Бурятия',
       'Республика Саха (Якутия)', 'Забайкальский край', 'Камчатский край',
       'Приморский край', 'Хабаровский край', 'Амурская область',
       'Магаданская область', 'Сахалинская область',
       'Еврейская автономная область', 'Чукотский автономный округ']

TABLE_NAME = 'Регионы Российской Федерации'
COL_NAME_ONE = 'Регионы'


# Create your views here.
def homepage(request):
    table_name = TABLE_NAME
    collumn_one_name = COL_NAME_ONE
    context = {'table_name': table_name,
               'collumn_one_name': collumn_one_name,
               'regions': reg[:12]}
    template = 'homepage/index.html'
    return render(request, template, context)
