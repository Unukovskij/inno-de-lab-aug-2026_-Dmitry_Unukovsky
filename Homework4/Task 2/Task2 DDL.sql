--Task2

--action1
CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL, 
Location VARCHAR(50)
);

--action2
ALTER TABLE Employees ADD COLUMN Email VARCHAR(100);

--action3
UPDATE Employees
SET Email = LOWER(FirstName) || '.' || LOWER(LastName) || '@company.com' 
WHERE Email IS NULL;

--action4
ALTER TABLE Employees ADD CONSTRAINT unique_email UNIQUE (Email);

--action5
ALTER TABLE Departments RENAME COLUMN Location TO OfficeLocation;