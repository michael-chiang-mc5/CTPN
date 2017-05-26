<<<<<<< HEAD
# MUST be imported first
=======
# MUST be imported firstly
>>>>>>> 510ef4a828eb89f43ae812ea60e9bc05755c3e37
import sys
import numpy as np

class Config:
    MEAN=np.float32([102.9801, 115.9465, 122.7717])
    TEST_GPU_ID=0
    SCALE=600
    MAX_SCALE=1000

    LINE_MIN_SCORE=0.6 # originally 0.7
    TEXT_PROPOSALS_MIN_SCORE=0.7
    TEXT_PROPOSALS_NMS_THRESH=0.3
    MAX_HORIZONTAL_GAP=50
    TEXT_LINE_NMS_THRESH=0.3
    MIN_NUM_PROPOSALS=0 # originally 2
    MIN_RATIO=0.9 # originally 1.2
    MIN_V_OVERLAPS=0.6 # originally 0.7
    MIN_SIZE_SIM=0.6 # originally 0.7
    TEXT_PROPOSALS_WIDTH=16

def init():
    sys.path.insert(0, "./tools")
    sys.path.insert(0, "./caffe/python")
    sys.path.insert(0, "./src")
init()

