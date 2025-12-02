[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")modelModel Sampling Continuous EDM
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Model Sampling Continuous EDM
![comfyUI节点-ModelSmaplingContinuousEDM|模型连续采样算法EDM](https://comfyui-wiki.com/advanced/model/ModelSmaplingContinuousEDM.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-continuous-edm#documentation)
  * Class name: `ModelSamplingContinuousEDM`
  * Category: `advanced/model`
  * Output node: `False`


This node is designed to enhance a model’s sampling capabilities by integrating continuous EDM (Energy-based Diffusion Models) sampling techniques. It allows for the dynamic adjustment of the noise levels within the model’s sampling process, offering a more refined control over the generation quality and diversity.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-continuous-edm#input-types)
Parameter | Comfy dtype | Python dtype | Description  
---|---|---|---  
`model` | `MODEL` | `torch.nn.Module` | The model to be enhanced with continuous EDM sampling capabilities. It serves as the foundation for applying the advanced sampling techniques.  
`sampling` | `COMBO[STRING]` | `str` | Specifies the type of sampling to be applied, either ‘eps’ for epsilon sampling or ‘v_prediction’ for velocity prediction, influencing the model’s behavior during the sampling process.  
`sigma_max` | `FLOAT` | `float` | The maximum sigma value for noise level, allowing for upper bound control in the noise injection process during sampling.  
`sigma_min` | `FLOAT` | `float` | The minimum sigma value for noise level, setting the lower limit for noise injection, thus affecting the model’s sampling precision.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-continuous-edm#output-types)
Parameter | Comfy dtype | Python dtype | Description  
---|---|---|---  
`model` | `MODEL` | `torch.nn.Module` | The enhanced model with integrated continuous EDM sampling capabilities, ready for further use in generation tasks.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/unet-loader "UNET Loader Guide | Load Diffusion Model - Documentation & Example")[Model Sampling Discrete](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model/model-sampling-discrete "Model Sampling Discrete")
Discover more
Stable Diffusion
Wiki
ComfyUI
Stable diffusion
Python
Sdxl
Comfy
Flux
AI
interface
