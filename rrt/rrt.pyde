largo = 600
ancho = 400
obstaculos = [[90, 150, 150], [300, 250, 100], [450, 100, 90]]
conf_inicial = [150, 250]
conf_final = [400, 230]
arbolito = [[conf_inicial[0], conf_inicial[1], -1]]
eta = 2
max_nodos = 1000

def colisiones(x, y, r, obstaculos):
    for obstaculo in obstaculos:
        if dist(x, y, obstaculo[0], obstaculo[1]) < r + obstaculo[2] / 2:
            return True
    return False

def nearest_neighbor(x, y, arbol):
    dist_min = dist(0, 0, largo, ancho)
    indice = 0
    for nodo in arbol:
        dist_new = dist(x, y, nodo[0], nodo[1])
        if dist_new < dist_min:
            dist_min = dist_new
            indice = arbol.index(nodo)
    return indice

def add_nodo(xnear, ynear, index_near, xrand, yrand, arbol, eta):
    norma = dist(xnear, ynear, xrand, yrand)
    xnew = xnear + eta * (xrad - xnear) / norma
    ynew = ynear + eta * (yrad - ynear) / norma
    arbol.append([int(xnew), int(ynew), index_near])

def setup():
    size(largo, ancho)
    circle(conf_inicial[0], conf_inicial[1], 20)
    circle(conf_final[0], conf_final[1], 20)
    for obstaculo in obstaculos:
        circle(obstaculo[0], obstaculo[1], obstaculo[2])
    
    xrand = int(random(0, width))
    yrand = int(random(0, height))
    circle(xrand, yrand, 80)
    print(nearest_neighbor(xrand, yrand, obstaculos))
