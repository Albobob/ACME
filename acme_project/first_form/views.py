from django.shortcuts import render
from .models import FirstForm
from pprint import pprint
from statistics import mean
from django.http import HttpResponseRedirect

TABLE_NAME = 'Регионы Российской Федерации'
FIRST_COLUMN = 'Регион'
SECOND_COLUMN = 'Округ'

territory_filter = 'Российская Федерация'
year_filter = (2013, 2014, 2015, 2016, 2017, 2018)


# Create your views here.
def check_outliers(data: list):
    result = {
        'outliers_max': None,
        'outliers_min': None,
        'value': None,
    }
    # Построение вариант в порядке возрастания
    sorted_data = sorted(data)

    # Критерии для исключения выскакивающих вариант
    exclusion_criteria: dict[int, dict[int, float]] = {
        3: {95: 0.941, 99: 0.988},
        4: {95: 0.765, 99: 0.889},
        5: {95: 0.642, 99: 0.78},
        6: {95: 0.56, 99: 0.698},
        7: {95: 0.507, 99: 0.637},
        8: {95: 0.468, 99: 0.59},
        9: {95: 0.437, 99: 0.555},
        10: {95: 0.412, 99: 0.527},
        11: {95: 0.392, 99: 0.502},
        12: {95: 0.376, 99: 0.482},
        15: {95: 0.338, 99: 0.438},
        20: {95: 0.3, 99: 0.391},
        24: {95: 0.281, 99: 0.367},
        30: {95: 0.26, 99: 0.341}
    }

    # Уровень достоверности, %
    # TODO: Переименовать переменные a, b
    a: float = exclusion_criteria[len(data)][95]
    b: float = exclusion_criteria[len(data)][99]

    # Вычисление разности между наибольшей и наименьшей вариантами ряда
    diff_max_min: float = max(data) - min(data)
    outliers: list = []

    try:
        ratio_max = (sorted_data[-1] - sorted_data[-2]) / diff_max_min
        if ratio_max > a or ratio_max > b:
            outliers.append(max(sorted_data))
            result['outliers_max'] = True

        ratio_min = (sorted_data[1] - sorted_data[0]) / diff_max_min
        if ratio_min > a or ratio_min > b:
            outliers.append(min(sorted_data))
            result['outliers_min'] = True

    except ZeroDivisionError:
        result['value'] = 0

    # Вычисление среднего значения, исключая выбросы

    data_final = [value for value in data if value not in outliers]
    result['value'] = round(mean(data_final), 2)

    # print(data)
    # print(outliers)
    # print(data_final)

    return result


def get_data():
    query = list(FirstForm.objects.values_list('territory__title_ru',
                                               'period_year__title_ru',
                                               'value').filter(
        territory__title_ru=territory_filter,
        period_year__title_ru__in=year_filter,
    ))

    output_data = [
        {
            'territory': i[0],
            'year': i[1],
            'value': i[2],

        } for i in query
    ]

    pprint(output_data)

    return output_data


def formatted_data(data: list):
    # Создание множества уникальных территорий
    unique_territories = {itm['territory'] for itm in data}
    years = set()
    output = []

    # Проход по каждой уникальной территории
    for territory in unique_territories:
        formatted_output = {}
        territory_data = {"data": {itm['year']: itm['value'] for itm in data if
                                   itm['territory'] == territory}}

        years.update(territory_data["data"].keys())

        # Получение значений и определение СМП
        values = list(territory_data["data"].values())
        smp = check_outliers(values)

        # Формирование строки для таблицы
        formatted_output["territory"] = territory
        formatted_output["data"] = territory_data["data"]
        formatted_output["smp"] = smp["value"]
        output.append(formatted_output)

    return output


data = formatted_data(get_data())


def my_view(request):
    if request.method == 'POST':
        # Логика обновления запроса
        # Например, перенаправление на ту же страницу
        return HttpResponseRedirect(request.path_info)


def first_form(request):
    years = year_filter

    context = {
        'table_name': TABLE_NAME,
        'data': data,
        'header': years,
        'row_data': data

    }
    template = 'first_form/index.html'
    return render(request, template, context=context)
