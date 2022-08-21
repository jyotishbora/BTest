from concurrent import futures
from email import message
import grpc
import json
import logging
import bluecora_tax_service_pb2 as tax_messages
import bluecora_tax_service_pb2_grpc as tax_service


class TaxService(tax_service.TaxServicer):
  
    def CalculateTaxReturn(self, request, context):
        logging.info(f'Caculating Tax return for {request.firstname} for the state of {request.state}')
        return tax_messages.TaxRefundResponse(refund=1920)
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tax_service.add_TaxServicer_to_server(TaxService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Server is starting")
    serve()