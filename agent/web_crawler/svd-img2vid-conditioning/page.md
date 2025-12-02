[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")video-modelsSVD img2vid Conditioning
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# SVD img2vid Conditioning
![comfyUI节点-SVD_img2vid_Conditioning|SVD_图像到视频_条件](https://comfyui-wiki.com/conditioning/video_models/SVD_img2vid_Conditioning.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/video-models/svd-img2vid-conditioning#documentation)
  * Class name: `SVD_img2vid_Conditioning`
  * Category: `conditioning/video_models`
  * Output node: `False`


This node is designed for generating conditioning data for video generation tasks, specifically tailored for use with SVD_img2vid models. It takes various inputs including initial images, video parameters, and a VAE model to produce conditioning data that can be used to guide the generation of video frames.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/video-models/svd-img2vid-conditioning#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip_vision` | `CLIP_VISION` | Represents the CLIP vision model used for encoding visual features from the initial image, playing a crucial role in understanding the content and context of the image for video generation.  
`init_image` | `IMAGE` | The initial image from which the video will be generated, serving as the starting point for the video generation process.  
`vae` | `VAE` | A Variational Autoencoder (VAE) model used for encoding the initial image into a latent space, facilitating the generation of coherent and continuous video frames.  
`width` | `INT` | The desired width of the video frames to be generated, allowing for customization of the video’s resolution.  
`height` | `INT` | The desired height of the video frames, enabling control over the video’s aspect ratio and resolution.  
`video_frames` | `INT` | Specifies the number of frames to be generated for the video, determining the video’s length.  
`motion_bucket_id` | `INT` | An identifier for categorizing the type of motion to be applied in the video generation, aiding in the creation of dynamic and engaging videos.  
`fps` | `INT` | The frames per second (fps) rate for the video, influencing the smoothness and realism of the generated video.  
`augmentation_level` | `FLOAT` | A parameter controlling the level of augmentation applied to the initial image, affecting the diversity and variability of the generated video frames.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/video-models/svd-img2vid-conditioning#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`positive` | `CONDITIONING` | The positive conditioning data, consisting of encoded features and parameters for guiding the video generation process in a desired direction.  
`negative` | `CONDITIONING` | The negative conditioning data, providing a contrast to the positive conditioning, which can be used to avoid certain patterns or features in the generated video.  
`latent` | `LATENT` | Latent representations generated for each frame of the video, serving as a foundational component for the video generation process.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/upscale-diffusion/sd-4xupscale-conditioning "SD_4X Upscale Conditioning")[WanFunControlToVideo](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/video-models/wan-fun-control-to-video "WanFunControlToVideo")
Discover more
ComfyUI
videos
Stable diffusion
Wiki
Stable Diffusion
video
Video
video’s
Workflow
FLUX
