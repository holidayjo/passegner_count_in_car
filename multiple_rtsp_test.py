import numpy as np
import subprocess as sp
import threading
import queue
import time

class CCTVReader(threading.Thread):
    def __init__(self, q, in_stream, chunk_size):
        super().__init__()
        self.q = q
        self.chunk.size = chunk_size
        self.command = ["ffmpeg",
                        "-c:v", "h264",     # Tell FFmpeg that input stream codec is h264
                        "-i", in_stream,    # Read stream from file vid.264
                        "-c:v", "copy",     # Tell FFmpeg to copy the video stream as is (without decoding and encoding)
                        "-an", "-sn",       # No audio an no subtitles
                        "-f", "h264",       # Define pipe format to be h264
                        "-"]                # Output is a pipe
        