import ffmpeg
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()

while True:
    for root, dirs, files in os.walk(args.dir):
        for filename in files:
            
            if not filename.endswith("mov"):
                continue

            fullpath = os.path.join(root, filename)
            basename, ext = os.path.splitext(fullpath)
            print(f"processing {fullpath}")
            ffmpeg.input(fullpath).output(basename + ".mp4").run()
            print(f"done")
            os.remove(fullpath)

