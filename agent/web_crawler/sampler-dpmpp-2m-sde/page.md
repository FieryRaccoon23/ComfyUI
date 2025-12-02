[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")[samplers](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/k-sampler-select "samplers")Sampler DPMPP_2M_SDE
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Sampler DPMPP_2M_SDE
![Sampler DPMPP_2M_SDE](https://comfyui-wiki.com/sampling/custom_sampling/samplers/SamplerDPMMPP_2M_SDE.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-2m-sde#documentation)
  * Class name: `SamplerDPMPP_2M_SDE`
  * Category: `sampling/custom_sampling/samplers`
  * Output node: `False`


This node is designed to generate a sampler for the DPMPP_2M_SDE model, allowing for the creation of samples based on specified solver types, noise levels, and computational device preferences. It abstracts the complexities of sampler configuration, providing a streamlined interface for generating samples with customized settings.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-2m-sde#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`solver_type` | `COMBO[STRING]` | Specifies the solver type to be used in the sampling process, offering options between ‘midpoint’ and ‘heun’. This choice influences the numerical integration method applied during sampling.  
`eta` | `FLOAT` | Determines the step size in the numerical integration, affecting the granularity of the sampling process. A higher value indicates a larger step size.  
`s_noise` | `FLOAT` | Controls the level of noise introduced during the sampling process, influencing the variability of the generated samples.  
`noise_device` | `COMBO[STRING]` | Indicates the computational device (‘gpu’ or ‘cpu’) on which the noise generation process is executed, affecting performance and efficiency.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-2m-sde#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sampler` | `SAMPLER` | The output is a sampler configured according to the specified parameters, ready for generating samples.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/k-sampler-select "KSampler Select")[Sampler DPMPP_SDE](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-sde "Sampler DPMPP_SDE")
