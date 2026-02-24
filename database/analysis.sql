-- Tổng số khách hàng
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM shopping_trends;

-- Doanh thu theo mùa
SELECT * FROM vw_revenue_by_season
ORDER BY total_revenue DESC;

-- Chi tiêu theo giới tính
SELECT * FROM vw_spending_by_gender
ORDER BY total_spent DESC;

-- Chi tiêu trung bình theo tần suất mua
SELECT
    frequency_of_purchases,
    AVG(purchase_amount_usd) AS avg_spent
FROM shopping_trends
GROUP BY frequency_of_purchases
ORDER BY avg_spent DESC;

-- Khách hàng có subscription vs không
SELECT
    subscription_status,
    AVG(purchase_amount_usd) AS avg_spent
FROM shopping_trends
GROUP BY subscription_status;