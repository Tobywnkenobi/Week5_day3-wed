--1) List all customers who live in Texas (use JOINs):
--Write a query to retrieve the full list of customers who reside in the state of Texas. Utilize the appropriate JOIN operation to combine the necessary tables.

SELECT CONCAT(first_name,' ',last_name),district
FROM address
JOIN customer
ON customer.address_id = address.address_id
WHERE district = 'Texas';


--2) Get all payments above $6.99 with the Customer's Full Name:
----Create a query that fetches all payment records where the payment amount exceeds $6.99. Additionally, include the full name of the customer associated with each payment

SELECT CONCAT(first_name,' ',last_name), payment.amount
FROM customer
JOIN payment ON customer.customer_id = payment.customer_id
WHERE payment.amount > 6.99;

--3) Show all customer names who have made payments over $175 (use subqueries):
--Construct a query to display the names of customers who have made payments exceeding $175. Employ subqueries to achieve this result.

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
    WHERE amount > 175
);

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
    GROUP BY customer_id
    HAVING SUM(amount) > 175
);


--4) List all customers that live in Nepal (use the city table):
--Formulate a query to list all customers who reside in Nepal. You will need to utilize the city table in your query.

SELECT CONCAT(first_name,' ',last_name),country
FROM country
JOIN city
ON country.country_id=city.country_id
JOIN address
ON city.city_id = address.city_id
JOIN customer
ON address.address_id = customer.address_id
WHERE country = 'Nepal';

--5) Which staff member had the most transactions?
--Write a query to determine the staff member who conducted the highest number of transactions. Consider the appropriate tables for this task.

SELECT staff_id, COUNT(payment_id) as transaction_count
FROM payment
GROUP BY staff_id
ORDER BY transaction_count DESC

--6) How many movies of each rating are there?
--Create a query that counts the number of movies for each distinct rating. Your query should display the rating category along with the corresponding count.

SELECT count(rating),rating
FROM film
GROUP BY rating;

--7) Show all customers who have made a single payment above $6.99 (Use Subqueries):
--Construct a query to retrieve the names of customers who have made only one payment, and the payment amount exceeds $6.99. Utilize subqueries to accomplish this task.

--SELECT CONCAT(first_name,' ', last_name) AS full_name
--FROM customer
--WHERE customer_id IN (
--	SELECT customer_id
--	FROM payment
--	GROUP BY customer_id
--	HAVING count(payment_id) = 1 AND MAX(amount) > 6.99
--);

SELECT CONCAT(first_name,' ',last_name) , amount
from customer
JOIN payment
ON customer.customer_id IN (
SELECT customer.customer_id
FROM payment
WHERE payment.amount > 6.99 );

--8) How many free rentals did our stores give away?
--Write a query to calculate the total number of free rentals given away by our stores.

SELECT count(amount)
FROM payment
WHERE amount = 0

