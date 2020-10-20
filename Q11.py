def char_freq(str):
    frequency = {}

    for i in str:
        if i in frequency:
           frequency[i] = int(frequency.get(i)) +1
        else:
               frequency[i]=1
        return frequency
    
print(char_freq("Some words"))
