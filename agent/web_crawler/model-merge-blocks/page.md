[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[model-merging](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save "model-merging")Model Merge Blocks
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Model Merge Blocks
![comfyUI节点-ModelMergeBlocks|融合模型（分层）](https://comfyui-wiki.com/advanced/model_merging/ModelMergeBlocks.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-blocks#documentation)
  * Class name: `ModelMergeBlocks`
  * Category: `advanced/model_merging`
  * Output node: `False`


ModelMergeBlocks is designed for advanced model merging operations, allowing for the integration of two models with customizable blending ratios for different parts of the models. This node facilitates the creation of hybrid models by selectively merging components from two source models based on specified parameters.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-blocks#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model1` | `MODEL` | The first model to be merged. It serves as the base model onto which patches from the second model are applied.  
`model2` | `MODEL` | The second model from which patches are extracted and applied to the first model, based on the specified blending ratios.  
`input` | `FLOAT` | Specifies the blending ratio for the input layer of the models. It determines how much of the second model’s input layer is merged into the first model.  
`middle` | `FLOAT` | Defines the blending ratio for the middle layers of the models. This parameter controls the integration level of the models’ middle layers.  
`out` | `FLOAT` | Determines the blending ratio for the output layer of the models. It affects the final output by adjusting the contribution of the second model’s output layer.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-blocks#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The resulting merged model, which is a hybrid of the two input models with patches applied according to the specified blending ratios.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-add "Model Merge Add")[Model Merge Simple](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-simple "Model Merge Simple")
Discover more
User interface
FLUX.1
user interface
Black Forest Labs
SDXL
Interface
FLUX
Comfy
ComfyUI
Flux.1
