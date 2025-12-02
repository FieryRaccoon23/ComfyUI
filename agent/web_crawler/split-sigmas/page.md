[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Sampling[custom-sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sampler-custom "custom-sampling")[sigmas](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/flip-sigmas "sigmas")Split Sigmas
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Split Sigmas
![comfyUI节点-SplitSigmas｜分离Sigmas](https://comfyui-wiki.com/sampling/custom_sampling/sigmas/SplitSigmas.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/split-sigmas#documentation)
  * Class name: `SplitSigmas`
  * Category: `sampling/custom_sampling/sigmas`
  * Output node: `False`


The SplitSigmas node is designed for dividing a sequence of sigma values into two parts based on a specified step. This functionality is crucial for operations that require different handling or processing of the initial and subsequent parts of the sigma sequence, enabling more flexible and targeted manipulation of these values.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/split-sigmas#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | `SIGMAS` | The ‘sigmas’ parameter represents the sequence of sigma values to be split. It is essential for determining the division point and the resulting two sequences of sigma values, impacting the node’s execution and results.  
`step` | `INT` | The ‘step’ parameter specifies the index at which the sigma sequence should be split. It plays a critical role in defining the boundary between the two resulting sigma sequences, influencing the node’s functionality and the characteristics of the output.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/split-sigmas#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`sigmas` | `SIGMAS` | The node outputs two sequences of sigma values, each representing a part of the original sequence divided at the specified step. These outputs are crucial for subsequent operations that require differentiated handling of sigma values.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/flip-sigmas "Flip Sigmas")[KSampler](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler "KSampler")
Discover more
Wiki
Stable Diffusion
ComfyUI
Workflow
Stable diffusion
SDXL
Black Forest Labs
Flux
Artificial intelligence
interface
