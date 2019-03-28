#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import cv2
import sys

PORT = 8080


class FaceCount(RequestHandler):
    def get(self):

        # Get user supplied values
        imagePath = "FaceDetect/abba.png"
        cascPath = "FaceDetect/haarcascade_frontalface_default.xml"

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Read the image
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
            # flags = cv2.CV_HAAR_SCALE_IMAGE
        )

        self.write("Found {0} faces!".format(len(faces)))


    def post(self):
        pass


def main():
    app = tornado.web.Application([
        (r'/count', FaceCount)
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
