[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[batch](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-batch "batch")Repeat Latent Batch
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Repeat Latent Batch
![comfyUI节点-Repeat Latent batch|复制Latent批次](https://comfyui-wiki.com/latent/batch/Rebatch_Latents.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/repeat-latent-batch#documentation)
  * Class name: `RepeatLatentBatch`
  * Category: `latent/batch`
  * Output node: `False`


The RepeatLatentBatch node is designed to replicate a given batch of latent representations a specified number of times, potentially including additional data like noise masks and batch indices. This functionality is crucial for operations that require multiple instances of the same latent data, such as data augmentation or specific generative tasks.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/repeat-latent-batch#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The ‘samples’ parameter represents the latent representations to be replicated. It is essential for defining the data that will undergo repetition.  
`amount` | `INT` | The ‘amount’ parameter specifies the number of times the input samples should be repeated. It directly influences the size of the output batch, thereby affecting the computational load and the diversity of the generated data.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/repeat-latent-batch#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a modified version of the input latent representations, replicated according to the specified ‘amount’. It may include replicated noise masks and adjusted batch indices, if applicable.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/rebatch-latents "Rebatch Latents")[Set Latent Noise Mask](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/set-latent-noise-mask "Set Latent Noise Mask")
Discover more
Stable Diffusion
Stable diffusion
ComfyUI
Flux.1
user interface
Wiki
Comfy
FLUX.1
AI
SDXL
