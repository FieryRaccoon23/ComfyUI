[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")model-mergingCheckpoint Save
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Checkpoint Save
![comfyUI节点-CheckpointSave|保存模型-](https://comfyui-wiki.com/advanced/model_merging/CheckpointSave.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save#documentation)
  * Class name: `CheckpointSave`
  * Category: `advanced/model_merging`
  * Output node: `True`


The CheckpointSave node is designed for saving the state of various model components, including models, CLIP, and VAE, into a checkpoint file. This functionality is crucial for preserving the training progress or configuration of models for later use or sharing.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The model parameter represents the primary model whose state is to be saved. It is essential for capturing the current state of the model for future restoration or analysis.  
`clip` | `CLIP` | The clip parameter is intended for the CLIP model associated with the primary model, allowing its state to be saved alongside the main model.  
`vae` | `VAE` | The vae parameter is for the Variational Autoencoder (VAE) model, enabling its state to be saved for future use or analysis alongside the main model and CLIP.  
`filename_prefix` | `STRING` | This parameter specifies the prefix for the filename under which the checkpoint will be saved, providing a means to organize and identify saved checkpoints.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save#output-types)
This node will output a checkpoint file, and the corresponding output file path is `output/checkpoints/` directory
## Checkpoint Save workflow example[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save#checkpoint-save-workflow-example)
For a workflow example of this node, please refer to: [Model Merging Workflow Example](https://comfyui-wiki.com/en/workflows/model-merging) Load the image below into ComfyUI to view the complete workflow:
  * First, enable the `CheckpointSave` node in the workflow, and load the models you want to merge in the two `Load Checkpoint` nodes
  * Generate an image once
  * Find the generated file in the `output/checkpoints/` directory
  * You can install the generated file as a new checkpoint in the `models\checkpoints\` folder, and then use a text-to-image workflow to check the results

![Example](https://comfyui-wiki.com/examples/model_merging/model_merging_basic.png)
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/rescale-cfg "Rescale CFG")[CLIPMerge Simple](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/clip-merge-simple "CLIPMerge Simple")
Discover more
Stable Diffusion
Wiki
Stable diffusion
ComfyUI
workflow
Workflow
Black Forest Labs
FLUX
user interface
stable diffusion
