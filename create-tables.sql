/* =========================
   CREATE DATABASE
========================= */
IF NOT EXISTS (
    SELECT name FROM sys.databases WHERE name = N'CustomerShopping'
)
BEGIN
    CREATE DATABASE CustomerShopping;
END
GO


/* =========================
   USE DATABASE
========================= */
USE CustomerShopping;
GO


/* =========================
   CREATE USER IF NOT EXISTS
========================= */
IF NOT EXISTS (
    SELECT name FROM sys.database_principals
    WHERE name = N'GISELLE-WINDOWS\nghoo'
)
BEGIN
    CREATE USER [GISELLE-WINDOWS\nghoo]
    FOR LOGIN [GISELLE-WINDOWS\nghoo];
END
GO


/* =========================
   ADD USER TO db_owner
========================= */
IF NOT EXISTS (
    SELECT 1
    FROM sys.database_role_members rm
    JOIN sys.database_principals r ON rm.role_principal_id = r.principal_id
    JOIN sys.database_principals u ON rm.member_principal_id = u.principal_id
    WHERE r.name = 'db_owner'
      AND u.name = 'GISELLE-WINDOWS\nghoo'
)
BEGIN
    ALTER ROLE db_owner
    ADD MEMBER [GISELLE-WINDOWS\nghoo];
END
GO


/* =========================
   CREATE TABLE
========================= */
IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'customer_shopping_trends'
)
BEGIN
    CREATE TABLE customer_shopping_trends (
        customer_id INT PRIMARY KEY,
        age INT,
        gender NVARCHAR(10),
        item_purchased NVARCHAR(50),
        category NVARCHAR(50),
        purchase_amount_usd INT,
        location NVARCHAR(50),
        size NVARCHAR(10),
        color NVARCHAR(30),
        season NVARCHAR(20),
        review_rating FLOAT,
        subscription_status NVARCHAR(10),
        payment_method NVARCHAR(50),
        shipping_type NVARCHAR(50),
        discount_applied NVARCHAR(10),
        promo_code_used NVARCHAR(10),
        previous_purchases INT,
        preferred_payment_method NVARCHAR(50),
        frequency_of_purchases NVARCHAR(30)
    );
END
GO


/* =========================
   VERIFY
========================= */
SELECT COUNT(*) AS total_rows
FROM customer_shopping_trends;
GO