[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing "Mask")Feather Mask
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Feather Mask
![comfyUI节点-FeatherMask|遮罩羽化](https://comfyui-wiki.com/mask/FeatherMask.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/feather-mask#documentation)
  * Class name: `FeatherMask`
  * Category: `mask`
  * Output node: `False`


The FeatherMask node applies a feathering effect to the edges of a given mask, smoothly transitioning the mask’s edges by adjusting their opacity based on specified distances from each edge. This creates a softer, more blended edge effect.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/feather-mask#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | MASK | The mask to which the feathering effect will be applied. It determines the area of the image that will be affected by the feathering.  
`left` | INT | Specifies the distance from the left edge within which the feathering effect will be applied.  
`top` | INT | Specifies the distance from the top edge within which the feathering effect will be applied.  
`right` | INT | Specifies the distance from the right edge within which the feathering effect will be applied.  
`bottom` | INT | Specifies the distance from the bottom edge within which the feathering effect will be applied.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/feather-mask#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | MASK | The output is a modified version of the input mask with a feathering effect applied to its edges.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/crop-mask "Crop Mask")[Grow Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/grow-mask "Grow Mask")
Discover more
ComfyUI
Workflow
Wiki
Stable Diffusion
Stable diffusion
Black Forest Labs
Artificial intelligence
Sdxl
AI
Flux
