from mayavi import mlab

def main():


    mlab.figure(size=(640, 800), bgcolor=(0.16, 0.28, 0.46))

    mlab.surf(data, warp_scale=0.2) 
    mlab.show()

if __name__ == '__main__':
    main()