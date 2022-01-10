-- Search by most mentioned
select count(*) as num_mentions, stock_id, symbol
from mention join stock on stock.id = mention.stock_id
group by stock_id, symbol order by num_mentions desc;