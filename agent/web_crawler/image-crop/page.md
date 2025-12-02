[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")transformImage Crop
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Image Crop
![comfyUI节点-ImageCrop|图像裁剪](https://comfyui-wiki.com/image/transform/ImageCrop.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/transform/image-crop#documentation)
  * Class name: `ImageCrop`
  * Category: `image/transform`
  * Output node: `False`


The ImageCrop node is designed for cropping images to a specified width and height starting from a given x and y coordinate. This functionality is essential for focusing on specific regions of an image or for adjusting the image size to meet certain requirements.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/transform/image-crop#input-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The input image to be cropped. This parameter is crucial as it defines the source image from which a region will be extracted based on the specified dimensions and coordinates.  
`width` | `INT` | Specifies the width of the cropped image. This parameter determines how wide the resulting cropped image will be.  
`height` | `INT` | Specifies the height of the cropped image. This parameter determines the height of the resulting cropped image.  
`x` | `INT` | The x-coordinate of the top-left corner of the cropping area. This parameter sets the starting point for the width dimension of the crop.  
`y` | `INT` | The y-coordinate of the top-left corner of the cropping area. This parameter sets the starting point for the height dimension of the crop.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/transform/image-crop#output-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The cropped image as a result of the cropping operation. This output is significant for further processing or analysis of the specified image region.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/save-image "Save Image - Save Images to Local in ComfyUI")[Image Scale](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale "Image Scale")
