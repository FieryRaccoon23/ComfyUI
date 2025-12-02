[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")preprocessorsCanny Node
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Canny
![comfyUI节点-Canny](https://comfyui-wiki.com/image/preprocessors/Canny.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/preprocessors/canny#documentation)
  * Class name: `Canny`
  * Category: `image/preprocessors`
  * Output node: `False`


The Canny node is designed for edge detection in images, utilizing the Canny algorithm to identify and highlight the edges. This process involves applying a series of filters to the input image to detect areas of high gradient, which correspond to edges, thereby enhancing the image’s structural details.
## 输入类型[](https://comfyui-wiki.com/en/comfyui-nodes/image/preprocessors/canny#%E8%BE%93%E5%85%A5%E7%B1%BB%E5%9E%8B)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The input image to be processed for edge detection. It is crucial as it serves as the base for the edge detection operation.  
`low_threshold` | `FLOAT` | The lower threshold for the hysteresis procedure in edge detection. It determines the minimum intensity gradient considered for an edge, affecting the sensitivity of edge detection.  
`high_threshold` | `FLOAT` | The upper threshold for the hysteresis procedure in edge detection. It sets the maximum intensity gradient considered for an edge, influencing the selectivity of edge detection.  
## 输出类型[](https://comfyui-wiki.com/en/comfyui-nodes/image/preprocessors/canny#%E8%BE%93%E5%87%BA%E7%B1%BB%E5%9E%8B)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The output is an image with highlighted edges, where the edges are detected using the Canny algorithm. This enhances the structural details of the original image.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-sharpen "Image Sharpen")[Preview Image](https://comfyui-wiki.com/en/comfyui-nodes/image/preview-image "Preview Image")
Discover more
Stable Diffusion
ComfyUI
Stable diffusion
Workflow
Sdxl
Interface
user interface
Flux
Black Forest Labs
Comfy
