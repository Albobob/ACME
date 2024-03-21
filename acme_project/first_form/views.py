from django.shortcuts import render
from .models import FirstForm
from pprint import pprint
from statistics import mean
from django.http import HttpResponseRedirect
from .forms import FirstChoiceForm


def get_current_years():
    query_uniq_years = FirstForm.objects.values_list('period_year__title_ru',
                                                     ).order_by(
        'period_year__id').distinct()

    return [year[0] for year in query_uniq_years]


def get_current_month():
    query_uniq_month = FirstForm.objects.values_list('period_month__title_ru',
                                                     ).order_by(
        'period_month__id').distinct()

    return [year[0] for year in query_uniq_month]


def get_month_range(month: list) -> int:
    if month == [1]:
        return 1
    elif month == [1, 2]:
        return 2
    elif month == [1, 2, 3] or month == [1, 3]:
        return 3
    elif month == [1, 2, 3, 4] or month == [1, 4]:
        return 4
    elif month == [1, 2, 3, 4, 5] or month == [1, 5]:
        return 5
    elif month == [1, 2, 3, 4, 5, 6] or month == [1, 6]:
        return 6
    elif month == [1, 2, 3, 4, 5, 6, 7] or month == [1, 7]:
        return 7
    elif month == [1, 2, 3, 4, 5, 6, 7, 8] or month == [1, 8]:
        return 8
    elif month == [1, 2, 3, 4, 5, 6, 7, 8, 9] or month == [1, 9]:
        return 9
    elif month == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] or month == [1, 10]:
        return 10
    elif month == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] or month == [1, 11]:
        return 11
    elif month == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] or month == [1, 12]:
        return 12
    elif month == [2]:
        return 13
    elif month == [2, 3]:
        return 14
    elif month == [2, 3, 4] or month == [2, 4]:
        return 15
    elif month == [2, 3, 4, 5] or month == [2, 5]:
        return 16
    elif month == [2, 3, 4, 5, 6] or month == [2, 6]:
        return 17
    elif month == [2, 3, 4, 5, 6, 7] or month == [2, 7]:
        return 18
    elif month == [2, 3, 4, 5, 6, 7, 8] or month == [2, 8]:
        return 19
    elif month == [2, 3, 4, 5, 6, 7, 8, 9] or month == [2, 9]:
        return 20
    elif month == [2, 3, 4, 5, 6, 7, 8, 9, 10] or month == [2, 10]:
        return 21
    elif month == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] or month == [2, 11]:
        return 22
    elif month == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] or month == [2, 12]:
        return 23
    elif month == [3]:
        return 24
    elif month == [3, 4]:
        return 25
    elif month == [3, 4, 5] or month == [3, 5]:
        return 26
    elif month == [3, 4, 5, 6] or month == [3, 6]:
        return 27
    elif month == [3, 4, 5, 6, 7] or month == [3, 7]:
        return 28
    elif month == [3, 4, 5, 6, 7, 8] or month == [3, 8]:
        return 29
    elif month == [3, 4, 5, 6, 7, 8, 9] or month == [3, 9]:
        return 30
    elif month == [3, 4, 5, 6, 7, 8, 9, 10] or month == [3, 10]:
        return 31
    elif month == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] or month == [3, 11]:
        return 32
    elif month == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12] or month == [3, 12]:
        return 33
    elif month == [4]:
        return 34
    elif month == [4, 5]:
        return 35
    elif month == [4, 5, 6] or month == [4, 6]:
        return 36
    elif month == [4, 5, 6, 7] or month == [4, 7]:
        return 37
    elif month == [4, 5, 6, 7, 8] or month == [4, 8]:
        return 38
    elif month == [4, 5, 6, 7, 8, 9] or month == [4, 9]:
        return 39
    elif month == [4, 5, 6, 7, 8, 9, 10] or month == [4, 10]:
        return 40
    elif month == [4, 5, 6, 7, 8, 9, 10, 11] or month == [4, 11]:
        return 41
    elif month == [4, 5, 6, 7, 8, 9, 10, 11, 12] or month == [4, 12]:
        return 42
    elif month == [5]:
        return 43
    elif month == [5, 6]:
        return 44
    elif month == [5, 6, 7] or month == [5, 7]:
        return 45
    elif month == [5, 6, 7, 8] or month == [5, 8]:
        return 46
    elif month == [5, 6, 7, 8, 9] or month == [5, 9]:
        return 47
    elif month == [5, 6, 7, 8, 9, 10] or month == [5, 10]:
        return 48
    elif month == [5, 6, 7, 8, 9, 11] or month == [5, 11]:
        return 49
    elif month == [5, 6, 7, 8, 9, 11, 12] or month == [5, 12]:
        return 50
    elif month == [6]:
        return 51
    elif month == [6, 7]:
        return 52
    elif month == [6, 7, 8] or month == [6, 8]:
        return 53
    elif month == [6, 7, 8, 9] or month == [6, 9]:
        return 54
    elif month == [6, 7, 8, 9, 10] or month == [6, 10]:
        return 55
    elif month == [6, 7, 8, 9, 10, 11] or month == [6, 11]:
        return 56
    elif month == [6, 7, 8, 9, 10, 11, 12] or month == [6, 12]:
        return 57
    elif month == [7]:
        return 58
    elif month == [7, 8]:
        return 59
    elif month == [7, 8, 9] or month == [7, 9]:
        return 60
    elif month == [7, 8, 9, 10] or month == [7, 10]:
        return 61
    elif month == [7, 8, 9, 10, 11] or month == [7, 11]:
        return 62
    elif month == [7, 8, 9, 10, 11, 12] or month == [7, 12]:
        return 63
    elif month == [8]:
        return 64
    elif month == [8, 9]:
        return 65
    elif month == [8, 9, 10] or month == [8, 10]:
        return 66
    elif month == [8, 9, 10, 11] or month == [8, 11]:
        return 67
    elif month == [8, 9, 10, 11, 12] or month == [8, 12]:
        return 68
    elif month == [9]:
        return 69
    elif month == [9, 10]:
        return 70
    elif month == [9, 10, 11] or month == [9, 11]:
        return 71
    elif month == [9, 10, 11, 12] or month == [9, 12]:
        return 72
    elif month == [10]:
        return 73
    elif month == [10, 11]:
        return 74
    elif month == [10, 11, 12] or month == [10, 12]:
        return 75
    elif month == [11]:
        return 76
    elif month == [11, 12]:
        return 77
    elif month == [12]:
        return 78
    else:
        return 0


territory_filter = [1]
year_filter = get_current_years()[-10::]
month_filter = 1


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
        territory__id__in=territory_filter,
        period_year__title_ru__in=year_filter,
        period_month__id=month_filter,

    ).order_by('territory__id'))

    output_data = [
        {
            'territory': i[0],
            'year': i[1],
            'value': i[2],

        } for i in query
    ]

    # pprint(output_data)

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


def my_view(request):
    if request.method == 'POST':
        # Логика обновления запроса
        # Например, перенаправление на ту же страницу
        return HttpResponseRedirect(request.path_info)


def first_form(request):
    TABLE_NAME = 'Регионы Российской Федерации'
    FIRST_COLUMN = 'Регион'
    SECOND_COLUMN = 'Округ'

    global territory_filter, year_filter, month_filter
    if request.method == 'GET':
        form = FirstChoiceForm(request.GET)

        if form.is_valid():
            territory_value = form.cleaned_data['territory']
            territory_filter = territory_value

            years_value = form.cleaned_data['years']
            year_filter = years_value

            months_value = list(map(int, form.cleaned_data['months']))
            months = get_month_range(months_value)

            if not months:
                print('Не верно введен месяц')
            else:
                print(month_filter)
                month_filter = months
                print(month_filter)

            # Обрабатываем значение territory,
            # например, сохраняем его или используем по необходимости
        else:
            print('Заполните все поля')
            pass
    # В случае ошибок формы можно добавить обработку здесь

    else:
        form = FirstChoiceForm()

    data = formatted_data(get_data())

    context = {
        'form': form,
        'table_name': TABLE_NAME,
        'data': data,
        'header': year_filter,
        'row_data': data,
    }
    template = 'first_form/index.html'
    return render(request, template, context=context)
