To debug locally, first you have to launch the cloud sql auth proxy with this command:
```bash
./cloud_sql_proxy -instances=scenic-cedar-324901:us-west1:candid-postgresql=tcp:5432
```

Then in a separate window, export all the variables in env.sh with:
```bash
export $(cat env.sh | xargs)
```

Now you can launch the fastapi server with:
```bash
uvicorn test_fastapi:app --reload
```



(This is outdated now, see build-deploy below)
To deploy to cloud run, I currently am just using plain container deploy but I want to replace this with a cloud build script.  For now though you just have to run:
```bash
gcloud run deploy
```

For source code location just hit enter to use the current directory.
For service name use "candidapi" (also probably the default)
For region use "us-west-1"
If it asks to "allow unauthenticated invocations", respond "y"


You can check on the service here: https://console.cloud.google.com/run?project=scenic-cedar-324901




(Updated build/deploy)
Now I have a cloud build script that will automatically build the docker image, upload the container to the cloud registry and then deploy it to the candidapi service.  The build steps are in cloudbuild.yaml and the code to run the build/deploy is just:
```bash
gcloud builds submit
```

You can track build progress here: https://console.cloud.google.com/cloud-build/builds?project=scenic-cedar-324901.
You can see the container in the registry here: https://console.cloud.google.com/gcr/images/scenic-cedar-324901?project=scenic-cedar-324901




Secret Manager: cloud secret manager is used to store the postgres database password (and later other things).  Secrets are passed in as environment variables defined in the cloudbuild script.  Secrets for the project can be viewed here: https://console.cloud.google.com/security/secret-manager?project=scenic-cedar-324901.


Poetry: When building with poetry you have to first run the following otherwise it will ignore the poetry.lock file.
```bash
gcloud config set gcloudignore/enabled false
```


Instructions on deploying: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python
Instructions on setting up sql connection from cloud run: https://cloud.google.com/sql/docs/mysql/connect-run#command-line
Instructions on setting up sql auth proxy: https://cloud.google.com/sql/docs/postgres/connect-admin-proxy#connecting-client
Instructions on setting up cloudbuild.yaml: https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run
Instructions on secret manager: https://cloud.google.com/build/docs/securing-builds/use-secrets
