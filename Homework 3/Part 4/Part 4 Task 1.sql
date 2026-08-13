-- Part 4: ORDER BY

-- Task 1
/*Выведите список клиентов, отсортированный по возрасту по убыванию.*/

SELECT 
	first_name,
	age
FROM Customers
ORDER BY age DESC;