from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    # request successful and you'll get your response
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return

"""
- if the request is correct and there are no problem : 200 ok
- if request is not correct or sth wrong from client side : 4XX,  404-> not found, 403-> forbidden
- if  response or sth wrong in the server side : 5xx, 500 
"""    