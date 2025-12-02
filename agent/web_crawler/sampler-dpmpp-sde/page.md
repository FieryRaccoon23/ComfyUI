[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")[samplers](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/k-sampler-select "samplers")Sampler DPMPP_SDE
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Sampler DPMPP_SDE
![Sampler DPMPP_SDE](https://comfyui-wiki.com/sampling/custom_sampling/samplers/SamplerDPMPP_SDE.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-sde#documentation)
  * Class name: `SamplerDPMPP_SDE`
  * Category: `sampling/custom_sampling/samplers`
  * Output node: `False`


This node is designed to generate a sampler for the DPM++ SDE (Stochastic Differential Equation) model. It adapts to both CPU and GPU execution environments, optimizing the sampler’s implementation based on the available hardware.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-sde#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`eta` | FLOAT | Specifies the step size for the SDE solver, influencing the granularity of the sampling process.  
`s_noise` | FLOAT | Determines the level of noise to be applied during the sampling process, affecting the diversity of the generated samples.  
`r` | FLOAT | Controls the ratio of noise reduction in the sampling process, impacting the clarity and quality of the generated samples.  
`noise_device` | COMBO[STRING] | Selects the execution environment (CPU or GPU) for the sampler, optimizing performance based on available hardware.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-sde#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sampler` | SAMPLER | The generated sampler configured with the specified parameters, ready for use in sampling operations.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-2m-sde "Sampler DPMPP_2M_SDE")[Basic Scheduler](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler "Basic Scheduler")
Discover more
Graphics processing unit
GPU
Wiki
Stable diffusion
Workflow
Stable Diffusion
ComfyUI
SDXL
User interface
FLUX
