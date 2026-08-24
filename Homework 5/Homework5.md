


--Data warehouse--

**Система бронирования в ресторане**

1. Процесс выполнения заказов
	бизнес-процесс: "Анализ заказов ресторана" 
	Клиент - Заказ - Позиции в заказе - Сотрудник - Столик - Дата/Время
	Интересующие вопросы:
	- Какой средний чек ?
	- Кто из сотрудников приносит больше выручки ?
	- Какие блюда продаются лучше всего?
	- В какие дни и часы происходит пик заказов ?

2. GRAIN 
	Одна запись в факте = одна строка в чеке (одна позиция в заказе)
	Один клиент (source_client_id),
	Один столик (source_table_id),
	Один сотрудник (source_staff_id),
	Один заказ (order_id),
	Один товар (source_menu_id),
	Количество (Quantity),
	Цена на момент заказа (UnitPrice)

3. Dimenshion Tables
	- DimClient (client_sk (PK), source_client_id, first_name, last_name, phone, email, registration_date) - использую для анализа заказов по клиентам, это поможет определить какие клиенты чаще совершают заказы и какую выручку они формируют
	- DimStaff (staff_sk (PK), source_staff_id, first_name, last_name, position, hire_date) - использую для анализа эффективности сотрудников, показывает какие сотрудники больше заказов обслуживает
	- DimMenu (menu_sk (PK), source_menu_id, dish_name, category, price, weight) - использую для анализа популярности блюд, показывает популярность блюд и выручку по отдельным блюдам
	- DimTable (table_sk (PK), source_table_id, table_number, number_of_seats, location (зал)) - использую для анализа заказов в зависимости от столика, где он находится и сколько человек может вместить
	- DimDate (date_sk (PK), full_date, year, month, quarter, day_of_week, is_weekend) - использую для анализа заказов по датам, дням недели, месяцам, кварталам, и определение периодов с наибольшей активностью
	- DimTime (time_sk (PK), hour, minute, part_of_day) - используется для анализа заказов по часам и по деление суток, позволяет определить на какой час приходился пик заказов

4. Fact Tables
	- sales_sk SERIAL (PK) Уникальный ID записи в хранилище
	- order_id INTEGER ID заказа из операционной системы
	- client_sk INTEGER (FK - DimClient) Кто заказал
	- staff_sk INTEGER (FK - DimStaff) Кто обслуживал
	- menu_sk INTEGER (FK - DimMenu) Что заказали
	- table_sk INTEGER (FK - DimTable) За каким столиком
	- date_sk INTEGER (FK - DimDate) Когда был сделан заказ
	- time_sk INTEGER (FK - DimTime) Время заказа
	- Quantity INTEGER Показывает количество проданных порций и используется для популярности блюд
	- UnitPrice DECIMAL(10,2) Цена одной порции на момент заказа, так как цена может изменится 
	- DiscountAmount DECIMAL(10,2) Показывает размер предоставленной скидка (если была) 
	- TotalAmount DECIMAL(10,2) Итоговая сумма, использую для расчета выручки и среднего чека

5. Физическая модель
	Star схема
	![[Pasted image 20260824124319.png]]

6. Аналитические запросы SQL
```sql



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



```



