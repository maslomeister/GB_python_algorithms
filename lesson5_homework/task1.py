# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple

def findHighestAndLowestEarningCompanies(companies):
    avg_profit = 0

    for company in companies:
        avg_profit += company.profit

    avg_profit = avg_profit / len(companies)

    print(f"\nСредняя годовая прибыль среди всех компаний: {avg_profit}")

    print(f"\nКомпании чья годовая прибыль выше средней:")

    for company in companies:
        if company.profit > avg_profit:
            print(
                f"\n{ company.name } ({ company.profit })")

    print(f"\nКомпании чья годовая прибыль ниже средней:")

    for company in companies:
        if company.profit < avg_profit:
            print(
                f"\n{ company.name } ({ company.profit })")


while True:
    try:

        amount_of_companies = int(input("\nВведите количество предприятий: "))
        assert amount_of_companies > 0

    except ValueError:

        print(
            "\nНеправильный ввод(Допускаются только целые положительные числа)")
        continue

    except AssertionError:

        print("\nКоличество компаний не может быть меньше или равно 0")

        continue
    break

Company = namedtuple(
    "Company", "name profit")

companies = []

for i in range(amount_of_companies):

    name = str(input("\nВведите название компании: "))

    profit = 0

    for i in range(4):

        while True:

            try:

                profit += (
                    float(input(f"\nВведите прибыль компании за { i + 1 } квартал: ")))

            except ValueError:

                print(
                    "\nНеправильный ввод(Допускаются числа вида: 1200; 1200.90; -1200 и т.д.)")

                continue

            break

    companies.append(Company(name, profit))


# print(companies_map)
findHighestAndLowestEarningCompanies(companies)
print("")
