[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[transform](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-crop "transform")Flip Latent
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Flip Latent
![comfyUI节点-Flip Latent｜Latent翻转](https://comfyui-wiki.com/latent/transform/Flip_Latent.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-flip#documentation)
  * Class name: `LatentFlip`
  * Category: `latent/transform`
  * Output node: `False`


The LatentFlip node is designed to manipulate latent representations by flipping them either vertically or horizontally. This operation allows for the transformation of the latent space, potentially uncovering new variations or perspectives within the data.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-flip#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The ‘samples’ parameter represents the latent representations to be flipped. The flipping operation alters these representations, either vertically or horizontally, depending on the ‘flip_method’ parameter, thus transforming the data in the latent space.  
`flip_method` | `COMBO[STRING]` | The ‘flip_method’ parameter specifies the axis along which the latent samples will be flipped. It can be either ‘x-axis: vertically’ or ‘y-axis: horizontally’, determining the direction of the flip and thus the nature of the transformation applied to the latent representations.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-flip#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a modified version of the input latent representations, having been flipped according to the specified method. This transformation can introduce new variations within the latent space.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-crop "Crop Latent")[Rotate Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-rotate "Rotate Latent")
Discover more
FLUX
Flux.1
Black Forest Labs
Stable Diffusion
ComfyUI
interface
User interface
Artificial intelligence
SDXL
stable diffusion
