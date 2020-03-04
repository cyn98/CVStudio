# ./build/examples/openpose/openpose.bin --video ~/openpose/demo1.mov --write_json ~/openpose/output/demo1 --write_video ~/openpose/output/demo1.avi --render_pose 1 --write_images ~/openpose/output/demo1 --keypoint_scale 4

import json

def appendZeros(i):
    if (i < 10): return '00' + str(i)
    elif (i < 100): return '0' + str(i)
    else: return str(i)

clap = True
clapDist = 0.022
clapDistReset = 0.03
for i in range(85):
    f = open('clap/demo1_000000000' + appendZeros(i) + '_keypoints.json')
    data = json.load(f)
    joints = data['people'][0]['pose_keypoints_2d']
    wrist1X = joints[3*3]
    wrist1Y = joints[3*3+1]
    wrist2X = joints[3*7]
    wrist2Y = joints[3*7+1]
    dist = (wrist1X-wrist2X)**2+(wrist1Y-wrist2Y)**2
    if dist <= clapDist and clap:
        clap = False
        print('clap')
    elif dist >= clapDistReset:
        clap = True
