use nuria;
-- getting all app install id requests from apps

drop table if exists classifier_training_data_human;
create table  classifier_training_data_human
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
    md5(concat(ip, substr(user_agent,0,200), accept_language, uri_host, COALESCE(x_analytics_map['wmfuuid'],parse_url(concat('http://bla.org/woo/', uri_query), 'QUERY', 'appInstallID')))) AS sessionId,
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
and year=2019 and month=07 and day=01 
and is_pageview=1
and COALESCE(x_analytics_map['wmfuuid'],parse_url(concat('http://bla.org/woo/', uri_query), 'QUERY', 'appInstallID')) is not null limit 1000000000;


drop table if exists classifier_training_data_human_sorted;
drop table if exists classifier_training_data_human_sorted_tmp;
drop table if exists distinct_sessions;

create table classifier_training_data_human_sorted_tmp
as 
    select *
    from 
    classifier_training_data_human
    order by sessionId,ts limit 1000000000;

-- we need a table with 100.000 distinct sessions

create table distinct_sessions as 
    select distinct sessionId from classifier_training_data_human_sorted_tmp limit 100000;

create table classifier_training_data_human_sorted as 
    select * from classifier_training_data_human_sorted_tmp c 
    where c.sessionId in (select sessionId  from distinct_sessions) order by sessionId, ts limit 100000000;

drop table distinct_sessions;
drop table classifier_training_data_human_sorted_tmp;
