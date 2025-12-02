[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")samplersKSampler Select
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# KSampler Select
![ KSampler Select ](https://comfyui-wiki.com/sampling/custom_sampling/samplers/KSamplerSelect.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/k-sampler-select#documentation)
  * Class name: `KSamplerSelect`
  * Category: `sampling/custom_sampling/samplers`
  * Output node: `False`


The KSamplerSelect node is designed to select a specific sampler based on the provided sampler name. It abstracts the complexity of sampler selection, allowing users to easily switch between different sampling strategies for their tasks.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/k-sampler-select#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sampler_name` | `COMBO[STRING]` | Specifies the name of the sampler to be selected. This parameter determines which sampling strategy will be used, impacting the overall sampling behavior and results.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/k-sampler-select#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sampler` | `SAMPLER` | Returns the selected sampler object, ready to be used for sampling tasks.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "SamplerCustom")[Sampler DPMPP_2M_SDE](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/samplers/sampler-dpmpp-2m-sde "Sampler DPMPP_2M_SDE")
Discover more
Text-to-image model
ComfyUI
Stable Diffusion
Stable diffusion
Wiki
Workflow
Image Generation
interface
FLUX.1
Interface
