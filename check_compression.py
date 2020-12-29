import numpy as np 
import matplotlib.pyplot as plt 
import math

def twos_complement(hexstr,bits):
    value = int(hexstr,16)
    if value & (1 << (bits-1)):
        value -= 1 << bits
    return value

# --------- ------- ------- FPGA --------- ------- -------
file = 'log2_output.txt'
f = open(file, 'r')
datalines = [line for line in f]
fpga_data = [twos_complement(p,8) for p in datalines]
fpga_in = [fpga_data[i] for i in range(0,len(fpga_data),2)]
print(fpga_in)
fpga_out = [fpga_data[i] for i in range(1,len(fpga_data),2)]
#print(fpga_in_data.index(119074))
# --------- ------- ------- compress --------- ------- -------
python_cm = [np.uint64(round(math.log2(fi) * 64)) for fi in fpga_in]
#print(python_cm[15])
# --------- ------- ------- FPGA --------- ------- -------
#file = 'log2_output.txt'
#f = open(file, 'r')
#datalines = [line for line in f]
#fpga_out_data = [twos_complement(p,64) for p in datalines]
#print(fpga_out_data[15])

diff = [np.abs(pi) - np.abs(fi) for pi,fi in zip(python_cm, fpga_out)]
plt.plot(diff)
plt.show()
plt.close()