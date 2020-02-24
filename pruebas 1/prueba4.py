print
u'Programa para la resolución dados cinco puntos x y y.'
print
u'Determinar cuál es el más cercano al primero.'
print
u'Escribe cero(0) en el primero, para salir.'
while True:
    try:
        from math import sqrt

        x1 = int(raw_input('Escribe el eje de x1: '))
        y1 = float(raw_input('Escribe el eje de y1: '))
        x2 = float(raw_input('Escribe el eje de x2: '))
        y2 = float(raw_input('Escribe el eje de y2: '))
        x3 = float(raw_input('Escribe el eje de x3: '))
        y3 = float(raw_input('Escribe el eje de y3: '))
        x4 = float(raw_input('Escribe el eje de x4: '))
        y4 = float(raw_input('Escribe el eje de y4: '))
        x5 = float(raw_input('Escribe el eje de x5: '))
        y5 = float(raw_input('Escribe el eje de y5: '))

        xy1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        xy2 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        xy3 = sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        xy4 = sqrt((x1 - x5) ** 2 + (y1 - y5) ** 2)

        candidato = xy1
        if x1 == 0:
            break
        if candidato > xy2:
            candidato = xy2
        if candidato > xy3:
            candidato = xy3
        if candidato > xy4:
            candidato = xy4

        if candidato == xy1:
            masCerca = x2, y2
        if candidato == xy2:
            masCerca = x3, y3
        if candidato == xy3:
            masCerca = x4, y4
        if candidato == xy4:
            masCerca = x5, y5
        print
        u'El punto más cercano a x1 = {0} y y1 = {1} es: {2}'.format(x1, y1, masCerca)
    except ValueError:
        print
        u'No puedes dejar la entrada en blanco, ni escribir letras.'