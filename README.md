# where
# -TO-
# stay

# Overview
Airbnb is widely used by many people visitng Toronto and looking for temporary accomobodation. Yet, other than providing basic choices such as accomodation type (shared, private etc), the site does not allow to filter through listings using personal taste preferences. Users have to browse through the description of each listing to see the details and figure out if it suits their needs. e.g. no noise, close to subway, grocery etc. For many users, these preferences are an essestial requirement. Thus, users end up spending considerable amount of time on their search with no guarantee that their chosen listing is the best one among similar listings.

Developed using machine learning, Your-TO airbnb allows you to easily find the perfect Toronto Airbnb that satisfies your personal taste.
Features include:

(1) Find best finds based on YOUR-TO airbnb's pricing algorithm - it compares similar listings and identifies the underpriced ones.

(2) Want a modern apartment or a clean aesthetic one? No need to waste time reading through airbnb's long descriptions. Filter listings for your personal preferences.

(3) Understand a listings surroundings. Is the listing close to metro and/or grocery? Do you want to avoid noise?

# Data Collection, Cleaning and Preprocessing
A total of four datasets were used in this project.

(1) Airbnb listings and the relevant details: scraped data of Airbnb listings in Toronto. 

(2) Noise complains locations: 311 complains database was filtered to determine the noise complains in the Toronto region for the past two years.  

(3) TTc locations: geocoded from the map provided on the TTC website.

(4) Grocery store locations: obtained from the city of Toronto's open database. 

# Modelling
In this project, two models used: (1) the topic model and (2) the pricing model.

(1) Topic model
I am using a Latend Dirichlet Allocation (LDA) model to extract latent topics in Airbnb listing description. This way the user can easily select listings that match their taste. For instance, if the user is interested in searching for renovated listings with modern features, they can filter the topic #modern, which is extracted based on the topic model developed in this notebook.

(2) Pricing model
I am using XGBoost to develop a pricing model, where I predict the price of each Airbnb listing in Toronto using physical, surrounding environment and topic modeling features. The pricing model aims to improve UX by adding a level of pricing transparency showing not only the actual listing price, but also its estimated price. This estimate reflects (assuming a robust and unbiased model) essentially how similar listings are priced.
Moreover, based on the deviation between actual and estimated price the user can view underpriced listings, marked as great deals.
