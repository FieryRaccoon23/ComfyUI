[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")Conditioning Average
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Conditioning Average
![comfyUI节点-ConditioningAverage|条件平均](https://comfyui-wiki.com/conditioning/ConditioningAverage.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-average#documentation)
  * Class name: `ConditioningAverage`
  * Category: `conditioning`
  * Output node: `False`


The ConditioningAverage node is designed to blend two sets of conditioning data, applying a weighted average based on a specified strength. This process allows for the dynamic adjustment of conditioning influence, facilitating the fine-tuning of generated content or features.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-average#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning_to` | `CONDITIONING` | Represents the primary set of conditioning data to which the blending will be applied. It serves as the base for the weighted average operation.  
`conditioning_from` | `CONDITIONING` | Denotes the secondary set of conditioning data that will be blended into the primary set. This data influences the final output based on the specified strength.  
`conditioning_to_strength` | `FLOAT` | A scalar value that determines the strength of the blend between the primary and secondary conditioning data. It directly influences the balance of the weighted average.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-average#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The result of blending the primary and secondary conditioning data, producing a new set of conditioning that reflects the weighted average.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-vision-encode "CLIP Vision Encode")[Conditioning (Combine)](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-combine "Conditioning \(Combine\)")
