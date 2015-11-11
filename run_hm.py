__author__ = 'bruno'

import os

VALGRIND_CMD = 'valgrind'

HM_PATH = '/opt/HM-dev/'
HM_CMD = './TAppEncoderStatic'
VIDEOS_PATH = '/opt/'

VIDEOS_LIST = [
    'Shark_1.yuv',
    'Shark_5.yuv',
    'Shark_9.yuv',
    'MicroWorld_1.yuv',
    'MicroWorld_5.yuv',
    'MicroWorld_9yuv'
]

OUTPUT_LIST = []

# valgrind --tool=memcheck --cachegrind-out-file=hm.txt ./TAppEncoderStatic -c
# ../cfg/encoder_randomaccess_main.cfg -c ../cfg/per-sequence/