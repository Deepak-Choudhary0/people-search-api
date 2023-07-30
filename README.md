# People Search API

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)

## Description

The People Search API is a RESTful API that allows users to search for people based on their first names. It provides both local database search and online search using a dummyjson API.

## Installation

### Linux (Ubuntu/Debian)

To install the required dependencies, run the following command:

```bash
python3 install.py
```

### Manual Installation

If you are not on Linux, you need to install the following dependencies manually:

- Python 3.x
- SQLite3

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies (either using the provided `install.py` script or manually).
3. Run the Flask app by executing the `app.py` file.

## Demo



https://github.com/Deepak-Choudhary0/people-search-api/assets/114693662/494dc0c4-e08c-46d9-894a-7d957b9153ca



To use the People Search API, make a GET request to the following endpoint:

```
http://127.0.0.1:5000/api/users?first_name={first_name}
```

Replace `{first_name}` with the first name you want to search for.

### Local Database Search

If the API has local data entries for the given first name, it will return the matching users from the local database.

### Online Search

If the API does not have local data for the given first name, it will call the dummyjson API to fetch dummy user data for that first name. The fetched data will be inserted into the local database, and then the API will return the matching users.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push the changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: The demo section in this README provides a general description of how to use the People Search API.
