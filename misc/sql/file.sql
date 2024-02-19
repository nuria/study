create table website_view_fact (
    view_id integer not null,
    page_id integer not null,
    visitor_id integer not null,
    client_platform varchar not null,
    user_agent varchar not null,
    view_utc_ts integer not null,
    view_utc_date integer not null
    

);

create table page_dimension(
    page_id integer not null,
    page_url varchar(512) not null,
    page_name varchar(512) not null,
    page_category varchar(512) not null

);


INSERT into page_dimension values(1, 'home', 'home', 'landing_page');
INSERT into page_dimension values(2, 'detail', 'class1', 'detail_page');
INSERT into page_dimension values(3, 'detail', 'class3', 'detail_page');
INSERT into page_dimension values(4, 'detail', 'class5', 'detail_page');

INSERT into page_dimension values(5, 'search', 'search-de', 'search_page');
INSERT into page_dimension values(6, 'detail', 'class11', 'detail_page');
INSERT into page_dimension values(7, 'detail', 'class31', 'detail_page');
INSERT into page_dimension values(8, 'detail', 'class51', 'detail_page');


INSERT INTO website_view_fact values(1,1, '1000', 'Android', 'chrome', '100', 20240101);
INSERT INTO website_view_fact values(2,1, '1000', 'Android', 'chrome', '101', 20240102);
INSERT INTO website_view_fact values(3,5, '1002', 'IOS', 'chrome', '100', 20240101);
INSERT INTO website_view_fact values(4,5, '1002', 'IOS', 'chrome', '101', 20240102);


INSERT INTO website_view_fact values(5,6, '1000', 'Android', 'chrome', '100', 20240101);
INSERT INTO website_view_fact values(6,6, '1003', 'Android', 'chrome', '101', 20240102);
INSERT INTO website_view_fact values(7,6, '1003', 'IOS', 'chrome', '100', 20240201);
INSERT INTO website_view_fact values(8,6, '1004', 'IOS', 'chrome', '101', 20240202);

INSERT INTO website_view_fact values(9,1, '10004', 'Android', 'chrome', '100', 20240101);
INSERT INTO website_view_fact values(10,1, '1004', 'Android', 'chrome', '101', 20240103);
INSERT INTO website_view_fact values(11,7, '1005', 'desktop', 'chrome', '100', 20240103);
INSERT INTO website_view_fact values(12,8, '1005', 'desktop', 'chrome', '101', 20240103);


INSERT INTO website_view_fact values(21,1, '1010', 'Android', 'chrome', '100', 20240101);
INSERT INTO website_view_fact values(22,1, '1011', 'Android', 'chrome', '101', 20240102);
INSERT INTO website_view_fact values(23,5, '1013', 'IOS', 'chrome', '100', 20240101);
INSERT INTO website_view_fact values(24,5, '1002', 'IOS', 'chrome', '101', 20240102);


INSERT INTO website_view_fact values(25,6, '1010', 'Android', 'chrome', '100', 20240301);
INSERT INTO website_view_fact values(26,6, '1003', 'Android', 'chrome', '101', 20240302);
INSERT INTO website_view_fact values(27,6, '1013', 'IOS', 'chrome', '200', 20240301);
INSERT INTO website_view_fact values(28,6, '1004', 'IOS', 'chrome', '101', 20240202);

INSERT INTO website_view_fact values(29,1, '10004', 'Android', 'chrome', '100', 20240301);
INSERT INTO website_view_fact values(30,1, '1004', 'Android', 'chrome', '101', 20240303);
INSERT INTO website_view_fact values(31,7, '1005', 'desktop', 'chrome', '100', 20240303);
INSERT INTO website_view_fact values(32,8, '1005', 'desktop', 'chrome', '101', 20240303);







--drop table if exists website_view_fact;
--drop table if exists page_dimension;
