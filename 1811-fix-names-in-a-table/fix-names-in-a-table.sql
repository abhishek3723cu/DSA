select user_id, 
concat(upper(lower(left(name,1))),lower(substring(name,2))) as name
from users
group by user_id
order by user_id