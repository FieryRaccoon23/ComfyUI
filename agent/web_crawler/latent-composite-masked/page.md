[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")Latent Composite Masked
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Latent Composite Masked
![comfyUI节点-LatentCompositeMasked｜Latent遮罩复合](https://comfyui-wiki.com/latent/LatentCompositeMasked.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite-masked#documentation)
  * Class name: `LatentCompositeMasked`
  * Category: `latent`
  * Output node: `False`


The LatentCompositeMasked node is designed for blending two latent representations together at specified coordinates, optionally using a mask for more controlled compositing. This node enables the creation of complex latent images by overlaying parts of one image onto another, with the ability to resize the source image for a perfect fit.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite-masked#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`destination` | `LATENT` | The latent representation onto which another latent representation will be composited. Acts as the base layer for the composite operation.  
`source` | `LATENT` | The latent representation to be composited onto the destination. This source layer can be resized and positioned according to the specified parameters.  
`x` | `INT` | The x-coordinate in the destination latent representation where the source will be placed. Allows for precise positioning of the source layer.  
`y` | `INT` | The y-coordinate in the destination latent representation where the source will be placed, enabling accurate overlay positioning.  
`resize_source` | `BOOLEAN` | A boolean flag indicating whether the source latent representation should be resized to match the destination’s dimensions before compositing.  
`mask` | `MASK` | An optional mask that can be used to control the blending of the source onto the destination. The mask defines which parts of the source will be visible in the final composite.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite-masked#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The resulting latent representation after compositing the source onto the destination, potentially using a mask for selective blending.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-encode "VAE Encode")[Latent Add](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-add "Latent Add")
Discover more
ComfyUI
Stable diffusion
Stable Diffusion
FLUX
User interface
Comfy
AI
Wiki
user interface
Flux
