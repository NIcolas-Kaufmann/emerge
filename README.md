# Emerge: A Python Package for Planetesimal Formation Simulations
Emerge is a lightweight Python package designed to provide the data from Kaufmann+(2024) (in prep) to infere the time of embryo formation with a simple interpollation routine. 

## Installation
First, clone the repository, then install the necessary dependencies using pip:
```
pip install . 
```
## Usage

1. **read_data(file_name=None)**
This function reads the simulation data from a file and returns it as a NumPy structured array. By default, it reads from a file named data.dat located in the data directory of the package, but you can also specify a custom file path.

Parameters:

file_name (optional): The path to the data file. If not provided, the default file data/data.dat is used.
Returns:

A NumPy structured array containing the simulation results.



2. **t_embryo(grid, r0, M_star, flux_peb, M_em_fact, mode="trans")**
This function computes the time at which the largest planetesimal in the simulation grid reaches a specific transition mass, such as the Moon mass or 1e-3 Earth masses. The calculation is performed using logarithmic interpolation based on the provided parameters.

Parameters:

grid: The data grid returned by the read_data() function.
r0: Semi-major axis. [AU]
M_star: Stellar mass. [$M_\odot$]
flux_peb: Pebble flux. [$M_\oplus$/Myr]
M_em_fact: Embryo factor.
mode (optional): The transition mode for which to calculate the timing. Options include:
"trans": Time when the largest planetesimal reaches the transition mass $M_{tr}$.
"moon": Time when the largest planetesimal reaches Moon mass $\sim 10^{-3} M_\oplus$ .
"1e-3": Time when the largest planetesimal reaches $10^{-3} M_\oplus$.

Returns:

A float representing the interpolated time for the specified mode.

## Example:
```
from emerge import read_data, t_embryo

#Load simulation data
grid = read_data()

# Calculate the time when the largest planetesimal reaches the transition mass
time_to_transition = t_embryo(grid, r0=5.2, M_star=1.0, flux_peb=0.01, M_em_fact=0.5, mode="trans")
```

## Contact:
For further inquiries or issues, please open an issue on the GitHub repository



