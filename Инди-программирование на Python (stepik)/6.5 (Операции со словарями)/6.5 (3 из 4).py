# Задача:
# https://i.gyazo.com/8b58aff36ac23fa2746f7ec6cf215ecc.png

# Решение:
account = {
  "id": 3136,
  "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
  "account_number": "0847799459",
  "iban": "GB90XTND56373623909314",
  "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
  "routing_number": "126602476",
  "swift_bic": "BCYPGB2LHGB"
}

keys = []
for key in account:
    keys.append(key)
print(keys)