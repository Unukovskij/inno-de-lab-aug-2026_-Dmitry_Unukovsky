--Task4

--action1
UPDATE Employees
SET Salary = Salary * 1.1
WHERE Department = 'HR';

--action2
UPDATE Employees
SET Department  = 'Senior IT'
WHERE Salary > 70000.00;

--action3
DELETE FROM Employees
WHERE EmployeeID NOT IN (
    SELECT DISTINCT EmployeeID FROM EmployeeProjects
);

--action4
BEGIN;
INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate) 
VALUES ('AI Development', 250000.00, '2025-01-01', '2025-12-31');
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked) 
VALUES 
(1, (SELECT ProjectID FROM Projects WHERE ProjectName = 'AI Development'), 120),
(2, (SELECT ProjectID FROM Projects WHERE ProjectName = 'AI Development'), 100);
COMMIT;