-- Write your query below
SELECT seller_name FROM seller
WHERE seller_id NOT IN (
    SELECT seller_id AS numberoforders FROM orders
    WHERE sale_date >= '2020-01-01' AND sale_date <= '2020-12-31'
    GROUP BY seller_id
)
ORDER BY seller_name
;