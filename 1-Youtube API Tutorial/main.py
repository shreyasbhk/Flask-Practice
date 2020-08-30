# Python REST API Tutorial - Building a Flask REST API 
#  https://video.hukkeri.org/watch?v=GMppyAPbLYk

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)

videos = {}

def abort_if_video_not_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")


def abort_if_video_exist(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID...")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_not_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        abort_if_video_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self, video_id):
        abort_if_video_not_exist(video_id)
        del videos[video_id]
        return '', 204
        

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
    
"""
- 2
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, "/video/<int:video_id>")

- 1
names = {"tim": {"age": 19, "gender": "male"},
         "bill": {"age": 70, "gender": "male"},}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    
    def post(self):
        return {"data": "Posted"}
    
api.add_resource(HelloWorld, "/helloworld/<string:name>")

"""

