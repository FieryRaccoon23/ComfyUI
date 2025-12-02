[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")Empty Latent Image
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Empty Latent Image
![comfyUI节点-Empty Latent Image｜空Latent](https://comfyui-wiki.com/latent/Empty_Latent_Image.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/empty-latent-image#documentation)
  * Class name: `EmptyLatentImage`
  * Category: `latent`
  * Output node: `False`


The EmptyLatentImage node is designed to generate a blank latent space representation with specified dimensions and batch size. This node serves as a foundational step in generating or manipulating images in latent space, providing a starting point for further image synthesis or modification processes.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/empty-latent-image#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`width` | `INT` | Specifies the width of the latent image to be generated. This parameter directly influences the spatial dimensions of the resulting latent representation.  
`height` | `INT` | Determines the height of the latent image to be generated. This parameter is crucial for defining the spatial dimensions of the latent space representation.  
`batch_size` | `INT` | Controls the number of latent images to be generated in a single batch. This allows for the generation of multiple latent representations simultaneously, facilitating batch processing.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/empty-latent-image#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a tensor representing a batch of blank latent images, serving as a base for further image generation or manipulation in latent space.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent Upscale")[Latent Upscale By](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale-by "Latent Upscale By")
