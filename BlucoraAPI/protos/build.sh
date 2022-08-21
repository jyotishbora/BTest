
DESTDIR='gen-py'
mkdir -p $DESTDIR
python3 -m grpc_tools.protoc \
        --proto_path=. \
        --python_out=$DESTDIR \
        --grpc_python_out=$DESTDIR \
          *.proto
cp -a ./gen-py/. ../grpc-service
cp -a ./gen-py/. ../rest-api