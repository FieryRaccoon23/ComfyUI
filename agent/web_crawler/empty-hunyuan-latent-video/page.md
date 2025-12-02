[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")videoEmpty Hunyuan Latent Video Node Tutorial
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Empty Hunyuan Latent Video
![Empty Hunyuan Latent Video](https://comfyui-wiki.com/_next/static/media/EmptyHunyuanLatentVideo.b9aa137a.jpg)
## Empty Hunyuan Latent Video Node Overview[](https://comfyui-wiki.com/en/comfyui-nodes/latent/video/empty-hunyuan-latent-video#empty-hunyuan-latent-video-node-overview)
The `EmptyHunyuanLatentVideo` node is similar to the [EmptyLatent Image](https://comfyui-wiki.com/en/comfyui-nodes/latent/empty-latent-image) node. You can think of it as providing a blank canvas for video generation, where the width, height and length define the canvas properties, and batch size determines how many canvases to create. This node creates fresh empty canvases ready for subsequent video generation tasks.
## Class Information[](https://comfyui-wiki.com/en/comfyui-nodes/latent/video/empty-hunyuan-latent-video#class-information)
  * **Class Name** : `EmptyHunyuanLatentVideo`
  * **Category** : `latent/video`
  * **Output Node** : `True`


## Empty Hunyuan Latent Video Input Types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/video/empty-hunyuan-latent-video#empty-hunyuan-latent-video-input-types)
Parameter | Comfy Type | Description  
---|---|---  
`width` | `INT` | Video width, default 848, minimum 16, maximum `nodes.MAX_RESOLUTION`, step size 16.  
`height` | `INT` | Video height, default 480, minimum 16, maximum `nodes.MAX_RESOLUTION`, step size 16.  
`length` | `INT` | Video length, default 25, minimum 1, maximum `nodes.MAX_RESOLUTION`, step size 4.  
`batch_size` | `INT` | Batch size, default 1, minimum 1, maximum 4096.  
## Empty Hunyuan Latent Video Output Types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/video/empty-hunyuan-latent-video#empty-hunyuan-latent-video-output-types)
Parameter | Comfy Type | Description  
---|---|---  
`samples` | `LATENT` | Generated latent video samples containing zero tensors, ready for processing and generation tasks.  
## Empty Hunyuan Latent Video Workflow Example[](https://comfyui-wiki.com/en/comfyui-nodes/latent/video/empty-hunyuan-latent-video#empty-hunyuan-latent-video-workflow-example)
[Tencent Hunyuan Video Model Workflow](https://comfyui-wiki.com/en/tutorial/advanced/hunyuan-text-to-video-workflow-guide-and-example)
## Related Resources[](https://comfyui-wiki.com/en/comfyui-nodes/latent/video/empty-hunyuan-latent-video#related-resources)
Here are some relevant resources curated by [ComfyUI Wiki](https://comfyui-wiki.com/):
## Empty Hunyuan Latent Video Node Source Code[](https://comfyui-wiki.com/en/comfyui-nodes/latent/video/empty-hunyuan-latent-video#empty-hunyuan-latent-video-node-source-code)
  * ComfyUI Version: v0.3.10
  * 2025-01-07


```
class EmptyHunyuanLatentVideo:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "width": ("INT", {"default": 848, "min": 16, "max": nodes.MAX_RESOLUTION, "step": 16}),
                              "height": ("INT", {"default": 480, "min": 16, "max": nodes.MAX_RESOLUTION, "step": 16}),
                              "length": ("INT", {"default": 25, "min": 1, "max": nodes.MAX_RESOLUTION, "step": 4}),
                              "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096})}}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "generate"
    CATEGORY = "latent/video"
    def generate(self, width, height, length, batch_size=1):
        latent = torch.zeros([batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8], device=comfy.model_management.intermediate_device())
        return ({"samples":latent}, )

```

Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/transform/latent-rotate "Rotate Latent")[Checkpoint Loader (Simple)](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Checkpoint Loader \(Simple\)")
Discover more
video
Wiki
Node.js
Stable diffusion
Node
ComfyUI
Stable Diffusion
Workflow
Video
Artificial intelligence
