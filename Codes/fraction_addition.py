#take inputs
f1_nume = int(input('Enter the numerator for 1st fraction :'))
f1_deno = int(input('Enter the denominator for the 1st fraction :'))
f2_nume = int(input('Enter the numerator for 2nd fraction :'))
f2_deno = int(input('Enter the denominator for the 2nd fraction :'))
#check if denominators are same
if(f1_deno == f2_deno):
    #add numerator
    Fraction = f1_nume + f2_nume
    #print
    print('Addition of two fractions are :' + str(Fraction) + '/' + str(f1_deno))
#if denominators are not same    
else:
    #to find the sum
    #denominators should be same
    #apply cross Multiplication
    Fraction = (f1_nume * f2_deno) + (f2_nume * f1_deno)
    print('Addition of fractions are :' + str(Fraction) + '/' + str(f1_deno * f2_deno))
