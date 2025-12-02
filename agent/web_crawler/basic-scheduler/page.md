[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")schedulersBasic Scheduler
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# BasicScheduler
![comfyUI节点-basicScheduler｜基础调度器](https://comfyui-wiki.com/sampling/custom_sampling/basicScheduler.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler#documentation)
  * Class name: `BasicScheduler`
  * Category: `sampling/custom_sampling/schedulers`
  * Output node: `False`


The BasicScheduler node is designed to compute a sequence of sigma values for diffusion models based on the provided scheduler, model, and denoising parameters. It dynamically adjusts the total number of steps based on the denoise factor to fine-tune the diffusion process.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The model parameter specifies the diffusion model for which the sigma values are to be calculated. It plays a crucial role in determining the appropriate sigma values for the diffusion process.  
`scheduler` | `COMBO[STRING]` | The scheduler parameter determines the scheduling algorithm to be used for calculating the sigma values. It directly influences the progression and characteristics of the diffusion process.  
`steps` | `INT` | The steps parameter indicates the total number of steps in the diffusion process. It affects the granularity and duration of the process.  
`denoise` | `FLOAT` | The denoise parameter allows for adjusting the effective number of steps by scaling the total steps, enabling finer control over the diffusion process.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | `SIGMAS` | The sigmas output represents the computed sequence of sigma values for the diffusion process, essential for controlling the noise level at each step.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-sde "Sampler DPMPP_SDE")[Exponential Scheduler](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/exponential-scheduler "Exponential Scheduler")
