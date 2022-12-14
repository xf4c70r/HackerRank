width  = int(input()) 
char = 'H'

#Upper Cone
for i in range(width):
    print((char*i).rjust(width-1)+char+(char*i).ljust(width-1))

#Upper Pillars
for i in range(width+1):
    print((char*width).center(width*2)+(char*width).center(width*6))

#Middle
for i in range((width+1)//2):
    print((char*width*5).center(width*6))    

#Lower Pillars
for i in range(width+1):
    print((char*width).center(width*2)+(char*width).center(width*6))    

#Lower Cone
for i in range(width):
    print(((char*(width-i-1)).rjust(width)+char+(char*(width-i-1)).ljust(width)).rjust(width*6))