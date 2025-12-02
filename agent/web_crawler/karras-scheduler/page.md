[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")[schedulers](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler "schedulers")Karras Scheduler
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# KarrasScheduler
![comfyUI节点-karrasScheduler｜Karras调度器](https://comfyui-wiki.com/sampling/custom_sampling/karrasScheduler.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/karras-scheduler#documentation)
  * Class name: `KarrasScheduler`
  * Category: `sampling/custom_sampling/schedulers`
  * Output node: `False`


The KarrasScheduler node is designed to generate a sequence of noise levels (sigmas) based on the Karras et al. (2022) noise schedule. This scheduler is useful for controlling the diffusion process in generative models, allowing for fine-tuned adjustments to the noise levels applied at each step of the generation process.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/karras-scheduler#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`steps` | INT | Specifies the number of steps in the noise schedule, affecting the granularity of the generated sigmas sequence.  
`sigma_max` | FLOAT | The maximum sigma value in the noise schedule, setting the upper bound of noise levels.  
`sigma_min` | FLOAT | The minimum sigma value in the noise schedule, setting the lower bound of noise levels.  
`rho` | FLOAT | A parameter that controls the shape of the noise schedule curve, influencing how noise levels progress from sigma_min to sigma_max.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/karras-scheduler#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | SIGMAS | The generated sequence of noise levels (sigmas) following the Karras et al. (2022) noise schedule.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/exponential-scheduler "Exponential Scheduler")[Polyexponential Scheduler](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/polyexponential-scheduler "Polyexponential Scheduler")
Discover more
Stable diffusion
Text-to-image model
Image Generation
Workflow
Wiki
Stable Diffusion
ComfyUI
Flux.1
FLUX
Comfy
