# Warbler (Twitter Clone) - README

## Dependencies

To set up and run the Warbler project, the following dependencies are required:

- Python 3
- Virtualenv
- PostgreSQL

## Project Overview

Warbler is a Twitter clone project that allows users to post short messages called "warbles." Users can follow each other, like warbles, and view warbles from users they follow on their homepage. It provides basic social networking functionality similar to Twitter.

## Setup

To set up the Warbler project, follow the steps below:

1. Create a Python virtual environment:
```
$ python3 -m venv venv
$ source venv/bin/activate
```

2. Install the required dependencies:
```
(venv) $ pip install -r requirements.txt
```

3. Set up the database:
```
(venv) $ psql
=# CREATE DATABASE warbler;
=# (control-d)
(venv) $ python seed.py
```

4. Create an `.env` file to hold the configuration:
```
.env»
SECRET_KEY=abc123
DATABASE_URL=postgresql:///warbler
```

5. Start the server:
```
(venv) $ flask run
```
**Note:** If you encounter an "address already in use" error, try running on port 5001 instead. Use the command `flask run -p 5001` to run on port 5001.

Feel free to explore the project and customize it as needed to suit your requirements.

If you have any questions or need further assistance, please contact the project maintainers.
