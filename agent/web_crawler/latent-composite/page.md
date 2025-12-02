[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")Latent Composite
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Latent Composite
![comfyUI节点-Latent Composite｜Latent复合](https://comfyui-wiki.com/latent/Latent_Composite.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite#documentation)
  * Class name: `LatentComposite`
  * Category: `latent`
  * Output node: `False`


The LatentComposite node is designed to blend or merge two latent representations into a single output. This process is essential for creating composite images or features by combining the characteristics of the input latents in a controlled manner.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples_to` | `LATENT` | The ‘samples_to’ latent representation where the ‘samples_from’ will be composited onto. It serves as the base for the composite operation.  
`samples_from` | `LATENT` | The ‘samples_from’ latent representation to be composited onto the ‘samples_to’. It contributes its features or characteristics to the final composite output.  
`x` | `INT` | The x-coordinate (horizontal position) where the ‘samples_from’ latent will be placed on the ‘samples_to’. It determines the horizontal alignment of the composite.  
`y` | `INT` | The y-coordinate (vertical position) where the ‘samples_from’ latent will be placed on the ‘samples_to’. It determines the vertical alignment of the composite.  
`feather` | `INT` | A boolean indicating whether the ‘samples_from’ latent should be resized to match the ‘samples_to’ before compositing. This can affect the scale and proportion of the composite result.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a composite latent representation, blending the features of both ‘samples_to’ and ‘samples_from’ latents based on the specified coordinates and resizing option.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale-by "Latent Upscale By")[VAE Decode](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-decode "VAE Decode")
