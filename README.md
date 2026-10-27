# SonicBench

**SonicBench** is a web application developed with Django for exploring speaker manufacturers, managing audio equipment, and organizing personalized listening setups.

The application allows visitors to maintain a catalog of speakers and audio brands, create listening rooms, and combine different speaker models into custom sound systems.

## Technologies

- Python 3.12+
- Django 6.1.2
- SQLite
- HTML5
- CSS3
- Django Template Language
- Git and GitHub

## Main Features

### Audio Brands

- Browse speaker manufacturers.
- Add manufacturers with country, description, website, and logo URL.
- View manufacturer details and related speakers.
- Edit and delete manufacturers.
- Prevent deletion of manufacturers that have associated speakers.

### Speaker Catalog

- Add, view, edit, and delete speakers.
- Store technical specifications, including RMS power, frequency response, category, price, and wireless connectivity.
- Search speakers by name or manufacturer.
- Sort speakers by price, name, or creation date.
- Browse paginated results.
- Validate speaker data before saving.

### Listening Rooms

- Create listening rooms.
- Choose room categories.
- Record room dimensions and descriptions.
- View the listening setups assigned to each room.

### Listening Setups

- Create personalized audio configurations.
- Assign each setup to a listening room.
- Select multiple speakers for one setup.
- View, edit, and delete listening setups.
- Explore the speakers associated with each setup.

## Project Structure

The project contains three custom Django applications:

| Application | Responsibility |
|---|---|
| `brands` | Speaker manufacturers and brand management |
| `speakers` | Speaker catalog, specifications, searching, and sorting |
| `setups` | Listening rooms and audio configurations |

## Database Models

The project defines four primary models:

- **Brand:** Information about audio manufacturers.
- **Speaker:** Speaker specifications and a ForeignKey relationship to Brand.
- **Room:** Information about physical listening spaces.
- **ListeningSetup:** Audio configurations with a ForeignKey to Room and a ManyToMany relationship to Speaker.

## Installation and Setup

### 1. Clone the repository

`git clone https://github.com/nikolay1321/SonicBench.git`

Then navigate into the project folder:

`cd SonicBench`

### 2. Create a virtual environment

On Windows:

`py -m venv .venv`

### 3. Activate the virtual environment

In PowerShell:

`.\.venv\Scripts\Activate.ps1`

### 4. Install dependencies

`python -m pip install -r requirements.txt`

### 5. Apply database migrations

`python manage.py migrate`

The application uses SQLite, so no separate database server is required.

### 6. Start the development server

`python manage.py runserver`

### 7. Open the application

Visit:

`http://127.0.0.1:8000/`

## Configuration

The default configuration is intended for local development and evaluation.

No external database, third-party API credentials, or preloaded data are required for the standard local setup.

The evaluator can create all necessary records through the website.

## Using the Application

The recommended order for creating data is:

1. Create an audio brand.
2. Add a speaker and assign it to the brand.
3. Create a listening room.
4. Create a listening setup, choose the room, and select one or more speakers.

All required objects can be created using the website's navigation and forms.

The application supports an initially empty database.

## Django Features Demonstrated

- Multiple Django applications
- ForeignKey and ManyToManyField relationships
- Django ModelForms
- Custom form and model validation
- Generic Class-Based Views
- Full CRUD operations
- Template inheritance and reusable partial templates
- Built-in and custom template filters
- Custom template tags
- Pagination
- Query filtering and sorting
- Custom 404 page
- Responsive CSS design

## Development

This application was created as an individual Django Basics course project.

## License

No license has been specified for this repository.