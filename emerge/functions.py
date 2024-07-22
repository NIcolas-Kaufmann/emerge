import numpy as np 
from scipy.interpolate import griddata
import os 





#Read the data 

def read_data(file_name = None):
    
    if(file_name == None):
     # Get the path of the directory where this script is located
        module_dir = os.path.dirname(__file__)
        # Construct the full path to the file
        file_path = os.path.join(module_dir, "data.dat")
    else:
        file_path = file_name

    grid = np.genfromtxt(fname=file_path,names=True)

    return grid 






#
def t_embryo(grid,r0,M_star,flux_peb,M_em_fact,mode="trans"):
    names = ["r0","M_star","flux_peb","M_em_fact"]
    x0 = [r0,M_star,flux_peb,M_em_fact]
    x_p = np.vstack((grid[name] for name in names))

    
    if(mode == "trans"):
        f_p = grid["t_trans"]
    elif(mode == "moon"):
        f_p = grid["t_moon"]
    elif(mode == "1e-3"):
        f_p = grid["1e-3"]
    else:
        raise ValueError("unknown mode")
    
    f_p = np.maximum(f_p,1e-2)
    y_p = np.log(f_p)
    return np.exp(griddata(x_p.T,y_p,x0,rescale=True,method= "linear"))






    
