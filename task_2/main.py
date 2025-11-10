# Бесанец Алексей
print("start code...\n")

import json

# Загружаем данные
with open("dump.json", encoding="utf-8") as f:
    data = json.load(f)

# Создаем словарь специальностей по pk для быстрого доступа
specialties = {}
for item in data:
    if item.get("model") == "data.specialty":
        pk = item.get("pk")
        fields = item.get("fields", {})
        specialties[pk] = fields

# Ввод номера квалификации пользователем
qualification_code = input("Введите номер квалификации: ").strip()

found = False

for item in data:
    if item.get("model") == "data.skill":
        fields = item.get("fields", {})
        code = fields.get("code")
        title = fields.get("title")
        specialty_pk = fields.get("specialty")

        if code == qualification_code:
            found = True
            print("=============== Найдено ===============")
            if specialty_pk in specialties:
                sp = specialties[specialty_pk]
                sp_code = sp.get("code")
                sp_title = sp.get("title")
                sp_type = sp.get("c_type")
                print(f"{sp_code} >> Специальность \"{sp_title}\", {sp_type}")
            print(f"{code} >> Квалификация \"{title}\"")
            break

if not found:
    print("=============== Не найдено ===============")



print("end code...\n\n")