[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")[schedulers](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler "schedulers")Exponential Scheduler
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Exponential Scheduler
![comfyUI节点-ExponentialScheduler｜Exponential调度器](https://comfyui-wiki.com/sampling/custom_sampling/ExponentialScheduler.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/exponential-scheduler#documentation)
  * Class name: `ExponentialScheduler`
  * Category: `sampling/custom_sampling/schedulers`
  * Output node: `False`


The ExponentialScheduler node is designed to generate a sequence of sigma values following an exponential schedule for diffusion sampling processes. It provides a customizable approach to control the noise levels applied at each step of the diffusion process, allowing for fine-tuning of the sampling behavior.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/exponential-scheduler#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`steps` | INT | Specifies the number of steps in the diffusion process. It influences the length of the generated sigma sequence and thus the granularity of the noise application.  
`sigma_max` | FLOAT | Defines the maximum sigma value, setting the upper limit of noise intensity in the diffusion process. It plays a crucial role in determining the range of noise levels applied.  
`sigma_min` | FLOAT | Sets the minimum sigma value, establishing the lower boundary of noise intensity. This parameter helps in fine-tuning the starting point of the noise application.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/exponential-scheduler#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | SIGMAS | A sequence of sigma values generated according to the exponential schedule. These values are used to control the noise levels at each step of the diffusion process.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler "Basic Scheduler")[Karras Scheduler](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/karras-scheduler "Karras Scheduler")
Discover more
ComfyUI
SDXL
Stable diffusion
User interface
Interface
Artificial intelligence
user interface
Comfy
Flux
Flux.1
