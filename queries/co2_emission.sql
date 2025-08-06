SELECT
     Country,CO2_Emission
FROM world_bank_dataset
WHERE CO2_Emission > 15
ORDER BY CO2_Emission DESC