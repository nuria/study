use nuria;
-- getting all app install id requests from apps

drop table if exists classifier_testing_data_human;
create table  classifier_testing_data_human
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
    agent_type,
    COALESCE(x_analytics_map['wmfuuid'],parse_url(concat('http://bla.org/woo/', uri_query), 'QUERY', 'appInstallID')) as appInstallId

from wmf.webrequest 

where agent_type="user" and access_method="mobile app"
and year=2018 and month=09 and day=08 
and is_pageview=1
and COALESCE(x_analytics_map['wmfuuid'],parse_url(concat('http://bla.org/woo/', uri_query), 'QUERY', 'appInstallID')) is not null;


drop table if exists classifier_testing_data_human_sorted;

create table classifier_testing_data_human_sorted
as 
    select *
    from 
    classifier_testing_data_human
    order by sessionId,ts limit 1000000000;

