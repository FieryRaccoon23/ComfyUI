[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")Upscale Model Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load Upscale Model
![comfyUI节点-Load Upscale Model｜放大模型加载器](https://comfyui-wiki.com/loaders/Load_Upscale_Model.jpg)
This node will detect models located in the `ComfyUI/models/upscale_models` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/upscale-model-loader#documentation)
  * Class name: `UpscaleModelLoader`
  * Category: `loaders`
  * Output node: `False`


The UpscaleModelLoader node is designed for loading upscale models from a specified directory. It facilitates the retrieval and preparation of upscale models for image upscaling tasks, ensuring that the models are correctly loaded and configured for evaluation.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/upscale-model-loader#input-types)
Field | Comfy dtype | Description  
---|---|---  
`model_name` | `COMBO[STRING]` | Specifies the name of the upscale model to be loaded, identifying and retrieving the correct model file from the upscale models directory.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/upscale-model-loader#output-types)
Field | Comfy dtype | Description  
---|---|---  
`upscale_model` | `UPSCALE_MODEL` | Returns the loaded and prepared upscale model, ready for use in image upscaling tasks.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/unclip-checkpoint-loader "unCLIP Checkpoint Loader")[VAE Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/vae-loader "VAE Loader")
Discover more
ComfyUI
Stable diffusion
Stable Diffusion
Wiki
FLUX.1
User interface
Interface
Flux
stable diffusion
Flux.1
