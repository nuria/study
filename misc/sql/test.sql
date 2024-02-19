
select 
    page_id as most_viewed_pageview_id,
    page_category,
    total_pageviews_ctn/(select count(*) from website_view_fact),
    total_pageviews_ctn

from (


    select 
        page_id, 
        page_category, 
        rank() over(partition by page_category order by total_pageviews desc ) as pageview_rank,
        sum(total_pageviews) over(partition by page_category) as total_pageviews_ctn
    from (

        select 
        W.page_id, 
        page_category, 
        count(*) as total_pageviews

        from website_view_fact W join page_dimension D on W.page_id = d.page_id group by W.page_id, page_category 

        ) as base_data
    ) as ranked_data
where pageview_rank = 1
;




