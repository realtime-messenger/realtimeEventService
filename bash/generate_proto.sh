python -m grpc_tools.protoc \
       -I ../src/proto \
       --python_out=../src/proto/pyproto \
       --pyi_out=../src/proto/pyproto \
       --grpc_python_out=../src/proto/pyproto ../src/proto/main.proto