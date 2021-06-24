import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--f", dest="filename", type=str, default="input_videos/People_Walk.mp4" , help="Specify the path to the video, either relative (e.g. input/People_Walk.mp4), or absolute (e.g. /home/username/Downloads/People_Walk.mp4).")
parser.add_argument("--show", type=bool, default=True, help="Show the detections while the algorithm runs.")
parser.add_argument("--save", type=bool, default=False, help="Save movie with detections.")
parser.add_argument("--c", dest="config",type=str, default="config_1.json" , help="Specify the path to the config, either relative (e.g. config_1.json), or absolute (e.g. /home/username/Downloads/config_1.json).")

def main(filename: str, show: bool, save: bool, config: str):
    print(filename, show, save, config)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args.filename, args.show, args.save, args.config)