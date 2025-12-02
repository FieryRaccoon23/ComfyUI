[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")Diff ControlNet Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load ControlNet Model (diff)
![comfyUI节点-Load ControlNet Model\(Diff\)｜Diff ControlNet加载器](https://comfyui-wiki.com/loaders/Load_ControlNet_Model\(Diff\).jpg)
This node will detect models located in the `ComfyUI/models/controlnet` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/diff-controlnet-loader#documentation)
  * Class name: `DiffControlNetLoader`
  * Category: `loaders`
  * Output node: `False`


The DiffControlNetLoader node is designed for loading differential control networks, which are specialized models that can modify the behavior of another model based on control net specifications. This node allows for the dynamic adjustment of model behaviors by applying differential control nets, facilitating the creation of customized model outputs.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/diff-controlnet-loader#input-types)
Field | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The base model to which the differential control net will be applied, allowing for customization of the model’s behavior.  
`control_net_name` | `COMBO[STRING]` | Identifies the specific differential control net to be loaded and applied to the base model for modifying its behavior.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/diff-controlnet-loader#output-types)
Field | Comfy dtype | Description  
---|---|---  
`control_net` | `CONTROL_NET` | A differential control net that has been loaded and is ready to be applied to a base model for behavior modification.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/controlnet-loader "ControlNet Loader")[GLIGEN Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/gligen-loader "GLIGEN Loader")
Discover more
AI
Flux.1
User interface
Interface
FLUX
SDXL
Stable Diffusion
user interface
Black Forest Labs
Wiki
