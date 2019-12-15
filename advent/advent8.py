#!usr/lib/python
import sys
from collections import Counter

# mmmm.. it feels like there is an easier way to do that
def add(layer1, layer2):
    result = []
    for i in range(0,len(layer1)):
        if layer1[i] == 2:
            result.append(layer2[i])
        elif layer2[i] == 2:
            result.append(layer1[i])
        else:
            result.append(layer1[i])
    return result


# the image you received is 25 pixels wide and 6 pixels tall, that means 150
if __name__=="__main__":
    f = open(sys.argv[1])
    layers = []
    layers_counter = []
    text = list(f.readline().strip())
    # now we have every single character
    # find all the layers

    text = map(int,text)

    layer = []
    for c in text:
        layer.append(c)
        if len(layer) == 150:
            # new layer
            layers_counter.append(Counter(layer))
            layers.append(layer)
            layer = []


    min_zeros = 100000000000
    min_layer = 678999
    k = 0

    for d in layers_counter:
        zeros = d.get('0')
        if zeros < min_zeros:
            min_zeros = zeros
            min_layer = k
        k = k +1

    #print layers_counter[min_layer]


    result = layers[0]

    for k in range(0, len(layers)-1):
        result = add(result, layers[k+1])

    # w = 25, h = 6
    # print a carriage return every 25th
    i = 1
    txt = ''
    result = map(str,result)
    for c in result:
        if c == '0':
            txt = txt + "."
        else :
            txt = txt + 'x'
        if i % 25 == 0:
            txt = txt + "\n"
        i = i + 1

    print txt





