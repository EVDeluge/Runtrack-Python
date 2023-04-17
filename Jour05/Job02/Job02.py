def draw_rectangle(width, height):
    print('+', end='')
    for i in range(width-2):
        print('-', end='')
    print('+')
    for i in range(height-2):
        print('|', end='')
        for j in range(width-2):
            print(' ', end='')
        print('|')
    print('+', end='')
    for i in range(width-2):
        print('-', end='')
    print('+')
width = int(input("Entrez la largeur du rectangle : "))
height = int(input("Entrez la hauteur du rectangle : "))
draw_rectangle(width, height)
