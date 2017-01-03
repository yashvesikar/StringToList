#Given string that we would like to split up into its component words
string = 'shoeboxmynameisyashIlikeCheeseandfish'

#Assume that some dictionary D is given that contains a large list of words including the words from within the string
D = ['he', 'hello','my','name','is','yash', "house",'shoebox','shoe','box','ox']

empty_string = ''


def p(string,dictionary):
    #This function finds the words within some given string given a 'dictionary' and a string
    if string == '':
        return string
    
    #This algorithm will find the longest possible word. 
    #i.e. shoe and shoebox are both in the tring and dictionary, however shoebox will be in the output
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
