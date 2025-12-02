[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Advanced[conditioning](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl "conditioning")Conditioning Zero Out
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Conditioning Zero Out
![comfyUI节点-ConditioningZeroOut|条件零化](https://comfyui-wiki.com/advanced/conditioning/ConditioningZeroOut.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/conditioning-zero-out#documentation)
  * Class name: `ConditioningZeroOut`
  * Category: `advanced/conditioning`
  * Output node: `False`


This node zeroes out specific elements within the conditioning data structure, effectively neutralizing their influence in subsequent processing steps. It’s designed for advanced conditioning operations where direct manipulation of the conditioning’s internal representation is required.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/conditioning-zero-out#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The conditioning data structure to be modified. This node zeroes out the ‘pooled_output’ elements within each conditioning entry, if present.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/conditioning-zero-out#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The modified conditioning data structure, with ‘pooled_output’ elements set to zero where applicable.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/conditioning-settimestep-range "Conditioning Set Timestep Range")[CLIPTextEncodeFlux Node for ComfyUI Explained](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/flux/clip-text-encode-flux "CLIPTextEncodeFlux Node for ComfyUI Explained")
