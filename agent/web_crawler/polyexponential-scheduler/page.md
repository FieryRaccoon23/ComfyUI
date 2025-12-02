[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")[schedulers](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler "schedulers")Polyexponential Scheduler
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# PolyexponentialScheduler
![comfyUI节点-PolyexponentialScheduler｜Polyexponential调度器](https://comfyui-wiki.com/sampling/custom_sampling/PolyexponentialScheduler.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/polyexponential-scheduler#documentation)
  * Class name: `PolyexponentialScheduler`
  * Category: `sampling/custom_sampling/schedulers`
  * Output node: `False`


The PolyexponentialScheduler node is designed to generate a sequence of noise levels (sigmas) based on a polyexponential noise schedule. This schedule is a polynomial function in the logarithm of sigma, allowing for a flexible and customizable progression of noise levels throughout the diffusion process.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/polyexponential-scheduler#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`steps` | INT | Specifies the number of steps in the diffusion process, affecting the granularity of the generated noise levels.  
`sigma_max` | FLOAT | The maximum noise level, setting the upper bound of the noise schedule.  
`sigma_min` | FLOAT | The minimum noise level, setting the lower bound of the noise schedule.  
`rho` | FLOAT | A parameter that controls the shape of the polyexponential noise schedule, influencing how noise levels progress between the minimum and maximum values.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/polyexponential-scheduler#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | SIGMAS | The output is a sequence of noise levels (sigmas) tailored to the specified polyexponential noise schedule.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/karras-scheduler "Karras Scheduler")[SD Turbo Scheduler](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/sd-turbo-scheduler "SD Turbo Scheduler")
Discover more
stable diffusion
Comfy
Stable Diffusion
Sdxl
AI
Black Forest Labs
Artificial intelligence
Wiki
Flux.1
Interface
