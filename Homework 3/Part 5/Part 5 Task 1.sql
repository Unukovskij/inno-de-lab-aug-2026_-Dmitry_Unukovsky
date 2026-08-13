-- Part 5: SUBQUERIES

-- Task 1
/*Найдите всех клиентов, которые сделали заказ с максимальной суммой.*/
-- использование подзапросов
SELECT 
    first_name,
    last_name,
    amount
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
WHERE Orders.amount = (SELECT MAX(amount) FROM Orders);