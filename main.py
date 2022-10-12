import streamlink
import time
import subprocess
import sys


def main(argv):
    streamer_channel = argv[1]
    delay_sec = int(argv[2])
    stream_url = f"twitch.tv/{streamer_channel}"

    while True:
        print("-> Waiting stream up...")
        streams = {}
        while len(streams) == 0:
            time.sleep(delay_sec)
            try:
                streams = streamlink.streams(stream_url)
            except Exception as e:
                print(f"Exception: {e}")
                streams = {}
                print("-> Waiting stream up...")

        print("-> Start download stream :)")
        subprocess.call([
            "streamlink", "-o", "{author}-{id}-{time:%Y-%m-%d %H:%M:%S}.ts",
            stream_url, "best"]
        )
        time.sleep(delay_sec)


if __name__ == '__main__':
    main(sys.argv)
