import numpy as np
from typing import List

import math
import random
import pygame
from typing import Any, Mapping, Tuple

"""
Useful vector transformation functions, and other to make the code more clear 
"""


def area(a, b: float):
    """

    :param a: object mid point
    :param b: scale
    :param b: float: 

    """
    if b < a:
        max = a + 0.5 * b
        min = a - 0.5 * b
    else:
        max = a + 0.25 * b
        min = a - 0.25 * b
    return min, max


def generate_coordinates(screensize) -> List[float]:
    """

    :param screensize: 

    """
    return [
        float(random.randrange(0, screensize[0])),
        float(random.randrange(0, screensize[1])),
    ]


def dist(a, b) -> float:
    """return the distance between two vectors

    :param a: np.array
    :param b: np.array

    """
    return norm(a - b)


def image_with_rect(filename, scale: Mapping[int, Any]) -> Tuple[Any, Any]:
    """

    :param filename: param scale:
    :param scale: Mapping[int: 
    :param Any]: 

    """
    _image = pygame.image.load(filename)
    _image = pygame.transform.scale(_image, (scale[0], scale[1]))  # 10,8
    return _image, _image.get_rect()


def randrange(a, b) -> Any:
    """Random number between a and b.

    :param a: param b:
    :param b: 

    """
    return a + np.random.random() * (b - a)


def plusminus() -> int:
    """ """
    # random 1 or -1
    return 1 if (random.random() > 0.5) else -1


def rotate(vector: Mapping[int, Any]) -> Any:
    """

    :param vector: 
    :param vector: Mapping[int: 
    :param Any]: 

    """
    new_vector = np.zeros(2)
    theta = np.deg2rad(random.randint(150, 210))
    cs = np.cos(theta)
    sn = np.sin(theta)
    new_vector[0] = vector[0] * cs - vector[1] * sn
    new_vector[1] = vector[0] * sn + vector[1] * cs
    return new_vector


def normalize(vector) -> Any:
    """Function to normalize a vector
    ----------
    param vector : np.array

    :param vector: 

    """
    n = norm(vector)
    if n < 1e-13:
        return np.zeros(2)
    else:
        return np.array(vector) / n


def truncate(vector, max_length, min_lenght=None) -> Any:
    """Truncate the length of a vector to a maximum/minimum value.

    :param vector: param max_length:
    :param min_lenght: Default value = None)
    :param max_length: 

    """
    n = norm(vector)
    if n > max_length:
        return normalize(vector) * max_length
    elif min_lenght is not None and n < min_lenght:
        return normalize(vector) * min_lenght
    else:
        return vector


def norm(vector) -> float:
    """Compute the norm of a vector.

    :param vector: 

    """
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)


def speedvector(max_speed) -> List[int]:
    """

    :param max_speed: 

    """
    return [
        random.randrange(1, max_speed * 2 + 1) * plusminus(),
        random.randrange(1, max_speed * 2 + 1) * plusminus(),
    ]


def relative(u, v) -> List[int]:
    """

    :param u: param v:
    :param v: 

    """
    return [int(u[i]) - int(v[i]) for i in range(len(u))]
