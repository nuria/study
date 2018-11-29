use nuria;

drop table classifier_data;

-- classifier data is sessionized data of 1 day of webrequest pageviews and eventlogging reqs
create table 
classifier_data
--partitioned by (year, month, day)

as
select 
    rand(1) row_id,
 --   year,
 --   month,
 --   day,
    dt, 
    ts,
    ip,
    lower(uri_host) AS domain,
    -- long user agents are  asign of bot traffic 
    md5(concat(ip, substr(user_agent,0,200), accept_language, uri_host)) AS sessionId,
    http_status,
    uri_path,
    uri_query,
    user_agent,
    x_analytics_map["nocookies"] as nocookies,
    x_analytics_map["WMF-Last-Access-Global"] as last_access,
    access_method,
    agent_type

from wmf.webrequest
where year=2018 and month=09 and day=08
and (is_pageview=1 
or uri_path="/beacon/event" or uri_query like "%action=edit%")

;


-- now sort this data by sessionId so we can compute requests per sec
drop table classifier_data_sorted;

create table 
    classifier_data_sorted 
  --  partitioned by (year, month, day)
as 
    select * from classifier_data order by sessionId,ts limit 1000000000;




