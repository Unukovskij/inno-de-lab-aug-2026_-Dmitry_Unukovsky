
```sql



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


-- Task 2
/*Выведите список доставок со статусом и именем клиента.*/

SELECT 
	status,
	first_name,
	last_name
FROM Shippings
JOIN Customers ON Shippings.customer = Customers.customer_id;




```