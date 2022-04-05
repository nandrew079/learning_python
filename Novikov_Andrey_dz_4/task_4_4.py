import utils

print(*utils.currency_rates('RUB'), sep=', ')
print(*utils.currency_rates('USD'), sep=', ')
print(*utils.currency_rates('eur'), sep=', ')
