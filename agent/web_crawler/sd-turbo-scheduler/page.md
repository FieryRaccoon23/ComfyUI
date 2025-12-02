[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")[schedulers](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler "schedulers")SD Turbo Scheduler
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# SD Turbo Scheduler
![comfyUI节点-SDTurboScheduler｜SDTurbo调度器](https://comfyui-wiki.com/sampling/custom_sampling/SDTurboScheduler.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/sd-turbo-scheduler#documentation)
  * Class name: `SDTurboScheduler`
  * Category: `sampling/custom_sampling/schedulers`
  * Output node: `False`


SDTurboScheduler is designed to generate a sequence of sigma values for image sampling, adjusting the sequence based on the denoise level and the number of steps specified. It leverages a specific model’s sampling capabilities to produce these sigma values, which are crucial for controlling the denoising process during image generation.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/sd-turbo-scheduler#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The model parameter specifies the generative model to be used for sigma value generation. It is crucial for determining the specific sampling behavior and capabilities of the scheduler.  
`steps` | `INT` | The steps parameter determines the length of the sigma sequence to be generated, directly influencing the granularity of the denoising process.  
`denoise` | `FLOAT` | The denoise parameter adjusts the starting point of the sigma sequence, allowing for finer control over the denoising level applied during image generation.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/sd-turbo-scheduler#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | `SIGMAS` | A sequence of sigma values generated based on the specified model, steps, and denoise level. These values are essential for controlling the denoising process in image generation.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/polyexponential-scheduler "Polyexponential Scheduler")[VP Scheduler](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/vp-scheduler "VP Scheduler")
Discover more
User interface
Comfy
AI
Stable Diffusion
Interface
FLUX
Artificial intelligence
ComfyUI
Wiki
SDXL
