[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")inpaintSet Latent Noise Mask
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Set Latent Noise Mask
![comfyUI节点-Set Latent Noise Mask-设置Latent噪波遮罩](https://comfyui-wiki.com/latent/inpaint/Set_Latent_Noise_Mask.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/set-latent-noise-mask#documentation)
  * Class name: `SetLatentNoiseMask`
  * Category: `latent/inpaint`
  * Output node: `False`


This node is designed to apply a noise mask to a set of latent samples. It modifies the input samples by integrating a specified mask, thereby altering their noise characteristics.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/set-latent-noise-mask#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The latent samples to which the noise mask will be applied. This parameter is crucial for determining the base content that will be modified.  
`mask` | `MASK` | The mask to be applied to the latent samples. It defines the areas and intensity of noise alteration within the samples.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/set-latent-noise-mask#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The modified latent samples with the applied noise mask.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/repeat-latent-batch "Repeat Latent Batch")[VAE Encode (for Inpainting)](https://comfyui-wiki.com/en/comfyui-nodes/latent/inpaint/vae-encode-for-inpaint "VAE Encode \(for Inpainting\)")
Discover more
Stable Diffusion
ComfyUI
Wiki
Workflow
Text-to-image model
Image Generation
Stable diffusion
AI
FLUX
Interface
