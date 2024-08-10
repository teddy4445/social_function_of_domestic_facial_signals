import math

def euclidean_distance(landmark_a, landmark_b):
    """
    Calculate the Euclidean distance between two landmarks.

    Args:
    - landmark_a: A tuple (x, y) representing the coordinates of landmark A.
    - landmark_b: A tuple (x, y) representing the coordinates of landmark B.

    Returns:
    - The Euclidean distance between the two landmarks.
    """
    x1, y1 = landmark_a
    x2, y2 = landmark_b
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def area_of_quadrilateral(a, b, c, d):
    """
    Calculate the area of a quadrilateral given the coordinates of its vertices.

    Args:
    - a, b, c, d: Tuples (x, y) representing the coordinates of the vertices of the quadrilateral.

    Returns:
    - The area of the quadrilateral.
    """
    def shoelace_formula(coords):
        n = len(coords)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += coords[i][0] * coords[j][1]
            area -= coords[j][0] * coords[i][1]
        area = abs(area) / 2.0
        return area

    vertices = [a, b, c, d]
    return shoelace_formula(vertices)

def angle_between_landmarks(a, b, c):
    """
    Calculate the angle formed by the lines a-b and a-c.

    Args:
    - a, b, c: Tuples (x, y) representing the coordinates of the landmarks a, b, and c.

    Returns:
    - The angle in degrees at landmark a formed by the lines a-b and a-c.
"""
    ab = (b[0] - a[0], b[1] - a[1])
    ac = (c[0] - a[0], c[1] - a[1])

    
    dot_product = ab[0] * ac[0] + ab[1] * ac[1]

    magnitude_ab = math.sqrt(ab[0]**2 + ab[1]**2)
    magnitude_ac = math.sqrt(ac[0]**2 + ac[1]**2)

    cos_angle = dot_product / (magnitude_ab * magnitude_ac)

    angle = math.acos(cos_angle)
    angle_degrees = math.degrees(angle)

    return angle_degrees

def translate_landmarks_to_ratios(landmarks):
    """
    Translate the coordinates of the landmarks to distances and angles.

    Args:
    - landmarks: A list of tuples (x, y) representing the coordinates of the landmarks.

     Returns:
    - All ratios/distances and angles.

    """
    def distance(a, b):
        return euclidean_distance(landmarks[a-1], landmarks[b-1])

    def angle(a, b, c):
        return angle_between_landmarks(landmarks[a-1], landmarks[b-1], landmarks[c-1])/180

    def area(a, b, c, d):
        return area_of_quadrilateral(landmarks[a-1], landmarks[b-1], landmarks[c-1], landmarks[d-1])

    output = []

    ## eRatio1 is not valid

    eRatio2 = 1/3 * (distance(25, 30) / distance(27, 28) +
                     distance(24, 31) / distance(27, 28) +
                     distance(26, 29) / distance(23, 32))
    output.append(eRatio2)

    eRatio3 = 0.5 * (distance(23, 30) / distance(10, 6) +
                     distance(32, 25) / distance(10, 6))
    output.append(eRatio3)

    eRatio4 = 0.5 * (distance(24, 30) / distance(10, 6) +
                     distance(31, 25) / distance(10, 6))
    output.append(eRatio4)

    area_quad1 = area(26, 27, 28, 29)
    area_quad2 = area(23, 32, 9, 5)

    ePRatio1 = area_quad1 / area_quad2
    #ePRatio2 is not valid

    output.append(ePRatio1)

    eAngle1 = 0.5 * (angle(27, 25, 28) + angle(28, 27, 30))
    output.append(eAngle1)

    eAngle2 = 0.5 * (angle(27, 23, 25) + angle(28, 32, 30))
    output.append(eAngle2)

    eAngle3 = 0.5 * (angle(23, 25, 32) + angle(32, 30, 23))
    output.append(eAngle3)

    eAngle4 = 0.5 * (angle(23, 24, 31) + angle(32, 31, 24))
    output.append(eAngle4)

    ### EYES
    eyRatio0 = 0.5 * (distance(5, 6) / distance(7, 8) + distance(10, 9) / distance(11, 12))
    output.append(eyRatio0)

    eyRatio1 = 0.5 * (distance(37, 38) / distance(39, 4) + distance(41, 42) / distance(40, 2))
    output.append(eyRatio1)

    eyRatio2 = 0.5 * (distance(37, 38) / distance(5, 6) + distance(41, 42) / distance(9, 10))
    output.append(eyRatio2)

    eyRatio3 = 0.5 * (distance(39, 4) / distance(7, 8) + distance(40, 2) / distance(11, 12))
    output.append(eyRatio3)

    eyAngle1 = 0.5 * (angle(6, 7, 8) + angle(10, 11, 12) + angle(5, 7, 8) + angle(12, 9, 11))
    eyAngle2 = 0.5 * (angle(7, 6, 8) + angle(9, 10, 11))
    output.append(eyAngle1)
    output.append(eyAngle2)

    area_quad1 = area(5, 7, 6, 8)
    area_quad2 = area(10, 9, 11, 12)
    area_common = area(5, 8, 9, 5)
    area_quad3 = area(7, 11, 12, 8)
    area_quad4 = area(37, 39, 38, 4)
    area_quad5 = area(41, 40, 42, 2)

    eyPRatio1 = 0.5 * (area_quad1 / area_common + area_quad2 / area_common)
    eyPRatio2 = area_quad3 / area_common
    eyPRatio3 = 0.5 * (area_quad4/area_quad1 + area_quad5/area_quad2)
    output.append(eyPRatio1)
    output.append(eyPRatio2)
    output.append(eyPRatio3)

    ## MUZZLE

    mRatio1 = 0.5 * (distance(15, 21) / distance(15, 16) + distance(19, 16) / distance(15, 16))
    mRatio2 = 0.5 * (distance(47, 17) / distance(15, 16) + distance(48, 17) / distance(15, 16))
    mRatio3 = distance(17, 18) / distance(15, 16)
    mRatio4 = 0.5 * (distance(22, 17) / distance(17, 16) + distance(20, 17) / distance(17, 16))
    mRatio5 = distance(22, 20) / distance(18, 3)
    mRatio6 = 0.5 * (distance(33, 17) / distance(15, 16) + distance(36, 17) / distance(15, 16))
    mRatio7 = 0.5 * (distance(7, 8) / distance(3, 18) + distance(11, 12) / distance(3, 18))
    mRatio8 = 1/3 * (distance(43, 44) / distance(13, 14) +
                     distance(33, 36) / distance(34, 35) +
                     distance(47, 48) / distance(22, 20))

    area_large = area(33, 36, 20, 22)
    area_small = area(34, 35, 19, 21)
    area_bottom = area(47, 48, 20, 22)
    area_top = area(43, 44, 35, 34)
    mPRatio1 = 0.5 * (area_bottom / area_large + area_top / area_large)
    mPRatio2 = area_small / area_large

    mAngle1 = 0.5 * (angle(15, 18, 47) + angle(16, 18, 48))
    mAngle2 = angle(18, 21, 19)
    mAngle3 = 0.5 * (angle(18, 15, 21) + angle(18, 16, 19))

    output.append(mRatio1)
    output.append(mRatio2)
    output.append(mRatio3)
    output.append(mRatio4)
    output.append(mRatio5)
    output.append(mRatio6)
    output.append(mRatio7)
    output.append(mRatio8)
    output.append(mPRatio1)
    output.append(mPRatio2)
    output.append(mAngle1)
    output.append(mAngle2)
    output.append(mAngle3)

    return output
