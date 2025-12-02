[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[advanced](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-add "advanced")Latent Subtract
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Latent Subtract
![comfyUI节点-LatentSubtract-Latent相减](https://comfyui-wiki.com/latent/advanced/LatentSubtract.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-subtract#documentation)
  * Class name: `LatentSubtract`
  * Category: `latent/advanced`
  * Output node: `False`


The LatentSubtract node is designed for subtracting one latent representation from another. This operation can be used to manipulate or modify the characteristics of generative models’ outputs by effectively removing features or attributes represented in one latent space from another.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-subtract#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples1` | `LATENT` | The first set of latent samples to be subtracted from. It serves as the base for the subtraction operation.  
`samples2` | `LATENT` | The second set of latent samples that will be subtracted from the first set. This operation can alter the resulting generative model’s output by removing attributes or features.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-subtract#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The result of subtracting the second set of latent samples from the first. This modified latent representation can be used for further generative tasks.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-multiply "Latent Multiply")[Latent Batch](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-batch "Latent Batch")
Discover more
Flux.1
Wiki
User interface
ComfyUI
Sdxl
user interface
SDXL
stable diffusion
Stable diffusion
Comfy
