[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Mask[compositing](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/join-image-with-alpha "compositing")Split Image with Alpha
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Split Image with Alpha
![comfyUI节点-Split Image with Alpha|分离图像Alpha](https://comfyui-wiki.com/mask/compositing/Split_Image_with_Alpha.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/split-image-with-alpha#documentation)
  * Class name: `SplitImageWithAlpha`
  * Category: `mask/compositing`
  * Output node: `False`


The SplitImageWithAlpha node is designed to separate the color and alpha components of an image. It processes an input image tensor, extracting the RGB channels as the color component and the alpha channel as the transparency component, facilitating operations that require manipulation of these distinct image aspects.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/split-image-with-alpha#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The ‘image’ parameter represents the input image tensor from which the RGB and alpha channels are to be separated. It is crucial for the operation as it provides the source data for the split.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/split-image-with-alpha#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The ‘image’ output represents the separated RGB channels of the input image, providing the color component without the transparency information.  
`mask` | `MASK` | The ‘mask’ output represents the separated alpha channel of the input image, providing the transparency information.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/porter-duff-image-composite "Porter-Duff Image Composite")[Crop Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/crop-mask "Crop Mask")
Discover more
interface
Flux.1
Interface
AI
user interface
Stable Diffusion
User interface
Wiki
ComfyUI
stable diffusion
