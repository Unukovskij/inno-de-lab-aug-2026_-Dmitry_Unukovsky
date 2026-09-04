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
