 # Open Circle | Accessible Events Directory
 A moderated, accessibility-first events directory designed for queer and alternative communities.

 Marginalised attendees — particularly disabled and/or queer users — often struggle to find reliable accessibility and safer-space information. Event details are frequently inconsistent, vague, or scattered across social media. This creates uncertainty and forces users into “DM the organiser” culture to clarify essential access needs.

 Open Circle addresses this by:
- Standardising accessibility and safer-space information
- Providing structured, comparable event listings
- Implementing moderation to improve trust
- Reducing cognitive load through clear information hierarchy

 The platform enables attendees to make informed decisions without relying on fragmented or informal sources.

 Live site: https://hannahashe-opencircle-cd40453b0631.herokuapp.com/
 
 # Table of Contents
- [Open Circle | Accessible Events Directory](#open-circle--accessible-events-directory)
- [Table of Contents](#table-of-contents)
- [Design \& Planning](#design--planning)
  - [Agile Methodology](#agile-methodology)
  - [User Stories](#user-stories)
    - [Epic 1: Public Event Discovery](#epic-1-public-event-discovery)
    - [Epic 2: Authentication \& Access Control](#epic-2-authentication--access-control)
    - [Epic 3: Organiser Event Management](#epic-3-organiser-event-management)
    - [Epic 4: Moderation \& Trust](#epic-4-moderation--trust)
    - [Epic 5: Notifications](#epic-5-notifications)
    - [Additional User Stories](#additional-user-stories)
  - [User Story Summary](#user-story-summary)
  - [Wireframes](#wireframes)
  - [Typography](#typography)
  - [Colour Scheme](#colour-scheme)
  - [Database Diagram](#database-diagram)
    - [Core Models](#core-models)
    - [Relationships](#relationships)
- [Features](#features)
  - [Navigation](#navigation)
  - [Footer](#footer)
  - [Home page](#home-page)
    - [Hero section](#hero-section)
    - [Featured events \& Our Values](#featured-events--our-values)
  - [Profile page](#profile-page)
    - [User/Profile information](#userprofile-information)
    - [My events section](#my-events-section)
  - [Create \& Edit Event pages](#create--edit-event-pages)
  - [Event list \& Event detail pages](#event-list--event-detail-pages)
  - [CRUD](#crud)
  - [Authentication \& Authorisation](#authentication--authorisation)
    - [User Roles](#user-roles)
    - [Visitor (Logged out)](#visitor-logged-out)
    - [User / Attendee (Logged in)](#user--attendee-logged-in)
    - [Organiser (is\_organiser=True)](#organiser-is_organisertrue)
    - [Admin / Moderator (is\_staff=True)](#admin--moderator-is_stafftrue)
- [Technologies Used](#technologies-used)
- [Libraries](#libraries)
- [Testing](#testing)
  - [Validation](#validation)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Responsiveness](#responsiveness)
  - [Browser Compatibility](#browser-compatibility)
  - [Feature testing](#feature-testing)
    - [Manual Testing (MVP)](#manual-testing-mvp)
  - [User Story Testing](#user-story-testing)
    - [Epic 1: Public Event Discovery](#epic-1-public-event-discovery-1)
    - [Epic 2: Authentication \& Access Control](#epic-2-authentication--access-control-1)
    - [Epic 3: Organiser Event Management](#epic-3-organiser-event-management-1)
    - [Epic 4: Moderation \& Trust](#epic-4-moderation--trust-1)
    - [Epic 5: Notifications](#epic-5-notifications-1)
    - [Additional User Stories (Completed in MVP)](#additional-user-stories-completed-in-mvp)
    - [Future Releases (Not Implemented)](#future-releases-not-implemented)
  - [Bugs Encountered \& Resolutions](#bugs-encountered--resolutions)
    - [Production Bugs (non-exhaustive list)](#production-bugs-non-exhaustive-list)
    - [Deployment Bugs](#deployment-bugs)
  - [✅ Final Deployment State](#-final-deployment-state)
  - [Testing](#testing-1)
    - [Deployment Testing](#deployment-testing)
  - [Deployment](#deployment)
    - [Deployment Steps](#deployment-steps)
      - [Prepare the Project for Deployment](#prepare-the-project-for-deployment)
      - [Configure Settings for Production](#configure-settings-for-production)
      - [Example production configuration:](#example-production-configuration)
      - [Create Procfile \& Specify Python Version for Deployment](#create-procfile--specify-python-version-for-deployment)
      - [Create Heroku App](#create-heroku-app)
      - [Add Database](#add-database)
      - [Set Environmental Variables](#set-environmental-variables)
      - [Deploy to Heroku](#deploy-to-heroku)
      - [Run Migrations](#run-migrations)
      - [Datebase Notes](#datebase-notes)
    - [Live Deployed Application:](#live-deployed-application)
- [Ai](#ai)
- [Credits](#credits)

# Design & Planning

 ## Agile Methodology
 - This project followed Agile principles using:
 - - GitHub Projects board
 - - User stories with acceptance criteria
 - - Iterative development
 - - MoSCoW prioritisation
 - - Project board includes:
 - - - Epics
 - - - User stories
 - - - Tasks
 - - - Labels
- Link to project board: https://github.com/users/hannahashe/projects/6

## User Stories
The project follows five MVP epics with additional should-have and could-have user stories. Complete details with acceptance criteria, tasks, and labels are available on the [GitHub Open Circle Project board](https://github.com/users/hannahashe/projects/6). Labels organise epics, prioritization (MoSCoW), frontend/backend distinctions, and future releases.

### Epic 1: Public Event Discovery
- **User Story #1** (must-have): View approved upcoming events
  - As a visitor, I can browse and view events so that I can access essential information without needing to create an account.
- **User Story #10** (must-have): Pagination
  - As a visitor, I can navigate long lists of events using pages so that the events list remains easy to navigate through to find specific events and/or dates.
- **User Story #11** (must-have): View detailed event information
  - As a visitor, I can view full event details so that I can decide if an event meets my needs and interests.

### Epic 2: Authentication & Access Control
- **User Story #2** (must-have): Register
  - As a visitor, I can register for an account so that I can access features that require authentication and permissions.
- **User Story #3** (must-have): Log in & Log out
  - As a registered user, I can log in and log out so that I can securely access authenticated features.
- **User Story #6** (must-have): Prevent Unauthorised Access
  - As a site owner, I can prevent unauthorised users from accessing restricted actions so that the platform remains secure.

### Epic 3: Organiser Event Management
- **User Story #4** (must-have): Create events
  - As an organiser, I can create an event so that I can securely submit it for approval.
- **User Story #5** (must-have): Edit & Delete events
  - As an organiser, I can edit or delete my own events so that I can keep my event information accurate.

### Epic 4: Moderation & Trust
- **User Story #7** (must-have): Moderate events
  - As an admin, I can review and moderate event submissions so that the directory remains trustworthy.
- **User Story #8** (must-have): Review pending events
  - As an admin, I can review submitted events clearly and easily so that events are organised and approved or rejected promptly.

### Epic 5: Notifications
- **User Story #12** (must-have): Notify organisers of moderation decisions
  - As an organiser, I can be notified when my event is reviewed so that I know whether it has been approved or rejected.
- **User Story #13** (should-have): Admin feedback on rejected events
  - As an organiser, I can see a brief reason when an event is rejected so that I can improve future submissions.

### Additional User Stories
- **User Story #9** (should-have): Filter by structured accessibility criteria
  - As a visitor, I can filter events by accessibility and/or date so that I find events suitable for me.
- **User Story #14** (should-have): Display category/access badges
  - As a visitor, I can clearly see access and/or category badges on event cards so that I can quickly identify events suited to my needs.
- **User Story #15** (could-have): Save or bookmark events
  - As a user, I can save events so that I can return to them later.
- **User Story #16** (could-have): Keyword search events
  - As a visitor, I can search events by keyword so that I can quickly find relevant events.
- **User Story #17** (could-have): Embedded Google Maps iframe
  - As a visitor, I can see the rough location of an event on Google Maps so that I can determine if it's accessible to me.
- **User Story #18** (won't-have): Ticket sales/payments
  - As a user, I can book tickets for events on the website so that I don't have to use a third-party site.
- **User Story #19** (won't-have): Rate & review events
  - As an attendee, I can rate and review events so that others can make informed decisions.
- **User Story #20** (won't-have): Full Maps API
  - As a visitor, I can search by addresses and radius so that I can more easily see accessible events.
 ## User Story Summary

 All must-have and should-have user stories were tested and validated against acceptance criteria (see Testing section).

 To prevent scope creep, user stories #15, #17, #18, #19, and #20 were designated as future releases. User stories #9, #12, #13, #14, and #16 were completed as part of the MVP to deliver a well-rounded, accessibility-focused product.

 ## Wireframes
 Wireframes were made using Figma, using mobile-first design, UX design and User Centered design principles. 

 <img src="static/images/readme-images/wireframes/home-page.png" width="20%">
 <img src="static/images/readme-images/wireframes/events-page.png" width="20%">
 <img src="static/images/readme-images/wireframes/event-detail-page.png" width="20%">

 ## Typography
Typography was selected with accessibility as a priority:

| Element | Font | Purpose |
|:---|:---|:---|
| Headings | Space Grotesk | Clear visual hierarchy and brand identity |
| Body text | Atkinson Hyperlegible | Enhanced readability for neurodivergent users |

**Design principles:**
- Clean, readable sans-serif typefaces
- Accessibility-first sizing and spacing
- High contrast for comfortable reading
 ## Colour Scheme
 The colour palette was carefully selected to balance visual appeal with accessibility requirements:

 | Colour Type | Hex Codes | Purpose |
 |:---|:---|:---|
 | Primary | #3a7f7a, #c08ab3, #9657e3 | Core brand identity and key interface elements |
 | Secondary | #1c3d43, #7c4c7b, #e3a857 | Supporting accents and complementary design |
 | Neutral | #f7f7f5 | Backgrounds and subtle surfaces |
 | Text | #1f1f1f, #4a4a4a | Primary and secondary text for readability |

 The colour combination prioritises readability and reduces sensory overwhelm for neurodivergent users while maintaining a modern, professional appearance.

 - Calm, low cognitive-load palette
 - Accessibility-first contrast consideration
 - Soft background tones with high-contrast text

 <img src="static/images/readme-images/open-circle-colour-pattern.png" alt="Brand colours in pattern" width="40%"/>
 <img src="static/images/readme-images/open-circle-pallet.png" alt="Brand colour pallet" width="50%">

 ## Database Diagram
 The Database mdoels included three custom models; Event, Notification and Profile. 

 The Notification model is currently **not in use** in the MVP. In the interest of developing a robust and error-free MVP, notifications in the MVP are handled by Django's built-in messages system with custom styling for brand cohesion. 

 The Notification model was added as part of the original database setup to make the future implentation of the notification dashboard easier and more straight forward. 

 ### Core Models
 - User (Django built-in)
 - Profile
 - Event
 - Notification (future feature - NOT IN USE)
  
 ### Relationships
 - User ↔ Profile (OneToOne)
 - User ↔ Event (ForeignKey as organiser)
 - Event ↔ Notification (ForeignKey)
  
  A signals.py file was set up to connect the Profile model with the User model, using a signal receiver function to trigger the creation of a corresponding profile instance when a new instance of a User is saved. 
  This allows the newly signed up User to access and alter the information in the instance of the Profile model; Namely their 'organiser status' and profile image. 
  Altering and saving the value of the 'organiser status' in the Profile model authorises the user into the 'organiser' role which allows the user to create, edit and delete their own events. See more details in the 'Authentication & Authorisation' section below.

  Entity Relationship Diagram, created with LucidChart:
  
  <img src="static/images/readme-images/open-circle-erd.png">  

 # Features
 
 ## Navigation
 - Navigation uses a responsive collapsing Bootstrap Navbar, with:
   - Role-based link visibility:
     - 'My profile' only visible to logged in users
     - 'Create Event' only visible to organisers
     - 'Admin' panel link only visible to staff/moderators (is_staff=True)
   - Login/Logout conditional rendering
   - Accessible pagination
   
  Visitor (not logged in):

 <img src="static/images/readme-images/screenshots/links-visible-1.png">

  Organiser logged in:

 <img src="static/images/readme-images/screenshots/links-visible-2.png">

  Admin/moderator logged in:
  
 <img src="static/images/readme-images/screenshots/links-visible-3.png">

 ## Footer
 - Consistent site-wide footer
 - Minimal, non-distracting design
 - Social links, copyright and contact information
  
 <img src="static/images/readme-images/screenshots/footer-desk.png">

 ## Home page
 ### Hero section

 - Hero section & CTA buttons for Browse events & Create an event (call-to-action to attendees & organisers)
 - Descriptive title and tagline, repsonsive gradient frame with low-contrast background to lessen sensory overload.
 - Hero section on mobile:

  <img src="static/images/readme-images/screenshots/hero-cta-mob.png">
 
 ### Featured events & Our Values

 - Featured events section which uses get_context_data() in the HomeView to override the default context and filter events by "approved" status and start datetime, ensuring only approved events in the future are featured.
 - "Our values" section, giving more insight into the event moderation process and the ethics of the platform.
 - Featured events section & Values section on desktop:
  
  <img src="static/images/readme-images/screenshots/featured-events-values-desk.png" width="70%">

  
 ## Profile page 
 ### User/Profile information
 - Displays user details (email, username, organiser status)
 - Displays profile image and input for user uploaded images, including guidelines on file size.
<img src="static/images/readme-images/screenshots/profile-desk.png">
<img src="static/images/readme-images/screenshots/profile-mob.png">

 ### My events section
 - "My events" section is hidden in the UI unless user changes their organiser status to 'organiser'
 - "My events" section shows edit/delete buttons, moderation status (Approved, Pending, Rejected), conditional link to the Event detail page *only if* the event has been approved.
 - 'Delete event' button triggers a confirmation modal to confirm deletion of event. 
 - 'Edit event' directs to the Edit event page.
  
 - Rejection message (either default or custom added by Admin) is displayed in the table *only if* the event has been rejected.
<img src="static/images/readme-images/screenshots/my-events-desk.png">
<img src="static/images/readme-images/screenshots/my-events-mob.png">
 - On login, when clicking on the profile page, an organiser recieves messages regarding the rejection or approval of their event. 
<img src="static/images/readme-images/screenshots/profile-approval-msg.png">
<img src="static/images/readme-images/screenshots/profile-rejection-msg.png">
 
 ## Create & Edit Event pages 
 - Structured form validation
 - Important detail fields required 

<img src="static/images/readme-images/screenshots/create-event-required.png">

 - Edited events return to pending and organiser is notified of successful event submission

<img src="static/images/readme-images/resubmission-msg.png">

 - Server-side ownership enforcement
 - Accordions displaying guidelines for successful submissions

<img src="static/images/readme-images/screenshots/create-event-desk.png">
<img src="static/images/readme-images/screenshots/create-event-mob.png">

 - Title of event automatically fills in slug in the Event model, which produces the Event detail page URL for the submitted event. Because of this, editing the title of the Event after the creation of the Event model instance was causing issues with the slug, redirection and URL paths.
 - To solve this issue, I created a seperate 'Edit event' page which excludes the Event title, so the event title cannot be edited after creation, meaning the slug can also not be changed once the event is first submitted, and the Event Model instance created. See more details in 'Development Bugs' section, below.

<img src="static/images/readme-images/screenshots/edit-event-mob.png">
<img src="static/images/readme-images/screenshots/delete-event-confirmation.png">

 ## Event list & Event detail pages
 - Public browsing of approved events, accessible to visitors, users, organsers & admin.
 - Structured accessibility display
 - Paginated results
 - Search function covering keywords, accessibility filters, start datetime & end datetime filters.

<img src="static/images/readme-images/screenshots/event-list-desk.png">
<img src="static/images/readme-images/screenshots/event-list-mob.png">
<img src="static/images/readme-images/screenshots/pagination-event-list-mob.png">
<img src="static/images/readme-images/screenshots/event-detail-desk.png">
<img src="static/images/readme-images/screenshots/event-detail-mob.png">
 ## CRUD

 | Action      | Visitor | User | Organiser | Admin |
 | :---        |    :----:   |          ---: |   ---: |          ---: |
 | Create An Event        | No | No | Yes | Yes |
 | Read (Browse all Events)          | Yes | Yes | Yes | Yes |
 | Update Own Event    | No | No | Yes | Yes |
 | Update Any Event    | No | No | No | Yes |
 | Delete Own Event    | No | No | Yes | Yes|
 | Approve/Reject Events | No | No | No | Yes

 ## Authentication & Authorisation

 - Django AllAuth authentication was used for sign up, log in and log out, redirecting to custom templates for brand cohesion.
 - A role-based permission model was used, to ensure clarity, security, and trust.
 - Server-side ownership checks are included for robust ownership/permisison checks, and UI elements are hidden throughout for unauthorised users, using Python conditional statements.

 ### User Roles
 
 ### Visitor (Logged out)
 **Purpose**: Public event discovery
 - View event list and detail pages
 - Use filters and pagination
 - Cannot create, edit, or moderate events
 
 ### User / Attendee (Logged in)
 **Purpose**: Future-facing account role 
 - Same permissions as Visitor
 - Can log in and log out
 - Cannot create events
 - Can assign themselves Organiser status

 ### Organiser (is_organiser=True)
 **Purpose**: Submit and manage own events
 - Create events
 - Edit/delete own events
 - View event status
 - Cannot approve events
 - Cannot edit others’ events
 - Ownership rule is enforced server-side:
 `event.organiser == request.user`
 
 ### Admin / Moderator (is_staff=True)
 **Purpose**: Maintain trust and quality
 - Review moderation queue
 - Approve/reject events (with rejection message)
 - Edit/delete any event
 - Override ownership rules

  Flowcharts to illustrate the User roles & permissions in practice: 

  Visitor/user/organiser:
  <img src="static/images/readme-images/mermaid-user.png" width="%30">

  Admin/moderator workflow:
  <img src="static/images/readme-images/mermaid-admin.png" wdith="%30">

 # Technologies Used 
 - Python 3.12
 - Django 
 - PostgreSQL (Production)
 - SQLite (Development)
 - HTML5
 - CSS3
 - Bootstrap 6
 - Heroku
 - Cloudinary
 - WhiteNoise
 - Gunicorn
 - Git & Github
  
 # Libraries
 - dj-database-url
 - psycopg2 / psycopg2-binary
 - django-allauth
 - cloudinary
 - pillow
 - whitenoise
 - gunicorn

 # Testing
 ## Validation
 - HTML validated via W3C Validator 
  <img src="static/images/readme-images/html-css-validation/validator-home-page.png">
  <img src="static/images/readme-images/html-css-validation/validator-event-detail.png">
 - CSS validated via WSC Validator 
  <img src="static/images/readme-images/html-css-validation/validator-css.png">
 - Python validated using CI Python Linter
  <img src="static/images/readme-images/ci-python-linter/linter-models.png">

 No critical errors present

 Screenshots of all Validators can be found in static/images/readme-images/html-css-validation

 ## Lighthouse Testing
 Tested on:
 - Homepage
 - Event List
 - Event Detail
 - Event create/edit
 - Profile
 - sign up, log in, log out
 - Both Mobile & Desktop tested.

 <img src="static/images/readme-images/lighthouse-reports/lighthouse-homepage-desk.png">
 <img src="static/images/readme-images/lighthouse-reports/lighthouse-event-detail-desk.png">
 <img src="static/images/readme-images/lighthouse-reports/lighthouse-create-event-desk.png">

 Screenshots of all Lighthouse reports can be found in static/images/readme-images/lighthouse-reports

 ## Responsiveness
 Tested using:
 - Chrome DevTools and different physical devices.
 - Multiple viewport sizes
 - HD TV, Desktop, tablet, mobile breakpoints

Mobile screen:
  <img src="static/images/readme-images/responsive-sm.png" width="60%">
Tablet screen:
  <img src="static/images/readme-images/responsive-med.png" width="40%">#
Large Desktop/TV:
  <img src="static/images/readme-images/responsive-xl.png">

 ## Browser Compatibility
 Tested on:
 - Chrome
 - Firefox
 - Edge
 All core features functon as expected.

## Feature testing
 All implemented features tested manually table here. 

 ### Manual Testing (MVP)

| Feature | Test Performed | Expected Result | Actual Result | Status |
|----------|---------------|----------------|---------------|--------|
| User Registration | Registered new user with valid details | Account created, redirected to login | Account successfully created | ✅ Pass |
| Registration Validation | Submitted empty/invalid fields | Clear validation errors displayed | Validation errors displayed correctly | ✅ Pass |
| Login | Logged in with valid credentials | User logged in and redirected | Login successful | ✅ Pass |
| Invalid Login | Used incorrect password | Error message displayed | Correct error message shown | ✅ Pass |
| Logout | Logged out from authenticated session | User redirected and session ended | Logout successful | ✅ Pass |
| View Events (Visitor) | Accessed event list while logged out | Approved events visible | Events displayed correctly | ✅ Pass |
| Event Detail Page | Clicked event card | Full event details visible | Details displayed correctly | ✅ Pass |
| Accessibility Filters | Applied accessibility filters | Only matching events displayed | Filters worked correctly | ✅ Pass |
| Pagination | Navigated between event pages | Events split correctly across pages | Pagination functioning | ✅ Pass |
| Create Event (Organiser) | Submitted new event | Event saved as Pending | Event created successfully | ✅ Pass |
| Edit Own Event | Edited organiser’s own event | Event updated and returned to Pending | Worked as expected | ✅ Pass |
| Prevent Editing Others’ Events | Attempted editing another organiser’s event | Access denied or redirect | Access correctly blocked | ✅ Pass |
| Delete Event | Deleted own event | Confirmation shown and event removed | Event deleted successfully | ✅ Pass |
| Moderation Access | Accessed moderation queue as non-admin | Access denied | Correctly restricted | ✅ Pass |
| Approve Event (Admin) | Approved pending event | Event becomes publicly visible | Event visible in listings | ✅ Pass |
| Reject Event (Admin) | Rejected event | Event remains hidden | Event correctly hidden | ✅ Pass |
| Notification on Moderation | Approved/rejected event | Organiser receives notification | Notification displayed after login | ✅ Pass |
| Role-Based UI | Logged in as different roles | Only appropriate UI options visible | UI matched role permissions | ✅ Pass |
| Static Files (Production) | Loaded deployed site | CSS and styling load correctly | Static files served via WhiteNoise | ✅ Pass |
| Media Upload (Cloudinary) | Uploaded event image | Image stored and displayed | Media displayed correctly | ✅ Pass |
| Database Separation | Checked local vs production events | Databases operate independently | Confirmed separate SQLite & Postgres DBs | ✅ Pass |


 ## User Story Testing

All must-have and should-have user stories were manually tested against their acceptance criteria. Evidence screenshots are stored in `/static/images/readme-images/screenshots/` and `/static/images/readme-images/responsive-design/`

---

### Epic 1: Public Event Discovery

| ID | User Story | Acceptance Criteria summary | Test Steps | Expected Result | Pass/Fail | Evidence |
|----|------------|--------------------|------------|----------------|-----------|----------|
| #1 | View approved upcoming events | Only approved upcoming events display to visitors without login. | 1. Open homepage while logged out <br> 2. Inspect event list | Only approved events visible. No pending/rejected events displayed. | PASS / FAIL | event-list-mob.png event-list-desk.png |
| #10 | Pagination | Event list paginates after defined number per page. Navigation controls function correctly. | 1. Add > set pagination limit of events <br> 2. Navigate using next/previous links | Event list splits correctly across pages. Navigation loads correct results. | PASS / FAIL | pagination-event-list-mob.png |
| #11 | View detailed event information | Event detail page displays full event information including accessibility data. | 1. Click event card <br> 2. Review event detail page | Full event data renders correctly including structured access info. | PASS / FAIL |  |

---

### Epic 2: Authentication & Access Control

| ID | User Story | Acceptance Criteria | Test Steps | Expected Result | Pass/Fail | Evidence |
|----|------------|--------------------|------------|----------------|-----------|----------|
| #2 | Register | Visitors can create account using valid credentials. Validation prevents invalid input. | 1. Navigate to Sign Up <br> 2. Submit valid form <br> 3. Attempt invalid submission | Valid account created. Invalid inputs rejected with errors. | PASS / FAIL | ![US2](assets/testing/us2.png) |
| #3 | Log in & Log out | Registered users can securely login and logout. | 1. Login with valid credentials <br> 2. Logout | Session created and destroyed appropriately. | PASS / FAIL | ![US3](assets/testing/us3.png) |
| #6 | Prevent unauthorised access | Unauthenticated users cannot access restricted routes (create/edit/delete/moderation). | 1. Attempt direct URL access to restricted page while logged out | User redirected to login page or denied access. | PASS / FAIL | ![US6](assets/testing/us6.png) |

---

### Epic 3: Organiser Event Management

| ID | User Story | Acceptance Criteria | Test Steps | Expected Result | Pass/Fail | Evidence |
|----|------------|--------------------|------------|----------------|-----------|----------|
| #4 | Create events | Authenticated organiser can submit event. Event status set to pending. | 1. Login <br> 2. Submit event form | Event saved to database with pending status. | PASS / FAIL | ![US4](assets/testing/us4.png) |
| #5 | Edit & Delete events | Organiser can edit/delete only their own events. | 1. Login as event owner <br> 2. Edit event <br> 3. Delete event <br> 4. Attempt edit as different user | Owner can edit/delete successfully. Other users denied access. | PASS / FAIL | ![US5](assets/testing/us5.png) |

---

### Epic 4: Moderation & Trust

| ID | User Story | Acceptance Criteria | Test Steps | Expected Result | Pass/Fail | Evidence |
|----|------------|--------------------|------------|----------------|-----------|----------|
| #7 | Moderate events | Admin can approve or reject event submissions. | 1. Login as admin <br> 2. Review pending event <br> 3. Approve or reject | Event status updates correctly. Approved events visible publicly. | PASS / FAIL | ![US7](assets/testing/us7.png) |
| #8 | Review pending events | Admin can clearly identify pending events for review. | 1. Login as admin <br> 2. View moderation dashboard/admin panel | Pending events displayed clearly and organised. | PASS / FAIL | ![US8](assets/testing/us8.png) |

---

### Epic 5: Notifications

| ID | User Story | Acceptance Criteria | Test Steps | Expected Result | Pass/Fail | Evidence |
|----|------------|--------------------|------------|----------------|-----------|----------|
| #12 | Notify organisers of moderation decisions | Organiser receives notification after event approval/rejection. | 1. Submit event <br> 2. Admin approves/rejects <br> 3. Login as organiser | Notification message appears once on profile/dashboard. | PASS / FAIL | ![US12](assets/testing/us12.png) |
| #13 | Admin feedback on rejected events | Rejected event includes short feedback message visible to organiser. | 1. Reject event with feedback <br> 2. Login as organiser | Feedback reason displayed clearly. | PASS / FAIL | ![US13](assets/testing/us13.png) |

---

### Additional User Stories (Completed in MVP)

| ID | User Story | Acceptance Criteria | Test Steps | Expected Result | Pass/Fail | Evidence |
|----|------------|--------------------|------------|----------------|-----------|----------|
| #9 | Filter by structured accessibility criteria | Visitors can filter events by access criteria and/or date. | 1. Apply accessibility filter <br> 2. Apply date filter | Event list updates dynamically to match selected filters. | PASS / FAIL | ![US9](assets/testing/us9.png) |
| #14 | Display category/access badges | Event cards display clear visual access/category badges. | 1. View event list <br> 2. Inspect event cards | Structured badges visible and styled consistently. | PASS / FAIL | ![US14](assets/testing/us14.png) |
| #16 | Keyword search events | Visitors can search events by keyword. | 1. Enter keyword in search field <br> 2. Submit | Relevant events returned. No-match message shown when applicable. | PASS / FAIL | ![US16](assets/testing/us16.png) |

---

### Future Releases (Not Implemented)

| ID | Status | Notes |
|----|--------|-------|
| #15 | Could-have | Save/bookmark events – designated future enhancement. |
| #17 | Could-have | Embedded Google Maps iframe – future enhancement. |
| #18 | Won’t-have | Ticket sales/payments excluded from MVP scope. |
| #19 | Won’t-have | Rate & review system excluded from MVP scope. |
| #20 | Won’t-have | Full Maps API with radius search excluded to prevent scope creep. |


 ## Bugs Encountered & Resolutions

### Production Bugs (non-exhaustive list)

| Bug | Issue | Cause | Resolution |
|-----|-------|--------|------------|
| **Virtual Environment Activation (Windows)** | PowerShell would not activate the virtual environment. | PowerShell execution policy prevented script execution. | Updated execution policy using `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, then activated with `.\.venv\Scripts\Activate.ps1`. |
| **`super(): no arguments` RuntimeError** | `makemigrations` raised a RuntimeError in the `Event` model. | Incorrect `save()` override using `super()` improperly. | Updated method to use `super(Event, self).save(*args, **kwargs)`. |
| **Slug Causing 404 After Editing** | Editing an event caused 404 errors when redirecting to detail page. | Slug was tied to editable title, causing URL mismatch. | Created separate `EditEventForm` excluding title & slug and prevented slug regeneration during edits. |
| **Cloudinary Images Returning 404** | Uploaded images showed 404 errors in browser. | Cloud name was changed after rotating API credentials; images were stored under old cloud account. | Updated environment variables, reconfigured Cloudinary, and re-uploaded images under correct cloud. Ensured `.url` was used in templates. |
| **`__str__ returned non-string (type NoneType)`** | Event detail page crashed due to TypeError. | `__str__` method could return `None`. | Updated `__str__` methods to always return a string (e.g., `return self.title or "Untitled Event"`). |
| **Pagination Not Rendering** | Pagination worked in the view but not visible in template. | Pagination markup was outside `{% block content %}`. | Moved pagination controls inside `{% block content %}` section. |
| **Rejected Events Not Editable** | Organisers could not edit rejected events. | Public event list only displayed approved events. | Added “My Events” section to profile page showing all organiser events regardless of status. |
| **Moderation Message Not Appearing on Approval** | Organisers received rejection messages but not approval messages. | `moderation_notified` flag was not resetting when status changed. | Updated `Event.save()` to reset `moderation_notified` when status changed to approved/rejected. |
| **Exposed Secret Key & API Credentials** | GitGuardian flagged sensitive credentials in repository. | API keys were hardcoded in `settings.py`. | Rotated credentials, removed hardcoded values, moved secrets to `env.py`, added to `.gitignore`, and used environment variables. |
| **PowerShell venv Creation Hanging (KeyboardInterrupt)** | `python -m venv .venv` appeared to hang and threw a `KeyboardInterrupt`. | The process was interrupted during environment creation, leaving a partial `.venv` folder. | Deleted the incomplete `.venv` directory and recreated the virtual environment successfully. |
| **`SyntaxError: leading zeros in decimal integer literals` During Migration** | Django prompted for a default datetime value when making migrations and raised a syntax error. | A datetime value was entered with leading zeros (e.g. `02` instead of `2`). | Entered datetime values without leading zeros (e.g. `datetime(2026, 2, 17, 12, 0)`). |
| **CloudinaryField Displaying Public ID Instead of URL** | Uploaded image displayed as a string (e.g. `efqr69ejfcymuqk4jrp4`) instead of rendering an image. | Template used `{{ event.event_img }}` instead of `{{ event.event_img.url }}`. | Updated template to use `.url` to generate full Cloudinary delivery URL. |
| **ImageField Error: Pillow Not Installed** | Django raised error: `Cannot use ImageField because Pillow is not installed.` | `Pillow` dependency was missing. | Installed Pillow via `pip install Pillow` and updated requirements. |
| **Admin Comment Field Breaking Admin View** | Admin panel crashed after adding `admin_comment` to `EventAdmin`. | Database migration had not been run after adding the new model field. | Ran `makemigrations` and `migrate` to sync database schema. |
| **AllAuth 404 on `/signup/` Route** | Visiting `/signup/` returned 404 error. | AllAuth routes are namespaced under `/accounts/`. | Used correct route `/accounts/signup/` and updated navigation links accordingly. |
| **AllAuth Middleware Configuration Error** | Django raised `ImproperlyConfigured: allauth.account.middleware.AccountMiddleware must be added to settings.MIDDLEWARE`. | Required middleware was missing after installing AllAuth. | Added `allauth.account.middleware.AccountMiddleware` to `MIDDLEWARE` in settings.py. |
| **Profile `RelatedObjectDoesNotExist` Error** | Visiting profile page caused `User has no profile.` error. | Profile auto-creation signal had not created profile for existing superuser. | Manually created profile for existing user and confirmed signal setup for new users. |
| **NOT NULL Constraint on `profile_img`** | Admin failed when creating Profile due to NOT NULL constraint. | `profile_img` field was required but no default provided. | Updated field to allow `blank=True, null=True` to prevent constraint error. |

### Deployment Bugs

The following issues were encountered during deployment to Heroku and resolved through debugging and configuration updates.

| Issue | Error Message / Symptom | Cause | Resolution |
|-------|--------------------------|--------|------------|
| App crashed on startup (H10) | `ModuleNotFoundError: No module named 'opencircle'` | Gunicorn was pointing to the wrong project module name in the Procfile and/or `wsgi.py` | Updated `Procfile` to `web: gunicorn config.wsgi` and ensured `DJANGO_SETTINGS_MODULE = 'config.settings'` |
| 400 Bad Request | Generic “Bad Request (400)” | Duplicate or incorrect `ALLOWED_HOSTS` configuration in `settings.py` | Removed duplicate `ALLOWED_HOSTS = []` and ensured environment-based configuration was used |
| Static CSS not loading | `Not Found: /static/css/styles.css` | Project-level static folder not included in `STATICFILES_DIRS` | Added `STATICFILES_DIRS = [BASE_DIR / "static"]` and redeployed |
| Static files not served in production | CSS missing despite correct paths | `collectstatic` had not properly gathered static files | Verified WhiteNoise configuration and confirmed `collectstatic` ran during deployment (149 files copied) |
| 500 Server Error after fixing hosts | Internal server error with no visible traceback | `DEBUG=False` suppressed detailed error output | Temporarily set `DEBUG=True` in Heroku config to view error details, then restored `DEBUG=False` |
| Fixture not found when loading JSON | `CommandError: No fixture named 'data' found` | `data.json` file had not been committed and pushed to Heroku | Committed `data.json` to repository and redeployed |
| JSON encoding error | `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff` | Fixture file saved in UTF-16 encoding (Windows default) instead of UTF-8 | Regenerated fixture using UTF-8 encoding |
| Cursor does not exist during dumpdata | `cursor "_django_curs_..." does not exist` | SQLite dump issue during large or unstable serialization | Chose to abandon full DB migration and manually add clean production data via Django Admin |
| Argument parsing error with collectstatic | `Nonexistent flag: --no-input` | Heroku CLI interpreted flag incorrectly | Used `heroku run -- python manage.py collectstatic --no-input` (added `--` to separate CLI arguments) |
| Events missing in production | No events visible after deployment | Production uses Heroku Postgres, separate from local SQLite database | Confirmed separate databases; manually added production events via Django Admin |

---

## ✅ Final Deployment State

After resolving the above issues:

- Application successfully deployed to Heroku  
- Gunicorn running correctly  
- WhiteNoise serving static files  
- Cloudinary handling media storage  
- Postgres connected in production  
- `DEBUG` set to `False`  
- Role-based permissions functioning as expected  

## Testing
- HTML & CSS validators, Python CI linter
- Lighthouse testing 
- DevTools testing 
- Manual testing against User Stories 

---

### Deployment Testing

| Test | Expected Outcome | Result |
|------|------------------|--------|
| Heroku Build | Successful build without errors | ✅ Successful |
| Gunicorn Startup | App boots without H10 crash | ✅ Successful |
| `DEBUG=False` | Site loads without debug information | ✅ Successful |
| Environment Variables | SECRET_KEY, DATABASE_URL, ALLOWED_HOSTS configured | ✅ Confirmed |
| collectstatic | Static files copied during deployment | ✅ 149 files copied |

## Deployment
This project is deployed using Heroku, with:
- Gunicorn as the production WSGI server
- WhiteNoise for static file handling
- Cloudinary for media file storage
- Heroku Postgres as the production database
### Deployment Steps 
#### Prepare the Project for Deployment 
The following production packages were installed:
- gunicorn
- whitenoise
- dj-database-url
- psycopg2 & pscopg2-binary

requirements.txt was updated:
`pip freeze > requirements.tx`
#### Configure Settings for Production
In settings.py:
- DEBUG is controlled by environmental variables
- SECRET_KEY is stored securely in Heroku config vars 
- ALLOWED_HOSTS is set using environment variables 
- Database is configured using dj_database 
- WhiteNoise is used for static files 
- Cloudinary is used for media storage 

#### Example production configuration:
```
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
       "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
```

#### Create Procfile & Specify Python Version for Deployment
A Procfile was created in the root directory:
`web: gunicorn config.wsgi`

A .python-version file was added:
`3.12.7`

#### Create Heroku App
The Heroku CI was used for deployment. 
`heroku login` 
`heroku create hannahashe-opencircle`

#### Add Database
The Code Institue Postgres Database maker was used. 
`heroku addons:create heroku-postgresql:essential-0`

#### Set Environmental Variables
The following config vars were set in Heroku:
```
heroku config:set SECRET_KEY="my-secret-key"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="hannahashe-opencircle-cd40453b0631.herokuapp.com, hannahashe-opencircle.herokuapp.com/"
```

#### Deploy to Heroku 
Using the Heroku CI in the VS Code terminal, the project was pushed to Heroku for deployment. 
`git push heroku main`

Heroku runs collectstatic during deployment to gather static files for WhietNoise.

#### Run Migrations
After deployment, migrations were run in the terminal:
`heroku run python manage.py migrate`

Also, a superuser (admin) was created with:
`heroku run python manage.py createsuperuser`

#### Datebase Notes
- Local development uses SQLite.
- Production uses Heroku Postgres.
- These are separate databases.
- Production data was manually added via Django Admin.

### Live Deployed Application:
The live site can be accessed here:
https://hannahashe-opencircle-cd40453b0631.herokuapp.com/

 # Ai
 Ai tools (ChatGPT, Microsoft Copilot, VS Code Copilot) were used to:
 - Refine user stories
 - Debug configuration issues 
 - Profile signal.py setup 
 - Admin panel development
 - Login & sign up template implementation
 - Generate documentation structure 
 - Improve README table formatting
 - Troubleshoot deployment errors
All code was reviewed, understood and adapted before implementation.

 # Credits 
 - Django Documentation
 - Code Institute course materials
 - Bootstrap documentation
 - Heroku documentation
 - Freepik for free stock images: https://www.freepik.com/app
 - ChatGPT Codex for debugging and explanatory prompts