# Write your MySQL query statement below
select product_name, year , price from Product join sales where sales.product_id=product.product_id