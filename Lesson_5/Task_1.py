# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple


def get_company_and_average_profit_list(companies_amount):
    companies_list = []

    for i in range(companies_amount):
        company_name = str((input("Введите имя компаниии: ")))
        q_1 = float(input("Введите прибыль за 1 квартал: "))
        q_2 = float(input("Введите прибыль за 2 квартал: "))
        q_3 = float(input("Введите прибыль за 3 квартал: "))
        q_4 = float(input("Введите прибыль за 4 квартал: "))
        Company = namedtuple(company_name, ['name', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4', 'profit_avr'])
        company = Company(name=company_name, quarter_1=q_1, quarter_2=q_2, quarter_3=q_3, quarter_4=q_4,
                          profit_avr=(q_1 + q_2 + q_3 + q_4) / 4)
        companies_list.append(company)
    return companies_list


def get_average_profit_all_companies():
    n = int(input("Введите колличество компаний: "))
    companies = get_company_and_average_profit_list(n)
    companies_profits_average = 0
    companies_data = {'average_all_profits': 0, 'more_then_average': [], 'less_then_average': []}

    for i in range(n):
        companies_profits_average += companies[i].profit_avr / n
    companies_data['average_all_profits'] = companies_profits_average
    for i in range(n):
        if companies[i].profit_avr > companies_profits_average:
            companies_data['more_then_average'].append(companies[i].name)
        if companies[i].profit_avr < companies_profits_average:
            companies_data['less_then_average'].append(companies[i].name)

    return companies_data


print(get_company_and_average_profit_list(2))