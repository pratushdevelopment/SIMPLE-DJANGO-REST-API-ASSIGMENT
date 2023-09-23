# Django REST API for Task Management

This project implements a RESTful API for managing tasks using Django REST Framework. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks.

## Getting Started

To set up and run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/pratushdevelopment/SIMPLE-DJANGO-REST-API-ASSIGMENT.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SIMPLE-DJANGO-REST-API-ASSIGMENT/taskapi
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Migrate the database:

   ```bash
   python manage.py migrate
   ```

5. (Optional) Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the API at [http://localhost:8000/api/tasks/](http://localhost:8000/api/tasks/).

## API Endpoints

- List all tasks: `/api/tasks/` (GET)
- Retrieve a single task by ID: `/api/tasks/<task_id>/` (GET)
- Create a new task: `/api/tasks/` (POST)
- Update an existing task: `/api/tasks/<task_id>/` (PUT)
- Delete a task: `/api/tasks/<task_id>/` (DELETE)

## Authentication

Token-based authentication is implemented to protect the API endpoints. To obtain an API token:

1. Create a user or use the superuser created during setup.
2. Authenticate and obtain a token by sending a POST request to `/api/token/`. Provide your username and password in the request body (see API documentation for details).

Include the token in the `Authorization` header of your requests as `Bearer <token>`.

## Error Handling

The API includes proper error handling to manage cases such as invalid data submissions or non-existent tasks. You will receive appropriate error messages and status codes when issues occur.

## Optional Enhancements

- Filtering and Sorting: You can filter and sort tasks using query parameters in the API URL.
- Pagination: The list of tasks is paginated to manage large datasets.
- User Authentication: Tasks are associated with specific users.

## Documentation

For more detailed information, usage examples, and API documentation, refer to the [API Documentation](api_documentation.txt) provided in this repository.

## Contributing

Contributions to this project are welcome. If you'd like to contribute, please follow the standard GitHub fork and pull request process.

## Acknowledgments

- This project was built using [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/).
- Special thanks to the [Django community](https://www.djangoproject.com/community/) for their excellent documentation and support.
```
