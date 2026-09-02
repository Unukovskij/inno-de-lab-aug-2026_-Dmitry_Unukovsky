# Task3
# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

#Безопасно получаю вложенный словарь
connection = db_config.get("connection", {})

# Извдекаю host и post через get
host = connection.get("host", "localhost")
port = connection.get("port", 5432)

# Проверяю наличие ssl_settings
ssl_settings = db_config.get("ssl_settings", {}) #Изменил connection на db_config
ssl_mode = ssl_settings.get("ssl_mode", "verify-full")

# Меняю user на admin
connection["user"] = "admin"
# Добавляю новый парамтр max_connection = 100
connection["max_connections"] = 100
# Вывод обновленного содержимого connection


print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")
# items() возвращает (ключ, значение) для итерации
for key, value in connection.items():
    print(f"* {key}: {value}")
