import os 
for i in range(600):
    os.system(f"cp ./prop/prop{i}.dat prop.dat")
    os.system("./main.e > shape")
    os.system(f"cp displacement ./disp1/displacement{i}")
    os.system(f"cp stressnode ./stress1/stressnode{i}")
