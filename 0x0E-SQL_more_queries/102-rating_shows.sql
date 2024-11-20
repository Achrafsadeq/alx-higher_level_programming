-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
-- 'tv_shows' table contains TV show information while 'tv_show_ratings' has ratings
-- INNER JOIN ensures only shows with ratings are included
-- GROUP BY combines all ratings for each show
-- SUM calculates total rating points for each show
-- ORDER BY sorts results by total rating in descending order
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
