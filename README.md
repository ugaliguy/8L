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
> - I downloaded and ran the app locally. I would have found it helpful if the project's readme contained some instructions about how to get a copy up and running in a development enviroginment. Details such as this can really help someone who is unfamiliar with a project's layout get up to speed quickly.
> - I had to guess which dependencies the project required due to a lack of a requirements.txt or equivalent. Although it was relatively easy to infer the flask and requests dependencies in this case, a larger project may have very specific dependency management requirements.
> - I noticed a couple of source code files (books.py and application.py) that don't seem to be required. Unused code becomes a burden over time and makes it harder to understand what a program is supposed to be doing.

I deleted both of the files books.py and application.py

> - I would have liked to run a test suite against your web app. Unit tests are a particularly effective tool for developing clean and maintainable code, as well as providing a means to safely refactor existing code. I think it's fair to say unit tests are integral to our development approach at 8th Light and it's a shame that I've not been able to see how you'd approach unit testing this project.
> - I'd find it helpful if you could tell me a bit about your reasons for using javascript to perform client-side rendering of the Google Books API response rather than leveraging Flask's server-side rendering capabilities? index.js makes heavy use of anonymous / arrow functions, effectively combining lots of responsibilities into one function. Code written in such a manner can be difficult to test, and as the codebase grows it becomes harder to maintain.