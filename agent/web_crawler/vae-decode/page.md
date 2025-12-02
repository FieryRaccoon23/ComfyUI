[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")VAE Decode
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# VAE Decode
![comfyUI节点-VAE Decode｜VAE解码](https://comfyui-wiki.com/latent/VAE_Decode.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-decode#documentation)
  * Class name: `VAEDecode`
  * Category: `latent`
  * Output node: `False`


The VAEDecode node is designed for decoding latent representations into images using a specified Variational Autoencoder (VAE). It serves the purpose of generating images from compressed data representations, facilitating the reconstruction of images from their latent space encodings.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-decode#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The ‘samples’ parameter represents the latent representations to be decoded into images. It is crucial for the decoding process as it provides the compressed data from which the images are reconstructed.  
`vae` | `VAE` | The ‘vae’ parameter specifies the Variational Autoencoder model to be used for decoding the latent representations into images. It is essential for determining the decoding mechanism and the quality of the reconstructed images.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-decode#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The output is an image reconstructed from the provided latent representation using the specified VAE model.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite "Latent Composite")[VAE Encode](https://comfyui-wiki.com/en/comfyui-nodes/latent/vae-encode "VAE Encode")
Discover more
ComfyUI
Stable diffusion
Stable Diffusion
SDXL
FLUX.1
Interface
user interface
interface
Flux
Black Forest Labs
