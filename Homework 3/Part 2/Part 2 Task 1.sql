-- Part 2: Join

-- Task 1
/*Получите список заказов вместе с именем клиента, который сделал заказ.*/

SELECT 
	first_name,
	last_name,
	item,
	amount
FROM Orders 
JOIN Customers ON Orders.customer_id = Customers.customer_id;