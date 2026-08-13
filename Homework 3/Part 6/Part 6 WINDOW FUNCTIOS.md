
```sql



-- Part 6: WINDOW FUNCTIONS

-- Task 1
/*Для каждого заказа добавьте колонку с суммой всех заказов этого клиента (используя оконную функцию).*/

SELECT 
    order_id,
    customer_id,
    item,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id) AS total_by_customer
FROM Orders
ORDER BY order_id;



```