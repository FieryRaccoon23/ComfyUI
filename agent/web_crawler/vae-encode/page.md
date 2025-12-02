[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")VAE Encode
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# VAE Encode
![comfyUI节点-VAE Encode｜VAE编码](https://comfyui-wiki.com/latent/VAE_Encode.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-encode#documentation)
  * Class name: `VAEEncode`
  * Category: `latent`
  * Output node: `False`


This node is designed for encoding images into a latent space representation using a specified VAE model. It abstracts the complexity of the encoding process, providing a straightforward way to transform images into their latent representations.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-encode#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`pixels` | `IMAGE` | The ‘pixels’ parameter represents the image data to be encoded into the latent space. It plays a crucial role in determining the output latent representation by serving as the direct input for the encoding process.  
`vae` | `VAE` | The ‘vae’ parameter specifies the Variational Autoencoder model to be used for encoding the image data into latent space. It is essential for defining the encoding mechanism and characteristics of the generated latent representation.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-encode#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a latent space representation of the input image, encapsulating its essential features in a compressed form.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-decode "VAE Decode")[Latent Composite Masked](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite-masked "Latent Composite Masked")
Discover more
ComfyUI
Stable diffusion
Stable Diffusion
stable diffusion
Flux.1
Sdxl
Artificial intelligence
AI
Comfy
user interface
