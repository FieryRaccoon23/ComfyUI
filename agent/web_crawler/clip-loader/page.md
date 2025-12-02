[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")loadersCLIP Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load CLIP
![comfyUI节点-Load CLIP|CLIP加载器](https://comfyui-wiki.com/advanced/loaders/Load_CLIP.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader#documentation)
  * Class name: `CLIPLoader`
  * Category: `advanced/loaders`
  * Output node: `False`


The CLIPLoader node is designed for loading CLIP models, supporting different types such as stable diffusion and stable cascade. It abstracts the complexities of loading and configuring CLIP models for use in various applications, providing a streamlined way to access these models with specific configurations.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip_name` | `COMBO[STRING]` | Specifies the name of the CLIP model to be loaded. This name is used to locate the model file within a predefined directory structure.  
`type` | `COMBO[STRING]` | Determines the type of CLIP model to load, offering options between ‘stable_diffusion’ and ‘stable_cascade’. This affects how the model is initialized and configured.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip` | `CLIP` | The loaded CLIP model, ready for use in downstream tasks or further processing.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/flux/flux-guidance "FluxGuidance - ComfyUI Node Functionality Description")[Load Checkpoint With Config (DEPRECATED)](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-checkpoint-loader "Load Checkpoint With Config \(DEPRECATED\)")
