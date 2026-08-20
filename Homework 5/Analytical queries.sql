--Analitical queries

--Выручка по дням недели (В какие дни недели ресторан больше зарабатывает)
SELECT 
    DimDate.DayOfWeek,
    COUNT(DISTINCT FactOrders.OrderID) AS OrdersCount,
    SUM(FactOrders.TotalAmount) AS TotalRevenue
FROM FactOrders
JOIN DimDate ON FactOrders.DateID = DimDate.DateID
GROUP BY DimDate.DayOfWeek
ORDER BY TotalRevenue DESC;

--Работа сотрудников (какой сотрудник приносит больше выручки)
SELECT 
    CONCAT(DimStaff.FirstName, ' ', DimStaff.LastName) AS StaffName,
    DimStaff.Position,
    COUNT(DISTINCT FactOrders.OrderID) AS OrdersServed,
    SUM(FactOrders.TotalAmount) AS TotalRevenue
FROM FactOrders
JOIN DimStaff ON FactOrders.StaffID = DimStaff.StaffID
GROUP BY DimStaff.StaffID, DimStaff.FirstName, DimStaff.LastName, DimStaff.Position
ORDER BY TotalRevenue DESC;

--Средний чек по часам (В какое время суток люди больше заказывают)
SELECT 
    DimDate.Hour,
    AVG(FactOrders.TotalAmount) AS AvgCheck,
    COUNT(DISTINCT FactOrders.OrderID) AS OrdersCount
FROM FactOrders
JOIN DimDate ON FactOrders.DateID = DimDate.DateID
GROUP BY DimDate.Hour
ORDER BY AvgCheck DESC;

