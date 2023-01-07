# [TPU](https://ieeexplore.ieee.org/document/9351692)\_like design discription file for [Timeloop](https://github.com/Accelergy-Project/accelergy-timeloop-infrastructure) simulator

## To run simulator

```bash
timeloop-mapper arch/*.yaml arch/components/*.yaml constraints/*.yaml mapper/*.yaml ['problems'] -o output/ -v 1
```

Please refer to the [TimeLoop-Accelergy-exercises](https://github.com/Accelergy-Project/timeloop-accelergy-exercises/tree/master/workspace/baseline_designs/layer_shapes) for `problems` design example, or simply refer to the `run.sh` for simulation on Superpoint network.

## TPU_like design

This design is based on the TPUv2 Training Chips developed by Google, with similar dataflow (weight-stationary) used in the [systolic array](https://cloud.google.com/blog/products/ai-machine-learning/an-in-depth-look-at-googles-first-tensor-processing-unit-tpu) of TPU.  
All the parameters of hardware size (buffer size, word-bits, ... etc.) follows the TPUv2 design (not the original TPU). Therefore, the word-bits is 16 rather than 8.

## Other Useful Links

- [timeloop-accelergy tutorial](https://accelergy.mit.edu/tutorial.html)
- [installation instructions for Timeloop](https://accelergy.mit.edu/infra_instructions.html)
- [timeloop source code](https://github.com/NVlabs/timeloop)
- [timeloop docs](https://timeloop.csail.mit.edu/)
