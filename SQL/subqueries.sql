-- Get all invoices where the unit_price on the invoice_line is greater than $0.99.

SELECT *
FROM invoice_line
WHERE unit_price IN (
  SELECT unit_price FROM invoice_line WHERE unit_price > 0.99
);


-- Get all playlist tracks where the playlist name is Music.

SELECT *
FROM playlist
WHERE playlist_id IN (
  SELECT playlist_id FROM playlist WHERE name = 'Music'
);

-- Get all track names for playlist_id 5.

SELECT *
FROM playlist
WHERE playlist_id IN (
  SELECT playlist_id FROM playlist WHERE playlist_id = 5
);


-- Get all tracks where the genre is Comedy.

SELECT *
FROM genre
WHERE genre_id IN (
  SELECT genre_id from genre where name = 'Comedy' );

-- Get all tracks where the album is Fireball.

SELECT *
FROM album
WHERE title IN (
  SELECT title from album where title = 'Fireball' );

-- Get all tracks for the artist Queen ( 2 nested subqueries ).


SELECT *
FROM artist
WHERE name IN (
  SELECT name from artist where name = 'Queen' );