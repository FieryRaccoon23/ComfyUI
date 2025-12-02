[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[model-merging](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save "model-merging")CLIPMerge Simple
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# CLIPMerge Simple
![comfyUI节点-CLIPMergeSimple|融合CLIP](https://comfyui-wiki.com/advanced/model_merging/CLIPMergeSimple.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/clip-merge-simple#documentation)
  * Class name: `CLIPMergeSimple`
  * Category: `advanced/model_merging`
  * Output node: `False`


This node specializes in merging two CLIP models based on a specified ratio, effectively blending their characteristics. It selectively applies patches from one model to another, excluding specific components like position IDs and logit scale, to create a hybrid model that combines features from both source models.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/clip-merge-simple#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip1` | `CLIP` | The first CLIP model to be merged. It serves as the base model for the merging process.  
`clip2` | `CLIP` | The second CLIP model to be merged. Its key patches, except for position IDs and logit scale, are applied to the first model based on the specified ratio.  
`ratio` | `FLOAT` | Determines the proportion of features from the second model to blend into the first model. A ratio of 1.0 means fully adopting the second model’s features, while 0.0 retains only the first model’s features.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/clip-merge-simple#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip` | `CLIP` | The resulting merged CLIP model, incorporating features from both input models according to the specified ratio.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save "Checkpoint Save")[CLIP Save](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/clip-save "CLIP Save")
