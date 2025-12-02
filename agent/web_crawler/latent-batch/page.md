[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")batchLatent Batch
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Latent Batch
![comfyUI节点-LatentBatch｜Latent组合批次](https://comfyui-wiki.com/latent/batch/Repeat_Latent_batch.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-batch#documentation)
  * Class name: `LatentBatch`
  * Category: `latent/batch`
  * Output node: `False`


The LatentBatch node is designed to merge two sets of latent samples into a single batch, potentially resizing one set to match the dimensions of the other before concatenation. This operation facilitates the combination of different latent representations for further processing or generation tasks.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-batch#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples1` | `LATENT` | The first set of latent samples to be merged. It plays a crucial role in determining the final shape of the merged batch.  
`samples2` | `LATENT` | The second set of latent samples to be merged. If its dimensions differ from the first set, it is resized to ensure compatibility before merging.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-batch#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The merged set of latent samples, now combined into a single batch for further processing.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-subtract "Latent Subtract")[Latent From Batch](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-from-batch "Latent From Batch")
Discover more
ComfyUI
Stable Diffusion
Stable diffusion
Wiki
Workflow
Sdxl
Comfy
AI
SDXL
FLUX.1
