
# move the rover 
# return the label 

class RoverControl:
    def roverMove(self,size, cmds):
        now = [0, 0]
        map = dict()
        map['UP'] = [0, -1]
        map['DOWN'] = [0, 1]
        map['RIGHT'] = [1, 0]
        map ['LEFT'] = [-1, 0]

        for cmd in cmds:
            operation = map.get(cmd)

            #check validation
            x =now[0] + operation[0]
            y = now[1] + operation[1]
            if x < 0 or x >= size or y<0 or y>= size:
                continue
            else:
                now[0] = x
                now[1] = y

        return now[0] + now[1] * size

a = RoverControl()
now = a.roverMove(4, ["RIGHT", "DOWN", "LEFT", "LEFT", "DOWN"])
print(now)
