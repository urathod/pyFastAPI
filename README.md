# pyFastAPI — Product API

A simple REST API for managing **products** and **sellers**, built with [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), and SQLite.

## Features

- CRUD operations for products
- Seller registration with bcrypt-hashed passwords
- SQLAlchemy ORM models with a product–seller relationship
- Auto-generated interactive API docs (Swagger UI & ReDoc)

## Tech Stack

- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **Pydantic** — request/response validation
- **Uvicorn** — ASGI server
- **passlib + bcrypt** — password hashing
- **SQLite** — database (`products.db`)

## Project Structure

```
.
├── main.py              # (entry placeholder)
├── product/
│   ├── main.py          # FastAPI app and route definitions
│   ├── models.py        # SQLAlchemy ORM models (Product, Seller)
│   ├── schemas.py       # Pydantic schemas
│   └── database.py      # Database engine and session setup
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/urathod/pyFastAPI.git
   cd pyFastAPI
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the App

Start the development server with Uvicorn:

```bash
uvicorn product.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Products

| Method | Endpoint                | Description                                  |
|--------|-------------------------|----------------------------------------------|
| GET    | `/products/`            | List products (`skip`, `limit` query params) |
| GET    | `/product/{product_id}` | Get a single product by ID                   |
| POST   | `/products/`            | Create a new product                         |
| PUT    | `/product/{product_id}` | Update an existing product                   |
| DELETE | `/product/{product_id}` | Delete a product                             |

### Sellers

| Method | Endpoint     | Description                              |
|--------|--------------|------------------------------------------|
| POST   | `/sellers/`  | Register a new seller (password hashed)  |

## Example

Create a product:

```bash
curl -X POST http://127.0.0.1:8000/products/ \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Widget", "price": 9.99, "description": "A handy widget"}'
```

## License

This project is licensed under the [MIT License](LICENSE).
