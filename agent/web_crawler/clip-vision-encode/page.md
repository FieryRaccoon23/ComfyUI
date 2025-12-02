[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")CLIP Vision Encode
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# CLIP Vision Encode
![comfyUI节点-CLIP Vision Encode｜CLIP视觉编码](https://comfyui-wiki.com/conditioning/CLIP_Vision_Encode.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-vision-encode#documentation)
  * Class name: `CLIPVisionEncode`
  * Category: `conditioning`
  * Output node: `False`


The CLIPVisionEncode node is designed to encode images using a CLIP vision model, transforming visual input into a format suitable for further processing or analysis. This node abstracts the complexity of image encoding, offering a streamlined interface for converting images into encoded representations.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-vision-encode#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip_vision` | `CLIP_VISION` | The CLIP vision model used for encoding the image. It is crucial for the encoding process, as it determines the method and quality of the encoding.  
`image` | `IMAGE` | The image to be encoded. This input is essential for generating the encoded representation of the visual content.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-vision-encode#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip_vision_output` | `CLIP_VISION_OUTPUT` | The encoded representation of the input image, produced by the CLIP vision model. This output is suitable for further processing or analysis.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-text-encode "CLIP Text Encode \(Prompt\)")[Conditioning Average](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-average "Conditioning Average")
