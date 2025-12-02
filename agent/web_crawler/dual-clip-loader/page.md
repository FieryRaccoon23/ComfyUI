[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[loaders](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader "loaders")Dual CLIP Loader - How it work and how to use it.
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Dual CLIP Loader
![comfyUI节点-DualCLIPLoader|双CLIP加载器](https://comfyui-wiki.com/advanced/loaders/DualCLIPLoader.jpg)
## Dual CLIP Loader Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/dual-clip-loader#dual-clip-loader-documentation)
  * Class name: `DualCLIPLoader`
  * Category: `advanced/loaders`
  * Output node: `False`


The DualCLIPLoader node is designed for loading two CLIP models simultaneously, facilitating operations that require the integration or comparison of features from both models.
Imagine you’re in a kitchen preparing a dish, and you have two different spice jars—one with salt and one with pepper. Each spice adds a unique flavor to your dish. Now, imagine you have a special tool that lets you use both jars at the same time to season your food. This is similar to the DualCLIPLoader node. It lets you load and use two different CLIP models simultaneously, so you can combine their unique capabilities and styles to create more versatile and refined AI-generated art.
## Download ComfyUI flux_text_encoders clip models[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/dual-clip-loader#download-comfyui-flux_text_encoders-clip-models)
💡
This content is for FP8’s CLIP model with Flux.1, if you need to use GGUF versions CLIP you need to install [Flux.1 ComfyUI Guide & Workflow Examples](https://comfyui-wiki.com/en/tutorial/advanced/image/flux/flux-1-dev-t2i)
Model File Name | Size | Note | Link  
---|---|---|---  
`clip_l.safetensors` | 246 MB |  |   
`t5xxl_fp8_e4m3fn.safetensors` (Recommended) | 4.89 GB | For lower memory usage (8-12GB) |   
`t5xxl_fp16.safetensors` | 9.79 GB | For better results, if you have high VRAM and RAM(more than 32GB ram). |   
  1. Download **clip_l.safetensors**
  2. Download **t5xxl_fp8_e4m3fn.safetensors** or **t5xxl_fp16.safetensors** Depend on your VRAM and RAM
  3. Place downloaded model files in `ComfyUI/models/clip/` folder. Note: If you have used SD 3 Medium before, you might already have the above two models


[Flux.1 ComfyUI Guide & Workflow Example](https://comfyui-wiki.com/en/tutorial/advanced/image/flux/flux-1-dev-t2i)
## Input types - Dual CLIP Loader[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/dual-clip-loader#input-types---dual-clip-loader)
Parameter | Comfy dtype | Description  
---|---|---  
`clip_name1` | `COMBO[STRING]` | Specifies the name of the first CLIP model to be loaded. This parameter is crucial for identifying and retrieving the correct model from a predefined list of available CLIP models.  
`clip_name2` | `COMBO[STRING]` | Specifies the name of the second CLIP model to be loaded. This parameter enables the loading of a second distinct CLIP model for comparative or integrative analysis alongside the first model.  
`type` | `option` | Choose from “sdxl”, “sd3”, “flux” to adapt to different models.  
  * The order of loading does not affect the output effect


## Output types - Dual CLIP Loader[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/dual-clip-loader#output-types---dual-clip-loader)
Parameter | Comfy dtype | Description  
---|---|---  
`clip` | `CLIP` | The output is a combined CLIP model that integrates the features or functionalities of the two specified CLIP models.  
## Workflow example - Dual CLIP Loader[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/dual-clip-loader#workflow-example----dual-clip-loader)
Flux Basic Workflow example
The original workflow Quote from 
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-diffusers-loader "Diffusers Loader")[QuadrupleCLIPLoader](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/quadruple-clip-loader "QuadrupleCLIPLoader")
Discover more
flux
ComfyUI
workflow
Flux.1
Flux
workflows
Stable diffusion
sdxl
Workflow
Wiki
