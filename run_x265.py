__author__ = 'Bruno Reinaldo'

# coding=UTF-8

import os

VALGRIND_CMD = 'valgrind'

X265_PATH = '/home/bruno/x265/build/linux/'
X265_CMD = './x265'
VIDEOS_PATH = X265_PATH + 'videos/'

VIDEOS_LIST = [
    'BasketballDrive_1920x1080_50.yuv',
    'BQSquare_416x240_60.yuv'
    'BQTerrace_1920x1080_60.yuv',
    'Cactus_1920x1080_50.yuv',
    'Kimono1_1920x1080_24.yuv',
    'Traffic_2560x1600_30.yuv'
]

SEARCH_ALGORITHM = [
    'hex',
    'star'
]

SEARCH_AREA = [
    '32',
    '64',
    '96',
    '128'
]

I1 = [str(16 * 1024), '4', '64']
D1 = [str(16 * 1024), '4', '64']
LL = [str(64 * 1024 * 1024), '8', '64']

OUTPUT_LIST = []
# cd /home/bruno/x265/build/linux/
# valgrind --tool=cachegrind --cachegrind-out-file=video.txt ./x265 --input entrada.yuv --fps number_fps 
# --input-res LarguraxAltura --seek first_frame_to_encode --frames number_frames --me <hex> --merange
# --output saida.x265

# Callgrind:
# --I1 = <size>, <assoc>, <line>
# --D1 =
# --LL =

for algorithm in SEARCH_ALGORITHM:
    for search in SEARCH_AREA:
        cont = 1
        for video in VIDEOS_LIST:
            p = video.split('_')
            command = 'cd ' + X265_PATH + ' && '
            command += VALGRIND_CMD + ' --tool=callgrind '
            command += '--callgrind-out-file=x265_' + p[0] + '_' + algorithm + '_' + \
                       search + '-I1_16K_4_64-D1_16K_4_64-LL_64M_8_64.txt '
            command += '--I1=' + I1[0] + ',' + I1[1] + ',' + I1[2] + ' '
            command += '--D1=' + D1[0] + ',' + D1[1] + ',' + D1[2] + ' '
            command += '--LL=' + LL[0] + ',' + LL[1] + ',' + LL[2] + ' '
            command += X265_CMD
            command += ' --input ' + VIDEOS_PATH + video + ' --fps ' + video[-6:-4] + ' --input-res '
            command += p[1] + ' --frames 1 --me ' + algorithm + ' --merange ' + search + ' --output ' + p[0] + '.265'
            print(command)
            os.system(command)

            arq = open(X265_PATH + 'video' + str(cont) + '.txt', 'r')
            lista = arq.readlines()
            arq.close()
            string = ""
            for i in range(0, len(lista)):
                if 'summary' in lista[i]:
                    string = "x265_" + p[0] + '_' + algorithm + '_' + search + ';'
                    print(video)
                    arq_sum = open('summary.txt', 'r')
                    l = arq_sum.readlines()
                    arq_sum.close()
                    arq_sum = open('summary.txt', 'w')
                    line = lista[i].split(" ")
                    del line[0]
                    word = line[-1]
                    word = list(word)
                    del word[-1]
                    line[-1] = ''.join(word)
                    for w in range(0, len(line)):
                        if w == (len(line) - 1):
                            string += line[w] + ";\n"
                        else:
                            string += line[w] + ";"
                    l.append(string)
                    arq_sum.writelines(l)
                    arq_sum.close()
            cont += 1