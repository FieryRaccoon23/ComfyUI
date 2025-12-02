[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")Conditioning (Set Area)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Conditioning (Set Area)
![comfyUI节点-Conditioning\(Set Area\)｜条件采样区域](https://comfyui-wiki.com/conditioning/Conditioning\(Set_Area\).jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area#documentation)
  * Class name: `ConditioningSetArea`
  * Category: `conditioning`
  * Output node: `False`


This node is designed to modify the conditioning information by setting specific areas within the conditioning context. It allows for the precise spatial manipulation of conditioning elements, enabling targeted adjustments and enhancements based on specified dimensions and strength.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The conditioning data to be modified. It serves as the base for applying spatial adjustments.  
`width` | `INT` | Specifies the width of the area to be set within the conditioning context, influencing the horizontal scope of the adjustment.  
`height` | `INT` | Determines the height of the area to be set, affecting the vertical extent of the conditioning modification.  
`x` | `INT` | The horizontal starting point of the area to be set, positioning the adjustment within the conditioning context.  
`y` | `INT` | The vertical starting point for the area adjustment, establishing its position within the conditioning context.  
`strength` | `FLOAT` | Defines the intensity of the conditioning modification within the specified area, allowing for nuanced control over the adjustment’s impact.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The modified conditioning data, reflecting the specified area settings and adjustments.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-concat "Conditioning \(Concat\)")[Conditioning (Set Area with Percentage)](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area-percentage "Conditioning \(Set Area with Percentage\)")
Discover more
Stable Diffusion
Stable diffusion
ComfyUI
Workflow
Wiki
SDXL
FLUX.1
Artificial intelligence
AI
Black Forest Labs
