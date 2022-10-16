money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
grow = 1.05
month_spend = salary - spend
while money_capital + month_spend >= spend:
    money_capital += month_spend
    spend = spend * grow
    month += 1


print(month)
