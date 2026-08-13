-- Part 3: GROUP BY

-- Task 2
/*Посчитайте общее количество заказов и среднюю сумму по каждому товару.*/

SELECT 
	item,
	COUNT(*) AS count,
	ROUND(AVG(amount),2) AS avg_amount
FROM Orders
GROUP BY item;
