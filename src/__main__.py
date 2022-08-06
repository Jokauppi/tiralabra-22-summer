from mayavi import mlab
from noise import snoise2
import numpy as np

def main():
    
    map_options = {
        'size': 400,
        'octaves': 5
    }
    map_shape = (map_options["size"], map_options["size"])

    map_data = np.zeros(map_shape)

    for index in np.ndindex(map_shape):
        x, y = index
        map_data[x, y] = 10*(1 + snoise2(x, y, octaves=5))

    print(map_data)
    
    mlab.figure(size=(800, 800), bgcolor=(0, 0, 0))

    mlab.surf(map_data)

    mlab.show()

if __name__ == '__main__':
    main()