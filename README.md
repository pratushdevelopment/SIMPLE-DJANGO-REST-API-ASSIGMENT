# SIMPLE-DJANGO-REST-API-ASSIGMENT


Objective: Your task is to create a basic RESTful API using Django REST Framework. The API should allow users to perform CRUD (Create, Read, Update, Delete) operations on a resource named "Tasks." 

Requirements:

Models:

Create a Task model with the following fields:
Title
Description (text field)
Due date
Status (choices: "To Do", "In Progress", "Done")
API Endpoints: Create the following API endpoints using Django REST Framework's ModelViewSet:

List all tasks.
Retrieve a single task by ID.
Create a new task.
Update an existing task.
Delete a task.
Serializers:

Create a serializer to convert the Task model into JSON format for API responses and request data.
Functionality:

Implement proper error handling for cases such as invalid data submissions or non-existent tasks.
Add appropriate authentication (e.g., token-based authentication) to protect the API.
Optional Enhancements (if time allows):

Add filtering and sorting options to the API for tasks.
Implement pagination for the list of tasks.
Create a user authentication system and associate tasks with specific users.
Instructions:

Fork or clone this GitHub repository: Simple Django REST API Assignment.
Create a new Django project within the repository.
Develop the required models, serializers, views, and functionality as per the requirements.
Implement proper URL routing for the API endpoints.
Implement authentication mechanisms as needed.

