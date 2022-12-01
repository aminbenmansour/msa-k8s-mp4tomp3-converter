import pika, json, tempfile, os
from bson.objectid import ObjectId
import moviepy.editor

def start(message, fs_videos, fs_mp3s, channel):
    message = json.loads(message)

    # empty temp file
    tf = tempfile.NamedTemporaryFile()
    # video contents
    out = fs_videos.get(ObjectId(message["video_fid"]))
    # add video contents to emty file
    tf.write(out.read())
    # create audio from temp video file
    audio = moviepy.editor.VideoFileClip(tf.name).audio
    tf.close()
