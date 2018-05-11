           beginShape()
        for x in range(int(width*0.2), int(width*0.9),1):
            ypos = map(noise(x/100 + xoff, y/100 + yoff), 0, 1, -100, 100)
            if x< width*0.5:
                magnitude= p3map(x, width*0.1, width*0.5, 0,1)
            else:
                magnitude = map(x, width*0.5, width*0.9, 1, 0) 
            ypos *= magnitude
            if ypos > 0: ypos = 0
            vertex(x, ypos)
        endShape()
