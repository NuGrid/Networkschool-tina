# One-zone equilibrium i-process nucleosynthesis simulations in TINA

This project differs from the project `i-process`. It computes equilibrium abundances using the method
described in the notebook `Constant-neutron-density-method.ipynb`.

Start with the `Model-runner` notebook to run and save a simulation. Then use the `Result-Explorer` to plot a chart of isotopes. The `Rate-changer` notebook allows you to change reaction rates using multiplication factors for a new run.

Find more analysis notebooks in the folder `i-process/Notebooks`. Some of the
plots in those notebooks require reaction flux output which is by default turned off for new
runs. Turn it on by setting `iplot_flux_option = 1` in the input file
`ppn_frame.input`. 

**For advanced users:** The code can run in two modes. If `ININET  = 0` in the input file `ppn_physics.input` then a new network will be created with default choices for all reaction rates. This new generated network is written to the `networksetup.txt` file. The procedure described in the `Rate-Changer` notebook will apply changes of reaction rates in the `networksetup.txt` file. When run in mode `ININET  = 3` the code will read in the network from the current `networksetup.txt` file and not attempt to create a default. 
 
 This directory lives on Github: https://github.com/NuGrid/Networkschool-tina/tree/main/i-process-Nnconst
