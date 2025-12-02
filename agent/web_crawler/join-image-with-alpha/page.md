[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")MaskcompositingJoin Image with Alpha
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Join Image with Alpha
![comfyUI节点-Join Image with Alpha|合并图像Alpha](https://comfyui-wiki.com/mask/compositing/Join_Image_with_Alpha.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/join-image-with-alpha#documentation)
  * Class name: `JoinImageWithAlpha`
  * Category: `mask/compositing`
  * Output node: `False`


This node is designed for compositing operations, specifically to join an image with its corresponding alpha mask to produce a single output image. It effectively combines visual content with transparency information, enabling the creation of images where certain areas are transparent or semi-transparent.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/join-image-with-alpha#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The main visual content to be combined with an alpha mask. It represents the image without transparency information.  
`alpha` | `MASK` | The alpha mask that defines the transparency of the corresponding image. It is used to determine which parts of the image should be transparent or semi-transparent.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/join-image-with-alpha#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The output is a single image that combines the input image with the alpha mask, incorporating transparency information into the visual content.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/video-models/image-only-checkpoint-loader "Image Only Checkpoint Loader \(img2vid model\)")[Porter-Duff Image Composite](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/porter-duff-image-composite "Porter-Duff Image Composite")
Discover more
User interface
Flux
Wiki
Stable Diffusion
SDXL
user interface
ComfyUI
Sdxl
Comfy
Flux.1
