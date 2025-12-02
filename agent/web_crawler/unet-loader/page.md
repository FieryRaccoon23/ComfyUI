[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[loaders](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader "loaders")UNET Loader Guide | Load Diffusion Model - Documentation & Example
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# UNET Loader Guide | Load Diffusion Model
![comfyUI节点-UNETLoader|UNET加载器](https://comfyui-wiki.com/advanced/loaders/UNETLoader.jpg)
This node has been renamed as `Load Diffusion Model`.
![comfyUI节点-Load-Diffusion-Model|UNET加载器](https://comfyui-wiki.com/advanced/loaders/Load-Diffusion-Model.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/unet-loader#documentation)
  * Class name: `UNETLoader`
  * Category: `advanced/loaders`
  * Output node: `False`


The UNETLoader node is designed for loading U-Net models by name, facilitating the use of pre-trained U-Net architectures within the system.
## Input types - UNET Loader Guide | Load Diffusion Model[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/unet-loader#input-types---unet-loader-guide--load-diffusion-model)
Parameter | Comfy dtype | Description  
---|---|---  
`unet_name` | `COMBO[STRING]` | Specifies the name of the U-Net model to be loaded. This name is used to locate the model within a predefined directory structure, enabling the dynamic loading of different U-Net models.  
`weight_dtype` | … | 🚧 fp8_e4m3fn fp9_e5m2  
## Output types - UNET Loader Guide | Load Diffusion Model[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/unet-loader#output-types----unet-loader-guide--load-diffusion-model)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | Returns the loaded U-Net model, allowing it to be utilized for further processing or inference within the system.  
## Load Diffusion Model Workflow Example | UNET Loader Guide[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/unet-loader#load-diffusion-model-workflow-example--unet-loader-guide)
Download UNET Loader Workflow example
  1. Install the UNET models
  2. Dwonload the workflow file
  3. Import workflow in comfyUI
  4. Chose the UNET model and run the workflow


### Download FLux.1 UNET Model[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/unet-loader#download-flux1-unet-model)
File Name | Size | Link | Note  
---|---|---|---  
`flux1-schnell.safetensors` | 23.8GB |  | For lower memory usage  
`flux1-dev.safetensors` | 23.8GB |  | If you have high VRAM and RAM.  
  1. Downloaded the `flux1-schnell.safetensors`
  2. Place downloaded model files in `ComfyUI/models/unet/` folder


[Flux.1 ComfyUI Guide & Workflow Example](https://comfyui-wiki.com/en/tutorial/advanced/image/flux/flux-1-dev-t2i)
## Where you can download UNet models and how to install it?[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/unet-loader#where-you-can-download-unet-models-and-how-to-install-it)
  1. You can download UNet models in folloow link:[Unet Model Resource](https://comfyui-wiki.com/en/resource/unet-models)
  2. After download the model files, you shou place it in `/ComfyUI/models/unet`, than refresh the ComfyUI or restart it. If everything is fine, you can see the model name in the dropdown list of the UNETLoader node.


Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/quadruple-clip-loader "QuadrupleCLIPLoader")[Model Sampling Continuous EDM](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-continuous-edm "Model Sampling Continuous EDM")
Discover more
Flux
comfyUI
FLux.1
flux1
ComfyUI
Flux.1
Wiki
Stable diffusion
FLUX.1
Stable Diffusion
