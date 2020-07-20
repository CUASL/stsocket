from twython import TwythonStreamer
import time
import socket
import json
class TweetStreamer(TwythonStreamer):
    def on_success(self, data):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        localIP = '127.0.0.1'
        localPort = 3001
        
        text = ''
        
        text = data['text']
        jsontext = json.dumps(data)

        texttomatlab = jsontext.encode('utf-8')
        print('PYTHON SENT:/n ' + jsontext)
        
        s.connect((localIP, localPort))
        
        s.sendall(texttomatlab)
        list.append(jsontext)
    def on_error(self, status_code, data):
        print (status_code)
        self.disconnect()
consumer_key = 'X5gCNKpqL6NUsLvBJjIYIm4Pz'
consumer_secret = 'UrlJVaRjpWmZrMjmWH7uADCBCzXwdoceIWVv2ftC34z85wpmMR'
access_token = '1267471839929880577-ks8UGM7ydtxJ8xWJpHtv55tUCVGh7Z'
access_token_secret = 'QjKJ2FLe3R6gGtGD17lyBauOAqfptcnK75B5Sk8qZRSYN'

streamer = TweetStreamer(consumer_key, consumer_secret,access_token, access_token_secret)
BUFFER_SIZE = 1000000
list = []
streamer.statuses.filter(track = '#covid19')
