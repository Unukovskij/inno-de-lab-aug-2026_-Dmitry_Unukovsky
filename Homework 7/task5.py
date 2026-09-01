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