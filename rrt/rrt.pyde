obstaculos = [[90, 150, 150], [300, 250, 100], [450, 100, 90]]
conf_inicial = [150, 250]
conf_final = [400, 230]

def colisiones(x, y, r, obstaculos):
    for obstaculo in obstaculos:
        if dist(x, y, obstaculo[0], obstaculo[1]) < r + obstaculo[2] / 2:
            print(dist(x, y, obstaculo[0], obstaculo[1]), r + obstaculo[2] / 2)
            return True
    print("No hay colision")
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
    colisiones(xrand, yrand, 40, obstaculos)
