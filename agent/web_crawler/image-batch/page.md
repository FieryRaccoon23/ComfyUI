[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")Image Batch
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Batch Images
![comfyUI节点-Batch Images|图像组合批次](https://comfyui-wiki.com/image/Batch_Images.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-batch#documentation)
  * Class name: `ImageBatch`
  * Category: `image`
  * Output node: `False`


The ImageBatch node is designed for combining two images into a single batch. If the dimensions of the images do not match, it automatically rescales the second image to match the first one’s dimensions before combining them.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-batch#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image1` | `IMAGE` | The first image to be combined into the batch. It serves as the reference for the dimensions to which the second image will be adjusted if necessary.  
`image2` | `IMAGE` | The second image to be combined into the batch. It is automatically rescaled to match the dimensions of the first image if they differ.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-batch#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The combined batch of images, with the second image rescaled to match the first one’s dimensions if needed.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/empty-image "Empty Image")[Image Composite Masked](https://comfyui-wiki.com/en/comfyui-nodes/image/image-composite-masked "Image Composite Masked")
Discover more
Workflow
Image Generation
ComfyUI
Stable Diffusion
Stable diffusion
Text-to-image model
Wiki
Sdxl
Artificial intelligence
user interface
