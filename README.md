# Discussion forum application

## Description
The discussion forum application is built by Django and React. The forum web app allows any user to view threads. Users can register and login to create new thread and reply to any threads to join any discussion.


## Distinctiveness and Complexity
This forum app is different from other projects in the course. This forum app is neither a social network nor an e-commerce site.  
The forum app exhibits different functionalities to provide an online platform for discussion. The forum app permits guests to view all the threads and posts without an account. There are different views to view threads sorted by different topics. Users who are authenticated can add a new threads to start a dicusssion and add post to reply own thread and threads created by other users. In addition, authenticated users can make bookmarks to threads and edit their avatar and biography in profile page..

The complexity of the forum app is higher than any projects in CS50 Web. The forum app separates the frontend and backend into two technologies. The frontend and user interface is built by React and the backend is built by Django. React provides component based architecture to manipulate the DOM to create a single-page forum application.  

In the user interface, infinite scroll is employed to replace pagination to provide users smoother experience to browse threads in different devices. Viewing most of the pages in this forum app does not require any reload and refresh of the page given the advantages of React.  

Django is used to build the web API and database to function the backend. There are 4 django models to create the database to store forum data. The backend has various endpoints available through the created API to allow the client side to retrieve and return data.  

This forum app has token-based authentication to validate the user login. 

## Contained Files

## Getting Started to run the app
```

```

## Additional Information

## Features

## Tech Stack


## Application API
The application supports the following API routes:

Compose a new post
```
POST /post/
```

Retrieve all the posts
```
GET /posts/
```

Retrieve a single post
```
GET /posts/<int:post_id>
```

Edit a post
```
PUT /edit/<int:post_id>
```

Follow and unfollow a user (implemeneted in profile page)
```
POST /follow
POST /unfollow
```

Like and unlike a post
```
POST /like/<int:post_id>
```

Get the number of followers for a user
```
GET /followerCount/<str:name>
```

Get the number of likes for a post
```
GET /likeCount/<int:post_id>
```





## Requirements
In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:
- Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza    project), and more complex than those.
    - A project that appears to be a social network is a priori deemed by the staff to be indistinct from Project 4, and should not be submitted; it will be rejected.
    - A project that appears to be an e-commerce site is strongly suspected to be indistinct from Project 2, and your README.md file should be very clear as to why it’s not. Failing that, it should not be submitted; it will be rejected.

- Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
    -   Under its own header within the README called Distinctiveness and Complexity: Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.
    -   What’s contained in each file you created.
    -   How to run your application.
    -   Any other additional information the staff should know about your project.
- Your web application must be mobile-responsive.
- In a README.md in your project’s main directory, include a writeup describing your project, and specifically your file MUST include all of the following:
- If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to a requirements.txt file!
- Though there is not a hard requirement here, a README.md in the neighborhood of 500 words is likely a solid target, assuming the other requirements are also satisfied.
## Demonstration

