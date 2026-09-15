# User Stories

## #1 Browse Events
As a user, I want to be able to browse events by category so that I can filter the list of events to those that are of interest to me. 

Acceptance Criteria:
1. The user should be able to browse events, filtered by category, through an intuitive interface.
2. The list of events should automatically update to reflect the user’s choice of category.
3. Only events with a status of ‘Open’ should be viewable.

## #2 Searching for Events
As a user, I want to be able to search for specific events using a search bar, and have similar events recommended to me based on the key words I type.  

Acceptance Criteria:
1. A search bar that users can type keywords into to search for specific events.
2. Recommended events are shown based on the input, and refreshes as the input changes.
3. This search bar supports both traditional keyword-based search and an AI-enhanced event discovery capability that improves a user's ability to locate relevant events beyond simple keyword matching.

## #3 Viewing Event Details
As a user, I want to be able to view more details for an event I am interested in beyond the summary shown when I am browsing through events. I want to be able to see details important to me, such as how much the tickets cost, when and where it will take place, and if the event is adults only.  

Acceptance Criteria:
1. An event details page that displays all information relevant to the event.
2. The page must include an image, description, date and time, as well as any other information provided by the organiser.
3. Each event details page includes a comment section, which can be viewed by users not logged in.

## #4 Booking Tickets
As a logged-in user, I want to be able to purchase tickets for events I am interested in attending.  

Acceptance Criteria:
1. Buying tickets is only available to users who have logged into an account.
2. The number of tickets must be submitted by the user.
3. The total cost is calculated by multiplying the number of tickets required by the ticket price for the specified event.
4. The number of tickets available for an event must be updated after tickets are purchased, and the user cannot purchase more than are available.
5. The transaction must be approved and finalised before the user is able to access and use the tickets.
6. This transaction and its details must be recorded in the user’s booking history.

## #5 Posting Comments
As a logged-in user, I want to be able to review events I have attended to share my experience with others, either positive or negative.  

Acceptance Criteria:
1. Posting comments is only available to users who have logged into an account.
2. The system must record the event, timestamp, comment text and the user who posted the review. 
3. The comment is able to be viewed by any user or visitor to the site.

## #6 Viewing Booking History
As a logged-in user, I want to be able to view tickets I have previously bought while using this account.  

Acceptance Criteria:
1. Viewing a user’s booking history is only available to users who have logged into an account.
2. Users are only able to view the booking history for the account they are logged into.
3. The page should list all the orders this user has made, including each order id, number of tickets, total price and the name of the event.

## #7 User Registration
As a user, I want to be able to create an account so that I can book tickets for events and create my own.  

Acceptance Criteria:
1. An account registration page, where the user must complete a form in order to create their account.
2. The user must provide, and the database must store, the user’s full name, unique email, password, contact number (phone) and street address (address).
3. Payment details are not required for account registration, but are required to purchase tickets.
4. For security purposes, the password must not be stored as plaintext. Instead, it should be stored as a hash.

## #8 User Login
As a user, I want to be able to log into my account so that I can purchase tickets and create events.  

Acceptance Criteria:
1. A login page, where the user must provide their email address and password to be able to login.
2. The website must confirm that the login credentials are correct before the user is able to access their account and be logged in.

## #9 Creating Events
As a logged-in user, I want to be able to create my own events so that I can sell tickets on the website.  

Acceptance Criteria:
1. Creating events is only available to users who have logged into an account.
2. The user who creates the event has the role and privileges of an organiser for that event. Only this user may make changes to or cancel the event.
3. The database must store the event details, including its status and Acknowledgement of Country Statement.

## #10 Updating Events
As a logged-in user and event creator, I want to be able to update my events so that attendees are informed of any changes or cancellations.

Acceptance Criteria:
1. The event creator is able to cancel an event that they created.
2. An event creator is not able to cancel an event that they did not create.
3. An event must have a status of either 'Open', 'Inactive', 'Sold Out' or 'Cancelled', that is updated by the site.
4. The event creator is not able to directly change the event status.
5. The event creator is able to change any details about the event, excluding the status.

## #11 Site Navigation
As a user, I want to be able to navigate the site easily and intuitively so that my booking experience is seamless.

Acceptance Criteria:
1. The user must be able to see and use a navigation menu on each page.
2. The navigation menu must 
3. Any navigation that results in an error must provide the relevant feedback to the user (such as a 404 page).

## #12 User Logout
As a logged-in user, I want to be able to log out of the site so that my data is protected when I am not using the site.

Acceptance Criteria:
1. The user is able to log out from the site.
2. The session data and cookies are removed from the applicable device.
3. Other users cannot access a logged-out user's data.
