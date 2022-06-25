# Write your MySQL query statement below
SELECT
    patient_id, patient_name, conditions
FROM
    Patients
HAVING
    conditions LIKE 'DIAB1%'
OR
    conditions LIKE '% DIAB1%';