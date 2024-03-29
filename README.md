# A Basic App Using the Google Books API

This is a bare-bones Flask app that uses the [Google books api](https://developers.google.com/books/) to retrieve information about books containing the text entered by the user.

The app can be found [here](http://ugaliguy.pythonanywhere.com/).

## Setting up a development environment:

This app was developed using the Anaconda package management system in an environment using Python 3.7.2.
We assume that you are using `git`.

- Clone the code repository into the directory of your choice
`git clone https://github.com/ugaliguy/8L.git`

- Install the required Python packages
`pip install -r requirements.txt`

## Running the app

- In your directory, type `flask run`

- If you get the following error message ... 
`Error: Could not locate Flask application. You did not provide the FLASK_APP environment variable.`  
set the environment variable to `app.py'

In WINDOWS, type `set FLASK_APP=app.py` and type `flask run` again.


- Point your web browser to [http://localhost:5000/](http://localhost:5000/)


## Feedback and To-Do List

This is a minimally viable product. There is work that still needs to be done.
This includes:
- error handling
- unit tests
- styling of the HTML
- refine the search so that a user can search by title, author, or isbn


I received the following feedback on June 28, 2019 (t I've added my responses/clarifications below each comment):

> I reviewed your Book Search Application, and have the following feedback to share with you:

> - I thought your application met all of the functional requirements, although from a non-functional perspective I think the styling could be improved. I tried inputting some "bad" data and was pleased to see that it doesn't seem to cause any real problems. How do you expect your app to handle a search with the entire manuscript for a film?

As far as styling goes, I'm open to suggestions and would like to learn about proper styling. I tend to choose headache-inducing colors and backgrounds and so have left the page mostly untouched. I added a little padding to `styles.css` so that the text box wasn't lurking at the top of the page.

I noticed that on [google.books](https://books.google.com/), the character limit is 2048. This suggests that I should impose a similar limit. In `index.html`, I set the maximum number of characters to 2048. As an experiment, I entered the entire text of _A Tale of Two Cities_ before setting a character limit and got an error message. After setting the limit, I had no errors.

> - I downloaded and ran the app locally. I would have found it helpful if the project's readme contained some instructions about how to get a copy up and running in a development enviroginment. Details such as this can really help someone who is unfamiliar with a project's layout get up to speed quickly.

I added instructions for both obtaining the app and running it in a development environment.

> - I had to guess which dependencies the project required due to a lack of a requirements.txt or equivalent. Although it was relatively easy to infer the flask and requests dependencies in this case, a larger project may have very specific dependency management requirements.

I added a requirements.txt file.

> - I noticed a couple of source code files (books.py and application.py) that don't seem to be required. Unused code becomes a burden over time and makes it harder to understand what a program is supposed to be doing.

I deleted both of the files books.py and application.py

> - I would have liked to run a test suite against your web app. Unit tests are a particularly effective tool for developing clean and maintainable code, as well as providing a means to safely refactor existing code. I think it's fair to say unit tests are integral to our development approach at 8th Light and it's a shame that I've not been able to see how you'd approach unit testing this project.

I understand the importance of tests, however I have never written them. Over the weekend, I tried to teach myself how to write them and found myself searching for a needle in a haystack. I tried to follow some simple examples of using pytest and quickly got lost - all of the examples were for blog apps with testing focused on user-authentication and database creation. I could not figure out how to do something relatively simple because of the more complex examples.

What I would have tested for were the following:
- Do requests receive responses - i.e. is the response status code equal to 200
- Does entering a 10- or 13-digit ISBN return the correct book

I'm sure there are many things I should test for, but I don't know what they are at the moment.


> - I'd find it helpful if you could tell me a bit about your reasons for using javascript to perform client-side rendering of the Google Books API response rather than leveraging Flask's server-side rendering capabilities? index.js makes heavy use of anonymous / arrow functions, effectively combining lots of responsibilities into one function. Code written in such a manner can be difficult to test, and as the codebase grows it becomes harder to maintain.

I respect the point you make about the arrow function in index.js being difficult to test. I used javascript for client-side rendering because it was more familiar to me and I was under some time-pressure to complete the challenge before leaving for an overseas wedding. I tried to better understand how to use Flask's server-side rendering this weekend but was unable to.  