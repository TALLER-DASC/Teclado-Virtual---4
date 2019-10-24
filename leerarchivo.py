rows = 0
cols = 0
teclado = []
#LEER EL ARCHIVO
fil=open("archivo.txt", "r")
fil.close
if fil.mode == 'r':
    #obtener el contenido
    lines = fil.readlines()
    c = 1
    l = 0
    #recorrer los renglones
    for line in lines:

        #encontrar el primer renglón
        if c == 1:
            row_col = line.split(' ')
            print(row_col[0], ' - ' , row_col[1])
            rows = int(row_col[0])
            cols = int(row_col[1])

        #encontrar las letras del teclado
        if c > 1 and c <= (rows+1):
            letters = list(line)
            letters.pop()
            print(letters)
            teclado.append(letters)

        if c == rows+2:
            word = line[:-1]
            print("Palabra a encontrar:",word)
            word += '*'

        c+=1

posX = 0
posY = 0
mov = 0
moves = []
Total = 0
temp = 0
for i in range(len(word)):
    for x in range(len(teclado)):
        for y in range(len(teclado[x])):
            if word[i] == teclado[x][y]:
                if posX < x:
                    mov = x - posX
                    posX = x
                    temp += mov
                    moves.append(mov)
                elif posX > x:
                    mov = posX - x
                    posX = x
                    temp += mov
                    moves.append(mov)
                if posY < y:
                    mov = y - posY
                    posY = y
                    temp += mov
                    moves.append(mov)
                elif posY > y:
                    mov = posY - y
                    posY = y
                    temp += mov
                    moves.append(mov)

Total = temp - 1
Total += len(word)
print("Total de movimientos: ",Total)
