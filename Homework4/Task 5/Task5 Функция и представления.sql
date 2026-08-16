--Task5

--action1
CREATE OR REPLACE FUNCTION CalculateAnnualBonus(emp_id INT, sal DECIMAL)
RETURNS DECIMAL AS $$
BEGIN
    RETURN sal * 0.10;
END;
$$ LANGUAGE plpgsql;

--action2
SELECT 
    EmployeeID,
    FirstName,
    LastName,
    Salary,
    CalculateAnnualBonus(EmployeeID, Salary) AS Bonus
FROM Employees;

--action3
CREATE OR REPLACE VIEW IT_Department_View AS
SELECT 
    EmployeeID,
    FirstName,
    LastName,
    Salary
FROM Employees
WHERE Department = 'IT';

--action4
SELECT * FROM IT_Department_View;