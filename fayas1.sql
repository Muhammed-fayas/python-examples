use Sakila;
SELECT * FROM customer;
SELECT first_name, last_name, email from customer;
SELECT * FROM film WHERE rating = 'PG-13';
select * from customer c join address ad on c.address_id=ad.address_id join city ci on ad.city_id=ci.city_id ;      
select * from customer c join address ad on c.address_id=ad.address_id join city ci on ad.city_id=ci.city_id
 join country co on ci.country_id=co.country_id where co. country='united states';  
select * from customer c join rental rl on c. customer_id=rl.customer_id;
select * from film where rental_duration>5;

#sorting queries

select *from customer order by last_name ASC;
SELECT * FROM FILM order by rental_rate desc;

# AGGREGATION QUERIES

SELECT COUNT(*) FROM CUSTOMER;    
SELECT SUM(amount) FROM payment; 

#select customer name and flim title

select c.first_name,c.last_name, f.title from customer c join rental r ON c.customer_id= r.customer_id join inventory i ON r.inventory_id= i.inventory_id join film f ON i.film_id= f.film_id;

#select film title and category 

select f .title, c.name from film f inner join film_category fc on f. film_id inner join category c on fc. category_id=c.category_id;

   #subquery queries

select * from customer where customer_id in (select customer_id from rental group by customer_id having count(*)> 10);

select * from  film where rental_rate =(select  max(rental_rate) from film);
select title,rating, rental_duration from film where rental_duration=(select min(rental_duration) from film) and rating='PG';
select rating,count(*)from film group by rating;

#inner join
select c. first_name, c.last_name, f.title from customer c inner join rental r on  c. customer_id= r. customer_id= r.customer_id inner join inventory i on r.inventory_id= i.inventory_id inner join film f on i.film_id = f.film_id;



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

                                                                                                                                                                                                                                                                                                                                                                                                                        