import argparse
import os
import cv2
import yaml
from draw_boxes import draw_boxes
from detection import Detector

parser = argparse.ArgumentParser()
parser.add_argument("--p", dest="path", type=str, default="input_videos/People_Walk.mp4" , help="Specify the path to the video, either relative (e.g. input/People_Walk.mp4), or absolute (e.g. /home/username/Downloads/People_Walk.mp4).")
parser.add_argument("--save", action="store_true", help="Save movie with detections.")
parser.add_argument("--show", action="store_true", help="Show the detections while the algorithm runs.")
parser.add_argument("--c", dest="config_path",type=str, default="configs/main-config.yaml" , help="Specify the path to the yaml config, either relative (e.g. config_1.yaml), or absolute (e.g. /home/username/Downloads/config_1.yaml).")

def main(path: str, save: bool, show: bool, config_path: str) -> None:
    """Perform pedestrian detection on a video.

    Args:
        path: A path with filetype, e.g. video.mp4.
        save: If True, a video with detections will be saved.
        show: If True, the video with detections will be displayed.
        config_path: Path to a yaml config file.
    """

    with open (config_path, "r") as stream:
        cfg = yaml.safe_load(stream)
    os.makedirs(cfg["out_dir"], exist_ok=True)
    out_name = os.path.join(cfg["out_dir"], os.path.basename(path))

    # Set OpenCV settings
    cap = cv2.VideoCapture(path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(out_name, fourcc, 20.0, (width, height))

    detector = Detector(cfg)
    print("Starting detection...")
    processed = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect objects
        boxes = detector.detect(frame)
        boxes = detector.post_process(boxes)
        for box in boxes.pred_boxes:
            box = box.int().numpy()
            draw_boxes(frame, (box[0], box[1]), (box[2],box[3]))

        if save:
            out.write(frame)
        if show:
            cv2.imshow("frame", frame)
            cv2.waitKey(1)

        processed += 1
        if processed % 10 == 0:
            print(f"{processed:8} frames processed.")

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    args = parser.parse_args()
    main(args.path, args.save, args.show, args.config_path)
