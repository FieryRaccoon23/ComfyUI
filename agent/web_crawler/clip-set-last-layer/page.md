[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")CLIP Set Last Layer
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# CLIP Set Last Layer
![comfyUI节点-CLIP Set Last Layer|CLIP设置停止层](https://comfyui-wiki.com/conditioning/CLIP_Set_Last_Layer.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-set-last-layer#documentation)
  * Class name: `CLIPSetLastLayer`
  * Category: `conditioning`
  * Output node: `False`


This node is designed to modify the behavior of a CLIP model by setting a specific layer as the last one to be executed. It allows for the customization of the depth of processing within the CLIP model, potentially affecting the model’s output by limiting the amount of information processed.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-set-last-layer#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip` | `CLIP` | The CLIP model to be modified. This parameter allows the node to directly interact with and alter the structure of the CLIP model.  
`stop_at_clip_layer` | `INT` | Specifies the layer at which the CLIP model should stop processing. This allows for control over the depth of computation and can be used to adjust the model’s behavior or performance.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-set-last-layer#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip` | `CLIP` | The modified CLIP model with the specified layer set as the last one. This output enables further use or analysis of the adjusted model.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning-batched "Stable Zero 123 Conditioning Batched")[CLIP Text Encode (Prompt)](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-text-encode "CLIP Text Encode \(Prompt\)")
Discover more
Workflow
ComfyUI
Stable diffusion
Wiki
Stable Diffusion
Comfy
FLUX.1
FLUX
SDXL
Black Forest Labs
