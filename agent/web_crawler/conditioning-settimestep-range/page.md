[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Advanced[conditioning](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl "conditioning")Conditioning Set Timestep Range
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Conditioning Set Timestep Range
![comfyUI节点-ConditinoingSetTimstepRange|设置条件时间](https://comfyui-wiki.com/advanced/conditioning/ConditinoingSetTimstepRange.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/conditioning-settimestep-range#documentation)
  * Class name: `ConditioningSetTimestepRange`
  * Category: `advanced/conditioning`
  * Output node: `False`


This node is designed to adjust the temporal aspect of conditioning by setting a specific range of timesteps. It allows for the precise control over the start and end points of the conditioning process, enabling more targeted and efficient generation.
## ConditioningSetTimestepRange Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/conditioning-settimestep-range#conditioningsettimesteprange-input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The conditioning input represents the current state of the generation process, which this node modifies by setting a specific range of timesteps.  
`start` | `FLOAT` | The start parameter specifies the beginning of the timestep range as a percentage of the total generation process, allowing for fine-tuned control over when the conditioning effects begin.  
`end` | `FLOAT` | The end parameter defines the endpoint of the timestep range as a percentage, enabling precise control over the duration and conclusion of the conditioning effects.  
## ConditioningSetTimestepRange Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/conditioning-settimestep-range#conditioningsettimesteprange-output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The output is the modified conditioning with the specified timestep range applied, ready for further processing or generation.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit "CLIP Text Encode Hunyuan DiT")[Conditioning Zero Out](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/conditioning-zero-out "Conditioning Zero Out")
Discover more
Flux
Stable diffusion
Stable Diffusion
flux
SDXL
ComfyUI
user interface
AI
Black Forest Labs
Comfy
