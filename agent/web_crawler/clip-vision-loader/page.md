[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")CLIP Vision Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load CLIP Vision
![comfyUI节点-Load CLIP Vision｜CLIP视觉加载器](https://comfyui-wiki.com/loaders/Load_CLIP_Vision.jpg)
This node will detect models located in the `ComfyUI/models/clip_vision` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/clip-vision-loader#documentation)
  * Class name: `CLIPVisionLoader`
  * Category: `loaders`
  * Output node: `False`


The CLIPVisionLoader node is designed for loading CLIP Vision models from specified paths. It abstracts the complexities of locating and initializing CLIP Vision models, making them readily available for further processing or inference tasks.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/clip-vision-loader#input-types)
Field | Comfy dtype | Description  
---|---|---  
`clip_name` | `COMBO[STRING]` | Specifies the name of the CLIP Vision model to be loaded, used to locate the model file within a predefined directory structure.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/clip-vision-loader#output-types)
Field | Comfy dtype | Description  
---|---|---  
`clip_vision` | `CLIP_VISION` | The loaded CLIP Vision model, ready for use in encoding images or performing other vision-related tasks.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Checkpoint Loader \(Simple\)")[ControlNet Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/controlnet-loader "ControlNet Loader")
Discover more
Stable diffusion
Stable Diffusion
Wiki
ComfyUI
Workflow
Comfy
User interface
Flux.1
FLUX.1
interface
