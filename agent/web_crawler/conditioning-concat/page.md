[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")Conditioning (Concat)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Conditioning (Concat)
![comfyUI节点-Conditioning\(Concat\)｜条件联结](https://comfyui-wiki.com/conditioning/Conditioning\(Concat\).jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-concat#documentation)
  * Class name: `ConditioningConcat`
  * Category: `conditioning`
  * Output node: `False`


The ConditioningConcat node is designed to concatenate conditioning vectors, specifically merging the ‘conditioning_from’ vector into the ‘conditioning_to’ vector. This operation is fundamental in scenarios where the conditioning information from two sources needs to be combined into a single, unified representation.
Imagine that you are cooking a dish, `conditioning_to` is the basic recipe, and `conditioning_from` are some additional seasonings or condiments. The ConditioningConcat class is like a tool that helps you add these seasonings to the recipe, making your dish more colorful and rich.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-concat#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning_to` | `CONDITIONING` | Represents the primary set of conditioning vectors to which the ‘conditioning_from’ vectors will be concatenated. It serves as the base for the concatenation process.  
`conditioning_from` | `CONDITIONING` | Consists of conditioning vectors that are to be concatenated to the ‘conditioning_to’ vectors. This parameter allows for additional conditioning information to be integrated into the existing set.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-concat#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The output is a unified set of conditioning vectors, resulting from the concatenation of ‘conditioning_from’ vectors into the ‘conditioning_to’ vectors.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-combine "Conditioning \(Combine\)")[Conditioning (Set Area)](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area "Conditioning \(Set Area\)")
Discover more
ComfyUI
Workflow
Wiki
Stable diffusion
Stable Diffusion
stable diffusion
Artificial intelligence
FLUX
Interface
SDXL
