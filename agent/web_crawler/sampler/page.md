[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling "Sampling")Sampler
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Sampler Detailed Explanation
ComfyUI currently has samplers
### Old Sampler[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/sampler#old-sampler)
### DPM Sampler[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/sampler#dpm-sampler)
### New Sampler[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/sampler#new-sampler)
  * heun
  * heunpp2
  * dpmpp_2
  * dpmpp_2_ancestral
  * lms
  * dpm_fast
  * dpm_adaptive
  * dpmpp_2s_ancestral
  * dpmpp_sde
  * dpmpp_sde_gpu
  * dpmpp_2m
  * dpmpp_2m_sde
  * dpmpp_2m_sde_gpu
  * dpmpp_3m_sde
  * dpmpp_3m_sde_gpu
  * ddpm
  * lcm
  * ddim
  * uni_pc
  * uni_pc_bh2


  1. Samplers with names containing ‘a’ or ‘ancestral’


  * **a** is an abbreviation for `ancestral (ancestral sampler)` in English, such samplers will continuously add noise during the sampling process, making each step of the sampling process generate images with a certain degree of randomness, which means **non-convergence**


  1. Samplers with ‘GPU’ in their names


  * Samplers like `dpmpp_sde_gpu` are optimized for GPU hardware, they can efficiently run large-scale parallel computing tasks on graphics processors, significantly speeding up image generation.


### Scheduler[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/sampler#scheduler)
The scheduler controls the denoising process, determining the number of denoising steps and the denoising intensity of each step. The main schedulers in ComfyUI are
  * norlmal
  * karras


> Rendering time is consistent, but after 8 sampling steps, there will be fewer noise points
  * exponential


> The image will be smoother, the background will be cleaner, but the drawback is that it will lose some details
  * sgm_uniform
  * simple
  * ddim_uniform


Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler-advanced "KSampler \(Advanced\)")[Video Linear CFG Guidance](https://comfyui-wiki.com/en/comfyui-nodes/sampling/video-models/video-linear-cfg-guidance "Video Linear CFG Guidance")
Discover more
GPU
Graphics processing unit
ComfyUI
Samplers
Sampler
Stable diffusion
gpu
Wiki
Stable Diffusion
samplers
