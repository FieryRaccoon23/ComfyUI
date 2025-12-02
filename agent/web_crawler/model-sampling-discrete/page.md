[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[model](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-continuous-edm "model")Model Sampling Discrete
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Model Sampling Discrete
![comfyUI节点-ModelSamplingDiscrete|模型离散采样算法](https://comfyui-wiki.com/advanced/model/ModelSamplingDiscrete.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-discrete#documentation)
  * Class name: `ModelSamplingDiscrete`
  * Category: `advanced/model`
  * Output node: `False`


This node is designed to modify the sampling behavior of a model by applying a discrete sampling strategy. It allows for the selection of different sampling methods, such as epsilon, v_prediction, lcm, or x0, and optionally adjusts the model’s noise reduction strategy based on the zero-shot noise ratio (zsnr) setting.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-discrete#input-types)
Parameter | Comfy dtype | Python dtype | Description  
---|---|---|---  
`model` | `MODEL` | `torch.nn.Module` | The model to which the discrete sampling strategy will be applied. This parameter is crucial as it defines the base model that will undergo modification.  
`sampling` | `COMBO[STRING]` | `str` | Specifies the discrete sampling method to be applied to the model. The choice of method affects how the model generates samples, offering different strategies for sampling.  
`zsnr` | `BOOLEAN` | `bool` | A boolean flag that, when enabled, adjusts the model’s noise reduction strategy based on the zero-shot noise ratio. This can influence the quality and characteristics of the generated samples.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-discrete#output-types)
Parameter | Comfy dtype | Python dtype | Description  
---|---|---|---  
`model` | `MODEL` | `torch.nn.Module` | The modified model with the applied discrete sampling strategy. This model is now equipped to generate samples using the specified method and adjustments.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-continuous-edm "Model Sampling Continuous EDM")[Rescale CFG](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/rescale-cfg "Rescale CFG")
