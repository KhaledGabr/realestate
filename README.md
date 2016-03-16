Aim:
Creating a web app for realtors to upload, and manage properties online.

Github:
https://github.com/hostship/realestate






Version 1:



-------------------------------------- 

Database:
A user is the real estate agent that uses the system
Single user can upload multiple properties
A property can contain multiple images

Main Refernces:
https://docs.djangoproject.com/en/dev/topics/db/
https://docs.djangoproject.com/en/dev/ref/models/


1) User
user_id ( Primary Key )
name
username
password




2) Property
property_id ( Primary Key )
user_id (  FOREIGN KEY )

property_name
property_owner
property_description
property_address
property_image

property_price

date_created
date_removed



3) Property image
property_id
property_image_url

-------------------------------------- 






HTML:
1) Login
2) Add property
3) List of properties

CSS:
whatever is needed





Django:

Model : represents layer

View:
-handles http requests
-retreiving data from database
-it may call component from the template layer

Template:









References:
PSD templte from Symu.co ( Liscence is included under PSD template )



Courses I took to accomplish my project

1) Intro to Relational Databases - Udacity 
2) Full Stack Foundations - Udacity 
3) Django Fundemantals - pluralsight
