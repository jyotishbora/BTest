# Create the proto stubs

run the build.sh script in /protos folds, which will generate the stubs and copy to be used for both grpc service and the rest api

# Run the grpc server

- cd to /grpc-service
```
- python3 ./server.py

```
# Run the client and connect to the server
```
python3 ./sample-client.py

```
# Run the API

cd to /rest-api

```
python3 ./blucora_rest_api.py

$ curl localhost:8000/taxreturn/
{
  "refund": "1000"
}

```

 # echo ${${GITHUB_REF#refs/heads/} != ${github.event.repository.default_branch}}
          # echo ${{ (GITHUB_REF#refs/heads/) != github.event.repository.default_branch }

