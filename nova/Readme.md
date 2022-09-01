# One-zone nova nucleosynthesis simulations in TINA

Start with the `Model-runner` notebook to run and save a simulation. Then use the `Result-Explorer` to plot a chart of isotopes. The `Rate-changer` notebook allows you to change reaction rates by using multiplication factors for a new run.

Find more analysis notebooks in the folder `Notebooks`. Some of the
plots in those notebooks require reaction flux output which is by default turned off for new
runs. Turn it on by setting `iplot_flux_option = 1` in the input file
`ppn_frame.input`. 

The `master-result` folder does contain the default reference output including flux data. It is available as a compressed archive `tina-nova-master-result.tgz` in `/data/nugrid-data/projects/tina` which is also accessible via the Globus endpoint `astrohub#nugrid:/data/projects/tina`. To extract this zipped tar archive you need to use the terminal, navigate into the correct run directory and issue the command
```Shell
tar -xzvf /data/nugrid_data/projects/tina/tina-nova-master-result.tgz 
```



In the file `run_me.sh` you can select different nova cases that use their corresponding trajectories (the peak temperature and density as functions of time) and initial abundances that were taken from the following reference:

[Denissenkov P.A., Truran J.W., Pignatari M., Trappitsch R., Ritter C., Herwig F., Battino U., Setoodehnia K., Paxton B. 2014. MESA and NuGrid simulations of classical novae: CO and ONe nova nucleosynthesis. Monthly Notices of the Royal Astronomical Society. 442:2058.](https://ui.adsabs.harvard.edu/abs/2014MNRAS.442.2058D/abstract)

**For advanced users:** The code can run in two modes. If `ININET  = 0` in the input file `ppn_physics.input` then a new network will be created with default choices for all reaction rates. This new generated network is written to the `networksetup.txt` file. The procedure described in the `Rate-Changer` notebook will apply changes of reaction rates in the `networksetup.txt` file. When run in mode `ININET  = 3` the code will read in the network from the current `networksetup.txt` file and not attempt to create a default. 
 
 This directory lives on Github: https://github.com/NuGrid/Networkschool-tina/tree/main/nova
