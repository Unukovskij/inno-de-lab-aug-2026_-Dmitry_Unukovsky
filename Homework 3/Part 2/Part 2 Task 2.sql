-- Part 2: Join

-- Task 2
/*Выведите список доставок со статусом и именем клиента.*/

SELECT 
	status,
	first_name,
	last_name
FROM Shippings
JOIN Customers ON Shippings.customer = Customers.customer_id;