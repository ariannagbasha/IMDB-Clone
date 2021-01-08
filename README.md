# IMDB Clone

## A website for hosting information about movies and TV. Best known for its extensive lists of actors and roles.

## Learning Objectives

* At least three (3) class-based views

* Secrets are not committed to VCS (hint: use .env)

* All network requests have sufficient exception handling for 4xx and 5xx responses. Specifically looking to handle 404 and 500 errors

* All views are DRY with all helpers factored out to appropriate modules

* At least one simple form and one model form

* All models are registered with the admin interface

* At least three database queryset methods used: all(), get(), filter()

* This criterion is linked to a Learning OutcomeAt least five fields of the following list are used among all models: BooleanField, CharField, DateField, DatetimeField, FloatField, EmailField, TextField, URLField

* At least one view has additional arguments passed via url path

## Functionality Objectives
### 1. Search for movies / actors 

 * Autocomplete Feature
 * A message, when the search results do not match, a did you mean this message

### 2. Movie detail page (includes all actors / roles involved in production, user reviews, aggregate review score based on reviews)

* Add more movies to the database
* Suggested Movies to watch feature

### 3. User signin

* Did you forget your password feature

### 4. User signup

* Email confirmation 
* Password confirmation
* Message: Error handling

### 5. User profile -- view all movies you’ve marked as seen, marked as want to see, or reviews you’ve given

* Recently Viewed
* Upload Photo
* Edit information
* Delete user

### 6. Review submission page

* Emoji Dropdown- Cross-Platform available