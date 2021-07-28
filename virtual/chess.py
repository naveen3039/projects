from itertools import product
def vaild_move_or_not(piece,currentpos,nextpos):
    if currentpos[0] or nextpos[0] == 'a':
        pos,pos1 = 0,0
    if currentpos[0] or nextpos[0] == 'b':
        pos,pos1 = 1,1
    if currentpos[0] or nextpos[0] == 'c':
        pos,pos1=2,2
    if currentpos[0] or nextpos[0] == 'd':
        pos,pos1=3,3
    if currentpos[0] or nextpos[0] == 'e':
        pos,pos1=4,4
    if currentpos[0] or nextpos[0] == 'f':
        pos,pos1=5,5
    if currentpos[0] or nextpos[0] == 'g':
        pos,pos1=6,6
    if currentpos[0] or nextpos[0] == 'h':
        pos,pos1=7,7
    nextpos = (pos1,int(nextpos[1])-1)
    if piece == 'Knight':
        x, y = pos,int(currentpos[1])-1
        moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
        moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
        nextpos = (pos1,int(nextpos[1])-1)
        if nextpos in moves:
            return True
        else:
            return False
    if piece == 'Bishop':
        def sign(z):
            if z >= 0:
                return 1  
            else:
                return -1
        l, m = pos,int(currentpos[1])-1
        c,n = pos1,int(nextpos[1])-1
        if l!=m and  n!=c  and abs(l-m)==abs(c-n): 
            dl = sign(m - l)
            dc = sign(n - c)
            x, y = c + dc, l + dl
            while x != n and y != m:
                x += dc
                y += dl
            return True
        return False
    return True
print(vaild_move_or_not('Knight','a1','a2'))