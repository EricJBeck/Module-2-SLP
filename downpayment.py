price = 100000
good_credit = False


if good_credit:
    down_payment = price * .15
else:
    down_payment = price * .27
print(f'Down payment: ${down_payment}')
