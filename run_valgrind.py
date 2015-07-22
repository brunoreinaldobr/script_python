__author__ = 'bruno'

# coding=UTF-8

# import sys
import os

# images_filelist = sys.argv[2]
# print images_filelist

VALGRIND_CMD = 'valgrind'

JPEG_PATH = '/opt/jpeg-9a/'
JPEG_CMD = 'cjpeg'
IMAGES_PATH = JPEG_PATH + 'imagens/'

IMAGES_LIST = [
    'bolas.BMP',
    'disneyBMP.bmp',
    'RAY.BMP',
    'LAND2.BMP',
    'land.BMP',
    'LAND.BMP',
    'test_pattern_original.bmp',
    'metal.bmp'
]

OUTPUT_LIST = []

# valgrind --tool=cachegrind --cachegrind-out-file=jpeg.txt /opt/jpeg-9a/cjpeg
# -outfile /opt/jpeg-9a/imagens/saida.jpg entrada.jpg
# ----------------------------------------------------------------------------

cont = 1
y = 0
for image in IMAGES_LIST:
    command = 'touch jpeg' + str(cont) + '.txt && '
    command += VALGRIND_CMD + ' --tool=cachegrind '
    command += '--cachegrind-out-file=jpeg' + str(cont) + '.txt '  # saida do valgrind para cada imagem
    command += JPEG_PATH + JPEG_CMD
    command += ' -outfile ' + IMAGES_PATH + image[:-3] + 'jpg '
    command += IMAGES_PATH + image

    print (command)

    os.system(command)
    # ---------------------------------------------------------------------------
    arq = open('jpeg' + str(cont) + '.txt', 'r')
    lista = arq.readlines()
    arq.close()
    string = ""
    # string = "Execution;Ir;Dr;Dw;I1mr;D1mr;D1mw;I2mr;D2mr;D2mw;\n"
    for i in range(0, len(lista)):
        if 'summary' in lista[i]:
            image = IMAGES_LIST[y]
            # print image
            string += "jpeg_" + image[:-4] + ";"
            arq_sum = open('summary.txt', 'r')
            l = arq_sum.readlines()
            arq_sum.close()
            arq_sum = open('summary.txt', 'w')
            line = lista[i].split(" ")
            del line[0]  # apaga a palavra "summary:"
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
    y += 1

