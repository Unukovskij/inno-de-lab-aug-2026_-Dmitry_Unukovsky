


--Data warehouse--

**Система бронирования в ресторане**

1. Процесс выполнения заказов
	Клиент бронирует столик, приходит, делает заказ, после оплачивает.
	Клиент - Бронирует - Приходит - заказывает - оплачивает

2. GRAIN = одна запись в чеке
	Один клиент(CkientID), Один столик(TableID), Один сотрудник(StaffID), Один заказ(OrderID), Один товар(MenuID), Количество (Quantity), Цена на момент заказа (PriceAtOrderTime)

3. Dimenshion Tables
	- DimClient (ClientKey (PK), ClientID, FirstName, LastName, Phone, Email, RegistrationDate)
	- DimStaff (StaffKey (PK), StaffID, FirstName, LastName, Position, HireDate)
	- DimMenu (MenuKey (PK), MenuID, DishName, Category, Price, Weight)
	- DimTable (TableKey (PK), RTableID, TableNumber, NumberOfSeats, Location (зал))
	- DimDate (DateKey (PK), FullDate, Year, Month, Quarter, DayOfWeek, IsWeekend, Hour)

4. Fact Tables
	- sales_sk SERIAL (PK) Уникальный ID записи в хранилище
	- client_sk INTEGER (FK - DimClient) Кто заказал
	- staff_sk INTEGER (FK - DimStaff) Кто обслуживал
	- menu_sk INTEGER (FK - DimMenu) Что заказали
	- table_sk INTEGER (FK - DimTable) За каким столиком
	- date_sk INTEGER (FK - DimDate) Когда был сделан заказ
	- Quantity INTEGER Количество порций
	- UnitPrice DECIMAL(10,2) Цена одной порции на момент заказа
	- DiscountAmount DECIMAL(10,2) Скидка (если была)
	- TotalAmount DECIMAL(10,2) Итоговая сумма (Quantity × UnitPrice - DiscountAmount)

5. Физическая модель
	Star схема
	![[Pasted image 20260820215609.png]]

6. Аналитические запросы SQL
```sql



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


```
