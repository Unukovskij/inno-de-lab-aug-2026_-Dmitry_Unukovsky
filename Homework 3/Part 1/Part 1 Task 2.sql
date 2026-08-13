-- Part 1: Where

-- Task 2
/*Выведите все заказы, у которых сумма (amount) больше 1000.*/

SELECT
	order_id,
	item,
	amount,
	customer_id
FROM Orders
WHERE amount > 1000;