-- List shows by rating sum
SELECT tv_shows.title, SUM(tv_shows_rates.rate) AS rating
FROM tv_shows
JOIN tv_shows_rates ON tv_shows.id = tv_shows_rates.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
