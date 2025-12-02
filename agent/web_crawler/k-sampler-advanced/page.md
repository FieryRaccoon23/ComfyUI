[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling "Sampling")KSampler (Advanced)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# KSampler (Advanced)
![comfyUI节点-KSampler\(Advanced\) K采样器（高级）｜ComfyUI组件节点](https://comfyui-wiki.com/sampling/KSampler\(Advanced\).jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler-advanced#documentation)
  * Class name: `KSamplerAdvanced`
  * Category: `sampling`
  * Output node: `False`


The KSamplerAdvanced node is designed to enhance the sampling process by providing advanced configurations and techniques. It aims to offer more sophisticated options for generating samples from a model, improving upon the basic KSampler functionalities.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler-advanced#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | MODEL | Specifies the model from which samples are to be generated, playing a crucial role in the sampling process.  
`add_noise` | COMBO[STRING] | Determines whether noise should be added to the sampling process, affecting the diversity and quality of the generated samples.  
`noise_seed` | INT | Sets the seed for noise generation, ensuring reproducibility in the sampling process.  
`steps` | INT | Defines the number of steps to be taken in the sampling process, impacting the detail and quality of the output.  
`cfg` | FLOAT | Controls the conditioning factor, influencing the direction and space of the sampling process.  
`sampler_name` | COMBO[STRING] | Selects the specific sampler to be used, allowing for customization of the sampling technique.  
`scheduler` | COMBO[STRING] | Chooses the scheduler for controlling the sampling process, affecting the progression and quality of samples.  
`positive` | CONDITIONING | Specifies the positive conditioning to guide the sampling towards desired attributes.  
`negative` | CONDITIONING | Specifies the negative conditioning to steer the sampling away from certain attributes.  
`latent_image` | LATENT | Provides the initial latent image to be used in the sampling process, serving as a starting point.  
`start_at_step` | INT | Determines the starting step of the sampling process, allowing for control over the sampling progression.  
`end_at_step` | INT | Sets the ending step of the sampling process, defining the scope of the sampling.  
`return_with_leftover_noise` | COMBO[STRING] | Indicates whether to return the sample with leftover noise, affecting the final output’s appearance.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler-advanced#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | LATENT | The output represents the latent image generated from the model, reflecting the applied configurations and techniques.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler "KSampler")[Sampler](https://comfyui-wiki.com/en/comfyui-nodes/sampling/sampler "Sampler")
Discover more
Stable diffusion
ComfyUI
Stable Diffusion
Wiki
Sdxl
FLUX.1
User interface
AI
SDXL
Black Forest Labs
