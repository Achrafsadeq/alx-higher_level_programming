-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
-- 'tv_genres' contains genre names, 'tv_show_genres' links shows and genres
-- 'tv_show_ratings' contains the rating data for each show
-- First INNER JOIN connects genres with their shows
-- Second INNER JOIN adds the ratings for those shows
-- GROUP BY combines all ratings for each genre
-- SUM calculates total rating points per genre
-- Results sorted by total ratings in descending order
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON s.`genre_id` = g.`id`

       INNER JOIN `tv_show_ratings` AS r
       ON r.`show_id` = s.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
