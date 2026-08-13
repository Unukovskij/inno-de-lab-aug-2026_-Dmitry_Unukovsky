
```sql



-- Part 1: Where

-- Task 1
/*Найдите всех клиентов из страны 'USA', которым больше 25 лет.*/

SELECT 
	first_name,
	last_name,
	age,
	country
FROM Customers
WHERE country = 'USA'
  AND age > 25;



-- Task 2
/*Выведите все заказы, у которых сумма (amount) больше 1000.*/

SELECT
	order_id,
	item,
	amount,
	customer_id
FROM Orders
WHERE amount > 1000;



```