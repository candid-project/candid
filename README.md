# Candid

#### Repo for the Candid Project

## Set Up

To install all pre-commit hooks and poetry dependencies for the first time, run:

```sh
$ make local-setup
```

You can then run the pre-commit hooks on all files:

```sh
$ pre-commit run --all-files
```


## Testing

You can run linting and coverage tests with the following two commands:

```sh
$ make lint
$ make coverage
```

You must pass all linting checks and pytest tests in order to commit and you must have a test coverage over 80% to push.


## Running locally

env_template.sh provides a template for the connection environment variables you need.  Follow instructions in db/ to setup a local postgres db and/or use the cloud_sql_proxy (instructions in src/candid_api/README.md).  I keep two copies, one for a local db connection and the other for gcloud connection via the cloud_sql_proxy.

To launch candid_api run:
```sh
poetry run gunicorn src.candid_api.test_fastapi:app -c src/candid_api/gunicorn_config.py
```


## Deploy

Follow the guide here to setup up gcloud command-line tool: https://cloud.google.com/sdk/docs/quickstart.

Before deploying you must run (Probably a way around this):

```sh
gcloud config set gcloudignore/enabled false
```

To deploy, from the repo root, run:
```sh
gcloud builds submit
```

You can track build progress here: https://console.cloud.google.com/cloud-build/builds?project=scenic-cedar-324901.
