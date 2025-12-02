[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[advanced](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-add "advanced")Latent Multiply
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Latent Multiply
![comfyUI节点-LatentMutiply-Latent相乘](https://comfyui-wiki.com/latent/advanced/LatentMutiply.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-multiply#documentation)
  * Class name: `LatentMultiply`
  * Category: `latent/advanced`
  * Output node: `False`


The LatentMultiply node is designed to scale the latent representation of samples by a specified multiplier. This operation allows for the adjustment of the intensity or magnitude of features within the latent space, enabling fine-tuning of generated content or the exploration of variations within a given latent direction.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-multiply#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The ‘samples’ parameter represents the latent representations to be scaled. It is crucial for defining the input data on which the multiplication operation will be performed.  
`multiplier` | `FLOAT` | The ‘multiplier’ parameter specifies the scaling factor to be applied to the latent samples. It plays a key role in adjusting the magnitude of the latent features, allowing for nuanced control over the generated output.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-multiply#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a modified version of the input latent samples, scaled by the specified multiplier. This allows for the exploration of variations within the latent space by adjusting the intensity of its features.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-interpolate "Latent Interpolate")[Latent Subtract](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-subtract "Latent Subtract")
Discover more
Stable diffusion
ComfyUI
AI
Flux
FLUX
Sdxl
FLUX.1
Wiki
interface
SDXL
