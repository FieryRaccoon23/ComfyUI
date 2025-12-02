[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[model-merging](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save "model-merging")Model Merge Add
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Model Merge Add
![comfyUI节点-ModelMergeAdd|融合模型（相加）](https://comfyui-wiki.com/advanced/model_merging/ModelMergeAdd.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-add#documentation)
  * Class name: `ModelMergeAdd`
  * Category: `advanced/model_merging`
  * Output node: `False`


The ModelMergeAdd node is designed for merging two models by adding key patches from one model to another. This process involves cloning the first model and then applying patches from the second model, allowing for the combination of features or behaviors from both models.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-add#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model1` | `MODEL` | The first model to be cloned and to which patches from the second model will be added. It serves as the base model for the merging process.  
`model2` | `MODEL` | The second model from which key patches are extracted and added to the first model. It contributes additional features or behaviors to the merged model.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-add#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The result of merging two models by adding key patches from the second model to the first. This merged model combines features or behaviors from both models.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/clip-save "CLIP Save")[Model Merge Blocks](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-blocks "Model Merge Blocks")
Discover more
user interface
ComfyUI
interface
Flux.1
Stable Diffusion
Flux
Wiki
Interface
Sdxl
AI
