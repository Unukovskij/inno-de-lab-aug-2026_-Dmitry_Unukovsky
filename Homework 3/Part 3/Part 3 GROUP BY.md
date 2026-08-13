
```sql



-- Part 3: GROUP BY

-- Task 1
/*Подсчитайте количество клиентов в каждой стране.*/

SELECT 
	country,
	COUNT(*) AS count
FROM Customers
GROUP BY country;

-- Task 2
/*Посчитайте общее количество заказов и среднюю сумму по каждому товару.*/

SELECT 
	item,
	COUNT(*) AS count,
	ROUND(AVG(amount),2) AS avg_amount
FROM Orders
GROUP BY item;




```