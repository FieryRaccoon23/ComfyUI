[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")ControlNet Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load ControlNet Model
![comfyUI节点-Load ControlNet Model｜ControlNet加载器](https://comfyui-wiki.com/loaders/Load_ControlNet_Model.jpg)
This node will detect models located in the `ComfyUI/models/controlnet` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/controlnet-loader#documentation)
  * Class name: `ControlNetLoader`
  * Category: `loaders`
  * Output node: `False`


The ControlNetLoader node is designed to load a ControlNet model from a specified path. It plays a crucial role in initializing ControlNet models, which are essential for applying control mechanisms over generated content or modifying existing content based on control signals.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/controlnet-loader#input-types)
Field | Comfy dtype | Description  
---|---|---  
`control_net_name` | `COMBO[STRING]` | Specifies the name of the ControlNet model to be loaded, used to locate the model file within a predefined directory structure.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/controlnet-loader#output-types)
Field | Comfy dtype | Description  
---|---|---  
`control_net` | `CONTROL_NET` | Returns the loaded ControlNet model, ready for use in controlling or modifying content generation processes.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/clip-vision-loader "CLIP Vision Loader")[Diff ControlNet Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/diff-controlnet-loader "Diff ControlNet Loader")
Discover more
Stable diffusion
Workflow
User interface
Wiki
ComfyUI
Stable Diffusion
interface
Comfy
stable diffusion
FLUX.1
