## Project Name
Neighborhood
## Author's Name

##  Project Description
Mountain Place Community is a platform that allows you to be updated with what's happening in your neighborhood.
## BDD

<img src="rome1.png">
<img src="rome2.png



### Cloning
* In your terminal:
        
        $ git clone https://github.com/RonnyLincoln/neighborhood/
        $ cd neigbourhood

## Running the Application
* Install virtual environment using `$ python3 -m venv venv
* Activate virtual environment using `$ source virtual/bin/activate`
* Install all the dependencies from the requirements.txt file by running `pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ make migrations neighbourhood
        $ make migrate 

* To run the application, in your terminal:

        $ make server
        
## Testing the Application
* To run the tests for the class file:

        $ python3.8 manage.py test neighbourhood

## Technologies used

- Bootstrap
- Python 
- Django
- Postgresql

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets directed to the login page  | User logs in | Directed to the home page | 
If user has no account, they click on `sign up` | User signs up | User is redirected to the profile set up page |

## Projects livelink

https://mountain-place.herokuapp.com/


## Contact Information

- Email:mwithiamoki@gamil.com
- Github:RonnyLincoln

### License

* LICENSED UNDER  [![License: MIT](https://github.com/RonnyLincoln/neighborhood/blob/master/LICENSE)](license/MIT)
