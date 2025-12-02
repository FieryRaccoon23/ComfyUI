[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")[postprocessing](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-blend "postprocessing")Image Sharpen
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Image Sharpen
![comfyUI节点-ImageSharpen|图像锐化](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-sharpen)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-sharpen#documentation)
  * Class name: `ImageSharpen`
  * Category: `image/postprocessing`
  * Output node: `False`


The ImageSharpen node enhances the clarity of an image by accentuating its edges and details. It applies a sharpening filter to the image, which can be adjusted in intensity and radius, thereby making the image appear more defined and crisp.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-sharpen#input-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The input image to be sharpened. This parameter is crucial as it determines the base image on which the sharpening effect will be applied.  
`sharpen_radius` | `INT` | Defines the radius of the sharpening effect. A larger radius means that more pixels around the edge will be affected, leading to a more pronounced sharpening effect.  
`sigma` | `FLOAT` | Controls the spread of the sharpening effect. A higher sigma value results in a smoother transition at the edges, while a lower sigma makes the sharpening more localized.  
`alpha` | `FLOAT` | Adjusts the intensity of the sharpening effect. Higher alpha values result in a stronger sharpening effect.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-sharpen#output-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The sharpened image, with enhanced edges and details, ready for further processing or display.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-quantize "Image Quantize")[Canny Node](https://comfyui-wiki.com/en/comfyui-nodes/image/preprocessors/canny "Canny Node")
Discover more
Stable diffusion
Wiki
ComfyUI
Workflow
Stable Diffusion
stable diffusion
Flux.1
Interface
Sdxl
FLUX
