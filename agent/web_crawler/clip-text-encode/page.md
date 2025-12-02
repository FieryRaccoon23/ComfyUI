[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")CLIP Text Encode (Prompt)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# CLIP Text Encode (Prompt)
![CLIP Text Encode](https://comfyui-wiki.com/_next/static/media/CLIP_Text_Encode-prompt.ad6d454a.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-text-encode#documentation)
  * Class name: `CLIPTextEncode`
  * Category: `conditioning`
  * Output node: `False`


The CLIPTextEncode node is designed to encode textual inputs using a CLIP model, transforming text into a form that can be utilized for conditioning in generative tasks. It abstracts the complexity of text tokenization and encoding, providing a streamlined interface for generating text-based conditioning vectors.
Besides normal text prompts, you can also use embedding models. For example, if you add an embedding model in the `ComfyUI/models/embeddings` directory, you can use this embedding model in the prompt.
For example, if the corresponding model name is `EasyNegative`, you can use `embedding:EasyNegative,` in the prompt to use this corresponding model.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-text-encode#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`text` | `STRING` | The ‘text’ parameter is the textual input that will be encoded. It plays a crucial role in determining the output conditioning vector, as it is the primary source of information for the encoding process.  
`clip` | `CLIP` | The ‘clip’ parameter represents the CLIP model used for text tokenization and encoding. It is essential for converting the textual input into a conditioning vector, influencing the quality and relevance of the generated output.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-text-encode#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The output ‘conditioning’ is a vector representation of the input text, encoded by the CLIP model. It serves as a crucial component for guiding generative models in producing relevant and coherent outputs.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-set-last-layer "CLIP Set Last Layer")[CLIP Vision Encode](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-vision-encode "CLIP Vision Encode")
Discover more
Stable Diffusion
ComfyUI
Wiki
Stable diffusion
interface
Flux
AI
stable diffusion
SDXL
Comfy
