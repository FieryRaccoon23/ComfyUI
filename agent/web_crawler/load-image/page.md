[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")Load Image
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load Image
![comfyUI节点-Load Image|加载图像](https://comfyui-wiki.com/image/Load_Image.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/load-image#documentation)
  * Class name: `LoadImage`
  * Category: `image`
  * Output node: `False`


The LoadImage node is designed to load and preprocess images from a specified path. It handles image formats with multiple frames, applies necessary transformations such as rotation based on EXIF data, normalizes pixel values, and optionally generates a mask for images with an alpha channel. This node is essential for preparing images for further processing or analysis within a pipeline.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/load-image#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `COMBO[STRING]` | The ‘image’ parameter specifies the identifier of the image to be loaded and processed. It is crucial for determining the path to the image file and subsequently loading the image for transformation and normalization.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/load-image#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The processed image, with pixel values normalized and transformations applied as necessary. It is ready for further processing or analysis.  
`mask` | `MASK` | An optional output providing a mask for the image, useful in scenarios where the image includes an alpha channel for transparency.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-pad-for-outpaint "Image Pad For Outpainting")[Image Blend](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-blend "Image Blend")
Discover more
Stable Diffusion
ComfyUI
Stable diffusion
Wiki
interface
user interface
Flux.1
Comfy
Artificial intelligence
SDXL
