## Example Designs for Timeloop-Accelergy Evaluation System

This folder contains some baseline implementations of an Eyeriss-like architecture,a NVDLA-like architecture, and a TPU-like architecture.

### System requirement

In order to run the example designs, you need to be either inside a docker with installed tools
(e.g., [infrastructure docker](https://github.com/Accelergy-Project/accelergy-timeloop-infrastructure)
or manually install the Accelergy-Timeloop evaluation system.

### File Structure

- example_designs:
  - architecture descriptions, compound component descriptions,
    constraints descriptions, mapper descriptions for the example designs.
  - note that for each architecture, we have 2 constraint files:
    1. \*\_arch_constraints.yaml describes the necessary hardware and dataflow constraints
    2. \*\_map_constraits.yaml describes the map space optimizations for the designs
- layer_shapes:
  - Example workloads: AlexNet, VGG01, VGG02 from original Timeloop example.
  - superpoint: A workload of [Superpoint network](https://github.com/magicleap/SuperPointPretrainedNetwork)
- scripts
  - A set of scripts for generating your own workloads in Timeloop format
  - Instructions:
    - `cd scripts`
    - modify the `cnn_layers.py` file to describe your own workload
    - `python3 construct_workloads.py <my_dnn_model_name>`

### Run simulations

To run a simulation using timeloop-accelergy system you should `cd` to the specific design's folder and run timeloop
simulations on a specific workload

Here is an example for running AlexNet Layer1 on the `simple_weight_stationary` architecture:

```
cd example_designs/eyeriss_like
timeloop-mapper arch/eyeriss_like.yaml arch/components/*.yaml constraints/*.yaml mapper/mapper.yaml ../../layer_shapes/superpoint/superpoint_layer1.yaml
```

The order of these yaml file doesn't matter, just make sure that you have included all the design files.

You may also use the `-o` flag to specify the output directory.

You will see the following outputs generated:

- timeloop-mapper.accelergy.log: accelergy's runtime info while generating the ERT.
- timeloop-mapper.ART.yaml: the area reference table generated by Accelergy for the architecture
- timeloop-mapper.ART_summary.yaml: the area reference table for the components as well as the associated plug-ins used for generating the outputs.
- timeloop-mapper.ERT.yaml: the energy reference table generated by Accelergy for the architecture.
- timeloop-mapper.ERT_summary.yaml: the energy reference table for the components as well as the associated plug-ins used for generating the outputs.
- timeloop-mapper.flattened_architecture.yaml: the fully defined and flattened architecture interpreted by Accelergy.
- timeloop-mapper.log: timeloop runtime info.
- timeloop-mapper.map.txt: the best mapping found by Timeloop mapper.
- timeloop-mapper.stats.txt: the runtime behaviors of the components in the design generated by Timeloop.
- timeloop-mapper.ma+stats.xml: the raw information generated by Timeloop -- you don't need to read into it.

If you prefer to run the simulation in background without the interactive thread updates, please trun of the `live-status` flag in
`mapper/mapper.yaml` in each design folder.

** Note that for the provided designs and workloads, your simulation should generally converge within 30 mins. Once you see
the simulations converging, you can press `ctrl + C` to manually stop them. They sometimes will take much longer to
automaticaly stop as we set the converging criteria to be pretty high to avoid early-stop with subooptimal mappings.
Please use you own judgement. **

### Related reading

- [eyeriss-like design](https://people.csail.mit.edu/emer/papers/2017.01.jssc.eyeriss_design.pdf)

- [timeloop-accelergy tutorial](https://accelergy.mit.edu/tutorial.html)
- [installation instructions for Timeloop](https://accelergy.mit.edu/infra_instructions.html)
- [timeloop source code](https://github.com/NVlabs/timeloop)
- [timeloop docs](https://timeloop.csail.mit.edu/)

- [NVDLA docs](http://nvdla.org/hw/v1/ias/unit_description.html?fbclid=IwAR09tlno4CsLmlO4REsiY_OMe-JT1drAXP2miMFCl5SlUpW1R30O_L-EO1M)