# 🚀 Python REST API Sample

## 🏗️ Project Structure

```
├── app.py                  # Application entry point
├── domain/                 # Business logic and entities
│   ├── entities/           # Domain models
│   ├── repositories/       # Repository interfaces
│   └── use_cases/          # Application use cases
├── application/            # Framework-specific implementations
│   ├── fast_api/           # FastAPI implementation
│   │   ├── controllers/    # FastAPI controllers
│   │   ├── router/         # FastAPI routes
│   │   └── setup.py        # FastAPI app configuration
│   └── quart/              # Quart implementation
│       ├── controllers/    # Quart controllers
│       ├── router/         # Quart routes
│       └── setup.py        # Quart app configuration
├── infrastructure/        # External systems implementation
│   └── motor/              # MongoDB implementation
└── shared/                 # Shared utilities and helpers
    ├── api_response.py     # Standardized API response format
    ├── encoder.py          # JSON encoding utilities
    ├── result.py           # Result pattern implementation
    └── types.py            # Type definitions
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- MongoDB

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YeissonXIX/python-rest-api-sample.git
   cd python-rest-api-sample
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📝 API Endpoints

- `GET /comments` - Get all comments

## 🧩 Architecture

This project follows a domain-driven design approach with clear separation between:

- **Domain Layer**: Contains business logic, entities, repository interfaces, and use cases
- **Application Layer**: Framework-specific implementations (FastAPI and Quart)
- **Infrastructure Layer**: Provides concrete implementations for external systems (MongoDB)
- **Shared Layer**: Contains utilities, helpers, and common patterns like Result objects

## 🔄 Framework Support

The project supports multiple web frameworks:

### FastAPI
- Modern, high-performance web framework with automatic OpenAPI documentation
- To use FastAPI, uncomment the FastAPI import in app.py and comment out the Quart import

### Quart
- Asynchronous web framework compatible with Flask's API
- To use Quart, uncomment the Quart import in app.py and comment out the FastAPI import

## 📊 Result Pattern

The application implements the Result pattern for consistent error handling:

- `SuccessResult` - Operation completed successfully
- `CreatedResult` - Resource created successfully
- `NoContentResult` - No content available
- `NotFoundErrorResult` - Resource not found
- `NotAllowedErrorResult` - Operation not allowed
- `InvalidDataResult` - Invalid data provided
- `UnknownErrorResult` - Unknown error occurred

This project is licensed under the MIT License - see the LICENSE file for details.
