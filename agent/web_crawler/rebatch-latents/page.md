[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[batch](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-batch "batch")Rebatch Latents
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Rebatch Latents
![comfyUI节点-Rebatch Latents｜重设Latent批次](https://comfyui-wiki.com/latent/batch/LatentBatch.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/rebatch-latents#documentation)
  * Class name: `RebatchLatents`
  * Category: `latent/batch`
  * Output node: `False`


The RebatchLatents node is designed to reorganize a batch of latent representations into a new batch configuration, based on a specified batch size. It ensures that the latent samples are grouped appropriately, handling variations in dimensions and sizes, to facilitate further processing or model inference.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/rebatch-latents#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latents` | `LATENT` | The ‘latents’ parameter represents the input latent representations to be rebatched. It is crucial for determining the structure and content of the output batch.  
`batch_size` | `INT` | The ‘batch_size’ parameter specifies the desired number of samples per batch in the output. It directly influences the grouping and division of the input latents into new batches.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/rebatch-latents#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a reorganized batch of latent representations, adjusted according to the specified batch size. It facilitates further processing or analysis.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-from-batch "Latent From Batch")[Repeat Latent Batch](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/repeat-latent-batch "Repeat Latent Batch")
Discover more
Stable diffusion
Workflow
ComfyUI
Wiki
Stable Diffusion
Flux.1
Artificial intelligence
Black Forest Labs
user interface
Interface
