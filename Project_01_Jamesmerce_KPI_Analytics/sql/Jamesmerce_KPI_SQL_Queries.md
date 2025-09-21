# Jamesmerce E-commerce KPI SQL Queries

All KPI SQL queries for Jamesmerce E-commerce using the dbo.ECData table.

```sql
-- 1. Revenue ($)
-- a. Total Revenue
SELECT SUM(Sales) AS Total_Revenue
FROM dbo.ECData;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Total_Revenue.png)

-- b. Revenue by Discount Level
SELECT CONCAT(CAST(Discount * 100 AS INT), '%') AS Discount_Level, 
       SUM(Sales) AS Total_Revenue
FROM dbo.ECData
GROUP BY Discount 
ORDER BY Discount;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Revenue_by_discount_level.png)


-- 2. Profit ($)
-- a. Total Profit (Positive Profit + Negative Profit)
SELECT SUM(Profit) AS Total_Profit
FROM dbo.ECData;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Total_profit.png)

-- b. Total Positive Profit
SELECT SUM(Profit) AS Total_Positive_Profit
FROM dbo.ECData
WHERE Profit > 0;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Total_positive_profit.png 

-- c. Total Negative Profit
SELECT SUM(Profit) AS Total_Negative_Profit
FROM dbo.ECData
WHERE Profit < 0;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Total_negative_profit.png)

-- d. Profit by Discount Level
SELECT CONCAT(CAST(Discount * 100 AS INT), '%') AS Discount_Level,
       SUM(Profit) AS Total_Profit
FROM dbo.ECData
GROUP BY Discount
ORDER BY Discount;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Profit_by_discount_level.png)

-- 3. Profit Ratio
-- a. Overall Profit Ratio
SELECT CONCAT(CAST(ROUND(SUM(Profit) * 1.0 / SUM(Sales) * 100, 2) AS VARCHAR(10)), '%') AS Overall_Profit_Ratio
FROM dbo.ECData;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Overall_Profit_Ratio.png)

-- b. Median Profit Ratio
SELECT DISTINCT CONCAT(CAST(ROUND(PERCENTILE_CONT(0.5)
                WITHIN GROUP (ORDER BY (Profit) * 1.0 / Sales * 100) 
                OVER(), 2) AS VARCHAR(10)), '%') AS Median_Profit_Ratio
FROM dbo.ECData;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Median_profit_ratio.png)

-- c. Profit Ratio by Discount Level
SELECT CONCAT(CAST(Discount * 100 AS INT), '%') AS Discount_Level,
       CONCAT(CAST(ROUND(SUM(Profit) * 1.0 / SUM(Sales) * 100, 2) AS VARCHAR(10)), '%') AS Overall_Profit_Ratio
FROM dbo.ECData
GROUP BY Discount
ORDER BY Discount;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Profit_ratio_by_discount_level.png)

-- 4. Quantity
-- a. Total Quantity
SELECT SUM(Quantity) AS Total_Quantity
FROM dbo.ECData;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Total_quantity.png)

-- b. Units Sold by Discount Level
SELECT CONCAT(CAST(Discount * 100 AS VARCHAR(10)), '%') AS Discount_Level, 
       SUM(Quantity) AS Total_Quantity
FROM dbo.ECData
GROUP BY Discount
ORDER BY Discount;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Quantity_by_discount_level.png)

-- 5. Discount
-- a. Total Discount Amount
SELECT ROUND(
           SUM(Sales * Discount / NULLIF(1 - Discount, 0)), 
           2
       ) AS Total_Discount_Amount
FROM dbo.ECData
ORDER BY Total_Discount_Amount DESC;

![](Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Total_Discount.png)



