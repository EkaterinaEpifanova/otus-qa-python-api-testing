# Python API Learning Project
This repository contains a collection of simple Python scripts created as part of a learning journey in Python programming.

## 📚 Contents

- This project contains automated tests for three public REST APIs:
  - [Dog API](https://dog.ceo/dog-api/)
  - [OpenBreweryDB API](https://www.openbrewerydb.org/)
  - [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
  - Common tests for URL + Status code verification
    - This explains how to run the `test_status_code_check.py` test with different expected HTTP status codes 
    using command-line options.
    ```bash
    pytest src/test/test_status_code_check.py --url=https://ya.ru --status_code=200
    ```
    ```bash
    pytest src/test/test_status_code_check.py --url=https://ya.ru/nonexistent-page --status_code=404
    ```

The tests are written using `pytest` and a custom `BaseService` class that provides a common wrapper for HTTP requests.

## ✅ Requirements

- Python 3.7 or higher

To check your version:
```bash
python --version
```