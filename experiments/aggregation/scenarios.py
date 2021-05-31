from typing import Any, List, Mapping, Tuple


def experiment0(screensize: Mapping[int, Any]) -> Tuple[list, List[int], bool]:  # Single aggregation site
    """

    :param screensize:
    :param screensize: Mapping[int:
    :param Any]:

    """
    area_loc1 = [screensize[0] / 2.0, screensize[1] / 2.0]

    scale1 = [110, 110]  # assuming a 1000 by 1000 screen

    big = False

    return area_loc1, scale1, big
