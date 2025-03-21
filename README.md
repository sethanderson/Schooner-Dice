# Seth Anderson's Schooner Dice Submission

## Test Live Online
View interactive API docs in
  **Swagger UI**: [https://schooner-dice.onrender.com/docs](https://schooner-dice.onrender.com/docs)


### /score Call and Response
  <p float="left" >
    <img src="images/image.png" style="vertical-align:top" alt="score call" width="300"/>
    <img src="images/image-1.png" style="vertical-align:top" alt="score resp" width="300"/>
  </p>

### /topCategories Call and Response
  <p float="left">
    <img src="images/image-2.png" style="vertical-align:top" alt="cats call" width="300"/>
  <img src="images/image-3.png" style="vertical-align:top" alt="cats resp" width="300"/>
  </p>

## Requirements

- **Python 3.12+** → [Download Python](https://www.python.org/downloads/)
- **pip (Package Manager)** → Installed with Python
- **Virtual Environment (venv)** → Recommended for dependency management

## Setup Instructions

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application in Dev Mode

```bash
fastapi dev main.py
```

- The server will start at [**http://127.0.0.1:8000/**](http://127.0.0.1:8000/)
- View interactive API docs at:
  - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Running Tests

```bash
pytest
```

## Formatting

```bash
black .
```

---

## Project Structure

```
Schooner Dice
 ┓ services
 ┃ ┗ category.py        # Enum Category
 ┃ ┗ schooner.py        # Where the two main functions live
 ┃ ┗ scoring.py         # Business logic
 ┓ tests
 ┃ ┗ test_scoring.py    # Unit tests for scoring.py
 ┗ main.py              # FastAPI entry point
 ┗ requirements.txt     # Python dependencies
 ┗ README.md            # Project setup guide
```

---
