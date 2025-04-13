# 🚀 Python REST API Sample

## 🏗️ Project Structure

```
├── app.py                  # Application entry point
├── domain/                 # Business logic and entities
│   ├── application/        # Application services and controllers
│   ├── entities/           # Domain models
│   └── repositories/       # Repository interfaces
├── infrastructure/         # External systems implementation
│   ├── fast_api/           # FastAPI implementation
│   ├── motor/              # MongoDB implementation
│   └── quart/              # Quart implementation
└── shared/                 # Shared utilities and helpers
    ├── api_response.py     # Standardized API response format
    ├── encoder.py          # JSON encoding utilities
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
   pip install quart motor
   ```

## 📝 API Endpoints

- `GET /comments` - Get all comments

## 🧩 Architecture

This project follows a domain-driven design approach with clear separation between:

- **Domain Layer**: Contains business logic, entities, and repository interfaces
- **Application Layer**: Implements use cases and coordinates domain operations
- **Infrastructure Layer**: Provides concrete implementations for external systems
- **Shared Layer**: Contains utilities and helpers used across the application

This project is licensed under the MIT License - see the LICENSE file for details.
