# Jamesmerce E-commerce KPI DAX Formulas

This document contains all DAX formulas for Jamesmerce KPI dashboard, with a complete structure for each KPI including a. Total, b. Month-over-Month (MoM), and c. Year-over-Year (YoY).

```DAX
-- 1. Total Revenue
a. Total Revenue
Total Revenue = SUM(ecommerce_sales[Sales])

b. Revenue Trend Month-over-Month
Vs Last Month (Re) = 
VAR _CM = [Total Revenue]
VAR _PM = CALCULATE([Total Revenue], PARALLELPERIOD('DateTable'[Date], -1, MONTH))
VAR _perc = DIVIDE(_CM - _PM, _PM)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)

c. Revenue Trend Year-over-Year
Vs Last Year (Re) = 
VAR _CM = [Total Revenue]
VAR _PY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('DateTable'[Date]))
VAR _perc = DIVIDE(_CM - _PY, _PY)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)

-- 2. Total Profit
a. Total Profit
Total Profit = SUM(ecommerce_sales[Profit])

b. Profit Trend Month-over-Month
Vs Last Month (Pro) = 
VAR _CM = [Total Profit]
VAR _PM = CALCULATE([Total Profit], PARALLELPERIOD('DateTable'[Date], -1, MONTH))
VAR _perc = DIVIDE(_CM - _PM, _PM)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)

c. Profit Trend Year-over-Year
Vs Last Year (Pro) = 
VAR _CM = [Total Profit]
VAR _PY = CALCULATE([Total Profit], SAMEPERIODLASTYEAR('DateTable'[Date]))
VAR _perc = DIVIDE(_CM - _PY, _PY)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)

-- 3. Quantity
a. Total Quantity
Total Quantity = COALESCE(SUM(ecommerce_sales[Quantity]), 0)

b. Quantity Trend Month-over-Month
Vs Last Month (Quan) = 
VAR _CM = [Total Quantity]
VAR _PM = CALCULATE([Total Quantity], PARALLELPERIOD('DateTable'[Date], -1, MONTH))
VAR _perc = DIVIDE(_CM - _PM, _PM)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)

c. Quantity Trend Year-over-Year
Vs Last Year (Quan) = 
VAR _CM = [Total Quantity]
VAR _PY = CALCULATE([Total Quantity], SAMEPERIODLASTYEAR('DateTable'[Date]))
VAR _perc = DIVIDE(_CM - _PY, _PY)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)

-- 4. Overall Profit Ratio
a. Overall Profit Ratio
Overall Profit Ratio = DIVIDE([Total Profit], [Total Revenue], 0)

b. Overall Profit Ratio MoM
Vs Last Month (OPR) = 
VAR _CM = [Overall Profit Ratio]
VAR _PM = CALCULATE([Overall Profit Ratio], PARALLELPERIOD('DateTable'[Date], -1, MONTH))
VAR _perc = DIVIDE(_CM - _PM, _PM)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)

c. Overall Profit Ratio YoY
Vs Last Year (OPR) = 
VAR _CM = [Overall Profit Ratio]
VAR _PY = CALCULATE([Overall Profit Ratio], SAMEPERIODLASTYEAR('DateTable'[Date]))
VAR _perc = DIVIDE(_CM - _PY, _PY)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)

-- 5. Total Discount ($)
a. Total Discount
Total Discount = COALESCE(SUMX(ecommerce_sales, ecommerce_sales[Sales] * DIVIDE(ecommerce_sales[Discount], 1 - ecommerce_sales[Discount], 0)), 0)

b. Total Discount MoM
Vs Last Month (Tdis) = 
VAR _CM = [Total Discount]
VAR _PM = CALCULATE([Total Discount], PARALLELPERIOD('DateTable'[Date], -1, MONTH))
VAR _perc = DIVIDE(_CM - _PM, _PM)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)

c. Total Discount YoY
Vs Last Year (Tdis) = 
VAR _CM = [Total Discount]
VAR _PY = CALCULATE([Total Discount], SAMEPERIODLASTYEAR('DateTable'[Date]))
VAR _perc = DIVIDE(_CM - _PY, _PY)
RETURN SWITCH(TRUE(),
    _perc > 0, UNICHAR(11165) & " " & FORMAT(_perc, "0.0%"),
    _perc < 0, UNICHAR(11167) & " " & FORMAT(-_perc, "0.0%"),
    FORMAT(_perc, "0.0%")
)
```
