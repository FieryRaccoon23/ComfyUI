[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")sigmasFlip Sigmas
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Flip Sigmas
![comfyUI节点-FlipSigmas｜翻转](https://comfyui-wiki.com/sampling/custom_sampling/sigmas/SplitSigmas.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/flip-sigmas#documentation)
  * Class name: `FlipSigmas`
  * Category: `sampling/custom_sampling/sigmas`
  * Output node: `False`


The FlipSigmas node is designed to manipulate the sequence of sigma values used in diffusion models by reversing their order and ensuring the first value is non-zero if originally zero. This operation is crucial for adapting the noise levels in reverse order, facilitating the generation process in models that operate by gradually reducing noise from data.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/flip-sigmas#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | `SIGMAS` | The ‘sigmas’ parameter represents the sequence of sigma values to be flipped. This sequence is crucial for controlling the noise levels applied during the diffusion process, and flipping it is essential for the reverse generation process.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/flip-sigmas#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | `SIGMAS` | The output is the modified sequence of sigma values, flipped and adjusted to ensure the first value is non-zero if originally zero, ready for use in subsequent diffusion model operations.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/schedulers/vp-scheduler "VP Scheduler")[Split Sigmas](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/split-sigmas "Split Sigmas")
Discover more
FLUX.1
AI
interface
Flux
ComfyUI
user interface
Artificial intelligence
Flux.1
Stable Diffusion
User interface
