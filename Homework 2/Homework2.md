# Part 1: Выбор сценария

Для данной работы выбран сценарий:  **Система бронирования в ресторане**: Эта система будет управлять бронированием клиентов, столиками, персоналом и пунктами меню.

# Part 2: Проектирование Базы Данных и документация 

## Идентификация Сущности и Атрибутов 

1. Клиент (Client) 
2. Персонал (Staff)
3. Столик (RTable)
4. Заказ (Orders)
5. Меню (Menu)
6. Состав заказа (OrderItem) - связь заказов с блюдами 
7. Бронирование (Reservation)

## Проектирование Таблиц: 

1. Table Name: Client
	- Description: Хранит информацию о клиентах ресторана. 
	- Attributes: 
	    - `ClientID`: PK, NOT NULL, UNIQUE
	    - `FirstName`: VARCHAR(100), NOT NULL
	    - `LastName`: VARCHAR(100), NOT NULL
	    - `PhoneNumber`: VARCHAR(20), NOT NULL, UNIQUE
	- **Constraints:**
	    - `PK_Client`: PRIMARY KEY (ClientID)
	    - `UQ_Client_Phone`: UNIQUE (PhoneNumber)
2. Table Name: Staff
	- Description: Хранит информацию о сотрудниках ресторана.
	- Attributes: 
	    - `StaffID`: PK, NOT NULL, UNIQUE
	    - `Position`: VARCHAR(100), NOT NULL
	    - `FirstName`: VARCHAR(100), NOT NULL
	    - `LastName`: VARCHAR(100), NOT NULL
	    - `PhoneNumber`: VARCHAR(20), NOT NULL, UNIQUE
	- **Constraints:**
	    - `PK_Staff`: PRIMARY KEY (StaffID)
	    - `UQ_Staff_Phone`: UNIQUE (PhoneNumber)
	    - `CHK_Position`: CHECK (Position IN ('Официант', 'Повар', 'Администратор', 'Менеджер'))
3. Table Name: RTable
	- Description: Хранит информацию о столиках в ресторане.
	- Attributes: 
	    - `RTableID`: PK, NOT NULL, UNIQUE
	    - `TableNumber`: INTEGER, NOT NULL, UNIQUE 
	    - `NumberOfSeats`: INTEGER, NOT NULL
	    - `Status`: VARCHAR(50), NOT NULL, DEFAULT 'Свободен' 
	- **Constraints:**
	    - `PK_RTable`: PRIMARY KEY (RTableID)
	    - `UQ_TableNumber`: UNIQUE (TableNumber)
	    - `CHK_Seats`: CHECK (NumberOfSeats > 0 AND NumberOfSeats <= 10)
	    - `CHK_RTableStatus`: CHECK (Status IN ('Свободен', 'Занят', 'Забронирован'))
4. Table Name: Orders
	- Description: Хранит информацию о заказах клиентов.
	- Attributes: 
	    - `OrdersID`: PK, NOT NULL, UNIQUE
	    - `ClientID`: INTEGER, FK (REFERENCES Client), NOT NULL
	    - `StaffID`: INTEGER, FK (REFERENCES Staff)
	    - `RTableID`: INTEGER, FK (REFERENCES RTable), NOT NULL
	    - `OrderDateTime`: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP
	    - `Status`: VARCHAR(50), NOT NULL, DEFAULT 'Активен'
	    - `TotalAmount`: DECIMAL(10,2), DEFAULT 0.00
	- **Constraints:**
	    - `PK_Orders`: PRIMARY KEY (OrdersID)
	    - `FK_Orders_Client`: FOREIGN KEY (ClientID) REFERENCES Client(ClientID)
	    - `FK_Orders_Staff`: FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
	    - `FK_Orders_RTable`: FOREIGN KEY (RTableID) REFERENCES RTable(RTableID)
	    - `CHK_OrderStatus`: CHECK (Status IN ('Активен', 'В процессе', 'Оплачен', 'Отменен'))
	    - `CHK_TotalAmount`: CHECK (TotalAmount >= 0)
5. Table Name: Menu
	- Description: Содержит информацию о блюдах и напитках в меню.
	- Attributes: 
	    - `MenuID`: PK, NOT NULL, UNIQUE
	    - `DishName`: VARCHAR(255), NOT NULL
	    - `Category`: VARCHAR(100), NOT NULL
	    - `Price`: DECIMAL(10,2), NOT NULL
	    - `Weight`: INTEGER 
	- **Constraints:**
	    - `PK_Menu`: PRIMARY KEY (MenuID)
	    - `CHK_Price`: CHECK (Price >= 0)
	    - `CHK_Weight`: CHECK (Weight > 0)
6. Table Name: OrderItem
	- Description: Связывает заказы и блюда из меню.
	- Attributes: 
	    - `OrderItemID`: PK, NOT NULL, UNIQUE
	    - `OrdersID`: INTEGER, FK (REFERENCES Orders), NOT NULL
	    - `MenuID`: INTEGER, FK (REFERENCES Menu), NOT NULL
	    - `Quantity`: INTEGER, NOT NULL
	    - `PriceAtOrderTime`: DECIMAL(10,2), NOT NULL
	- **Constraints:**
	    - `PK_OrderItem`: PRIMARY KEY (OrderItemID)
	    - `FK_OrderItem_Orders`: FOREIGN KEY (OrdersID) REFERENCES Orders(OrdersID)
	    - `FK_OrderItem_Menu`: FOREIGN KEY (MenuID) REFERENCES Menu(MenuID)
	    - `CHK_Quantity`: CHECK (Quantity > 0)
	    - `CHK_PriceAtOrderTime`: CHECK (PriceAtOrderTime >= 0)
7. Table Name: Reservation
	- Description: Хранит информацию о бронированиях столиков клиентами.
	- Attributes: 
	    - `ReservationID`: PK, NOT NULL, UNIQUE
	    - `ClientID`: INTEGER, FK (REFERENCES Client), NOT NULL
	    - `RTableID`: INTEGER, FK (REFERENCES RTable), NOT NULL
	    - `ReservationDateTime`: TIMESTAMP, NOT NULL
	    - `NumberOfGuests`: INTEGER, NOT NULL
	    - `Status`: VARCHAR(50), NOT NULL, DEFAULT 'Активно'
	- **Constraints:**
	    - `PK_Reservation`: PRIMARY KEY (ReservationID)
	    - `FK_Reservation_Client`: FOREIGN KEY (ClientID) REFERENCES Client(ClientID)
	    - `FK_Reservation_RTable`: FOREIGN KEY (RTableID) REFERENCES RTable(RTableID)
	    - `CHK_Guests`: CHECK (NumberOfGuests > 0)
	    - `CHK_ReservationStatus`: CHECK (Status IN ('Активно', 'Подтверждено', 'Отменено', 'Завершено'))

## Взаимосвязи: 

1. **Client и Reservation (Один-ко-Многим):**
    - Один клиент может иметь множество бронирований. Но каждое бронирование относится к одному клиенту.
    - `Reservation.ClientID` является внешним ключом, ссылающимся на `Client.ClientID`
2. **RTable и Reservation (Один-ко-Многим):**
    - Один столик может быть забронирован множество раз. Но каждое бронирование относится к одному столику.
    - `Reservation.RTableID` является внешним ключом, ссылающимся на `RTable.RTableID`
3. **Client и Orders (Один-ко-Многим):**
    - Один клиент может сделать множество заказов. Но каждый заказ принадлежит одному клиенту.
    - `Orders.ClientID` является внешним ключом, ссылающимся на `Client.ClientID`
4. **Staff и Orders (Один-ко-Многим):**
    - Один сотрудник может обслуживать множество заказов. Но каждый заказ может обслуживаться одним сотрудником.
    - `Orders.StaffID` является внешним ключом, ссылающимся на `Staff.StaffID`
5. **RTable и Order (Один-ко-Многим):**
    - Один столик может использоваться для множества заказов. Но каждый заказ привязан к одному столику.
    - `Orders.RTableID` является внешним ключом, ссылающимся на `RTable.RTableID`
6. **Order и Menu (Многие-ко-Многим):**
    - Один заказ может содержать множество блюд.  одно блюдо может быть заказано во множестве заказов.
    - Реализовано через промежуточную таблицу `OrderItem`.
    - `OrderItem.OrdersID` является внешним ключом, ссылающимся на `Orders.OrdersID`
    - `OrderItem.MenuID` является внешним ключом, ссылающимся на `Menu.MenuID`
