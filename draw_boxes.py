import cv2
from typing import Tuple

def draw_boxes(frame, point_1: Tuple[int, int], point_2: Tuple[int, int], color: Tuple[int, int] = (0,0,255), line_thickness: int = 2, line_type: int = 1):
    """Draw bounding boxes on frame.

    Args:
        frame: A video frame.
        point_1: One of the corner points of the rectangle.
        point_2: Diagonally opposite coner point from point_1.
        color: Optional; if not provided line color is red.
        line_thickness: Optional; line thickness in pixels.
        line_type: Optional; line type.

    Returns:
        Frame with bounding boxes on it.
    """
    return cv2.rectangle(frame, point_1, point_2, color, line_thickness, line_type)
