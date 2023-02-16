## Setup
`$ python -m venv venv` \
`$ pip install -r requirements.txt` \
`$ prefect config set PREFECT_ORION_DATABASE_CONNECTION_URL="sqlite+aiosqlite:////<path_to_repo>/prefect-example/database/orion.db" # instead of using default database location: ~/.prefect/orion.db`

## Run flow
In `flows/`, run the python file to run the flow.

## Web console
`$ prefect orion start`
