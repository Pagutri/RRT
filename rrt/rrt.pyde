obstaculos = [[90, 150, 150], [300, 250, 100], [450, 100, 90]]
conf_inicial = [150, 250]
conf_final = [400, 230]

def distancia(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def colision(x1, y1, r1, x2, y2, r2):
    if distancia(x1, y1, x2, y2) < r1 + r2:
        print(distancia(x1, y1, x2, y2), r1 + r2)
        return True
    else:
        return False

def setup():
    size(600, 400)
    circle(conf_inicial[0], conf_inicial[1], 20)
    circle(conf_final[0], conf_final[1], 20)
    for obstaculo in obstaculos:
        circle(obstaculo[0], obstaculo[1], obstaculo[2])
    
    xrand = int(random(0, width))
    yrand = int(random(0, height))
    circle(xrand, yrand, 80)
    colision(xrand, yrand, 40, obstaculos[0][0], obstaculos[0][1], obstaculos[0][2] // 2)
