string = 'shoeboxmynameisyashIlikeCheeseandfish'

D = ['he', 'hello','my','name','is','yash', "house",'shoebox','shoe','box',]

empty_string = ''


def p(string,dictionary):
    if string == '':
        return string
    
    i = 0
    words = []    
    while i <len(string):
        i+=1
        if string[i:] in D:
            words.append(string[i:])
            string = string[:i]
            i = 0
    
    if string in D:
        words.append(string)
    words.reverse()
    return words 


print(p(string,D) )    
