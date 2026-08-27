#Homework7

# Task1
# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

# Разбиваю строку по разделителю ";"
parts = raw_user_record.split(";")
# Очищаю элементы от пробелов в начале и конце
cleaned_parts = [part.strip() for part in parts]
# Добавить UID- к идентификатору
user_id = f"UID-{cleaned_parts[0]}"
# Меняю "_" на " " - пробел, привожу к заглавным
user_name = cleaned_parts[1].replace("_", " ").title()
# Тут городу делаю верхний регистр
city = cleaned_parts[2].upper()
# Статусу нижний регистр
status = cleaned_parts[3].lower()
# Объеденяю все в одну строку
result = " | ".join([user_id, user_name, city, status])
# Вывод
print("Нормализованная запись:", result)

# Task2
# Список транзакций, полученных от платежного шлюза
raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
                    "SUCCESS:0", "SUCCESS:250", "ERROR:200"]

# преобразую сумму в int, for tx ... - перебираю все транзакции,
# потом оставляю только success и отбрасываю <= 0
filtered_transactions = [
    int(tx.split(":")[1])
    for tx in raw_transactions
    if tx.startswith("SUCCESS") and int(tx.split(":")[1]) > 0
]

print("Очищенные транзакции:", filtered_transactions)

# Task3
# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

# Извдекаю host и post
host = db_config["connection"]["host"]
port = db_config["connection"]["port"]
# Проверяю наличие ssl_settings
ssl_mode = db_config.get("connection", {}).get("ssl_settings", {}).get("ssl_mode", "verify-full")
# Меняю user на admin
db_config["connection"]["user"] = "admin"
# Добавляю новый парамтр max_connection = 100
db_config["connection"]["max_connections"] = 100
# Вывод обновленного содержимого connection
print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")
# items() возвращает (ключ, значение) для итерации
for key, value in db_config["connection"].items():
    print(f"* {key}: {value}")

# Task4
# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]

# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# Дедупликация - преобразовываюсписок во множество
unique_roles = set(requested_roles)
# Пересечение множеств. Выбирает только то что есть в обоих множествах
common_admin_roles = unique_roles & required_admin_roles
# Разность множеств. Тут выбирает что есть в первом но нет во втором
missing_admin_roles = required_admin_roles - unique_roles
# Происходит проверка наличия security_officer
has_security_officer = "security_officer" in unique_roles
# Вывод результатов
print("Уникальные запрошенные роли:", unique_roles)
print("Общие административные роли:", common_admin_roles)
print("Недостающие административные роли:", missing_admin_roles)
print("Наличие роли security_officer в запросе:", has_security_officer)

# Task5
# Поток данных телеметрии от серверов кластера
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")]

# Распаковываю кортеж в заголовке for
active_servers = [node_name for node_name, cpu_load, ram_usage, status in system_telemetry if status == "online"]
# Список CPU нагрузок
cpu_loads = [cpu for node, cpu, ram, status in system_telemetry if status == "online"]
# Список ram нагрузок
ram_usages = [ram for node, cpu, ram, status in system_telemetry if status == "online"]
# Считаю сколько серворов работают
active_count = len(active_servers)
# Находим среднее арефметическое. Складываем загрузку CPUи делим на количество
# Round - округляет до 2 знаков после запятой
avg_cpu = round(sum(cpu_loads) / len(cpu_loads), 2)
# Тут возвращаем максимальное число из списка
max_ram = max(ram_usages)
# Формирую итоговый словарь
result = {
    "active_nodes_count": active_count,
    "metrics": {
        "average_cpu": avg_cpu,
        "max_ram": max_ram
    }
}
# Вывод
print("Активные узлы в сети:", active_servers)
print("Итоговый отчет телеметрии:")
print(result)
