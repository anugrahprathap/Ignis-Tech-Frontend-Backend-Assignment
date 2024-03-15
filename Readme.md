# Ignis Tech Frontend/Backend Assignment

This project is a web application built with React.js for the frontend and Django for the backend. It allows users to view and like events.

## Features

- View a list of events with details such as title, date, location, price, organizer, and type.
- Like events to add them to a list of liked events.
- Remove liked events from the list.

## Technologies Used

- **Frontend:**
  - React.js: A JavaScript library for building user interfaces.
  - Axios: A promise-based HTTP client for making API requests.
  - FontAwesome: A library of icons and fonts.
  - Bootstrap: A CSS framework for responsive and mobile-first web development.

- **Backend:**
  - Django: A high-level Python web framework for rapid development and clean, pragmatic design.
  - Django REST Framework: A powerful and flexible toolkit for building Web APIs.
  - Django REST Framework Token Authentication: Token-based authentication for Django REST Framework.
  - Django Models: Define database models to represent events and user data.
  - Django Views: Handle requests and return responses.
  - Django URL Patterns: Define URL patterns to map endpoints to views.

## Authentication

This application implements authentication using JSON Web Tokens (JWT) for secure user authentication. Upon successful login, users receive a JWT token, which they include in subsequent requests to access protected routes. The token is verified by the backend to authenticate the user and grant access to restricted resources.

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd react-django-application
   ```

3. Set up the Django backend:

   ```bash
   cd backend
   python manage.py migrate
   python manage.py runserver
   ```

4. Set up the React frontend:

   ```bash
   cd frontend
   npm install
   npm start
   ```

5. Access the application in your web browser at `http://localhost:3000`.

## Usage

1. **View Events**: Upon accessing the application, users can view a list of events with their details.
2. **Like Events**: Users can like events to add them to their list of liked events.
3. **Remove Liked Events**: Users can remove liked events from their list by clicking on the heart icon again.

