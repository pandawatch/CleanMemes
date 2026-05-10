#!/usr/bin/env python3
"""Simple HTTP server for CleanMemes with CORS support for images."""

import http.server
import socketserver
import os
import sys
from pathlib import Path

PORT = int(os.environ.get('PORT', 3000))
HOST = os.environ.get('HOST', 'localhost')

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for images to support ZIP downloads
        if self.path.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
            self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    
    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def run_server():
    os.chdir(Path(__file__).parent)
    
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🚀 CleanMemes server running at http://{HOST}:{PORT}/")
            print("Press Ctrl+C to stop")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✋ Server stopped")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Try: PORT=3001 python3 server.py")
        else:
            print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    run_server()
