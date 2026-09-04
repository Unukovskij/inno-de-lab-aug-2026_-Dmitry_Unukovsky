#Task1
# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

#Разбиваю строку по разделителю ";"
parts = raw_user_record.split(";")
#Очищаю элементы от пробелов в начале и конце
cleaned_parts = [part.strip() for part in parts]
#Добавить UID- к идентификатору
user_id = f"UID-{cleaned_parts[0]}"
#Меняю "_" на " " - пробел, привожу к заглавным
user_name = cleaned_parts[1].replace("_", " ").title()
# Тут городу делаю верхний регистр
city = cleaned_parts[2].upper()
# Статусу нижний регистр
status = cleaned_parts[3].lower()
#Объеденяю все в одну строку
result = " | ".join([user_id, user_name, city, status])
#Вывод
print("Нормализованная запись:", result)
