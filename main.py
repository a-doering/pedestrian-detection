import argparse
import os
import cv2
from draw_boxes import draw_boxes

parser = argparse.ArgumentParser()
parser.add_argument("--f", dest="filename", type=str, default="input_videos/People_Walk.mp4" , help="Specify the path to the video, either relative (e.g. input/People_Walk.mp4), or absolute (e.g. /home/username/Downloads/People_Walk.mp4).")
parser.add_argument("--save", action="store_true", help="Save movie with detections.")
parser.add_argument("--show", action="store_true", help="Show the detections while the algorithm runs.")
parser.add_argument("--c", dest="config",type=str, default="config_1.json" , help="Specify the path to the config, either relative (e.g. config_1.json), or absolute (e.g. /home/username/Downloads/config_1.json).")

def main(filename: str, show: bool, save: bool, config: str) -> None:
    """Perform pedestrian detection on video.

    Args:
        filename: A filename with ending, e.g. video.mp4.
        show: If True, the video with detections will be displayed.
        save: If True, a video with detections will be saved.
        config: Path to a config file.
    """
    out_dir = "output_videos"
    os.makedirs(out_dir, exist_ok=True)
    out_name = os.path.join(out_dir, filename)

    # Set OpenCV settings
    cap = cv2.VideoCapture(filename)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(out_name, fourcc, 20.0, (width,height))

    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i > 50:
            break
        if show:
            cv2.imshow("frame", frame)
            cv2.waitKey(1)

        # TODO: use model to detect, somthing like
        # boxes = detect(frame)
        # for box in boxes:
        #     (x, y, w, h) = [int(val) for val in box]
 		#     draw_boxes(frame, (x, y), (x + w, y + h))           

        point_1 = (300, 300)
        point_2 = (0, 100)
        draw_boxes(frame, point_1, point_2)
        if save:
            print(i)
            i+=1
            out.write(frame)

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    args = parser.parse_args()
    main(args.filename, args.show, args.save, args.config)
