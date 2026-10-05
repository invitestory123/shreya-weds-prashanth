import http.server
import socketserver
import sys
import os

class NoCacheThreadingHTTPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent browser aggressive caching of dev files
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        # Keep logs clean
        pass

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Starting Threaded HTTP Server on port {port}...")
    with NoCacheThreadingHTTPServer(("", port), CustomHandler) as httpd:
        print(f"Serving at http://localhost:{port}")
        httpd.serve_forever()
