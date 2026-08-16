--Task3

--action1
CREATE USER hr_user WITH PASSWORD 'hruser0123';

--action2
GRANT SELECT ON Employees TO hr_user;

--action3
--Test1 должен работать
SELECT * FROM Employees;
--Test2 должен выдать ошибку
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('Test', 'User', 'HR', 50000.00);

--action4
GRANT INSERT, UPDATE ON Employees TO hr_user;

--action5
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('Test', 'User', 'HR', 50000.00);
UPDATE Employees SET Salary = 60000.00 WHERE FirstName = 'Test';