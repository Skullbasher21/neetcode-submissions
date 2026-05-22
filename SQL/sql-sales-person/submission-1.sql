WITH salesp AS (
    SELECT sales_id, name FROM sales_person
)
SELECT name FROM salesp
WHERE sales_id NOT IN (
SELECT sales_id FROM company
INNER JOIN orders
    ON company.com_id = orders.com_id
WHERE name = 'CRIMSON')
;