def gcd(a,b) : #Acidemis algorithm
    if (a==0) :
        return b 
    return (gcd(b%a,a));
def lcm(a,b) : # a x b = lcm x gcd
    return ((a*b)/gcd(a,b))
print(lcm(15,20))