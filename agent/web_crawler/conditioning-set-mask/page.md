[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")Conditioning (Set Mask)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Conditioning (Set Mask)
![comfyUI节点-Conditioning\(Set Mask\)｜条件设置遮罩](https://comfyui-wiki.com/conditioning/Conditioning\(Set_Mask\).jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-mask#documentation)
  * Class name: `ConditioningSetMask`
  * Category: `conditioning`
  * Output node: `False`


This node is designed to modify the conditioning of a generative model by applying a mask with a specified strength to certain areas. It allows for targeted adjustments within the conditioning, enabling more precise control over the generation process.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-mask#input-types)
### Required[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-mask#required)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The conditioning data to be modified. It serves as the basis for applying the mask and strength adjustments.  
`mask` | `MASK` | A mask tensor that specifies the areas within the conditioning to be modified.  
`strength` | `FLOAT` | The strength of the mask’s effect on the conditioning, allowing for fine-tuning of the applied modifications.  
`set_cond_area` | `COMBO[STRING]` | Determines whether the mask’s effect is applied to the default area or bounded by the mask itself, offering flexibility in targeting specific regions.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-mask#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The modified conditioning data, with the mask and strength adjustments applied.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-area-strength "Conditioning \(Set Area Strength\)")[Apply ControlNet](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply "Apply ControlNet")
Discover more
user interface
FLUX
SDXL
interface
Wiki
Sdxl
FLUX.1
Stable Diffusion
User interface
Stable diffusion
