# Задача:
# https://i.gyazo.com/04e8b64ca387bd0e072ff2800cb4f4bd.png

# Решение:
d1 = {'India': 'Delhi',
      'Canada': 'Ottawa',
      'United States': 'Washington D. C.'}

d2 = {'France': 'Paris',
      'Malaysia': 'Kuala Lumpur'}
capitals = d1 | d2
print(capitals)