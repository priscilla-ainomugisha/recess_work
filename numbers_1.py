#integers, floats, complex
w=10#int
r=3.0#float
s=2j #complex

print(type(w))
print(type(r))
print(type(s))

#Type conversions
w=10#int
r=3.9#float
s=2j #complex
#convert from int to complex
z=complex(w)
print(z)
print(type(z))
#convert from int to float
w_float = float(w)
print(w_float)
#convert from float to complex
r_complex = complex(r)
print(r_complex)
print(type(r_complex))
#convert from complex to float
#complex numbers cannot be directly converted into floats
# But the are rather converted to real for the rela part 
# and then the magnitude of the imaginary part got
s_real = s.real
print(s_real)

s_magnitude = abs(s)
print(s_magnitude)