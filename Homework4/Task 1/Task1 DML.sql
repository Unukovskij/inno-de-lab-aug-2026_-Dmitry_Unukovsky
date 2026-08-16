--Task1

--action1
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES
	('Danil', 'Kozlov', 'HR', 65000.00)
	('Max', 'Loginov', 'Finance', 71000.00);

--action2
SELECT * FROM Employees;

--action3
SELECT 
	FirstName,
	LastName
FROM Employees
WHERE Department = 'IT';

--action4
UPDATE Employees 
SET Salary = 65000.00
WHERE FirstName = 'Alice' AND LastName = 'Smith';

--action5
DELETE FROM Employees
WHERE FirstName = 'Eve' AND LastName = 'Davis';

--action6
SELECT * FROM Employees;