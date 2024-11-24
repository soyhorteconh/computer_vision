import cv2
import numpy as np

pts_left = np.array([
    [154,275],
    [213,271],
    [230,290],
    [320,275],
    [432,281],
    [477,278],
    [539,321],
    [107,266],
    [109,296],
    [106,326],
    [125,311],
    [162,297],
    [211,297],
    [260,297],
    [314,298],
    [368,298],
    [424,299],
    [477,300],
    [520,311],
    [532,299],
    [537,280],
    [78,306],
    [93,307],
    [124,280],
    [154,280],
    [163,272],
    [183,271],
    [212,281],
    [267,285],
    [310,284],
    [336,280],
    [349,291],
    [369,284],
    [400,287],
    [457,286],
    [483,283],
    [512,283],
    [537,280],
    [550,334],
    [551,320],
    [540,337],
    [539,353],
    [538,321],
    [538,279],
    [538,268],
    [509,17],
    [480,269],
    [487,326],
    [484,317],
    [266,315],
    [296,311],
    [321,312],
    [375,313],
    [401,312],
    [322,276],
    [214,373]
], dtype=np.float32)

# pts_left = np.array([
#     [530, 293],
#     [477, 308],
#     [477, 286],
#     [450, 283],
#     [528, 273],
#     [255, 308],
#     [139, 265],
#     [297, 286],
#     [297, 305],
#     [134, 310],
#     [318, 303],
#     [113, 292],
#     [340, 299],
#     [112, 314],
#     [347, 280],
#     [171, 292],
#     [371, 280],
#     [214, 292],
#     [235, 311],
#     [397, 280],
#     [251, 286],
#     [548, 315],
#     [210, 313],
#     [184, 312],
#     [159, 312],
#     [151, 285],
#     [548, 333],
#     [530, 294],
#     [479, 280],
#     [461, 281],
#     [444, 301],
#     [362, 289],
#     [381, 293],
#     [336, 300],
#     [420, 317],
#     [381, 313],
#     [401, 304],
#     [400, 278],
#     [423, 299],
#     [440, 282],
#     [484, 322],
#     [196, 280],
#     [111, 292],
#     [149, 299],
#     [157, 278],
#     [112, 272],
#     [91, 273],
#     [326, 302],
#     [305, 313],
#     [290, 295],
#     [173, 317],
#     [64, 266],
#     [215, 271],
#     [284, 314],
#     [131, 321],
#     [242, 290],
#     [111, 333],
#     [262, 277],
#     [237, 308],
#     [308, 295],
#     [130, 302],
#     [215, 310],
#     [328, 282]

# ], dtype=np.float32)

pts_center = np.array([
    [157, 51],
    [215,45],
    [234,65],
    [319,49],
    [422,46],
    [462,48],
    [521,85],
    [110,38],
    [111,70],
    [108,99],
    [128,83],
    [166,70],
    [214,70],
    [261,69],
    [312,69],
    [364,69],
    [414,68],
    [463,67],
    [500,77],
    [514,66],
    [517,48],
    [79,82],
    [93,80],
    [126,55],
    [157,53],
    [165,47],
    [186,46],
    [216,56],
    [268,57],
    [309,56],
    [333,53],
    [345,61],
    [365,55],
    [393,58],
    [445,56],
    [467,53],
    [494,51],
    [517,48],
    [532,97],
    [532,84],
    [521,100],
    [522,115],
    [519,85],
    [517,46],
    [518,36],
    [468,53],
    [465,39],
    [473,90],
    [470,83],
    [268,85],
    [297,82],
    [320,82],
    [371,82],
    [395,80],
    [319,49],
    [215,47]
], dtype=np.float32)

# pts_center = np.array([
#     [511, 60],
#     [464, 75],
#     [463, 55],
#     [437, 52],
#     [508, 42],
#     [257, 79],
#     [141, 39],
#     [296, 58],
#     [297, 75],
#     [138, 82],
#     [317, 73],
#     [115, 65],
#     [337, 69],
#     [116, 87],
#     [344, 51],
#     [174, 65],
#     [366, 51],
#     [217, 65],
#     [238, 82],
#     [389, 51],
#     [253, 59],
#     [529, 81],
#     [213, 84],
#     [188, 84],
#     [164, 84],
#     [155, 58],
#     [530, 98],
#     [511, 60],
#     [464, 50],
#     [448, 50],
#     [433, 69],
#     [358, 59],
#     [375, 63],
#     [333, 70],
#     [412, 84],
#     [376, 81],
#     [393, 73],
#     [392, 49],
#     [414, 68],
#     [429, 52],
#     [470, 87],
#     [199, 53],
#     [114, 66],
#     [152, 72],
#     [160, 51],
#     [115, 47],
#     [93, 49],
#     [325, 71],
#     [305, 83],
#     [290, 65],
#     [177, 89],
#     [67, 45],
#     [218, 45],
#     [285, 84],
#     [135, 93],
#     [245, 62],
#     [115, 105],
#     [263, 50],
#     [240, 79],
#     [308, 65],
#     [134, 74],
#     [219, 81],
#     [326, 54]	
	
# ], dtype=np.float32)

pts_right = np.array([
    [220, 69],
    [325,62],
    [429,60],
    [118,18],
    [63,44],
    [551,68]
], dtype=np.float32)

pts_center2 = np.array([
    [221, 309],
    [324,305],
    [427,304],
    [118,317],
    [60,335],
    [551,311]
], dtype=np.float32)

H_left2center, status1 = cv2.findHomography(pts_left, pts_center, cv2.RANSAC)

H_right2center, status2 = cv2.findHomography(pts_right, pts_center2, cv2.RANSAC)

print(H_left2center)
print(H_right2center)