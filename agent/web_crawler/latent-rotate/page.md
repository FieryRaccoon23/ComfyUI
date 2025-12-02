[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[transform](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-crop "transform")Rotate Latent
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Rotate Latent
![comfyUI节点-Rotate Latent｜Latent旋转](https://comfyui-wiki.com/latent/transform/Rotate_Latent.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-rotate#documentation)
  * Class name: `LatentRotate`
  * Category: `latent/transform`
  * Output node: `False`


The LatentRotate node is designed to rotate latent representations of images by specified angles. It abstracts the complexity of manipulating latent space to achieve rotation effects, enabling users to easily transform images in a generative model’s latent space.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-rotate#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The ‘samples’ parameter represents the latent representations of images to be rotated. It is crucial for determining the starting point of the rotation operation.  
`rotation` | `COMBO[STRING]` | The ‘rotation’ parameter specifies the angle by which the latent images should be rotated. It directly influences the orientation of the resulting images.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-rotate#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a modified version of the input latent representations, rotated by the specified angle.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-flip "Flip Latent")[Empty Hunyuan Latent Video Node Tutorial](https://comfyui-wiki.com/en/comfyui-nodes/latent/video/empty-hunyuan-latent-video "Empty Hunyuan Latent Video Node Tutorial")
Discover more
AI
user interface
SDXL
User interface
Black Forest Labs
Wiki
Flux.1
Comfy
interface
ComfyUI
