-- Part 7

-- Task 1
/*Найти клиента. 
Сделали хотя бы 2 заказа (любых),
Имеют хотя бы одну доставку со статусом 'Delivered'
Вывести Имя и Фамилию, общее количество заказов, сумму заказов, страну проживания.
*/

WITH customer_orders AS (
    SELECT 
        customer_id,
        COUNT(*) AS total_orders,
        SUM(amount) AS total_amount
    FROM Orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 2
),
customer_delivered AS (
    SELECT 
        customer,
        COUNT(*) AS delivered_count
    FROM Shippings
    WHERE status = 'Delivered'
    GROUP BY customer
    HAVING COUNT(*) >= 1
)
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.country,
    co.total_orders,
    co.total_amount
FROM Customers c
INNER JOIN customer_orders co ON c.customer_id = co.customer_id
INNER JOIN customer_delivered cd ON c.customer_id = cd.customer
ORDER BY total_amount DESC;