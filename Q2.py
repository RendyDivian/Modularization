def translate(text):
    newtext=""          
    for letter in text:         
        if letter not in 'aeiou':   
            newtext=newtext+letter+'o'+letter  
        else:       
            newtext=newtext+letter      
    return newtext      

text=input('Write: ')       
print (translate(text))




