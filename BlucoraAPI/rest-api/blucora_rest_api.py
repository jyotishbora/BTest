from flask import Flask,Response
import grpc
from google.protobuf.json_format import MessageToJson
import bluecora_tax_service_pb2 as tax_messages
import bluecora_tax_service_pb2_grpc as tax_service

app = Flask(__name__)

@app.route("/taxrefund")
def calculate_refund():
    with grpc.insecure_channel('localhost:50051') as channel:
            stub = tax_service.TaxStub(channel)
            request=tax_messages.TaxRefundRequest(firstname='jyotish',lastname='bora',state='IL',annual_income=100000)
            response = stub.CalculateTaxReturn(request)
            jsonResponse=MessageToJson(response);
            return Response(jsonResponse, content_type='application/json')
        
        
if __name__== '__main__':
    app.run(host="localhost",port=8000)
