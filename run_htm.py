__author__ = 'bruno'

import os

VALGRIND_CMD = 'valgrind'

HTM_PATH = '/opt/HTM-dev/bin/'
HTM_CMD = 'TAppEncoderStatic'
CFG_PATH = '../cfg/MV-HEVC/'

# valgrind --tool=memcheck --cachegrind-out-file=htm.txt ./opt/HTM-dev/bin/TAppEncoderStatic
# -c ../cfg/MV-HEVC/baseCfg_3view.cfg -c ../cfg/MV-HEVC/

VIDEO_LIST = [
    'baseCfg_3view.cfg',
    'baseCfg_3view_outro.cfg'
]

cont = 1
for video in VIDEO_LIST:
    command = 'touch htm' + str(cont) + '.txt && '
    command += VALGRIND_CMD + '--tool=memcheck '
    command += '--cachegrind-out-file=htm' + str(cont) + '.txt '
    command += '.' + HTM_PATH + HTM_CMD
    command += '-c ../cfg/MV-HEVC/' + video + ' -c ../cfg/MV-HEVC/seqCfg_Shark.cfg'

    print(command)

    os.system(command)
