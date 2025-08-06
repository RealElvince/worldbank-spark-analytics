SELECT Year,ROUND(AVG(Unemployment_Rate),2) AS avg_unemployment_rate
    FROM world_bank_dataset
    GROUP BY Year
    ORDER BY Year