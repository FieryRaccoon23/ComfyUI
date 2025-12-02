[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")[postprocessing](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-blend "postprocessing")Image Blur
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Image Blur
![comfyUI节点-ImageBlur|图像模糊](https://comfyui-wiki.com/image/postprocessing/ImageBlur.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-blur#documentation)
  * Class name: `ImageBlur`
  * Category: `image/postprocessing`
  * Output node: `False`


The ImageBlur node applies a Gaussian blur to an image, allowing for the softening of edges and reduction of detail and noise. It provides control over the intensity and spread of the blur through parameters.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-blur#input-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The input image to be blurred. This is the primary target for the blur effect.  
`blur_radius` | `INT` | Determines the radius of the blur effect. A larger radius results in a more pronounced blur.  
`sigma` | `FLOAT` | Controls the spread of the blur. A higher sigma value means the blur will affect a wider area around each pixel.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-blur#output-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The output is the blurred version of the input image, with the degree of blur determined by the input parameters.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-blend "Image Blend")[Image Quantize](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-quantize "Image Quantize")
Discover more
user interface
SDXL
Black Forest Labs
Stable diffusion
ComfyUI
Flux
FLUX
interface
Artificial intelligence
Sdxl
