import ffmpeg
import argparse
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("dir")
parser.add_argument("output")
args = parser.parse_args()

while True:
    time.sleep(1) # lazily sleep here
    for root, dirs, files in os.walk(args.dir):
        for filename in files:
            
            if not filename.lower().endswith("mov") and not filename.lower().endswith("mp4"):
                continue

            fullpath = os.path.join(root, filename)
            basename, ext = os.path.splitext(filename)
            print(f"processing {fullpath}")
            ffmpeg.input(fullpath).output(os.path.join(args.output, basename) + ".mp4").run()
            print(f"done")
            os.remove(fullpath)

