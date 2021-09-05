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



To deploy to cloud run, I currently am just using plain container deploy but I want to replace this with a cloud build script.  For now though you just have to run:
```bash
gcloud run deploy
```

For source code location just hit enter to use the current directory.
For service name use "candidapi" (also probably the default)
For region use "us-west-1"
If it asks to "allow unauthenticated invocations", respond "y"


You can check on the service here: https://console.cloud.google.com/run?project=scenic-cedar-324901


Instructions on deploying: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python
Instructions on setting up sql connection from cloud run: https://cloud.google.com/sql/docs/mysql/connect-run#command-line
Instructions on setting up sql auth proxy: https://cloud.google.com/sql/docs/postgres/connect-admin-proxy#connecting-client
