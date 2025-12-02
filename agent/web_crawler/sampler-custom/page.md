[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Samplingcustom-samplingSamplerCustom
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# SamplerCustom
![comfyUI节点-SamplerCustom 自定义采样器](https://comfyui-wiki.com/sampling/custom_sampling/SamplerCustom.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom#documentation)
  * Class name: `SamplerCustom`
  * Category: `sampling/custom_sampling`
  * Output node: `False`


The SamplerCustom node is designed to provide a flexible and customizable sampling mechanism for various applications. It enables users to select and configure different sampling strategies tailored to their specific needs, enhancing the adaptability and efficiency of the sampling process.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The ‘model’ input type specifies the model to be used for sampling, playing a crucial role in determining the sampling behavior and output.  
`add_noise` | `BOOLEAN` | The ‘add_noise’ input type allows users to specify whether noise should be added to the sampling process, influencing the diversity and characteristics of the generated samples.  
`noise_seed` | `INT` | The ‘noise_seed’ input type provides a seed for the noise generation, ensuring reproducibility and consistency in the sampling process when adding noise.  
`cfg` | `FLOAT` | The ‘cfg’ input type sets the configuration for the sampling process, allowing for fine-tuning of the sampling parameters and behavior.  
`positive` | `CONDITIONING` | The ‘positive’ input type represents positive conditioning information, guiding the sampling process towards generating samples that align with specified positive attributes.  
`negative` | `CONDITIONING` | The ‘negative’ input type represents negative conditioning information, steering the sampling process away from generating samples that exhibit specified negative attributes.  
`sampler` | `SAMPLER` | The ‘sampler’ input type selects the specific sampling strategy to be employed, directly impacting the nature and quality of the generated samples.  
`sigmas` | `SIGMAS` | The ‘sigmas’ input type defines the noise levels to be used in the sampling process, affecting the exploration of the sample space and the diversity of the output.  
`latent_image` | `LATENT` | The ‘latent_image’ input type provides an initial latent image for the sampling process, serving as a starting point for sample generation.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`output` | `LATENT` | The ‘output’ represents the primary result of the sampling process, containing the generated samples.  
`denoised_output` | `LATENT` | The ‘denoised_output’ represents the samples after a denoising process has been applied, potentially enhancing the clarity and quality of the generated samples.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/solid-mask "Solid Mask")[KSampler Select](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/k-sampler-select "KSampler Select")
Discover more
Stable diffusion
Wiki
Stable Diffusion
Workflow
ComfyUI
FLUX.1
User interface
Artificial intelligence
Sdxl
FLUX
