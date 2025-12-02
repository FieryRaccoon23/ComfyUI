[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling "Sampling")KSampler
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# KSampler | ComfyUI Component Node
![ComfyUI Node - KSampler | ComfyUI Component Node](https://comfyui-wiki.com/_next/static/media/ksampler.92895e69.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler#documentation)
  * Class Name: `KSampler`
  * Category: `Sampling`
  * Output Node: `No` The KSampler works like this: it modifies the provided original latent image information based on a specific model and both positive and negative conditions. First, it adds noise to the original image data according to the set **seed** and **denoise strength** , then inputs the preset **Model** combined with **positive** and **negative** guidance conditions to generate the image.


## Input Parameters[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler#input-parameters)
Parameter Name | Data Type | Required | Default | Range/Options | Description  
---|---|---|---|---|---  
Model | checkpoint | Yes | None | - | Input model used for the denoising process  
seed | Int | Yes | 0 | 0 ~ 18446744073709551615 | Used to generate random noise, using the same “seed” generates identical images  
steps | Int | Yes | 20 | 1 ~ 10000 | Number of steps to use in denoising process, more steps mean more accurate results  
cfg | float | Yes | 8.0 | 0.0 ~ 100.0 | Controls how closely the generated image matches input conditions, 6-8 recommended  
sampler_name | UI Option | Yes | None | Multiple algorithms | Choose sampler for denoising, affects generation speed and style  
scheduler | UI Option | Yes | None | Multiple schedulers | Controls how noise is removed, affects generation process  
Positive | conditioning | Yes | None | - | Positive conditions guiding denoising, what you want to appear in the image  
Negative | conditioning | Yes | None | - | Negative conditions guiding denoising, what you don’t want in the image  
Latent_Image | Latent | Yes | None | - | Latent image used for denoising  
denoise | float | No | 1.0 | 0.0 ~ 1.0 | Determines noise removal ratio, lower values mean less connection to input image  
control_after_generate | UI Option | No | None | Random/Inc/Dec/Keep | Provides ability to change seed after each prompt  
## Output[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler#output)
Parameter Name | Function  
---|---  
Latent | Outputs the latent after sampler denoising  
## Source Code[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler#source-code)
[Updated on May 15, 2025]
```
def common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent, denoise=1.0, disable_noise=False, start_step=None, last_step=None, force_full_denoise=False):
    latent_image = latent["samples"]
    latent_image = comfy.sample.fix_empty_latent_channels(model, latent_image)
    if disable_noise:
        noise = torch.zeros(latent_image.size(), dtype=latent_image.dtype, layout=latent_image.layout, device="cpu")
    else:
        batch_inds = latent["batch_index"] if "batch_index" in latent else None
        noise = comfy.sample.prepare_noise(latent_image, seed, batch_inds)
    noise_mask = None
    if "noise_mask" in latent:
        noise_mask = latent["noise_mask"]
    callback = latent_preview.prepare_callback(model, steps)
    disable_pbar = not comfy.utils.PROGRESS_BAR_ENABLED
    samples = comfy.sample.sample(model, noise, steps, cfg, sampler_name, scheduler, positive, negative, latent_image,
                                  denoise=denoise, disable_noise=disable_noise, start_step=start_step, last_step=last_step,
                                  force_full_denoise=force_full_denoise, noise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=seed)
    out = latent.copy()
    out["samples"] = samples
    return (out, )
class KSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL", {"tooltip": "The model used for denoising the input latent."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True, "tooltip": "The random seed used for creating the noise."}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000, "tooltip": "The number of steps used in the denoising process."}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0, "step":0.1, "round": 0.01, "tooltip": "The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality."}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"tooltip": "The algorithm used when sampling, this can affect the quality, speed, and style of the generated output."}),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {"tooltip": "The scheduler controls how noise is gradually removed to form the image."}),
                "positive": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to include in the image."}),
                "negative": ("CONDITIONING", {"tooltip": "The conditioning describing the attributes you want to exclude from the image."}),
                "latent_image": ("LATENT", {"tooltip": "The latent image to denoise."}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "The amount of denoising applied, lower values will maintain the structure of the initial image allowing for image to image sampling."}),
            }
        }
    RETURN_TYPES = ("LATENT",)
    OUTPUT_TOOLTIPS = ("The denoised latent.",)
    FUNCTION = "sample"
    CATEGORY = "sampling"
    DESCRIPTION = "Uses the provided model, positive and negative conditioning to denoise the latent image."
    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

```

Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling/sigmas/split-sigmas "Split Sigmas")[KSampler (Advanced)](https://comfyui-wiki.com/en/comfyui-nodes/sampling/k-sampler-advanced "KSampler \(Advanced\)")
Discover more
Stable Diffusion
Stable diffusion
ComfyUI
Workflow
Wiki
AI
User interface
Flux
interface
user interface
