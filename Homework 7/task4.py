#Task4
# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]

# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}

#Дедупликация - преобразовываюсписок во множество
unique_roles = set(requested_roles)
#Пересечение множеств. Выбирает только то что есть в обоих множествах
common_admin_roles = unique_roles & required_admin_roles
#Разность множеств. Тут выбирает что есть в первом но нет во втором
missing_admin_roles = required_admin_roles - unique_roles
#Происходит проверка наличия security_officer
has_security_officer = "security_officer" in unique_roles
#Вывод результатов
print("Уникальные запрошенные роли:", unique_roles)
print("Общие административные роли:", common_admin_roles)
print("Недостающие административные роли:", missing_admin_roles)
print("Наличие роли security_officer в запросе:", has_security_officer)
