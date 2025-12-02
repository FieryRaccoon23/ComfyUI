[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")transformCrop Latent
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Crop Latent
![comfyUI节点-Crop Latent｜Latent裁剪](https://comfyui-wiki.com/latent/transform/Crop_Latent.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-crop#documentation)
  * Class name: `LatentCrop`
  * Category: `latent/transform`
  * Output node: `False`


The LatentCrop node is designed to perform cropping operations on latent representations of images. It allows for the specification of the crop dimensions and position, enabling targeted modifications of the latent space.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-crop#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The ‘samples’ parameter represents the latent representations to be cropped. It is crucial for defining the data on which the cropping operation will be performed.  
`width` | `INT` | Specifies the width of the crop area. It directly influences the dimensions of the output latent representation.  
`height` | `INT` | Specifies the height of the crop area, affecting the size of the resulting cropped latent representation.  
`x` | `INT` | Determines the starting x-coordinate of the crop area, influencing the position of the crop within the original latent representation.  
`y` | `INT` | Determines the starting y-coordinate of the crop area, setting the position of the crop within the original latent representation.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-crop#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a modified latent representation with the specified crop applied.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/vae-encode-for-inpaint "VAE Encode \(for Inpainting\)")[Flip Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-flip "Flip Latent")
Discover more
Flux
interface
stable diffusion
Comfy
Flux.1
Artificial intelligence
user interface
AI
SDXL
FLUX.1
