[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")GLIGEN Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# GLIGEN Loader
![comfyUI节点-GLIGENLoader｜GLIGEN加载器](https://comfyui-wiki.com/loaders/GLIGENLoader.jpg)
This node will detect models located in the `ComfyUI/models/gligen` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/gligen-loader#documentation)
  * Class name: `GLIGENLoader`
  * Category: `loaders`
  * Output node: `False`


The GLIGENLoader node is designed for loading GLIGEN models, which are specialized generative models. It facilitates the process of retrieving and initializing these models from specified paths, making them ready for further generative tasks.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/gligen-loader#input-types)
Field | Comfy dtype | Description  
---|---|---  
`gligen_name` | `COMBO[STRING]` | The name of the GLIGEN model to be loaded, specifying which model file to retrieve and load, crucial for the initialization of the GLIGEN model.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/gligen-loader#output-types)
Field | Comfy dtype | Description  
---|---|---  
`gligen` | `GLIGEN` | The loaded GLIGEN model, ready for use in generative tasks, representing the fully initialized model loaded from the specified path.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/diff-controlnet-loader "Diff ControlNet Loader")[Hypernetwork Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/hypernetwork-loader "Hypernetwork Loader")
Discover more
Wiki
Stable Diffusion
ComfyUI
Stable diffusion
Flux
Black Forest Labs
Interface
Artificial intelligence
FLUX.1
Sdxl
