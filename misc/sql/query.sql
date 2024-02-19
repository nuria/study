
with base_data as (

select count(*) as total_pageviews, page_id 
from website_view_fact 
where view_utc_date > 20240101
group by page_id
)

select * from base_data where total_pageviews > 1;


/*
page_category_agg , data for the last 30 days


page_category 
total_page_view_count: total pageviews per category
total_page_view_pct: share of pageviews seen in this category 
most_viewed_category_page_id

snapshot_date
*/


-- need to first get all pageviews per category 
-- also and separate get max-page_id per category 


/**
This has to be done in two steps
calculate per day , per category
* page_category pageviews
* page_id pageviews
**/

select * from website_view_fact order by page_id;


with base_data as (
    select 
        page_category,
        W.page_id,
        count(*) pageviews_per_page_id_category,
        '20230301' as snapshot_date
from website_view_fact as W join page_dimension as P on W.page_id = P.page_id
group by W.page_id, page_category

),

max_values_page as (
    select 
    rank() over (partition by page_category order by pageviews_per_page_id_category desc ) as view_rank,
    page_id,
    page_category,
    '20230301' as snapshot_date
    from base_data

),

max_values_category as (
    select
    page_category, 
    sum(pageviews_per_page_id_category) pageviews_per_category
    from base_data
    group by page_category
),

total_pageviews as (
select count(*) as total_pageviews from website_view_fact
)


select  
P.page_category,
C.pageviews_per_category,
P.page_id as top_page_per_category,
total_pageviews,
(C.pageviews_per_category/total_pageviews)*  100  as pct

from max_values_category C 
    join max_values_page P on C.page_category = P.page_category , total_pageviews
where P.view_rank = 1;



