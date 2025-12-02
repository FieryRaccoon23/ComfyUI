[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[model-merging](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save "model-merging")Model Merge Simple
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Model Merge Simple
![comfyUI节点- ModelMergeSimple|融合模型](https://comfyui-wiki.com/advanced/model_merging/ModelMergeSimple.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-simple#documentation)
  * Class name: `ModelMergeSimple`
  * Category: `advanced/model_merging`
  * Output node: `False`


The ModelMergeSimple node is designed for merging two models by blending their parameters based on a specified ratio. This node facilitates the creation of hybrid models that combine the strengths or characteristics of both input models.
The `ratio` parameter determines the blending ratio between the two models. When this value is 1, the output model is 100% `model1`, and when this value is 0, the output model is 100% `model2`.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-simple#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model1` | `MODEL` | The first model to be merged. It serves as the base model onto which patches from the second model are applied.  
`model2` | `MODEL` | The second model whose patches are applied onto the first model, influenced by the specified ratio.  
`ratio` | `FLOAT` | When this value is 1, the output model is 100% `model1`, and when this value is 0, the output model is 100% `model2`.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-simple#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The resulting merged model, incorporating elements from both input models according to the specified ratio.  
## Model Merge Simple Workflow Example[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-simple#model-merge-simple-workflow-example)
For a workflow example of this node, refer to: [Model Merging Workflow Example](https://comfyui-wiki.com/en/workflows/model-merging)
Load the following image into ComfyUI, you can view the complete workflow, and adjust the `ratio` value to view different fusion effects.
![Example](https://comfyui-wiki.com/examples/model_merging/model_merging_basic.png)
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-blocks "Model Merge Blocks")[Model Merge Subtract](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/model-merge-subtract "Model Merge Subtract")
Discover more
Stable diffusion
Wiki
workflow
Text-to-image model
Image Generation
Stable Diffusion
Workflow
ComfyUI
interface
stable diffusion
