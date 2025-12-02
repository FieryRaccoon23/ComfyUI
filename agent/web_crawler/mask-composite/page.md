[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing "Mask")Mask Composite
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Mask Composite
![comfyUI节点-MaskComposite|遮罩混合](https://comfyui-wiki.com/mask/MaskComposite.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/mask-composite#documentation)
  * Class name: `MaskComposite`
  * Category: `mask`
  * Output node: `False`


This node specializes in combining two mask inputs through a variety of operations such as addition, subtraction, and logical operations, to produce a new, modified mask. It abstractly handles the manipulation of mask data to achieve complex masking effects, serving as a crucial component in mask-based image editing and processing workflows.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/mask-composite#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`destination` | MASK | The primary mask that will be modified based on the operation with the source mask. It plays a central role in the composite operation, acting as the base for modifications.  
`source` | MASK | The secondary mask that will be used in conjunction with the destination mask to perform the specified operation, influencing the final output mask.  
`x` | INT | The horizontal offset at which the source mask will be applied to the destination mask, affecting the positioning of the composite result.  
`y` | INT | The vertical offset at which the source mask will be applied to the destination mask, affecting the positioning of the composite result.  
`operation` | COMBO[STRING] | Specifies the type of operation to apply between the destination and source masks, such as ‘add’, ‘subtract’, or logical operations, determining the nature of the composite effect.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/mask-composite#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | MASK | The resulting mask after applying the specified operation between the destination and source masks, representing the composite outcome.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/load-image-mask "Load Image \(as Mask\)")[Mask To Image](https://comfyui-wiki.com/en/comfyui-nodes/mask/mask-to-image "Mask To Image")
