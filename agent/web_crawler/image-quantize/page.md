[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")[postprocessing](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-blend "postprocessing")Image Quantize
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Image Quantize
![comfyUI节点-ImageQuantize|图像量化](https://comfyui-wiki.com/image/postprocessing/ImageQuantize.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-quantize#documentation)
  * Class name: `ImageQuantize`
  * Category: `image/postprocessing`
  * Output node: `False`


The ImageQuantize node is designed to reduce the number of colors in an image to a specified number, optionally applying dithering techniques to maintain visual quality. This process is useful for creating palette-based images or reducing the color complexity for certain applications.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-quantize#input-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The input image tensor to be quantized. It affects the node’s execution by being the primary data upon which color reduction is performed.  
`colors` | `INT` | Specifies the number of colors to reduce the image to. It directly influences the quantization process by determining the color palette size.  
`dither` | `COMBO[STRING]` | Determines the dithering technique to be applied during quantization, affecting the visual quality and appearance of the output image.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-quantize#output-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The quantized version of the input image, with reduced color complexity and optionally dithered to maintain visual quality.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-blur "Image Blur")[Image Sharpen](https://comfyui-wiki.com/en/comfyui-nodes/image/postprocessing/image-sharpen "Image Sharpen")
Discover more
Wiki
ComfyUI
Stable Diffusion
User interface
Sdxl
Black Forest Labs
Stable diffusion
Interface
stable diffusion
Comfy
