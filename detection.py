import detectron2
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
import numpy as np

class Detector():
    def __init__(self, cfg_main):
        print("Initilizing detector.")
        self.cfg = get_cfg()
        self.cfg.merge_from_file(cfg_main["model_config"])
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = cfg_main["score_threshold"]
        self.class_id = cfg_main["class_id"]
        self.cfg.MODEL.WEIGHTS = cfg_main["model_weights"]
        self.predictor = DefaultPredictor(self.cfg)
        print("Initialization done.")

    def detect(self, frame: np.ndarray) -> detectron2.structures.Boxes:
        """"Detect objects in the frame.
        
        Args:
            frame: A video frame.
        
        Returns:
            Bounding boxes that contain objects.
        """

        boxes = self.predictor(frame)
        return boxes["instances"].to("cpu")

    def post_process(self, boxes: detectron2.structures.Boxes) -> detectron2.structures.Boxes:
        """"Post process the boxes, keep only target class.

        Args:
            boxes: Bounding boxes that contain objects.

        Returns:
            Post processed boxes.
        """

        if len(boxes) == 0:
            return boxes
        return boxes[boxes.pred_classes == self.class_id]
