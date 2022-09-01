# One-zone X-ray burst (XRB) nucleosynthesis simulations in TINA

Start with the `Model-runner` notebook to run and save a simulation. Then use the `Result-Explorer` to plot a chart of isotopes. The `Rate-changer` notebook allows you to change reaction rates using multiplication factors for a new run.

The model run program is `ppn.exe`. It takes the peak temperature and density as functions of time from an XRB model `trajectory.input` file. You can use one of the two available XRB model trajectories, either `trajectory.input.xrb_mesa` that was extracted from an XRB `MESA` model (https://github.com/dpa1983/canpan_projects/blob/main/xrb_rp_process/README_xrb.md), or 
`trajectory.input.xrb_example` from the NuGrid example `ppn_XRB_K04` that was taken from https://ui.adsabs.harvard.edu/abs/2004ApJ...603..242K/abstract. Choose one of these files and copy it to `trajectory.input` before running `./ppn.exe`.

**For advanced users:** The code can run in two modes. If `ININET  = 0` in the input file `ppn_physics.input` then a new network will be created with default choices for all reaction rates. This new generated network is written to the `networksetup.txt` file. The procedure described in the `Rate-Changer` notebook will apply changes of reaction rates in the `networksetup.txt` file. When run in mode `ININET  = 3` the code will read in the network from the current `networksetup.txt` file and not attempt to create a default. 
 
 This directory lives on Github: https://github.com/NuGrid/Networkschool-tina/tree/main/nova
