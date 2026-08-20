--Task6

--action1
SELECT DISTINCT Projects.ProjectName
FROM Projects
JOIN EmployeeProjects ON Projects.ProjectID = EmployeeProjects.ProjectID
JOIN Employees ON EmployeeProjects.EmployeeID = Employees.EmployeeID
WHERE Employees.FirstName = 'Bob' 
  AND Employees.LastName = 'Johnson' 
  AND EmployeeProjects.HoursWorked > 150;

--action2

--добавил тестового сотрудника на проект, я понял почему не надо привязываться к конекретному ID, но я для дз так сделал ибо знал что он точно есть
insert into EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
values (10,(select ProjectID from Projects where ProjectName = 'Website Redesign'),100);


--Исправил
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT 
    (SELECT EmployeeID FROM Employees WHERE FirstName = 'Test' AND LastName = 'User'),
    (SELECT ProjectID FROM Projects WHERE ProjectName = 'Website Redesign'),100
WHERE EXISTS (
    SELECT 1 FROM Employees WHERE FirstName = 'Test' AND LastName = 'User'
);


--увеличение budget на 10 процентов
UPDATE Projects
SET Budget = Budget * 1.10
WHERE EXISTS (
    SELECT 1
    FROM EmployeeProjects
    JOIN Employees ON EmployeeProjects.EmployeeID = Employees.EmployeeID
    WHERE EmployeeProjects.ProjectID = Projects.ProjectID 
      AND Employees.Department = 'IT'
);

--action3

--создаю тестовый проект без EndDate
INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
VALUES ('Test Project No End Date', 50000.00, '2025-01-01', NULL);

UPDATE Projects
SET EndDate = StartDate + INTERVAL '1 year'
WHERE EndDate IS NULL;

--action4
BEGIN;

--Исправил
WITH new_employee AS (
INSERT INTO Employees (FirstName, LastName, Department, Salary, Email)
VALUES ('Olga', 'Sokolova', 'Marketing', 50000.00, 'olga.sokolova@company.com')
RETURNING EmployeeID
)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT 
    EmployeeID,
    (SELECT ProjectID FROM Projects WHERE ProjectName = 'Website Redesign'),80
FROM new_employee;
COMMIT;

-- Проверка
SELECT * FROM Employees;
SELECT * FROM Projects;
SELECT * FROM EmployeeProjects;
