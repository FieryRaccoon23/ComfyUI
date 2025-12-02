[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[advanced](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-add "advanced")Latent Interpolate
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Latent Interpolate
![comfyUI节点-LatentInterpolate-Latent插值](https://comfyui-wiki.com/latent/advanced/LatentInterpolate.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-interpolate#documentation)
  * Class name: `LatentInterpolate`
  * Category: `latent/advanced`
  * Output node: `False`


The LatentInterpolate node is designed to perform interpolation between two sets of latent samples based on a specified ratio, blending the characteristics of both sets to produce a new, intermediate set of latent samples.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-interpolate#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples1` | `LATENT` | The first set of latent samples to be interpolated. It serves as the starting point for the interpolation process.  
`samples2` | `LATENT` | The second set of latent samples to be interpolated. It serves as the endpoint for the interpolation process.  
`ratio` | `FLOAT` | A floating-point value that determines the weight of each set of samples in the interpolated output. A ratio of 0 produces a copy of the first set, while a ratio of 1 produces a copy of the second set.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-interpolate#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a new set of latent samples that represent an interpolated state between the two input sets, based on the specified ratio.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-batch-seed-behavior "Latent Batch Seed Behavior")[Latent Multiply](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-multiply "Latent Multiply")
