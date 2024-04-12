account_balance_sum = 0

while True:
    text = input()

    if text == 'NoMoreMoney':
        break

    current_deposit_sum = float(text)

    if current_deposit_sum >= 0:
        account_balance_sum += current_deposit_sum
        print(f'Increase: {current_deposit_sum:.2f}')
    else:
        print(f'Invalid operation!')
        break

print(f'Total: {account_balance_sum:.2f}')
