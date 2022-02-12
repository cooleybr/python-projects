from flask import Flask,request
from pymongo import MongoClient
import werkzeug.serving
import requests
import ssl
import OpenSSL

app = Flask(__name__)

class PeerCertWSGIRequestHandler( werkzeug.serving.WSGIRequestHandler ):
        """
        We subclass this class so that we can gain access to the connection
        property. self.connection is the underlying client socket. When a TLS
        connection is established, the underlying socket is an instance of
        SSLSocket, which in turn exposes the getpeercert() method.
        The output from that method is what we want to make available elsewhere
        in the application.
        """
        def make_environ(self):
            """
            The superclass method develops the environ hash that eventually
            forms part of the Flask request object.
            We allow the superclass method to run first, then we insert the
            peer certificate into the hash. That exposes it to us later in
            the request variable that Flask provides
            """
            environ = super(PeerCertWSGIRequestHandler, self).make_environ()
            x509_binary = self.connection.getpeercert(True)
            x509 = OpenSSL.crypto.load_certificate( OpenSSL.crypto.FILETYPE_ASN1, x509_binary )
            environ['peercert'] = x509
            return environ

app_key = '/app/certs/server.key'
app_key_password = None
app_cert = '/app/certs/server.pem'
ca_cert = '/app/certs/ca.pem'
ssl_context = ssl.create_default_context( purpose=ssl.Purpose.CLIENT_AUTH, cafile=ca_cert )
ssl_context.load_cert_chain( certfile=app_cert, keyfile=app_key, password=app_key_password )
ssl_context.verify_mode = ssl.CERT_REQUIRED


@app.route('/')
def index():
  client_cert=request.environ['peercert']
  return "got server"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, ssl_context=ssl_context, request_handler=PeerCertWSGIRequestHandler)
