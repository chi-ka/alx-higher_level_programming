-- List all shows by their ratings
SELECT tv_shows.title, SUM(tvshows_rate.rating) AS rating_sum
FROM tv_shows
JOIN tvshows_rate ON tv_shows.id = tvshows_rate.show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating_sum DESC;
