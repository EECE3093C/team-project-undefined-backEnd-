# Team Undefined: Universal Wishlist

## Vision

**What is your product (high-level view)?**

Our product serves to provide an advanced tool to manage a users wishlist. This list may contain items from multiple websites and will use an api to find the best price for each item to make sure the list is efficient.

**Whom is it for?**

Our target audience includes users that need a way to organize a variety of items that they would want to purchase for themselves and others. It can be used for a variety of occasions like Weddings, baby showers, birthdays, etc. It is meant for people of all ages.

**What problem does it solve?**

This would help eliminate the need to have different wishlists across multiple websites. It will all be located in one place where all a user needs to do is login to their account to see one list. It also eliminates the stress of figuring out what to get someone for their wedding, birthday etc. You can just take a look at the persons wishlist and et them a meaningful gift that will be of use to them.

**What alternatives are available, who are your competitors?**

Currently there are other "Universal Wishlists" sites that exist however, they are just simply sites that store a list of urls. They do not have any additional functionalities such as being able to display the image, description, and price for the products added. We are also going to have a way to be able to share lists with other users.

**What is novel in your approach, why is this project compelling and worth developing**

Almost eveyone at some point has tried to create a list of products that they would want to purchase.Although there are many basic tools that exist to accomplish that, we feel that there is lots of room for improvment. Our Univerval Wishlist will provide a unique and innovative approach that will allow users to have a much more seemless expereince when creating their lists of products/gifts

## Software Architecture
**Make it clear that the system can be built, making good use of the available resources and technology.**

This system will require experience with Python and web development languages. Our group consists of a variety of these skill sets and we plan to simultaneously create the backend alongside the frontend. We are certain that this is achievable and, thanks to available languages and frameworks, we have already planned our development. 

**Describe at a very high level the system's architecture, identifying the components/modules that will interact.**

The server will be hosted on a local machine (localhost). This will be managed using Flask, a Python technology that deals with the hosting of html pages. This same framework will also allow for the handling of user data such as CSVs. To transfer the data to a database sqlite3 will be used in conjunction. HTML, CSS, and Javascript will all be used to handle the frontend and user experience; however, these will be handled by Flask's template system.

**Describe the specific data you will access/store.**

We will be storing account data (using CSV files) and extra data consisting of URLs of images and websites, prices, and lists that items belong to (created by user).

**What languages/toolkits do you intend to use for the development?**

We intend to use, Flask, Python, sqlite3, HTML, CSS and Javascript. But these might change according to the requirements of our product.

## Challenges and Risks

**What is the single most serious challenge you see in developing the product on schedule?**

Our product deals with using data pulled from multiple websites simultaneously. This can result in potential legal issues regarding web scraping. This is an issue that might delay our development process because we don’t want to disregard it till the end of the development process. Instead, we are more willing to solve the problem beforehand and make sure that our methods of web scraping are risk-free.

**How will you minimize or mitigate the risk?**

We are planning on doing enough research on web scraping before starting the project. The best way to mitigate this risk is by educating ourselves on the legalities of web scraping and only incorporating functionalities that will not compromise the privacy of the customers.

