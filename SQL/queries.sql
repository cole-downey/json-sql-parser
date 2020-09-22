-- Queries File
-- Number of queries: 20
-- Using Database: db908_group16_project2


-- 1.
SELECT * FROM public."Review Final"
ORDER BY review_id ASC LIMIT 100;
-- This command shows the first 100 rows of the Review Final Table
-- First 100 entries on the Review Table?

-- 2.
SELECT Text FROM public."Review Final"
WHERE Stars = '5'
ORDER BY review_id ASC LIMIT 100;
-- This command shows the first 100 rows of the text table entries that have a 5 star rating
-- First 100 5 star reviews?

-- 3.
SELECT Text FROM public."Review Final"
WHERE Stars = '1'
ORDER BY review_id ASC LIMIT 100;
-- This command shows the first 100 rows of the text table entries that have a 1 star rating
-- First 100 1 start reviews?


-- 4.
SELECT * FROM public."Review Final"
WHERE funny = '3'
ORDER BY review_id ASC LIMIT 100;
-- This command shows the first 100 rows of the table entries that have a 3 star rating for the funny column
-- First 100 reviews that received a 3 for funny?


-- 5.
SELECT text,date FROM public."Review Final"
WHERE funny = '3'
ORDER BY review_id ASC LIMIT 100;
-- This command shows the text and date for the first 100 rows which have a 3 star rating for the funny column
-- Just the text and date for the first 100 reviews that got a 3 rating for funny?

-- 6.
SELECT * FROM "Checkin Final" WHERE business_id='-000aQFeK6tqVLndf7xORg'
ORDER BY business_id ASC LIMIT 100;
-- “This command displays the row from the checkin table where the business id is ‘-000aQFeK6tqVLndf7xORg'”
-- THe date of business with id -000aQFeK6tqVLndf7xORg?

-- 7.
SELECT date FROM "Checkin Final" WHERE business_id LIKE '%00%'
ORDER BY business_id ASC LIMIT 100;
-- “This command displays the date objects from business that have a business ID that contain ‘00’”
-- Which business have an id which contain 00?

-- 8.
SELECT review_count FROM "User Final" WHERE name LIKE 'Randy'
ORDER BY user_id ASC LIMIT 100;
-- “This command displays the number of reviews posted by people named Randy”
-- “How many reviews are posted by people named Randy?”

-- 9.
SELECT name FROM "User Final" WHERE yelping_since LIKE '2016%'
ORDER BY user_id ASC LIMIT 100;
-- “This command displays the names of people who have been on yelp since 2016”
-- “Who has been a user since 2016?”

-- 10.
SELECT date FROM public.”Review Final” WHERE stars = 3
ORDER BY review_id ASC LIMIT 10;
-- “This command displays the date of which reviews were left when they only rated 3 stars”
-- “Which days have the most 3 star reviews?”

-- 11.
SELECT text FROM “Review Final” WHERE useful = 5
ORDER BY review_id ASC LIMIT 10;
-- “This command displays the text review from reviews that had 5 useful ratings”
-- “What reviews have been marked useful 5 times?”

-- 12.
SELECT * FROM public."Business Final"
ORDER BY business_id ASC
LIMIT 10;
-- “This command selects the first 10 rows of the business table, ordered by business_id”
-- “What are the first 10 businesses by id?”

-- 13.
SELECT business_id, name, address, city, stars
FROM public."Business Final"
ORDER BY name ASC LIMIT 10;
-- “This command displays business_id, name, address, city, and stars of the first 10 entries, ordered by name”
-- “What are the first 10 businesses by name?”


-- 14.
SELECT business_id, name, address, city, stars, categories
FROM public."Business Final"
WHERE 'Restaurants'=ANY(categories)
ORDER BY name ASC LIMIT 10;
-- “This command finds businesses where one of the categories is ‘restaurants’, and displays 10”
-- “How many businesses are restaurants?”

-- 15.
SELECT business_id, name, address, city, stars
FROM public."Business Final"
WHERE city="Las Vegas"
ORDER BY business_id ASC
LIMIT 10;
-- “This command finds 10 businesses located in las vegas, ordered by business_id”
-- “What businesses are located in Las Vegas?”

-- 16.
SELECT business_id FROM "Review Final" WHERE stars=5
ORDER BY review_id ASC LIMIT 10;
-- “This displays the business ids of business that were rated 5 stars”
-- “What businesses were rated 5 stars?”

-- 17.
SELECT * FROM "Review Final" WHERE business_id='5YvcrqwD4irC_-j-vNC5TA'
ORDER BY review_id ASC LIMIT 1;
-- “Displays the first reviews information from business with ID=’5YvcrqwD4irC_-j-vNC5TA'”
-- “What reviews does a certain business (business_id=5YvcrqwD4irC_-j-vNC5TA) have?”

-- 18.
SELECT name FROM "User Final" WHERE fans > 0
ORDER BY user_id ASC LIMIT 10;
-- “Displays the names of people with more than 0 fans on yelp”
-- “Who has multiple fans on yelp?”

-- 19.
SELECT yelping_since FROM "User Final" WHERE review_count > 200
ORDER BY user_id ASC LIMIT 10;
-- “Displays the date of when people who have more than 200 reviews joined yelp”
-- “When did someone join yelp if they have more than 200 reviews?”

-- 20.
SELECT name, useful, funny, cool FROM "User Final" WHERE review_count > 200
ORDER BY user_id ASC LIMIT 10;
-- “Displays the name and number of useful, funny, and cool ratings for people with more than 200 ratings”
-- “How many ratings do people have who leave more than 200 ratings?”
