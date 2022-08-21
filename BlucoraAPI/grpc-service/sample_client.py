
from __future__ import print_function

import logging
import grpc
import bluecora_tax_service_pb2 as tax_messages
import bluecora_tax_service_pb2_grpc as tax_service

class TaxClient(object):
    def __init__(self):
        self.host='localhost'
        self.port='50051'      

    def run(self):
        with grpc.insecure_channel('{}:{}'.format(self.host,self.port)) as channel:
            stub = tax_service.TaxStub(channel)
            request=tax_messages.TaxRefundRequest(firstname='jyotish',lastname='bora',state='IL',annual_income=100000)
            response = stub.CalculateTaxReturn(request)
        print(f"You are receiving a refund of : ${response.refund}" )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client=TaxClient()
    client.run()
    
