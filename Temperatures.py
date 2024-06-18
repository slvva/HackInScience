def fahrenheit_to_celsius(temp):
    C=(temp-32)*5/9
    return C

def celsius_to_fahrenheit(temp):
    F=temp*9/5+32
    return F
    
temp=100   
print(fahrenheit_to_celsius(temp))
print(celsius_to_fahrenheit(temp))
