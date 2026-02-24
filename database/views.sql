USE CustomerShopping;

-- Doanh thu theo mùa
CREATE VIEW vw_revenue_by_season AS
SELECT
    season,
    SUM(purchase_amount_usd) AS total_revenue
FROM shopping_trends
GROUP BY season;

-- Chi tiêu theo giới tính
CREATE VIEW vw_spending_by_gender AS
SELECT
    gender,
    SUM(purchase_amount_usd) AS total_spent
FROM shopping_trends
GROUP BY gender;