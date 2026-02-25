# OpenCircle – Accessible Events Directory

## Table of Contents

- [OpenCircle – Accessible Events Directory](#opencircle--accessible-events-directory)
  - [Table of Contents](#table-of-contents)
  - [Project Overview | Ideation, Roles \& User Stories (#overview)](#project-overview--ideation-roles--user-stories-overview)
    - [Project Purpose](#project-purpose)
  - [Site Owner Goals](#site-owner-goals)
  - [Site User Goals](#site-user-goals)
  - [User Roles (MVP)](#user-roles-mvp)
    - [Visitor (Logged out)](#visitor-logged-out)
    - [User / Attendee (Logged in)](#user--attendee-logged-in)
    - [Organiser (is\_organiser=True)](#organiser-is_organisertrue)
    - [Admin / Moderator (is\_staff=True)](#admin--moderator-is_stafftrue)
    - [Permission Summary](#permission-summary)
  - [User Stories (MVP)](#user-stories-mvp)
    - [Epic 1: Public Event Discovery](#epic-1-public-event-discovery)
    - [Epic 2: Authentication \& Access Control](#epic-2-authentication--access-control)
    - [Epic 3: Organiser Event Management](#epic-3-organiser-event-management)
    - [Epic 4: Moderation \& Trust](#epic-4-moderation--trust)
    - [Epic 5: Notifications (In-App)](#epic-5-notifications-in-app)
  - [Agile Methodology](#agile-methodology)
  - [Scope \& Prioritisation (MoSCoW)](#scope--prioritisation-moscow)
    - [Must Have](#must-have)
    - [Should Have](#should-have)
    - [Could Have](#could-have)
    - [Won't Have (future features)](#wont-have-future-features)
  - [UX / Design Decisions](#ux--design-decisions)
  - [Data Model](#data-model)
  - [Wireframes](#wireframes)
  - [Features](#features)
    - [Implemented](#implemented)
    - [Future Features](#future-features)
  - [Bugs Encountered \& Resolutions](#bugs-encountered--resolutions)
    - [Production Bugs](#production-bugs)
    - [Deployment Bugs](#deployment-bugs)
  - [✅ Final Deployment State](#-final-deployment-state)
  - [Testing](#testing)
    - [Manual Testing (MVP)](#manual-testing-mvp)
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
  - [Credits](#credits)

## Project Overview | Ideation, Roles & User Stories (#overview)
### Project Purpose
Open Circle is a moderated events directory designed for queer and alternative communities, with an accessibility-first approach.

Marginalised attendees — particularly disabled and/or queer users — often struggle to find reliable accessibility and safer-space information. Event details are frequently inconsistent, vague, or scattered across social media. This creates uncertainty and forces users into “DM the organiser” culture to clarify essential access needs.

Open Circle addresses this by:
- Standardising accessibility and safer-space information
- Providing structured, comparable event listings
- Implementing moderation to improve trust
- Reducing cognitive load through clear information hierarchy

The platform enables attendees to make informed decisions without relying on fragmented or informal sources.

The platform allows organisers to submit events for moderation and enables visitors to browse events without needing an account.

## Site Owner Goals
- Maintain a trustworthy directory
- Moderate event submissions
- Prevent unauthorised access to restricted actions

## Site User Goals


## User Roles (MVP)
A role-based permission model ensures clarity, security, and trust.

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

### Permission Summary 
| Role      | Create Events | Edit Own Events | Edit Others Events   | Approve/Reject |
| :---        |    :----:   |          ---: |          ---: |          ---: |
| Visitor      | No       | No   | No      | No         |
| User   | No        | No      | No      | No         |
| Organiser      | Yes       | Yes   | No      | No         |
| Moderator (Admin)   | Yes        | Yes      | Yes      | Yes         |

## User Stories (MVP)
### Epic 1: Public Event Discovery
- As a visitor, I can view a list of approved upcoming events.
- As a visitor, I can view detailed event information (description, date/time, location, accessibility, safer-space notes, image).
- As a visitor, I can filter events by structured accessibility criteria.
- As a visitor, I can navigate results using accessible pagination.

Events are ordered logically and only approved events are publicly visible.

### Epic 2: Authentication & Access Control
- As a visitor, I can register an account.
- As a registered user, I can log in and log out securely.
- As a site owner, I can prevent unauthorised users from accessing restricted actions.
- As a user, I only see interface elements appropriate to my role.

New users default to the User / Attendee role.
Registration does not grant organiser or admin privileges.

### Epic 3: Organiser Event Management
- As an organiser, I can create an event.
- As an organiser, I can edit or delete my own events.
- Edited events return to **Pending** status.
- Changes are not publicly visible until approved.

All forms validate required fields, including accessibility information.

### Epic 4: Moderation & Trust
- As an admin, I can review pending event submissions.
- As an admin, I can approve or reject events.
- Approved events become publicly visible.
- Rejected events remain hidden.
- Organisers are notified of moderation decisions.

Moderation is required to reduce misinformation and maintain trust in accessibility claims.

### Epic 5: Notifications (In-App)
- As an organiser, I receive notification when my event is approved or rejected.
- Notifications are visible after login.
- In-app messaging was chosen to keep MVP scope focused.

## Agile Methodology

This project was developed using Agile principles and MoSCoW prioritisation.
User stories and tasks were managed using a GitHub Project board.

## Scope & Prioritisation (MoSCoW)
### Must Have
- Public event browsing
- Structured accessibility filtering
- Authentication & role-based permissions
- Organiser event submission
- Admin moderation workflow
- In-app moderation notifications
### Should Have
- View my submitted events
- Admin feedback on rejection
- Date range filtering
### Could Have
- Bookmark events
- Email notifications
- Keyword search
- Embedded Google Maps (iframe)
### Won't Have (future features)
- Ticket sales/payments
- Ratings and reviews
- User-to-organiser messaging
- Full Maps API radius search

These were excluded to prevent scope creep and maintain focus on the core problem: **trusted, accessible event discovery.**

## UX / Design Decisions

- Accessibility-first layout
- Clear labelling of access information
- Minimal cognitive load
- Mobile-responsive templates
- Typography 
- Colour Pallet 
- Layout
- Responsive design

## Data Model

The project uses a relational database with the following core models:

- User (Django built-in)
- Profile
- Event
- Notification (Currently unused in MVP, included for ease in future implementation(s))

**include ERD diagrams here**

## Wireframes 
- Built using Lucidchart 

**include wireframes here**

## Features

### Implemented

- Public event browsing
- Event detail pages
- User registration and authentication
- Organiser event submission
- User-uploaded images in Cloud storage
- Admin moderation
- Notifications on approval/rejection
- Optional rejection message from Admin
- Pagination

### Future Features

- Saved events
- Keyword search
- Embedded maps
- Event reviews

## Bugs Encountered & Resolutions

### Production Bugs

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

Manual testing was conducted throughout development to ensure all core functionality, role-based permissions, and moderation workflows operate correctly.

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

## Credits

- Django documentation
- Code Institute learning materials
