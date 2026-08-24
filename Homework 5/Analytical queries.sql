--Analitical queries

/*Average customer check. 
Question: What is the average customer check?*/
SELECT 
    AVG(OrderTotals.OrderTotal) AS AverageCheck
FROM (
    SELECT
        FactOrders.order_id,
        SUM(FactOrders.total_amount) AS OrderTotal
    FROM FactOrders
    GROUP BY FactOrders.order_id
) AS OrderTotals;


/*Employee performance.
Question: Which employee generates the highest revenue?*/
SELECT 
    CONCAT(DimStaff.first_name, ' ', DimStaff.last_name) AS StaffName,
    DimStaff.position,
    COUNT(DISTINCT FactOrders.order_id) AS OrdersServed,
    SUM(FactOrders.total_amount) AS TotalRevenue
FROM FactOrders
JOIN DimStaff ON FactOrders.staff_sk = DimStaff.staff_sk
GROUP BY 
    DimStaff.staff_sk,
    DimStaff.first_name,
    DimStaff.last_name,
    DimStaff.position
ORDER BY TotalRevenue DESC;


/*Dish popularity.
Question: Which dishes are sold most frequently?*/

SELECT 
    DimMenu.dish_name AS DishName,
    DimMenu.category AS Category,
    SUM(FactOrders.quantity) AS QuantitySold,
    SUM(FactOrders.total_amount) AS TotalRevenue
FROM FactOrders
JOIN DimMenu  ON FactOrders.menu_sk = DimMenu.menu_sk
GROUP BY 
    DimMenu.menu_sk,
    DimMenu.dish_name,
    DimMenu.category
ORDER BY QuantitySold DESC;


/*Peak order periods.
Question: On which days and at which hours is the number of orders the highest?*/
SELECT 
    DimDate.day_of_week AS DayOfWeek,
    DimTime.hour AS Hour,
    COUNT(DISTINCT FactOrders.order_id) AS OrdersCount,
    SUM(FactOrders.total_amount) AS TotalRevenue
FROM FactOrders
JOIN DimDate ON FactOrders.date_sk = DimDate.date_sk
JOIN DimTime ON FactOrders.time_sk = DimTime.time_sk
GROUP BY 
    DimDate.day_of_week,
    DimTime.hour
ORDER BY OrdersCount DESC;
