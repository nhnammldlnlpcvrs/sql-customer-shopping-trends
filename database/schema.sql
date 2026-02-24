USE CustomerShopping;
GO

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
GO