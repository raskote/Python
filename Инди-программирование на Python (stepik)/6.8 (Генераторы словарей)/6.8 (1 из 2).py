# Задача:
# https://i.gyazo.com/36a8de1a3bdda8d75117dbd1b1fe6e70.png

# Решение:
user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17",
    "employment": {
        "title": "Central Hospitality Liaison",
        "key_skill": "Organisation"
    },
    "subscription": {
        "plan": "Essential",
        "status": "Idle",
        "payment_method": "Debit card",
        "term": "Annual"
    }
}

s = input().split()
print({key: user.get(key) for key in s})