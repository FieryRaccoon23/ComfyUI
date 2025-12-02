[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing "Mask")Grow Mask
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Grow Mask
![comfyUI节点-GrowMask|遮罩扩展](https://comfyui-wiki.com/mask/GrowMask.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/grow-mask#documentation)
  * Class name: `GrowMask`
  * Category: `mask`
  * Output node: `False`


The GrowMask node is designed to modify the size of a given mask, either expanding or contracting it, while optionally applying a tapered effect to the corners. This functionality is crucial for dynamically adjusting mask boundaries in image processing tasks, allowing for more flexible and precise control over the area of interest.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/grow-mask#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | MASK | The input mask to be modified. This parameter is central to the node’s operation, serving as the base upon which the mask is either expanded or contracted.  
`expand` | INT | Determines the magnitude and direction of the mask modification. Positive values cause the mask to expand, while negative values lead to contraction. This parameter directly influences the final size of the mask.  
`tapered_corners` | BOOLEAN | A boolean flag that, when set to True, applies a tapered effect to the corners of the mask during modification. This option allows for smoother transitions and visually appealing results.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/grow-mask#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | MASK | The modified mask after applying the specified expansion/contraction and optional tapered corners effect.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/feather-mask "Feather Mask")[Image Color To Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/image-color-to-mask "Image Color To Mask")
Discover more
ComfyUI
AI
SDXL
Artificial intelligence
Flux.1
FLUX
FLUX.1
Sdxl
User interface
Stable Diffusion
