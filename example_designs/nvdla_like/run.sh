#!/bin/bash
echo "Run Timeloop Simulation \a \n"
timeloop-mapper arch/*.yaml arch/components/*.yaml constraints/*.yaml mapper/mapper.yaml ../../layer_shapes/superpoint/superpoint_layer1.yaml -o output/layer1/
timeloop-mapper arch/*.yaml arch/components/*.yaml constraints/*.yaml mapper/mapper.yaml ../../layer_shapes/superpoint/superpoint_layer2.yaml -o output/layer2/
timeloop-mapper arch/*.yaml arch/components/*.yaml constraints/*.yaml mapper/mapper.yaml ../../layer_shapes/superpoint/superpoint_layer5.yaml -o output/layer5/
timeloop-mapper arch/*.yaml arch/components/*.yaml constraints/*.yaml mapper/mapper.yaml ../../layer_shapes/superpoint/superpoint_layer6.yaml -o output/layer6/
timeloop-mapper arch/*.yaml arch/components/*.yaml constraints/*.yaml mapper/mapper.yaml ../../layer_shapes/superpoint/superpoint_layer9.yaml -o output/layer9/
timeloop-mapper arch/*.yaml arch/components/*.yaml constraints/*.yaml mapper/mapper.yaml ../../layer_shapes/superpoint/superpoint_layer11.yaml -o output/layer11/
exit 0