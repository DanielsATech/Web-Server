#Web Server - Just for future needs.

"""Imports"""
from http.server import HTTPServer, BaseHTTPRequestHandler



"""Entrypoint"""
def main() -> None: 
    class TheServer(BaseHTTPRequestHandler): #Inherits BaseHTTPRequestHandler
        def do_GET(self):
            if self.path == '/': 
                self.path = '/index.html'
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                file_to_open = "404"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))


    httpd = HTTPServer(('localhost', 8080), TheServer) #Localhost running on port 8080
    httpd.serve_forever()


    

"""Run Entrypoint method"""
if __name__ == "__main__":
    main()
    
       


