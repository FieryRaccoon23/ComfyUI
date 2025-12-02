[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Advanced[conditioning](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl "conditioning")[flux](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/flux/clip-text-encode-flux "flux")FluxGuidance - ComfyUI Node Functionality Description
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# FluxGuidance - ComfyUI Node Functionality Description
## Input Parameters[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/flux/flux-guidance#input-parameters)
Parameter Name | Data Type | Function  
---|---|---  
conditioning | CONDITIONING | Input conditioning data, typically from previous encoding or processing steps  
guidance | FLOAT | Controls the influence of text prompts on image generation, adjustable range from 0.0 to 100.0  
## Output Parameters[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/flux/flux-guidance#output-parameters)
Parameter Name | Data Type | Function  
---|---|---  
CONDITIONING | CONDITIONING | Updated conditioning data, containing the new guidance value  
## Usage Recommendations[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/flux/flux-guidance#usage-recommendations)
For relatively short prompts and requirements, setting the guidance to 4 may be a good choice. However, if your prompt is longer or you want more creative content, setting the guidance between 1.0 and 1.5 might be a better option.
  * Higher values result in images that more closely match the prompt but may lack some creativity.
  * Lower values result in images that are less closely matched to the prompt but may be more creative.


Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/flux/clip-text-encode-flux "CLIPTextEncodeFlux Node for ComfyUI Explained")[CLIP Loader](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader "CLIP Loader")
