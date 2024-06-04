![readme-cover](https://github.com/0davidog/VideoDrome/assets/135815736/5fead196-6380-4d72-a4be-891aa77b7356)

# VideoDrome

<em>"Explore a vast collection of new and used DVDs, Blu-rays, and 4k Ultra HD films spanning the realms of horror, sci-fi, thriller and classic cinema. From cult favorites to timeless classics, find your next movie obsession at our online store today."</em>

VideoDrome is an ecommerce website dedicated to the sale of genre, cult and classic films on physical media such as blu-ray, DVD or UHD.

## Live Site

The live app is hosted on the Heroku platform. More details on how the project was deployed can be found below [here](#deployment).

[Heroku Link](https://videodrome-ff881eaa1b51.herokuapp.com/)

## Repo

The project's code and file repository is hosted by Github. More details on cloning or forking the repository can be found [here](#fork-and-clone-the-repository).

[Github link](https://github.com/0davidog/VideoDrome)

## Author

David C. O'Gara

## Table of Contents

- [VideoDrome](#videodrome)
  - [Live Site](#live-site)
  - [Repo](#repo)
  - [Author](#author)
- [Table of Contents](#table-of-contents)
  - [Agile Process](#agile-process)
    - [User Stories](#user-stories)
    - [Project Backlog](#project-backlog)
    - [Iteration 01 – Due 05/03/2024](#iteration-01--due-04062024)
- [UX](#ux)
  - [Project Goal](#project-goal)
  - [Target Audience](#target-audience)
  - [Wireframes](#wireframes)
  - [Information Architecture](#information-architecture)
  - [Design Choices](#design-choices)
  - [E-Commerce Business model](#e-commerce-business-model)
  - [Features](#features)
  - [Testing](#testing)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
  - [Deployment](#deployment)
    - [Prerequisites](#prerequisites)
      - [Heroku Postgres Database](#heroku-postgres-database)
      - [Create Superuser](#create-superuser)
      - [Cloudinary](#cloudinary)
    - [Fork and Clone the Repository](#fork-and-clone-the-repository)
    - [Local Deployment](#local-deployment)
    - [Production Deployment](#production-deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgments](#acknowledgments)

## Agile Process

This project is to be made using Agile develpment pricipals to plan and complete the work to a minimum viable product. This involves seperating the work in to a project back log of user stories in which an iteration of the project (MVP) must be achieved by project deadline.

### User Stories

Following Agile development practice this project has been divided into user stories to give a clear understanding of the project needs, goals and features and to split the work in to small achievable sets of tasks.

[User Stories on Github](https://github.com/users/0davidog/projects/4)
    
Here is a list of user stories for this project seperated in to their relative Epics. Each story links to its place on Github where you can view:

- User Story
- Acceptance criteria
- MSCW prioritisation label
- Linked iteration
- Linked project board.
    
Epic: User Registration and Authentication

- [As a new user, I want to be able to register an account on the website using my email address and password.](https://github.com/0davidog/VideoDrome/issues/1)
- [As a registered user, I want to be able to log in to my account securely so that I can shop easily with my saved information.](https://github.com/0davidog/VideoDrome/issues/2)
- [As a Site user, I want the option to reset my password in case I forget it, ensuring secure access to my account.](https://github.com/0davidog/VideoDrome/issues/3)

Epic: Product Browsing and Searching

- [As a Site User, I want a user-friendly navigation menu that helps me explore different sections of the site easily.](https://github.com/0davidog/VideoDrome/issues/32)
- [As a user, I want to be able to browse products by category so that I can better find the kind of products I'm interested in.](https://github.com/0davidog/VideoDrome/issues/4)
- [As a user, I want to be able to search for products by name or keyword so that I can find a particular product I'm interested in.](https://github.com/0davidog/VideoDrome/issues/5)
- [As a user, I want to be able to order products by price or release date, so I can browse in mind of the cheapest or newest items.](https://github.com/0davidog/VideoDrome/issues/14)

Epic: Product Detail and Reviews

- [As a shopper, I want to view detailed information about a product, including images, descriptions, and specifications so that I can be better informed about my purchases.](https://github.com/0davidog/VideoDrome/issues/6)
- [As a shopper, I want to be able to read reviews for a product so that I can be better informed before making a purchase decision.](https://github.com/0davidog/VideoDrome/issues/7)
- [As a registered site user, I would like to leave a review on a product I have already purchased so that I might help others be informed.](https://github.com/0davidog/VideoDrome/issues/33)
- [As a registered site-user, I want to be able to add a product to my wishlist so that I can easily return to a product I want to purchase at a more convenient time.](https://github.com/0davidog/VideoDrome/issues/8)
- [As a registered site-user, I can give a star rating to a product so that I can express my view on product quality without writing a review.](https://github.com/0davidog/VideoDrome/issues/12)

Epic: Shopping Cart and Checkout

- [As a shopper, I want to be able to add items to my shopping basket so that I can purchase multiple products in one transaction.](https://github.com/0davidog/VideoDrome/issues/9)
- [As a shopper, I want to be able to view and edit the contents of my shopping cart before proceeding to checkout so that I can be sure of my final purchase decision.](https://github.com/0davidog/VideoDrome/issues/10)
- [As a shopper, I want to be able to securely check out and provide shipping and payment information so that I may purchase items with ease and confidence.](https://github.com/0davidog/VideoDrome/issues/15)

Epic: Order Management

- [As a shopper, I want to be able to track the status of my orders, so I can be confident my order is handled and shipped in good time.](https://github.com/0davidog/VideoDrome/issues/26)(future feature)
- [As a shopper, I want to be able to view my order history so that I access the information for my records or a query.](https://github.com/0davidog/VideoDrome/issues/25)

Epic: Audience Reach and Search Engine optimisation.

- [As a site-owner, I want to include a site-map to ensure better site navigation and search engine optimisation](https://github.com/0davidog/VideoDrome/issues/17)
- [As a site owner, I want to Include Meta Description tags in the application HTML so that I can improve search engine optimisation](https://github.com/0davidog/VideoDrome/issues/18)
- [As a site-owner, I want to include a robots.txt file in my site so that I can control search engine bot crawling, preserve bandwidth and protect sensitive data.](https://github.com/0davidog/VideoDrome/issues/22)
- [As a site-owner, I want to include a newsletter sign up option, so that I can reach my audience with news and offers in a cost-effective manner.](https://github.com/0davidog/VideoDrome/issues/31)
- [As a site-owner, I want to include a 404 response page with an appropriate redirect for attempted access to non-existent content so that users who stumble on such errors are not put off from browsing.](https://github.com/0davidog/VideoDrome/issues/23)

Epic: User Accessibility

- [As a Site User with accessibility needs, I want the website to be accessible, with features like ALT text for images and keyboard navigation, to ensure a positive experience for all users.](https://github.com/0davidog/VideoDrome/issues/27)

Epic: Database Managment & Administration

- [As a site-admin I want to be able to add a product without the admin panel so that my work flow can stay oriented to the site.](https://github.com/0davidog/VideoDrome/issues/28)
- [As a site-admin I want to be able to edit a product without the admin panel so that my work flow can stay oriented to the site.](https://github.com/0davidog/VideoDrome/issues/29)
- [As a site-admin I want to be able to edit a product without the admin panel so that my work flow can stay oriented to the site.](https://github.com/0davidog/VideoDrome/issues/30)

### Project Backlog

Due to the small scope of this project, having a project backlog and seperate iterations didn't seem neccessary as their would only be one project to client hand-over. It was instead decided to keep all the user stories in the one project iteration list. A project backlog milestone was created however on github to follow agile practice.

[Project Backlog](https://github.com/0davidog/VideoDrome/milestone/2)

### Iteration 01 – Due 04/06/2024

[Iteration on Github](https://github.com/0davidog/VideoDrome/milestone/1)

As this is an accedemic porfolio project there is only one interation in which this project will be developed and tested. That being the project start date to it's hand-in date by which all its must-have deliverables are to be achieved.

## UX

### Project Goal

The project goal is a site that allows for the browsing and purchase of physical media items in the form of DVD, Blu-ray and 4k Ultra HD disks. 

### Target Audience

The target audience will be enthusiasts of genre and cult cinema, physical media collectors. Due to the content of many of these films the largest target audience would likely be 15 and up in keeping with film certification laws. An older audience would be more likely to be shopping for physical media due to a sense of nostalgia and not having been raised with streaming services and digital media purchases.

### Wireframes

Wireframes were created using Balsamiq to design the general look of the sites main features.

#### Landing Page Displaying All Products:

![Home](https://github.com/0davidog/VideoDrome/assets/135815736/70922b57-666d-4ca8-8a6f-9a7108ddcd37)

#### Product Detail Page:

![Product](https://github.com/0davidog/VideoDrome/assets/135815736/51bf13ad-1905-49fb-8bf0-061d2c677c3b)

#### Basket View:

![Basket](https://github.com/0davidog/VideoDrome/assets/135815736/eb8e798a-de3b-4c6f-99c0-b5ed9bf38931)

## Information Architecture

### Database Choice

The project uses the PostgreSQL database installed and managed through the Heroku Postgres service and the Psycopg2 database adapter for use with Python and Django. This is chosen as the project requires a relational database for interactivity between models.

### Full ERD

The diagram displayed here shows the relationship between the database models used in the project.

![VideoDrome ERD](https://github.com/0davidog/VideoDrome/assets/135815736/86878f91-8482-4475-ac26-b09e5ab3c676)


- The Video model is connected to the Language, Subtitle, Region, Genre and user models all as Many To Many fields. These represent the multiple attributes different videos can have and whether or not as user has added it to their wishlist.
- The UserRating model connects to the Video model and User model as Foreign Keys, representing subject and author respectively.
- The UserReview model also connects to bothe the Video and User models as Foreign Keys also representing the subject and author.
- The CustomerOrder model connects to the Customer model as a Foregin Key. This is the customer's saved information.
- The OrderItem model connects to the CustomerOrder and Video models as Foreign Keys and represent the videos purchased as a part of an order.
- The Customer model connects to the User model as a Foreign Key and contains the saved data chosen by the user.

[Heroku Postgres](https://www.heroku.com/postgres)

### Data Models

#### Video Model

![VideoDrome_ERD_Video](https://github.com/0davidog/VideoDrome/assets/135815736/edf1a469-f4f9-4005-afa4-84a6a95d6c72)

The Video model holds the data for each individual product sold on Videorome and contains a range of useful information to inform potential customers.

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|----------------------|
|id(Primary Key)|IntegerField|Unique numerical identifier.|Automatically generated.|
|title|CharField|This is the film's title.|Required, has to be unique and maz length is 250 characters.|
|slug|SlugField|This is a url friendly version of the title.|Is editable.|
|director|CharField|This is the name of the film's director.||
|format|CharField|This is the video format chosen from a list of DVD, Blu-Ray, UHD, 'Dual Format: Blu-Ray and DVD' and 'Dual Format: UHD and Blu-Ray'.|Default is set as DVD|
|discs|IntegerField|This is the number of disks the video has.|Default is set to 1.|
|condition|CharField|This is whether the video us used or new.|Default is set to Used.|
|price|DecimalField|This is the individual product's price.||
|stock|IntegerField|This is the quantitiy of items in stock.||
|cover|CloudinaryField|This is a photograph of the product.||
|overview|TextField|This is a description of the film.|blank=True||
|overview_source|URLField|This is the url of the film's wikipedia article.||
|trailer|URLField|This is a url for the film's trailer on youtube if found.||
|release_year|DecimalField|This is the year in which the film was originally released.||
|certificate|CharField|This is the film's age rating or certification.||
|aspect_ratio|CharField|This is the film's original aspect ratio.||
|feature_length|CharField|This is the length of the main feature.||
|added|DateTimeField|When the item was put up for sale.||
|on_sale|BooleanField|Whether the video is approved for sale or not by admin.||
|sku|CharField|A random number to represent a stock keeping unit.||
|languages|ManyToManyField|A list of available language tracks.||
|subtitles|ManyToManyField|A list of available subtitle tracks.||
|region|ManyToManyField|The region lock applied to the video.||
|genre|ManyToManyField|A list of genres applied to the film.||

Model functions.

The Video model contains 6 model functions.
-  __str__(self): Returns a string to identify model instance by title, year and format.
-  excerpt(self, num_words=25): Returns a truncated version of overview text string.
-  in_stock(self): Returns a different string value when the item stock is above 0
-  stocked(self): Returns a different boolean value when the item stock is above 0
-  _generate_sku(self): Generate random 8 digit number using uuid
-  save(self, *args, **kwargs): Override the original save method to set the sku number if it hasn't been set already.

- [x] Create - Users in an admin role can add Video entries via a front end form and the admin panel.
- [x] Read - Users both registered and unregistered can see a list of displayed videos and access their detail pages.
- [x] Update - Users in an admin role can edit video entries via a front end form and the admin panel.
- [x] Delete - Users in an admin role can delete video entries.

### UserRating Model

![VideoDrome_ERD_userrating](https://github.com/0davidog/VideoDrome/assets/135815736/bd8aa67e-6f03-4bca-a37b-38025218205b)

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|video|ForeignKey|This is the film that is the subject of the rating score.|Related to Video model.|
|user|ForeignKey|This is the user who rates the film.|Related to User model.|
|rating|IntegerField|This is the score out of 5 given to the film||

Model functions.
- __str__(self): String representation of UserRating.

- [x] Create - Users when logged in can submit a rating via the video detail page.
- [x] Read - User can see their rating displayed on the video detail page.
- [x] Update - Users can change their rating at any time via the video detail page.
- [x] Delete - User can remove thier rating at any time via the video detail page.

### UserReview Model

![VideoDrome_ERD_userreview](https://github.com/0davidog/VideoDrome/assets/135815736/d370e0b8-0b64-460e-981e-e478e71c90f9)

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|video|ForeignKey|This is the film that is the subject of the review.|Related to Video model.|
|title|CharField|This is the title of the review||
|content|TextField|This is the review content.||
|author|ForeignKey|This is the review author.|Realted to User model.|
|approved|BooleanField|Whether or not the review content is approved by admin.|Default is False|
|created_on|DateTimeField|When the review was first created|Automatically added on creation.|
|updated_on|DateTimeField|When the review was last edited|Automatically created on save.|

Model functions.
- __str__(self): String representation of UserReview.

- [x] Create - Registered users can create a review.
- [x] Read - All users can see published reviews on video detail pages.
- [x] Update - User can edit their own reviews.
- [x] Delete - Users can delete their own reviews.

### Language Model

![VideoDrome_ERD_language](https://github.com/0davidog/VideoDrome/assets/135815736/dc0e994c-7e39-4f2e-8ea5-58719005d4aa)

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|language|CharField|This is the name of the language track.||

Model functions.
- __str__(self): A string representation of the language track.

(Due to time constraints all CRUD functionality for this model remains in the admin panel)
- [ ] Create - Admin can create new language tracks in the admin panel.
- [ ] Read - Admin can view language tracks in the admin panel.
- [ ] Update - Admin can edit language track in the admin panel.
- [ ] Delete - Admin can delete language tracks in the admin panel.

### Subtitle Model

![VideoDrome_ERD_subtitle](https://github.com/0davidog/VideoDrome/assets/135815736/96f8b766-6bee-41af-bfb8-4971b32fc3d1)

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|subtitle|CharField|This is the name of the subtitle track.||

Model functions.
- def __str__(self): Function to return a string representation of the subtitle track name.

(Due to time constraints all CRUD functionality for this model remains in the admin panel)
- [ ] Create - Admin can create new subtitle tracks in the admin panel.
- [ ] Read - Admin can view subtitle tracks in the admin panel.
- [ ] Update - Admin can edit subtitle track in the admin panel.
- [ ] Delete - Admin can delete subtitle tracks in the admin panel.

### Region Model

![VideoDrome_ERD_region](https://github.com/0davidog/VideoDrome/assets/135815736/9916c9f2-c281-46fc-ba4e-6362a7e8904c)

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|regioncode|CharField|This is code name of the region such as A or B, 1 or 2.||
|region|CharField|This is the name of the region or regions the code represents such as Europe or US.||

Model functions.
- def __str__(self): Function to return a string representation of the region code and region.

(Due to time constraints all CRUD functionality for this model remains in the admin panel)
- [ ] Create - Admin can create new subtitle tracks in the admin panel.
- [ ] Read - Admin can view subtitle tracks in the admin panel.
- [ ] Update - Admin can edit subtitle track in the admin panel.
- [ ] Delete - Admin can delete subtitle tracks in the admin panel.

### Genre Model

![VideoDrome_ERD_genre](https://github.com/0davidog/VideoDrome/assets/135815736/8a4c78f4-c39f-4f9a-a3e7-ee7d8139fe83)

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|genre_name|CharField|This is the name of each genre added||

Model functions.
- def __str__(self): Function to return a string representation of the genre name.

(Due to time constraints all CRUD functionality for this model remains in the admin panel)
- [ ] Create - Admin can create new subtitle tracks in the admin panel.
- [ ] Read - Admin can view subtitle tracks in the admin panel.
- [ ] Update - Admin can edit subtitle track in the admin panel.
- [ ] Delete - Admin can delete subtitle tracks in the admin panel.

### CustomerOrder Model

![VideoDrome_ERD_customerorder](https://github.com/0davidog/VideoDrome/assets/135815736/0bf29d4f-a8ab-4bb0-81ce-a7f8acbe4b6e)

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|order_number|CharField|This is a unique number for each order.|Auto generated by method.|
|order_date|DateTimeField|This is the dat the order was processed.|Auto generated on creation.|    
|customer|ForeignKey|This is the saved information of the customer that placed the order.|Related to Customer model.|
|name|CharField|This is the customer's name, given at checkouts.||
|email|EmailField|This is the customer's email given at checkouts.||
|phone|CharField|This is the customer's phone number given at checkouts.||
|country|CountryField|This is the customer's country given at checkouts.|Picked from a dropdown list.|
|postcode|CharField|This is the customer's postcode given at checkouts.||
|town_or_city|CharField|This is the customer's city or town name given at checkouts.||
|street_address1|CharField|The first line of the street address given at checkouts.||
|street_address2|CharField|The second line of the street address given at checkouts.|Optional.|
|county|CharField|The county or province given at checkouts.|Optional.|
|delivery_cost|DecimalField|The cost of delivery.|Generated by method.|
|order_total|DecimalField|The total cost of goods.||
|grand_total|DecimalField|The total cost of goods plus elivery charge.|Updated by method.|
|original_basket|TextField|The original items in the basket saved as a json string.||
|stripe_pid|CharField|Stripes unique payment id created at checkout.||

Model functions.
- _generate_order_number(self): Generate a random, unique order number using UUID.
- update_total(self): Update grand total each time a line item is added, accounting for delivery costs.
- save(self, *args, **kwargs): Override the original save method to set the order number if it hasn't been set already.
- 

- [ ] Create - A CustomerOrder instance is created at checkouts.
- [ ] Read - Orders can be viewed by registered user associated with the order or admin only.
- [ ] Update - CustomerOrder instances can only be edited in the admin panel.
- [ ] Delete - CustomerOrder instances cah only be edited in the admin panel.

### OrderItem Model

![VideoDrome_ERD_orderitem](https://github.com/0davidog/VideoDrome/assets/135815736/1666a421-b7e6-4ff9-8bca-f84f538ae328)

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|order|ForeignKey|This is the order in which this item is a part of.|Related to CustomerOrder model.|
|video|ForeignKey|This is the video that has been purchased.|Related to Video model.|
|quantity|IntegerField|This is the quantity of the item ordered.||
|video_sub_total|DecimalField|This is the the price of the video multiplied by the quantity|Generated by method.|


Model functions.
- def save(self, *args, **kwargs): Override the save method to calculate the video subtotal before saving.

- [ ] Create - OrderItems are generated in the checkout process.
- [ ] Read - OrderItems can be read as part of the CustomerOrder model in the Admin panel or as a part of and order detail page.
- [ ] Update - OrderItems can only be updated by admin in the admin panel.
- [ ] Delete - OrderItems can only be deleted by admin in the admin panel.

### Customer Model

![VideoDrome_ERD_customer](https://github.com/0davidog/VideoDrome/assets/135815736/51730266-718a-4e39-b760-4edf2704ba5a)

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|user|OneToOneField|This is the user to whom this information belongs.|Related to User model.|
|saved_street_address1|CharField|This is the shipping information the user choses to save.|Saved at checkout.|
|saved_street_address2|CharField|This is the shipping information the user choses to save.|Saved at checkout.|
|saved_town_or_city|CharField|This is the shipping information the user choses to save.|Saved at checkout.|
|saved_county|CharField|This is the shipping information the user choses to save.|Saved at checkout.|
|saved_postcode|CharField|This is the shipping information the user choses to save.|Saved at checkout.|
|saved_country|CountryField|This is the shipping information the user choses to save.|Saved at checkout.|
|saved_phone_number|CharField|This is the shipping information the user choses to save.|Saved at checkout.|

Model functions.
- def __str__(self): String representation of the object

Signal Reciever
- create_or_update_customer_info(sender, instance, created, **kwargs): Create or update the user profile

- [ ] Create - Customer instance is created automatically via signal reciever.
- [x] Read - Customer can view their details in the customer info section.
- [x] Update - Customer can update their details in the customer info section.
- [ ] Delete - Only admin can currently delete an customer instance.

## Design Choices

### Title and Visual Inspiration

Deciding on the project title and the inspiration behind the visual design.
  
![videodrome_video_cover_videodrome_4k](https://github.com/0davidog/VideoDrome/assets/135815736/a4500b67-7ae7-4fa7-b266-dcebbf68d64f)
    
After deciding upon a business model that trades in genre films on physical media I looked to my own collection for ideas on the project title and David Cronenberg's Videodrome stood out. The title, 'videorome' suggests a video arena and would be an ideal name choice for a place of business in which a large stock of videos are traded. It also fits with the nostalgic feel of video rental business which an audience of over 30s would remember fondly. 

This gave me great place to start with the look of the project also...

![videodrome_video_cover_videodrome_blu_ray](https://github.com/0davidog/VideoDrome/assets/135815736/75b7ae34-43e2-427e-809f-8bccb3f682f9)

I like the mix of colours used in the special edition blu-ray release of this film and saw an opportunity for using greens and reds to highlight important parts of the site such as buttons, links and messages.

### Chosen Colour Palette

I took the colours from the blu-ray cover as inspiration and realised it could fit quite well with bootstraps options for colour themes. I wanted to include a yellow as part of the site because I had planned to use stars to represent a score out of five that users can give the products. I also went with a dark blue, I wanted to use this for the background of the header and footer while also use it as the text color on the main pages. I had decided to go with white as the background colour for the main page content to keep a focus on getting information to the audience in a clear manner.

![videodrome_palette](https://github.com/0davidog/VideoDrome/assets/135815736/ed47af8e-2ac6-4af6-b226-b96f4e36607a)

[via coolors](https://coolors.co/041348-198754-dc3545-0d6efd-ffc107)

### Font Choice

![videodrome_font_color_choice](https://github.com/0davidog/VideoDrome/assets/135815736/5ec04738-2823-456e-b30b-5b22fb812dc7)

In looking for font choices I had searched for a 'cyber-punk' themed font as I feel this would suit the video rental shop nostalgia that I was looking to envoke. Orbitron seemed perfect for the role however it was unsuitable for any serious body of text due to the blocky style of letters making for difficult reading. I searched for a suitable font pairing for the copy text and found a recommendation [here.](https://looka.com/blog/font-pair/)

![Screenshot 2024-06-04 at 01-36-22 25 Font Pairs to Build Your Brand ( Examples!) Looka](https://github.com/0davidog/VideoDrome/assets/135815736/d65b968d-de02-4eb0-bf11-4cd877ca6b6a)

Here's a screenshot of the article to save scrolling.

### Graphic Design

#### Background Image

![videodrome](https://github.com/0davidog/VideoDrome/assets/135815736/2c55f845-3a69-41ac-8d28-0378360f69c7)

I wanted a background image for the landing page that would suit the theme and purpose of the site. I chose to design this pixel art image of someone watching videos at home late night. the color palette is taken from the site's colors to blend in and attempts to capture that nostalgia of watching videos in the 80s and 90s.

#### Site Logo

![videodrome_logo](https://github.com/0davidog/VideoDrome/assets/135815736/e21a1c11-57ce-4087-b89c-d67d5fdc463c)

Keeping with the sites theme I decided the logo should represent a VHS video tape. Despite not being sold on the site, many of the site's target audience who are interested in home video may have fond memories of the VHS medium.

## E-commerce Business Model

The business to customer e-commerce business model of this site revolves around selling physical media products (DVDs, Blu-rays, and 4k Ultra HD films) related to horror, sci-fi, thriller and classic film genres predominantly. 
Here's a breakdown of its key components:

- Product Offering: The site will offer a range of products including both new and used DVDs, Blu-rays, and 4k Ultra HD films. The focus is on niche genres such as horror, sci-fi, and classic films, catering to enthusiasts and collectors within these genres.
- Inventory Management: The business will manage an inventory of physical media, ensuring availability of both popular and niche titles in its catalogue. This may involve sourcing products from distributors, acquiring used items through trade-ins or purchases, and maintaining stock levels to meet customer demand.
- Online Platform: The site will operate as an online platform where customers can browse, search, and purchase products. It should include features such as product listings, search functionality, shopping cart, secure payment processing, and order tracking (order tracking should be listed as a future feature as it is out of this project's scope).
- Customer Experience: Providing a positive customer experience is crucial for an ecommerce business model. This will involve offering a user-friendly website interface, accurate product descriptions and images, secure payment options, responsive customer support, and efficient order fulfilment and delivery (order fulfilment and delivery are outside the scope of this project and will be listed as future features).
- Marketing and Promotion: Marketing efforts should focus on targeting audiences interested in horror, sci-fi, thriller, and classic films through channels such as social media, email newsletters, content marketing (e.g., blog posts, reviews), and partnerships with influencers or related websites. Special promotions, discounts, and loyalty programs may also be used to attract and retain customers.
- Logistics and Fulfilment: The business would, if fully operational, manage logistics and fulfilment operations to ensure timely delivery of orders. This includes packaging products securely, arranging shipping or delivery services, and handling returns or exchanges.
- Revenue Model: Revenue is primarily generated through the sale of products, with pricing determined based on factors such as demand, rarity, condition (for used items), and competition. Additional revenue streams to consider may include shipping fees, handling fees, and potentially advertising or sponsorship revenue if the site features relevant promotional content.

Overall, the ecommerce business model of this site combines niche product offerings with an online platform and marketing efforts tailored to attract and engage customers interested in horror, sci-fi, and classic films.

### Facebook Business Page

A Facebook business page will be set up for this project. Setting up a Facebook business page can be an effective way to enhance your online presence, engage with your audience, and target potential customers. This would potentially drive sales for VideoDrome's DVD, Blu-ray, and 4k Ultra HD film business.

My goals for setting up a Facebook business page for VideoDrome could include:

- Increased Visibility: By creating a Facebook business page, I can increase my online presence and make your products more visible to potential customers.
- Direct Communication: A Facebook business page allows you to directly communicate with both my target audience and potential or existing customers. I can engage with customers through comments, messages, and posts, answering their questions, addressing concerns, and building relationships and a sense of community.
- Targeted Advertising: Facebook provides advertising tools that would allow me to target specific demographics and interests. This means I can tailor adverts to reach people who are most likely to be interested in horror, sci-fi, thriller, and classic films, increasing the effectiveness of any marketing efforts.
- Insights and Analytics: Facebook offers insights and analytics tools that provide valuable data about your audience, such as demographics, engagement metrics, and preferences. This information could help me better understand my customers and refine marketing strategies accordingly.
- Promotion and Marketing: I could easily use a Facebook business page to promote products, announce new arrivals, share special offers and discounts, as well as showcase customer reviews and feedback. This would hopefully help to drive traffic to the website and increase potential sales.
- Community Building: By creating a Facebook business page, I could build a community around my brand and products, encouraging discussions, sharing content, and creating a sense of belonging amongst my target audience.

![Screenshot 2024-06-02 at 20-33-54 Facebook](https://github.com/0davidog/VideoDrome/assets/135815736/123a81f5-2c1d-4f3f-9fd1-e1c7be1d8aa2)

A link to the page is provided [here](https://www.facebook.com/people/VideoDrome/61560545848203/), however it is apparently common for Facebook to delete innactive buiness pages so this link may not last.

### Newsletter Signup

<em>[As a site-owner, I want to include a newsletter sign up option, so that I can reach my audience with news and offers in a cost-effective manner.](https://github.com/0davidog/VideoDrome/issues/31)</em>

An email newsletter sign-up link will be added to this site with the use of Mailchimp's free services.

My goals for setting up an email newsletter for VideoDrome could include:

- Direct Communication: An email newsletter may provide a direct channel of communication with my audience. Unlike social media platforms where posts may get lost in users' feeds, emails land directly in subscribers' inboxes, giving me a higher chance for user engagement.
- Building Customer Relationships: Through regular newsletters, I could potentially build stronger relationships with my customers by providing them with useful content such as updates, and exclusive offers. This may help to keep the VideoDrome brand top-of-mind and encourage repeat purchases.
- Promoting Products and Offers: Email newsletters allow for promotion of products and special offers directly to the audience. With news of new arrivals, sales, discounts, or limited-time promotions, a newsletter could rive traffic to the store and increase sale potential.
- Targeted Marketing: With email marketing platforms, I can segment your subscriber list based on factors such as purchase history, interests, and engagement level. This enables me to send targeted and personalized emails to different segments of my audience, increasing relevance and effectiveness.
- Measurable Results: Email marketing platforms provide analytics and reporting tools that allow you to track the performance of your newsletters. You can see metrics such as open rates, click-through rates, and conversion rates, enabling you to measure the effectiveness of your campaigns and make data-driven decisions to optimize future efforts.
- Cost-Effectiveness: Compared to traditional marketing channels, email marketing is relatively inexpensive. Once I have set up my email list and created the templates, the cost of sending out newsletters is minimal, making it a cost-effective way to reach my target audience.
- Driving Website Traffic: By including links to my website or specific product pages in my newsletters, I can drive traffic directly to the site. This not only increases the visibility of my products but also may improve the website's SEO ranking.

AC1: Link to Sign Up form in footer:

![newsletter1](https://github.com/0davidog/VideoDrome/assets/135815736/77cd8c95-201a-453e-a85e-62ecb04ad6c3)

AC2: User can fill in form and submit:

![newsletter2](https://github.com/0davidog/VideoDrome/assets/135815736/6093cf6e-256f-4f17-8f95-68f457b13448)

AC3: Email is seen in Mailchimp dashboard:

![newsletter3](https://github.com/0davidog/VideoDrome/assets/135815736/0c0cece7-6a5a-427c-9cb7-32f0cda4ad59)

(emails can be seen as being added from the embedded Mailchimp form).

### Links

`rel="nofollow"`

This attribute is used in hyperlinks to tell search engines not to pass any link authority from the current page to the linked page. Essentially, it instructs search engine crawlers to not consider the linked URL when calculating the ranking of the linked page in search results. It's commonly used for user-generated content, comments, or other areas where the webmaster does not want to vouch for the credibility or endorse the linked content. It makes sense to use this for social links as the site-owner cannot entirely account for the the comments of social media users at all times, even on their own page. The main link provided as an example is a link to the Facebook business page set up for the project. I've also include links to my own social media pages as symbolic stand-ins for the multiple social accounts and pages a business would have to further extend their audience reach.
The github link isn't the strongest example of this as it is not a social media site but user comments and social interaction is still a factor so I've included it here anyway.

These links are situated on the site's footer section.

### Facebook

`<a class="btn btn-success" aria-current="page" href="https://www.facebook.com/people/VideoDrome/61560545848203/" target="_blank" rel="nofollower" aria-label="Visit out Facebook Page (opens in new tab)"><i class="fa-brands fa-facebook"></i>&nbsp;Facebook</a>`

### Instagram

`<a class="btn btn-success" aria-current="page" href="https://www.instagram.com/flatbythecemetery/" target="_blank" rel="nofollower" aria-label="Follow us on Instagram (opens in new tab)"><i class="fa-brands fa-instagram"></i>&nbsp;Instagram</a>`

### Github

`<a class="btn btn-success" aria-current="page" href="https://github.com/0davidog" target="_blank" rel="nofollower" aria-label="Check out my work on Github (opens in new tab)"><i class="fa-brands fa-github"></i>&nbsp;Github</a>`


## SEO Strategy

### Keywords

Despite the keyword Meta tag being no long used in SEO for google [[source](https://ahrefs.com/blog/meta-keywords/)], keyword research is still a useful practice for brainstorming how best to develop your site's content in a way that's relevant to your subject and audience.
    
![Screenshot 2024-05-29 at 14-42-56 dvd and blu-ray films for sale - Google Search](https://github.com/0davidog/VideoDrome/assets/135815736/ae88c72d-824f-43a1-8349-f94bd5b9c911)

The process for keyword research on the Videorome project looks like this:
- First I brainstormed the general topics of the site such as film, video, genre.
- Then a broad list of keywords were collected in relation to these topics such as 'horror dvd', 'sci-fi blu-ray'.
- These were then placed within a google search to both test for relevancy and similair search suggestions.
- With the short tail keywords especially, google's autocomplete suggestions offered insight into similar search queries.
- Google Ads Keyword planner service was then used with some of the better keyword suggestions (I could search 10 at a time for free) to refine keywords based on stats such as average monthly searches and competition. This allows the user to refine a list of keywords that could have the best effect on their site by chosing words that may be high in monthly searches but lower in competition.

![Screenshot 2024-05-29 at 15-10-59 Keyword ideas - Flat by the Cemetery - Google Ads](https://github.com/0davidog/VideoDrome/assets/135815736/861c0f83-cdc1-48e6-9169-bd208d0363fc)

- These results were exported to a google sheet [here.](https://docs.google.com/spreadsheets/d/1psnMIbEWKKW6LQ9D93t5Wqt6_GVWCzbAYhpCUuMVd8s/edit?usp=sharing)
- What these results suggest to me the most is that a vast majority of related searches in this topic will follow a format of [film] and [video format] such as 'evil dead rise dvd' or 'suspiria 4k'.
- This suggests an ideal heading convention for the videos listed in on the site.
- Example: `<h1>{{ video.title }} {{ video.format }}</h1>`

To close, here's a select list of some keywords that may serve this buisness model best:

#### Sort Tail

`horror blu-ray, horror dvd, horror 4k, sci-fi blu-ray, sci-fi dvd, sci-fi 4k` 

Note that with these keywords the genre can be replaced with the film title for a large range of relevant options.

#### Long Tail

`new horror movies on dvd, used horror DVDs for sale, new sci-fi blu-rays online, classic movie collection for sale, buy 4k ultra HD horror films, second-hand sci-fi DVDs, rare classic Blu-rays, discounted horror movies online, best deals on sci-fi Blu-rays, collectible classic films, limited edition 4k Ultra HD releases`

Here they are in a meta keywords tag as found in VideoDrome's base.html:

`<meta name="keywords" content="horror blu-ray, horror dvd, horror 4k, sci-fi blu-ray, sci-fi dvd, sci-fi 4k, new horror movies on dvd, used horror DVDs for sale, new sci-fi blu-rays online, classic movie collection for sale, buy 4k ultra HD horror films, second-hand sci-fi DVDs, rare classic Blu-rays, discounted horror movies online, best deals on sci-fi Blu-rays, collectible classic films, limited edition 4k Ultra HD releases">`

### Description

<em>[As a site owner, I want to Include Meta Description tags in the application HTML so that I can improve search engine optimisation](https://github.com/0davidog/VideoDrome/issues/18)</em>

A meta description is a brief summary of the content of a web page. It is typically displayed in search engine results pages (SERPs) beneath the page title and URL. The purpose of a meta description is to provide users with a concise preview of what they can expect to find on the webpage if they click on the link.

Here's the decription for this project chosen to hightlight the online sale of genre films in various formats:

`<meta name="description" content="Explore a vast collection of new and used DVDs, Blu-rays, and 4k Ultra HD films spanning the realms of horror, sci-fi, thriller and classic cinema. From cult favorites to timeless classics, find your next movie obsession at our online store today.">`

Goals for including a Meta Description:

- Informing Users: Meta descriptions help my audience understand the relevance and content of the webpage before clicking on it. They provide a snippet of information that can help potential users decide whether or not to visit the page.
- Improving Click-Through Rates (CTR): A well-written meta description can entice the target audience to click on the link and visit the webpage. By highlighting the most relevant or appealing aspects of the store content, a compelling meta description can increase the likelihood of users clicking through to the site.
- Enhancing Search Engine Optimization (SEO): While meta descriptions themselves do not directly impact search engine rankings, they play a role in SEO indirectly. A relevant and engaging meta description can lead to higher CTRs, which can signal to search engines that the page is valuable and relevant to users' search queries, potentially improving its ranking over time.
- Differentiating from Competitors: In SERPs where multiple search results are displayed, a well-crafted meta description can help your page stand out from competitors. By highlighting unique selling points, offers, or benefits, I could attract an audience's attention and encourage them to choose my page over others.
- Providing Context for Social Sharing: Meta descriptions are often used as the default description when a webpage is shared on social media platforms like Facebook, Twitter, or LinkedIn. A descriptive and engaging meta description can provide context for shared links, increasing engagement and click-throughs from social media users.

### Title

Here's the title for this project, chosen to highlight the sites content of genre films on various formats, the sites name and UK location:

`<title>VideoDrome UK - Genre and classic cinema on 4k, blu-ray and DVD.</title>`

A meta title, also known as a title tag, is an HTML element that defines the title of a web page. It is displayed prominently in search engine results pages (SERPs) as the clickable headline for a search result, appearing as the first line of text for each listing.

The meta title serves several important purposes:

- Search Engine Visibility: The meta title is a crucial element for search engine optimization (SEO). It helps search engines understand the topic and relevance of a web page's content. Including relevant keywords in the meta title can improve the page's chances of ranking well for those terms in search engine results.
- User Relevance: The meta title is the first thing users see when browsing search engine results. It provides users with a clear and concise indication of what the page is about. A well-crafted meta title can attract users' attention and encourage them to click on the search result to visit the page.
- Brand Recognition: Meta titles often include the brand name or website name, especially for homepage titles or pages associated with a specific brand. This helps users identify the source of the content and builds brand recognition.
- Browser Tab Label: The meta title is also displayed in the browser tab when the webpage is opened. This helps users keep track of multiple open tabs and quickly identify the content of each tab.
- Social Sharing: When a web page is shared on social media platforms or other websites, the meta title is often used as the default title for the shared link. A descriptive and compelling meta title can improve the visibility and engagement of shared content on social media.

### Relevant Content

The site's content involves use of keywords throughout in trying to provide usful information about it's products such as the media format, aspect ratio, film length and user reviews.

## Sitemap

<em>[As a site-owner, I want to include a site-map to ensure better site navigation and search engine optimisation](https://github.com/0davidog/VideoDrome/issues/17)</em>

A site-map serves as a blueprint for your website, outlining its structure and content organization. Search engines use site-maps to crawl and index your website more effectively. By providing a clear map of your site's structure and content hierarchy, you can help search engines understand and rank your pages better. The site map was genrated using [xml-sitemaps.com.](https://www.xml-sitemaps.com/)

The sitemap.xml for VideoDrome can be found [here.](https://github.com/0davidog/VideoDrome/blob/main/sitemap.xml)

## Robots.txt

<em>[As a site-owner, I want to include a robots.txt file in my site so that I can control search engine bot crawling, preserve bandwidth and protect sensitive data.](https://github.com/0davidog/VideoDrome/issues/22)</em>

A robots.txt file serves as a communication tool between your website and web robots (such as search engine crawlers) regarding which parts of your site should or should not be crawled or indexed. I chose to block access to the accounts, customer and checkouts pages as they are less about what the site is trying to sell and may contain personal or administative information. Also included in the robots file is a link to the sitemap.

The robots.txt for VideoDrome can be found [here.](https://github.com/0davidog/VideoDrome/blob/main/robots.txt)

## Features

<em>[As a shopper, I want to be able to add items to my shopping basket so that I can purchase multiple products in one transaction.](https://github.com/0davidog/VideoDrome/issues/9)</em>

Once set on a product, users need only click the 'add to basket' link that appears with the product on both the all videos view and video detail view.

#### Basket View

<em>[As a shopper, I want to be able to view and edit the contents of my shopping cart before proceeding to checkout so that I can be sure of my final purchase decision.](https://github.com/0davidog/VideoDrome/issues/10)</em>

Once items have been added to the basket, users have the ability to edit the quantity or remove any of the basket items.
  
### Checkout App

<em>[As a shopper, I want to be able to securely check out and provide shipping and payment information so that I may purchase items with ease and confidence.](https://github.com/0davidog/VideoDrome/issues/15)</em>

Users can checkout securely thanks to Stripe integration.

### Customer App

#### Order History

<em>[As a shopper, I want to be able to view my order history so that I access the information for my records or a query.](https://github.com/0davidog/VideoDrome/issues/25)</em>

Users are able to view their order history in the customer info section once they've made an order.

### Main App

#### Header

<em>[As a Site User, I want a user-friendly navigation menu that helps me explore different sections of the site easily.](https://github.com/0davidog/VideoDrome/issues/32)</em>

The header provides the main navigation links for the site as well as the search bar so users should have no trouble finding what they want.

#### Footer

The footer contains social links, a newsletter signup and an email contact form.

#### Authentication

<em>[As a new user, I want to be able to register an account on the website using my email address and password.](https://github.com/0davidog/VideoDrome/issues/1)</em>

Users are able to register for an account thanks to django-allauth. Email confirmation is required. Signing up provides access to benefits such as saved address, order history, wish list and reviews.

<em>[As a registered user, I want to be able to log in to my account securely so that I can shop easily with my saved information.](https://github.com/0davidog/VideoDrome/issues/2)</em>

Once registered, users can log in securely with their details.

<em>[As a Site user, I want the option to reset my password in case I forget it, ensuring secure access to my account.](https://github.com/0davidog/VideoDrome/issues/3)</em>

If a password is forgotten, allauth allows a process in which a user can recover their account.

#### Custom 404

<em>[As a site-owner, I want to include a 404 response page with an appropriate redirect for attempted access to non-existent content so that users who stumble on such errors are not put off from browsing.](https://github.com/0davidog/VideoDrome/issues/23)</em>

A custom 404 page is provided to ensure that users who attempt to access missing pages are not taken out of the flow of the site and can easily get back to browsing.

## Future Features

<em>[As a shopper, I want to be able to track the status of my orders, so I can be confident my order is handled and shipped in good time.](https://github.com/0davidog/VideoDrome/issues/26)</em>

As a real store would also handle shipping, an ideal future feature would be a way in which customers can keep up to date with their order status.

## Testing

Please refer to this seperate testing document for a full rundown of tests and audits:

[TEST-DOCUMENT](https://github.com/0davidog/VideoDrome/blob/main/TESTING.md)

## Technologies Used

### Languages

- HTML
- CSS
- Javascript
- Python

### Frameworks, Libraries & Programs Used

- Django
- Bootstrap
- Heroku (deployment)
- Cloudinary (image hosting)
- Django-Allauth (user authentication)
- VScode (IDE)
- Balsamiq (for Wireframes)
- ERD made with [Lucidchart](https://lucid.app/)
- GitBash
- Full requirements.txt:

<details><summary>REQUIREMENTS LIST</summary>
  
```
asgiref==3.8.1
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
cloudinary==1.40.0
crispy-bootstrap5==2024.2
cryptography==42.0.5
defusedxml==0.7.1
dj-database-url==0.5.0
Django==5.0.6
django-allauth==0.61.1
django-countries==7.6.1
django-crispy-forms==2.0
gunicorn==22.0.0
idna==3.6
oauthlib==3.2.2
packaging==24.0
psycopg2==2.9.9
pycparser==2.22
PyJWT==2.8.0
python3-openid==3.2.0
pytz==2024.1
requests==2.31.0
requests-oauthlib==2.0.0
six==1.16.0
sqlparse==0.4.4
stripe==9.6.0
typing_extensions==4.11.0
tzdata==2024.1
urllib3==2.2.1
whitenoise==6.6.0

```

</details>

## Deployment

### Prerequisites

This project requires some steps in preparation...

### Heroku Postgres Database:

<details><summary>DETAILS</summary>

Configuring your Django project to use Heroku Postgres involves several steps, including setting up the database configuration, installing necessary dependencies, and adjusting settings for deployment. Here's a general guide to help you migrate your Django project to Heroku Postgres:

Install Required Dependencies:
Ensure you have the dj-database-url package installed. This package allows you to utilize environment variables to configure your database connection.

```pip install dj-database-url```

Update requirements.txt:
If you haven't already, make sure to update your requirements.txt file with any new dependencies, including dj-database-url.

Update Django Settings:
In your Django project settings (typically settings.py), import dj_database_url and update the DATABASES setting to use environment variables for database configuration.

```
import dj_database_url

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if 'HEROKU_POSTGRESQL_TEAL_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('HEROKU_POSTGRESQL_TEAL_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

This configuration allows Django to automatically use the DATABASE_URL environment variable provided by Heroku to connect to the PostgreSQL database.

Set Environment Variables:
In your Heroku app settings, set the DATABASE_URL environment variable to the connection URL of your Heroku Postgres database. You can find this URL in the Heroku dashboard under the "Settings" tab.

Migrate Database:
Before deploying your Django app to Heroku, you need to migrate your database schema to Heroku Postgres.

```
python3 manage.py migrate
```

Collect Static Files:
If your Django project serves static files, you may need to collect them before deploying to Heroku.

```
heroku run python manage.py collectstatic
```

Deploy to Heroku:
Once you've made these changes, commit your code to your Git repository and deploy your Django app to Heroku using Git.

```
git push
```

Verify Deployment:
After deployment, you can verify that your Django app is running correctly on Heroku by visiting your Heroku app's URL in a web browser.

By following these steps, you should be able to successfully migrate your Django project to Heroku Postgres. Make sure to test your application thoroughly after deployment to ensure everything is working as expected. If you encounter any issues, Heroku provides detailed documentation and support resources to assist you further.

</details>

### Create Superuser

Use this command and enter details to create your superuser account:

`python3 manage.py createsuperuser`

### Cloudinary

Cloudinary is a hosting platform used for images in this project.

<details><summary>DETAILS</summary>


- Install The necessary Cloudinary Packages:
  
`pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15`

- Don't forget to add to requirements file:
  
`pip3 freeze --local > requirements.txt`

- Visit [Cloudinary](https://cloudinary.com/) and set up a free account if you don't already have one (you can use Google or Github to create an account easily).
- Login
- Navigate to Programmable Media - Dashboard
- Copy the API environment variable: CLOUDINARY_URL and fit it into your env.py file in this format:
  
`os.environ.setdefault("CLOUDINARY_URL", "<The URL copied from Cloudinary Dashboard>")`

- (remove 'CLOUDINARY_URL=' from the copy-pasted string)
- Open settings.py and add cloudinary and cloudinary_storage to INSTALLED_APPS.
- (The cloudinary_storage app should by place directly under django.contrib.staticfiles)

</details>

### Fork and Clone the Repository

<details><summary>DETAILS</summary>

#### Fork

To keep the original branch unaltered you can fork a repository on github.

- Navigate to the repository you want to fork.
- Click the 'Fork' button at the top right.
- Select the 'Owner' from the dropdown menu.
- Enter an optional description.
- Choose whether or not to copy main branch only.
- Click Create fork.

Source: [Github Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
    
#### Clone

On Github you can clone your repository to create a local and sync between the two locations.

- Navigate to the main page of the repository.
- Click thr '<>Code' button..
- Copy the repository URL.
- Open Git Bash or a terminal in your IDE.
- Choose the directory you want to place the repository.
- Type 'git clone', and then paste in the copied repo URL.

`git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

- Press Enter to create your local clone.

Source: [Github Docs]([https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))

</details>

### Local Deployment

<details><summary>DETAILS</summary>


To get started with local development in GitPod or your preferred IDE, follow these steps:

- Clone the repository.
- Install required packages (if project is already worked on)

`pip3 install -r requirements.txt`

- Create an 'env.py file in the app's root directory for environment variables (if using CI template this should already exist).

- In the 'env.py file, add a secret key in this format:

```
import os

os.environ.setdefault(
    "SECRET_KEY", 
    "<your chosen key goes here>"
)
```

- Add to settings.py in this format:

```
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
```

- Start the server by running the following command:

`python3 manage.py runserver`

- Now you can access the application by opening the provided URL in your browser (add your browser url to allowed hosts).

`ALLOWED_HOSTS = ['<browser URL>']`

</details>

### Production Deployment

<details><summary>DETAILS</summary>

        
Prepare the Django Project:

- Ensure your Django project is properly configured and runs smoothly locally.
- Make sure you have a requirements.txt file listing all Python dependencies required for your project.
- Ensure your project's settings are set up to work in a production environment (e.g., DEBUG = False, static files configuration, database settings).

Create a Procfile:
- Heroku uses a Procfile to determine how to run your application.
- Create a file named Procfile (no file extension) in your project's root directory.
- Inside the Procfile, specify the command needed to run your Django application. 

For example:

`web: gunicorn your_project_name.wsgi`

Create a runtime.txt File:

- Heroku needs to know which Python version your application requires. Create a runtime.txt file in your project's root directory.
- Inside runtime.txt, specify the Python version.

For example:

`python-3.9.5`

Install Gunicorn:

- Gunicorn is a WSGI HTTP server for Python web applications, and it's commonly used for deploying Django applications.
- Install Gunicorn and add it to your requirements.txt file:

`pip install gunicorn`
`pip freeze > requirements.txt`

Set Up Database:

Ad Heroku to allowed hosts in settins.py:

`ALLOWED_HOSTS = ['<browser URL>', '.herokuapp.com']`

Collect Static Files:

If your project uses static files, collect them using Django's collectstatic command:

`heroku run python manage.py collectstatic`

Commit your changes to Git:

`git add .
git commit -m "Initial commit"`

Create a new app on Heroku:
- Head over to heroku and log in. Choose 'create new app'.
- Choose a name for your app and your location. Hit 'create app'.
- Select the 'Settings' tab.
- In Config Vars, reveal config vars.
- Enter the config variables used in your env.py file.
- For example:
  - CLOUDINARY_URL
  - DATABASE_URL
  - EMAIL_USER - (gmail address)
  - EMAIL_PASS- (gmail password)
  - SECRET_KEY (The Django secret key is a crucial security setting used to provide cryptographic signing.)
   
    It is used for:
    - Security: The secret key is used to generate hashes for password reset tokens, user session tokens, and other cryptographic signatures. It helps protect against various security threats such as session hijacking, data tampering, and CSRF (Cross-Site Request Forgery) attacks.
    - Session Management: Django uses the secret key to sign and verify session cookies. This ensures that the session data stored in cookies cannot be tampered with by malicious users.
    - CSRF Protection: Django uses the secret key to create tokens for preventing CSRF attacks. When a form is rendered, Django includes a hidden CSRF token in the form. When the form is submitted, Django verifies that the CSRF token matches the one generated for the user's session, thus preventing CSRF attacks.
    - Cryptographic Signatures: The secret key is used to sign various pieces of data within Django, such as cookies, messages, and tokens. This allows Django to verify the integrity and authenticity of these pieces of data.
    - Given its critical role in security and various Django functionalities, it's essential to keep the secret key secret and never share it publicly or with unauthorized individuals. If the secret key is compromised, it could potentially lead to security vulnerabilities in your Django application.

- Head over to the Deploy tab.
- Select Github (you will need to authorize this).
- Choose your repository.
- Manually deploy the main branch of this GitHub repo.
- You can now view your app.

</details>

## Credits

### Content

The 'Boutique Ado' project was followed for the checkout and basket app due to the complexity of these functions.

### Media

Icons are sourced from [fontawesome](fontawesome.com/).

The favicon image was converted using [favicon.io](Favicon.io).

Site logo and background created by the site author.
Video cover images taken by site author.

### Acknowledgments

- Thanks to my Mentor, Malia, for her advice throughout the course.
- Thanks to those users who signed up and got involved in testing/using the site.
