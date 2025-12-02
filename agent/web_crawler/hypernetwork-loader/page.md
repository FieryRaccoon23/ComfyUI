[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")Hypernetwork Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Hypernetwork Loader
![comfyUI节点-HypernetworkLoader｜超网络加载器](https://comfyui-wiki.com/loaders/HypernetworkLoader.jpg)
This node will detect models located in the `ComfyUI/models/hypernetworks` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/hypernetwork-loader#documentation)
  * Class name: `HypernetworkLoader`
  * Category: `loaders`
  * Output node: `False`


The HypernetworkLoader node is designed to enhance or modify the capabilities of a given model by applying a hypernetwork. It loads a specified hypernetwork and applies it to the model, potentially altering its behavior or performance based on the strength parameter. This process allows for dynamic adjustments to the model’s architecture or parameters, enabling more flexible and adaptive AI systems.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/hypernetwork-loader#input-types)
Field | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The base model to which the hypernetwork will be applied, determining the architecture to be enhanced or modified.  
`hypernetwork_name` | `COMBO[STRING]` | The name of the hypernetwork to be loaded and applied to the model, impacting the model’s modified behavior or performance.  
`strength` | `FLOAT` | A scalar adjusting the intensity of the hypernetwork’s effect on the model, allowing fine-tuning of the alterations.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/hypernetwork-loader#output-types)
Field | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The modified model after the hypernetwork has been applied, showcasing the impact of the hypernetwork on the original model.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/gligen-loader "GLIGEN Loader")[Lora Loader - ComfyUI Node Documentation](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader "Lora Loader - ComfyUI Node Documentation")
Discover more
interface
Flux
Flux.1
stable diffusion
Artificial intelligence
Stable diffusion
FLUX
user interface
AI
Comfy
