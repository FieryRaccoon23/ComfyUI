[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")advancedLatent Add
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Latent Add
![comfyUI节点-LatentAdd-Latent相加](https://comfyui-wiki.com/latent/advanced/LatentAdd.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-add#documentation)
  * Class name: `LatentAdd`
  * Category: `latent/advanced`
  * Output node: `False`


The LatentAdd node is designed for the addition of two latent representations. It facilitates the combination of features or characteristics encoded in these representations by performing element-wise addition.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-add#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples1` | `LATENT` | The first set of latent samples to be added. It represents one of the inputs whose features are to be combined with another set of latent samples.  
`samples2` | `LATENT` | The second set of latent samples to be added. It serves as the other input whose features are combined with the first set of latent samples through element-wise addition.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-add#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The result of the element-wise addition of two latent samples, representing a new set of latent samples that combines the features of both inputs.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite-masked "Latent Composite Masked")[Latent Batch Seed Behavior](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-batch-seed-behavior "Latent Batch Seed Behavior")
