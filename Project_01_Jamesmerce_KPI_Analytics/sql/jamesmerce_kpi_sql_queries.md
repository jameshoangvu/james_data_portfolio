# Jamesmerce E-commerce KPI SQL Queries

```sql
-- 1. Revenue ($)

-- a. Total Revenue
SELECT SUM(Sales) AS Total_Revenue
FROM dbo.ECData;``` `
![](https://github.com/jameshoangvu/james_data_portfolio/blob/main/Project_01_Jamesmerce_KPI_Analytics/sql/KPI_result_images/Total_Revenue.png?raw=true)
-- b. Revenue by Discount Level
SELECT CONCAT(CAST(Discount * 100 AS INT), '%') AS Discount_Level, 
       SUM(Sales) AS Total_Revenue
FROM dbo.ECData
GROUP BY Discount
ORDER BY Discount;


-- 2. Profit ($)

-- a. Total Profit (Positive Profit + Negative Profit)
SELECT SUM(Profit) AS Total_Profit
FROM dbo.ECData;

-- b. Total Positive Profit
SELECT SUM(Profit) AS Total_Positive_Profit
FROM dbo.ECData
WHERE Profit > 0;

-- c. Total Negative Profit
SELECT SUM(Profit) AS Total_Negative_Profit
FROM dbo.ECData
WHERE Profit < 0;

-- d. Profit by Discount Level
SELECT CONCAT(CAST(Discount * 100 AS INT), '%') AS Discount_Level,
       SUM(Profit) AS Total_Profit
FROM dbo.ECData
GROUP BY Discount
ORDER BY Discount;


-- 3. Profit Ratio

-- a. Overall Profit Ratio
SELECT CONCAT(CAST(ROUND(SUM(Profit) * 1.0 / SUM(Sales) * 100, 2) AS VARCHAR(10)), '%') 
       AS Overall_Profit_Ratio
FROM dbo.ECData;

-- b. Median Profit Ratio
SELECT DISTINCT CONCAT(CAST(ROUND(
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY (Profit) * 1.0 / Sales * 100) OVER(), 2
       ) AS VARCHAR(10)), '%') AS Median_Profit_Ratio
FROM dbo.ECData;

-- c. Profit Ratio by Discount Level
SELECT CONCAT(CAST(Discount * 100 AS INT), '%') AS Discount_Level,
       CONCAT(CAST(ROUND(SUM(Profit) * 1.0 / SUM(Sales) * 100, 2) AS VARCHAR(10)), '%') 
       AS Overall_Profit_Ratio
FROM dbo.ECData
GROUP BY Discount
ORDER BY Discount;


-- 4. Quantity

-- a. Total Quantity
SELECT SUM(Quantity) AS Total_Quantity
FROM dbo.ECData;

-- b. Units Sold by Discount Level
SELECT CONCAT(CAST(Discount * 100 AS VARCHAR(10)), '%') AS Discount_Level, 
       SUM(Quantity) AS Total_Quantity
FROM dbo.ECData
GROUP BY Discount
ORDER BY Discount;


-- 5. Discount

-- a. Total Discount Amount
SELECT ROUND(
       SUM(Sales * Discount / NULLIF(1 - Discount, 0)), 
       2
) AS Total_Discount_Amount
FROM dbo.ECData
ORDER BY Total_Discount_Amount DESC;
