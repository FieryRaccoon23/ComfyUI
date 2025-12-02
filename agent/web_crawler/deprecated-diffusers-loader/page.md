[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[loaders](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader "loaders")Diffusers Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Diffusers Loader
![comfyUI节点-DiffuserLoader｜扩散加载器](https://comfyui-wiki.com/advanced/loaders/deprecated/DiffuserLoader.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-diffusers-loader#documentation)
  * Class name: `DiffusersLoader`
  * Category: `advanced/loaders/deprecated`
  * Output node: `False`


The DiffusersLoader node is designed for loading models from the diffusers library, specifically handling the loading of UNet, CLIP, and VAE models based on provided model paths. It facilitates the integration of these models into the ComfyUI framework, enabling advanced functionalities such as text-to-image generation, image manipulation, and more.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-diffusers-loader#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model_path` | `COMBO[STRING]` | Specifies the path to the model to be loaded. This path is crucial as it determines which model will be utilized for subsequent operations, affecting the output and capabilities of the node.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-diffusers-loader#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The loaded UNet model, which is part of the output tuple. This model is essential for image synthesis and manipulation tasks within the ComfyUI framework.  
`clip` | `CLIP` | The loaded CLIP model, included in the output tuple if requested. This model enables advanced text and image understanding and manipulation capabilities.  
`vae` | `VAE` | The loaded VAE model, included in the output tuple if requested. This model is crucial for tasks involving latent space manipulation and image generation.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-checkpoint-loader "Load Checkpoint With Config \(DEPRECATED\)")[Dual CLIP Loader - How it work and how to use it.](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/dual-clip-loader "Dual CLIP Loader - How it work and how to use it.")
