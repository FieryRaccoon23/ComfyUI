[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[model-merging](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save "model-merging")Model Merge Subtract
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Model Merge Subtract
![comfyUI节点-ModelMergeSubtract|融合模型（相减）](https://comfyui-wiki.com/advanced/model_merging/ModelMergeSubtract.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-subtract#documentation)
  * Class name: `ModelMergeSubtract`
  * Category: `advanced/model_merging`
  * Output node: `False`


This node is designed for advanced model merging operations, specifically to subtract the parameters of one model from another based on a specified multiplier. It enables the customization of model behaviors by adjusting the influence of one model’s parameters over another, facilitating the creation of new, hybrid models.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-subtract#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model1` | `MODEL` | The base model from which parameters will be subtracted.  
`model2` | `MODEL` | The model whose parameters will be subtracted from the base model.  
`multiplier` | `FLOAT` | A floating-point value that scales the subtraction effect on the base model’s parameters.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-subtract#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The resulting model after subtracting the parameters of one model from another, scaled by the multiplier.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-simple "Model Merge Simple")[VAE Save](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/vae-save "VAE Save")
Discover more
Stable Diffusion
Wiki
Stable diffusion
Workflow
ComfyUI
Artificial intelligence
interface
Flux
Interface
Comfy
