from django.shortcuts import render


# Create your views here.
def smp(request):
    context = {'districts': [('Центральный федеральный округ',
                              'Central Federal District',
                              'ЦФО',
                              'CFD'),
                             ('Северо-Западный федеральный округ',
                              'Northwestern Federal District',
                              'СЗФО',
                              'NW-FD'),
                             ('Южный федеральный округ',
                              'Southern Federal District',
                              'ЮФО',
                              'SFD'),
                             ('Северо-Кавказский федеральный округ',
                              'North Caucasus Federal District',
                              'СКФО',
                              'NCD'),
                             ('Приволжский федеральный округ',
                              'Privolzhsky Federal District',
                              'ПФО',
                              'PFD'),
                             ('Уральский федеральный округ',
                              'Urals Federal District',
                              'УФО',
                              'UFD'),
                             ('Сибирский федеральный округ',
                              'Siberian Federal District',
                              'СФО',
                              'SibFD'),
                             ('Дальневосточный федеральный округ',
                              'Fareast Federal District',
                              'ДФО',
                              'FED')
                             ],

               }

    template = 'smp/mean_morbidity.html'
    return render(request, template, context)
