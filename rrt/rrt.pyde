largo = 600
ancho = 400
obstaculos = [[90, 150, 150], [300, 250, 100], [450, 100, 90]]
conf_inicial = [150, 250]
conf_final = [400, 230]
eta = 5
tol = 10
max_nodos = 1000
r_robot = 20
#arbol = [[conf_inicial[0], conf_inicial[1], -1]]
arbol = obstaculos

def colisiones(x, y):
    for obstaculo in obstaculos:
        if dist(x, y, obstaculo[0], obstaculo[1]) < r_robot + obstaculo[2] / 2:
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

def calc_xnew(index_near, xrand, yrand):
    xnear = arbol[index_near][0]
    ynear = arbol[index_near][1]
    norma = dist(xnear, ynear, xrand, yrand)
    xnew = int(xnear + eta * (xrand - xnear) / norma)
    ynew = int(ynear + eta * (yrand - ynear) / norma)
    if colisiones(xnew, ynew) == False:
        return [xnew, ynew, index_near]
    else:
        return "colision"
    
def add_nodo(index_near, xrand, yrand):
    qnew = calc_xnew(index_near, xrand, yrand)
    if qnew != "colision":
        arbol.append(qnew)
        if dist(qnew[0], qnew[1], conf_final[0], conf_final[1]) < tol:
            return "Reached"
        else:
            return "Advanced"
    else:
        return "No se agrega qnew"

"""
def add_nodo(xnear, ynear, index_near, xrand, yrand, arbol, eta, r):
    norma = dist(xnear, ynear, xrand, yrand)
    #print(norma)
    if norma != 0.0:
        xnew = xnear + eta * (xrand - xnear) / norma
        ynew = ynear + eta * (yrand - ynear) / norma
    if colisiones(xnew, ynew, r, arbol) == False:
        arbol.append([int(xnew), int(ynew), index_near])
        if dist(xnew, ynew, conf_final[0], conf_final[1]) <= eta:
            return "Reached"
    else:
        return "Advanced"
    
def build_rrt(conf_inicial, conf_final, eta, max_nodos, r):
    arbol = [[conf_inicial[0], conf_inicial[1], -1]]
    k = 1
    while k < max_nodos:
        print(k)
        xrand = int(random(1, largo))
        yrand = int(random(1, ancho))
        pnear_index = nearest_neighbor(xrand, yrand, arbol)
        continuar = add_nodo(arbol[pnear_index][0], arbol[pnear_index][1], pnear_index, xrand, yrand, arbol, eta, r)
        print(continuar)
        if continuar == "Reached":
            return arbol
        elif continuar == "Advanced":
            k += 1
    print("No se alcanzó")
    return arbol
"""    

def setup():
    size(largo, ancho)
    circle(conf_inicial[0], conf_inicial[1], 20)
    circle(conf_final[0], conf_final[1], 20)
    for obstaculo in obstaculos:
        circle(obstaculo[0], obstaculo[1], obstaculo[2])
    
    #xrand = int(random(0, largo))
    #yrand = int(random(0, ancho))
    #circle(xrand, yrand, r_robot * 2)
    # Prueba de nearest_neighbor
    #print(nearest_neighbor(xrand, yrand, obstaculos))
    # Prueba del paso eta
    #nuevo = calc_xnew(0, xrand, yrand)
    #arbol.append(nuevo)
    #circle(nuevo[0], nuevo[1], 5)
    # Prueba de add_nodo
    #nuevo = nearest_neighbor(conf_final[0], conf_final[1], obstaculos)
    #print(nuevo, add_nodo(nuevo, conf_final[0], conf_final[1]))
    # Prueba de colisiones
    #print(colisiones(xrand, yrand))
    
    #arbolito = build_rrt(conf_inicial, conf_final, eta, max_nodos, radio_robot)
