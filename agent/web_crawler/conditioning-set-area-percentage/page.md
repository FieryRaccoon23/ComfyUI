[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")Conditioning (Set Area with Percentage)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Conditioning (Set Area with Percentage)
![comfyUI节点-Conditioning\(Set Area With Percentage\)｜按系数设置条件采样区域](https://comfyui-wiki.com/conditioning/Conditioning\(Set_Area_With_Percentage\).jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area-percentage#documentation)
  * Class name: `ConditioningSetAreaPercentage`
  * Category: `conditioning`
  * Output node: `False`


The ConditioningSetAreaPercentage node specializes in adjusting the area of influence for conditioning elements based on percentage values. It allows for the specification of the area’s dimensions and position as percentages of the total image size, alongside a strength parameter to modulate the intensity of the conditioning effect.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area-percentage#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | Represents the conditioning elements to be modified, serving as the foundation for applying area and strength adjustments.  
`width` | `FLOAT` | Specifies the width of the area as a percentage of the total image width, influencing how much of the image the conditioning affects horizontally.  
`height` | `FLOAT` | Determines the height of the area as a percentage of the total image height, affecting the vertical extent of the conditioning’s influence.  
`x` | `FLOAT` | Indicates the horizontal starting point of the area as a percentage of the total image width, positioning the conditioning effect.  
`y` | `FLOAT` | Specifies the vertical starting point of the area as a percentage of the total image height, positioning the conditioning effect.  
`strength` | `FLOAT` | Controls the intensity of the conditioning effect within the specified area, allowing for fine-tuning of its impact.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area-percentage#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | Returns the modified conditioning elements with updated area and strength parameters, ready for further processing or application.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area "Conditioning \(Set Area\)")[Conditioning (Set Area Strength)](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area-strength "Conditioning \(Set Area Strength\)")
Discover more
Sdxl
SDXL
AI
Flux.1
Wiki
FLUX
Artificial intelligence
interface
Flux
Comfy
