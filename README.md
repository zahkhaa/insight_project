# where-TO-stay
### 'Find your perfect Airbnb in Toronto'

## Overview
Airbnb is widely used by many people visiting Toronto and looking for temporary accommodation. Yet, other than providing basic filter choices such as accommodation type (shared, private etc), the site does not allow to filter through listings using personal taste preferences. Users have to browse through the description of each listing to see the details and figure out if it suits their needs. e.g. cozy apartment, no noise, close to subway, grocery etc. For many users, some of these preferences are an essential requirement. Thus, users end up spending considerable amount of time on their search with no guarantee that their chosen listing is the best one among similar listings.

Developed using machine learning, where-TO-stay allows you to easily find the perfect Toronto Airbnb that satisfies your personal taste.
Features include:

(1) Find best finds based on where-TO-stay airbnb's pricing algorithm - it compares similar listings and identifies the best underpriced ones.

(2) Want a cozy apartment or a modern one? No need to waste time reading through airbnb's long descriptions. Filter listings for your personal preferences.

(3) Understand listings surroundings. Is the listing at a walking distance to metro and/or grocery? Do you want to avoid noise?

![alt text](https://github.com/zahkhaa/insight_project/blob/master/app/pics/ezgif.com-gif-maker.gif?raw=true "DEMO: where-TO-stay")

# Data Collection, Cleaning and Preprocessing
A total of four datasets were used in this project.

(1) Airbnb listings and the relevant details: scraped data of Airbnb listings in Toronto. 

(2) Noise complains locations: 311 complains database was filtered to determine the noise complains in the Toronto region for the past two years.  

(3) TTc locations: geocoded from the map provided on the TTC website.

(4) Grocery store locations: filtered and geocoded from the city of Toronto's open database for liscened retail stores.

# Modelling
In this project, two models were used: (1) the topic model and (2) the pricing model.

(1) Topic model
I used a Latend Dirichlet Allocation (LDA) model to extract latent topics in Airbnb listing description. This way the user can easily select listings that match their taste. For instance, if the user is interested in searching for renovated listings with modern features, they can filter the topic #modern, which is extracted based on the topic model developed in the second notebook.

(2) Pricing model
I used XGBoost to develop a pricing model, where I predict the price of each Airbnb listing in Toronto using physical, surrounding environment and topic modeling features. The pricing model aims to improve the user experience by adding a level of pricing transparency showing not only the actual listing price, but also its estimated price. This estimate reflects (assuming a robust and unbiased model) essentially how similar listings are priced.

Moreover, based on the deviation between actual and estimated price the user can view the best underpriced listings, marked as "Best Finds".

# Web App
Using the aforementioned model, I created where-TO-stay, a web app deployed with Flask on AWS using carto.js. 

The app clearly describes to the user:

(a) its purpose; and

(b) how to utilize it to find the best deals for the users specific taste among all the Toronto airbnb listings.
