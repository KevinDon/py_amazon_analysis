CREATE VIEW "public"."view_i_auth_user_profile" AS  SELECT u.id,
    u.username,
    u.is_active,
    profile.nick,
    profile.ding_talk_account,
    gps.group_id,
    gps.group_name,
    department.id AS dep_id,
    department.name AS dep_name
   FROM (((auth_user u
     LEFT JOIN auth_user_profile profile ON ((u.id = profile.user_id)))
     LEFT JOIN ( SELECT ug.user_id,
            ug.group_id,
            gp.name AS group_name
           FROM (auth_user_groups ug
             LEFT JOIN auth_group gp ON ((gp.id = ug.group_id)))) gps ON ((gps.user_id = u.id)))
     LEFT JOIN auth_department department ON ((department.id = profile.department_id)));
