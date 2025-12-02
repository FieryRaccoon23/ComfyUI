[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[model](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-continuous-edm "model")Rescale CFG
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Rescale CFG
![comfyUI节点-RescaleCFG|缩放CFG](https://comfyui-wiki.com/advanced/model/RescaleCFG.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/rescale-cfg#documentation)
  * Class name: `RescaleCFG`
  * Category: `advanced/model`
  * Output node: `False`


The RescaleCFG node is designed to adjust the conditioning and unconditioning scales of a model’s output based on a specified multiplier, aiming to achieve a more balanced and controlled generation process. It operates by rescaling the model’s output to modify the influence of conditioned and unconditioned components, thereby potentially enhancing the model’s performance or output quality.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/rescale-cfg#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The model parameter represents the generative model to be adjusted. It is crucial as the node applies a rescaling function to the model’s output, directly influencing the generation process.  
`multiplier` | `FLOAT` | The multiplier parameter controls the extent of rescaling applied to the model’s output. It determines the balance between the original and rescaled components, affecting the final output’s characteristics.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/rescale-cfg#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The modified model with adjusted conditioning and unconditioning scales. This model is expected to produce outputs with potentially enhanced characteristics due to the applied rescaling.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-discrete "Model Sampling Discrete")[Checkpoint Save](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/checkpoint-save "Checkpoint Save")
