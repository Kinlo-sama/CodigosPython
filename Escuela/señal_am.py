import numpy as np
import math as mt 
m = float(input("m:"))
e_c = float(input("E_c:"))
f_c = float(input("f_c:"))
f_m = float(input("f_m:"))
n = float(input("n for fn:"))
f_n = n *( f_c + f_m )
inc = 1 / f_n
tot = 1 / f_m
usb = f_c + f_m
lsb = f_c - f_m
print(f"{'t(ms)':<5}  {'V_t':<5}  {'V_usb':<5}  {'V_lsb':<5}  {'V_am':<5}")
for i in np.arange(0,tot,inc):
	t = round(i*1000,2)
	s1= round(e_c * mt.sin(2 * mt.pi * f_c * i),2)
	s2= round(((e_c * m)/ 2) * mt.cos(2 * mt.pi * lsb * i),2)
	s3= round(-mt.cos(((e_c * m)/ 2) * mt.pi * usb * i),2)
	s_am= round((s1 +s2 + s3),2)
	print(f"{t:<5}  {s1:<5}  {s2:<5}  {s3:<5}  {s_am:<5}")
	input()
