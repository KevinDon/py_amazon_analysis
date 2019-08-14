-- 加入统计日期函数
do $$
declare
v_idx integer := 0;
dateFrom date := '2019-01-01'::date;
begin
	DELETE FROM pub_stat_days WHERE date_day >= dateFrom;
  while v_idx <= 365 loop
    insert into pub_stat_days (yr, mo, dy, date_day) values (
			(date_part('year', dateFrom + (v_idx ||' days')::interval)::INTEGER)
			, (date_part('month', dateFrom + (v_idx ||' days')::interval)::INTEGER)
			, (date_part('day', dateFrom + (v_idx ||' days')::interval)::INTEGER)
			, (dateFrom + (v_idx ||' days')::interval)
		);  -- 执行插入
		v_idx = v_idx+1;
  end loop;
end $$;


-- 加入统计月份函数
do $$
declare
v_idx integer := 0;
dateFrom date := '2019-01-01'::date;
begin
	DELETE FROM pub_stat_month WHERE first_day >= dateFrom;
  while v_idx <= 11 loop
    insert into pub_stat_month (yr, mo, first_day, last_day) values (
			(date_part('year', dateFrom + (v_idx ||' months')::interval)::INTEGER)
			, (date_part('month', dateFrom + (v_idx ||' months')::interval)::INTEGER)
			, (dateFrom + (v_idx ||' months')::interval)
			, ((dateFrom + (v_idx+1 ||' months')::interval) + '-1 days' :: INTERVAL)
		);  -- 执行插入
		v_idx = v_idx+1;
  end loop;
end $$;




-- 加入统计周数函数
do $$
declare
v_idx integer := 1;
yearFrom integer := 2019;
begin
-- 	DELETE FROM pub_stat_weeks WHERE yr >= yearFrom;
  while v_idx <= 53 loop
		DELETE FROM pub_stat_weeks WHERE first_day >= (SELECT "public"."f_getMonDateForWeekAndYear"(yearFrom,v_idx));
    insert into pub_stat_weeks (yr, wk, first_day, last_day) values (
			yearFrom
			, v_idx
			, (SELECT "public"."f_getMonDateForWeekAndYear"(yearFrom,v_idx))
			, (SELECT "public"."f_getMonDateForWeekAndYear"(yearFrom,v_idx) + '+6 days' :: INTERVAL)
		);  -- 执行插入
		v_idx = v_idx+1;
  end loop;
end $$;


-- SELECT "public"."f_getMonDateForWeekAndYear"(2019,1)


-- 输入年份、周数，获取本周第一天日期
CREATE OR REPLACE FUNCTION "public"."f_getMonDateForWeekAndYear"("inyear" int4, "inweek" int4)
  RETURNS "pg_catalog"."date" AS $BODY$
declare
    query text;
    monDay Date;
    curDate Date;
    curYear INTEGER;
		
begin
		curYear = date_part('year', CURRENT_DATE);
		curDate = CURRENT_DATE;
		
		if curYear = inyear THEN
			
			query:='SELECT 
				CURRENT_DATE + cast($2 - date_part(''week'', CURRENT_DATE) ||'' weeks'' as interval)
				+ ((-1 * (to_number(
				to_char(CURRENT_DATE + cast($2 - date_part(''week'', CURRENT_DATE) ||'' weeks'' as interval), ''D'')
				, ''99'') - 1)) || '' days'')::interval;';

		else 
			query:='SELECT CURRENT_DATE + cast($1 - date_part(''year'', CURRENT_DATE) ||'' year'' as interval)';
			execute query into curDate using inYear, inWeek; 
			
			query:='SELECT 
				$1 + cast($2 - date_part(''week'', $1) ||'' weeks'' as interval) + ((-1 * (to_number(
				to_char($1 + cast($2 - date_part(''week'', $1) ||'' weeks'' as interval), ''D'')
				, ''99'') - 1)) || '' days'')::interval;';
			
		end if;
    
		
		execute query into monDay using curDate, inWeek; 
    
		return monDay;

end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100
	



-- CREATE OR REPLACE FUNCTION "public"."f_addCountDate"("userDate" text)
--   RETURNS "pg_catalog"."int4" AS $BODY$
-- declare
--     query text;
-- 		v_idx integer := 0;
-- 		dateFrom date;
-- begin
-- 		dateFrom = userDate::date;
-- 		
-- 		DELETE FROM pub_stat_days WHERE date_day >= dateFrom;
-- 		
-- 		while v_idx <= 365 loop
-- 			insert into pub_stat_days (yr, mo, dy, date_day) values (
-- 				(date_part('year', dateFrom + (v_idx ||' days')::interval)::INTEGER)
-- 				, (date_part('month', dateFrom + (v_idx ||' days')::interval)::INTEGER)
-- 				, (date_part('day', dateFrom + (v_idx ||' days')::interval)::INTEGER)
-- 				, (dateFrom + (v_idx ||' days')::interval)
-- 			);  -- 执行插入
-- 			v_idx = v_idx+1;
-- 		end loop;
--     
-- 		return v_idx;
-- end;
-- $BODY$
--   LANGUAGE plpgsql VOLATILE
--   COST 100
-- 	
-- 
-- SELECT "public"."f_addCountDate"('2019-01-01'::text);


