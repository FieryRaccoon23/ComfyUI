[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Mask[compositing](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/join-image-with-alpha "compositing")Porter-Duff Image Composite
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Porter-Duff Image Composite
![comfyUI节点-Porter-Duff Image Composite|Porter-Duff图像合成](https://comfyui-wiki.com/mask/compositing/Porter_Duff_Image_Composite.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/porter-duff-image-composite#documentation)
  * Class name: `PorterDuffImageComposite`
  * Category: `mask/compositing`
  * Output node: `False`


The PorterDuffImageComposite node is designed to perform image compositing using the Porter-Duff compositing operators. It allows for the combination of source and destination images according to various blending modes, enabling the creation of complex visual effects by manipulating image transparency and overlaying images in creative ways.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/porter-duff-image-composite#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`source` | `IMAGE` | The source image tensor to be composited over the destination image. It plays a crucial role in determining the final visual outcome based on the selected compositing mode.  
`source_alpha` | `MASK` | The alpha channel of the source image, which specifies the transparency of each pixel in the source image. It affects how the source image blends with the destination image.  
`destination` | `IMAGE` | The destination image tensor that serves as the backdrop over which the source image is composited. It contributes to the final composited image based on the blending mode.  
`destination_alpha` | `MASK` | The alpha channel of the destination image, defining the transparency of the destination image’s pixels. It influences the blending of the source and destination images.  
`mode` | `COMBO[STRING]` | The Porter-Duff compositing mode to apply, which determines how the source and destination images are blended together. Each mode creates different visual effects.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/porter-duff-image-composite#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The composited image resulting from the application of the specified Porter-Duff mode.  
`mask` | `MASK` | The alpha channel of the composited image, indicating the transparency of each pixel.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/join-image-with-alpha "Join Image with Alpha")[Split Image with Alpha](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/split-image-with-alpha "Split Image with Alpha")
Discover more
Stable diffusion
Wiki
Stable Diffusion
ComfyUI
stable diffusion
Flux.1
User interface
FLUX
Black Forest Labs
user interface
