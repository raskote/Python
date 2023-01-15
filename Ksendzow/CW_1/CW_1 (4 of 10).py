# Задача:
# 4. Все emails у которых есть слово test вывести в другой список

# Решение:
l = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com'
     ]
n = []
for i in range(len(l)):
    if "test" in l[i]:
        n.append(l[i])
print(n)
