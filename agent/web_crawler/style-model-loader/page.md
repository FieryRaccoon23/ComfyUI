[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")Style Model Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load Style Model
![comfyUI节点-Load Style Model｜风格模型加载器](https://comfyui-wiki.com/loaders/Load_Style_Model.jpg)
This node will detect models located in the `ComfyUI/models/style_models` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/style-model-loader#documentation)
  * Class name: `StyleModelLoader`
  * Category: `loaders`
  * Output node: `False`


The StyleModelLoader node is designed to load a style model from a specified path. It focuses on retrieving and initializing style models that can be used to apply specific artistic styles to images, thereby enabling the customization of visual outputs based on the loaded style model.
## Input Types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/style-model-loader#input-types)
Parameter Name | Comfy dtype | Python dtype | Description  
---|---|---|---  
`style_model_name` | `COMBO[STRING]` | `str` | Specifies the name of the style model to be loaded. This name is used to locate the model file within a predefined directory structure, allowing for the dynamic loading of different style models based on user input or application needs.  
## Output Types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/style-model-loader#output-types)
Parameter Name | Comfy dtype | Python dtype | Description  
---|---|---|---  
`style_model` | `STYLE_MODEL` | `StyleModel` | Returns the loaded style model, ready for use in applying styles to images. This enables the dynamic customization of visual outputs by applying different artistic styles.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader-model-only "Lora Loader Model Only")[unCLIP Checkpoint Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/unclip-checkpoint-loader "unCLIP Checkpoint Loader")
Discover more
User interface
Comfy
Wiki
Stable diffusion
Flux
stable diffusion
FLUX
interface
Flux.1
Interface
