select p.product_name, sum(o.unit) as unit  from products p join
orders o on
p.product_id=o.product_id
WHERE o.order_date >= '2020-02-01' AND o.order_date <= '2020-02-29' 
group by p.product_name
having sum(o.unit)>=100
