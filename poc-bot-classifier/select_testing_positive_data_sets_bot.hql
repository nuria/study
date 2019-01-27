use nuria;
-- getting all requests from bots

drop table if exists classifier_testing_data_labeled_bot_all;
create table  classifier_testing_data_labeled_bot_all
AS
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
where agent_type="spider"
and year=2018 and month=09 and day=08
and is_pageview=1 ;


drop table classifier_testing_data_bot_sorted;

 
 create table
    classifier_testing_data_bot_sorted
 as
    select * 
    from classifier_testing_data_labeled_bot_all as A 
    order by A.sessionid,ts limit 10000000 ;





