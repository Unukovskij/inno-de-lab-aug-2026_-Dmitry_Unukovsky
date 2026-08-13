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