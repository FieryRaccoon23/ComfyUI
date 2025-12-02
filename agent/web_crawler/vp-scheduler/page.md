[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")[schedulers](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/basic-scheduler "schedulers")VP Scheduler
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# VP Scheduler
![comfyUI节点-VPScheduler｜VP调度器](https://comfyui-wiki.com/sampling/custom_sampling/VPScheduler.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/vp-scheduler#documentation)
  * Class name: `VPScheduler`
  * Category: `sampling/custom_sampling/schedulers`
  * Output node: `False`


The VPScheduler node is designed to generate a sequence of noise levels (sigmas) based on the Variance Preserving (VP) scheduling method. This sequence is crucial for guiding the denoising process in diffusion models, allowing for controlled generation of images or other data types.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/vp-scheduler#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`steps` | INT | Specifies the number of steps in the diffusion process, affecting the granularity of the generated noise levels.  
`beta_d` | FLOAT | Determines the overall noise level distribution, influencing the variance of the generated noise levels.  
`beta_min` | FLOAT | Sets the minimum boundary for the noise level, ensuring the noise does not fall below a certain threshold.  
`eps_s` | FLOAT | Adjusts the starting epsilon value, fine-tuning the initial noise level in the diffusion process.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/vp-scheduler#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | SIGMAS | A sequence of noise levels (sigmas) generated based on the VP scheduling method, used to guide the denoising process in diffusion models.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/sd-turbo-scheduler "SD Turbo Scheduler")[Flip Sigmas](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/flip-sigmas "Flip Sigmas")
Discover more
stable diffusion
Stable diffusion
Flux.1
Black Forest Labs
Interface
ComfyUI
Artificial intelligence
Wiki
Stable Diffusion
SDXL
