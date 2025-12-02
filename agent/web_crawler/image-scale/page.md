[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")upscalingImage Scale
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Upscale Image
![comfyUI节点-Upscale Image|图像缩放](https://comfyui-wiki.com/image/upscaling/Upscale_Image.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale#documentation)
  * Class name: `ImageScale`
  * Category: `image/upscaling`
  * Output node: `False`


The ImageScale node is designed for resizing images to specific dimensions, offering a selection of upscale methods and the ability to crop the resized image. It abstracts the complexity of image upscaling and cropping, providing a straightforward interface for modifying image dimensions according to user-defined parameters.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The input image to be upscaled. This parameter is central to the node’s operation, serving as the primary data upon which resizing transformations are applied. The quality and dimensions of the output image are directly influenced by the original image’s properties.  
`upscale_method` | `COMBO[STRING]` | Specifies the method used for upscaling the image. The choice of method can affect the quality and characteristics of the upscaled image, influencing the visual fidelity and potential artifacts in the resized output.  
`width` | `INT` | The target width for the upscaled image. This parameter directly influences the dimensions of the output image, determining the horizontal scale of the resizing operation.  
`height` | `INT` | The target height for the upscaled image. This parameter directly influences the dimensions of the output image, determining the vertical scale of the resizing operation.  
`crop` | `COMBO[STRING]` | Determines whether and how the upscaled image should be cropped, offering options for disabled cropping or center cropping. This affects the final composition of the image by potentially removing edges to fit the specified dimensions.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The upscaled (and optionally cropped) image, ready for further processing or visualization.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/transform/image-crop "Image Crop")[Image Scale By Node](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-by "Image Scale By Node")
Discover more
Wiki
ComfyUI
Flux.1
FLUX.1
Stable Diffusion
SDXL
Comfy
interface
AI
Stable diffusion
