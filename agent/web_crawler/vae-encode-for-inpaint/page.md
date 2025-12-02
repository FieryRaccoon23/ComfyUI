[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[inpaint](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/set-latent-noise-mask "inpaint")VAE Encode (for Inpainting)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# VAE Encode (for Inpainting)
![comfyUI节点-VAE Encoder\(for inpainting\)-VAE内补编码器](https://comfyui-wiki.com/latent/inpaint/VAE_Encoder\(for_inpainting\).jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/vae-encode-for-inpaint#documentation)
  * Class name: `VAEEncodeForInpaint`
  * Category: `latent/inpaint`
  * Output node: `False`


This node is designed for encoding images into a latent representation suitable for inpainting tasks, incorporating additional preprocessing steps to adjust the input image and mask for optimal encoding by the VAE model.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/vae-encode-for-inpaint#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`pixels` | `IMAGE` | The input image to be encoded. This image undergoes preprocessing and resizing to match the VAE model’s expected input dimensions before encoding.  
`vae` | `VAE` | The VAE model used for encoding the image into its latent representation. It plays a crucial role in the transformation process, determining the quality and characteristics of the output latent space.  
`mask` | `MASK` | A mask indicating the regions of the input image to be inpainted. It is used to modify the image before encoding, ensuring that the VAE focuses on the relevant areas.  
`grow_mask_by` | `INT` | Specifies how much to expand the inpainting mask to ensure seamless transitions in the latent space. A larger value increases the area affected by inpainting.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/vae-encode-for-inpaint#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output includes the encoded latent representation of the image and a noise mask, both crucial for subsequent inpainting tasks.  
## Workflow Examples[](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/vae-encode-for-inpaint#workflow-examples)
![VAE Encoder\(for inpainting\) usage example](https://comfyui-wiki.com/_next/static/media/demo-1.b116af56.jpg)
Others 
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/set-latent-noise-mask "Set Latent Noise Mask")[Crop Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-crop "Crop Latent")
Discover more
Stable diffusion
comfyUI
Workflow
workflow
ComfyUI
Stable Diffusion
user interface
Sdxl
Wiki
FLUX
