[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Advanced[conditioning](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl "conditioning")CLIP Text Encode Hunyuan DiT
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# CLIP Text Encode Hunyuan DiT
![CLIP Text Encode Hunyuan DiT](https://comfyui-wiki.com/_next/static/media/CLIPTextEncodeHunyuanDiT.fd723620.jpg)
## Overview of CLIP Text Encode Hunyuan DiT ComfyUI Node[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#overview-of-clip-text-encode-hunyuan-dit-comfyui-node)
The main functions of the `CLIPTextEncodeHunyuanDiT` node are:
  * **Tokenization** : Converting input text into token sequences that can be processed by the model.
  * **Encoding** : Using the CLIP model to encode token sequences into conditional encodings.


This node can be viewed as a “language translator” that converts user input text (whether English or other languages) into “machine language” that AI models can understand, enabling the model to generate corresponding content based on these conditions.
## Class Name[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#class-name)
  * **Class Name** : `CLIPTextEncodeHunyuanDiT`
  * **Category** : `advanced/conditioning`
  * **Output Node** : `False`


## CLIP Text Encode Hunyuan DiT Input Types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#clip-text-encode-hunyuan-dit-input-types)
Parameter | Comfy Data Type | Description  
---|---|---  
`clip` | `CLIP` | A CLIP model instance for text tokenization and encoding, core to generating conditions.  
`bert` | `STRING` | Text input for encoding, supports multiline and dynamic prompts.  
`mt5xl` | `STRING` | Another text input for encoding, supports multiline and dynamic prompts (multilingual).  
  * **`bert`parameter** : Suitable for English text input. It’s recommended to input concise text with context to help the node generate more accurate and meaningful token representations.
  * **`mt5xl`parameter** : Suitable for multilingual text input. You can input text in any language to help the model understand multilingual tasks.


## CLIP Text Encode Hunyuan DiT Output Types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#clip-text-encode-hunyuan-dit-output-types)
Parameter | Comfy Data Type | Description  
---|---|---  
`conditioning` | `CONDITIONING` | Encoded conditional output for further processing in generation tasks.  
## Methods[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#methods)
  * **Encoding Method** : `encode`
This method accepts `clip`, `bert`, and `mt5xl` as parameters. First, it tokenizes `bert`, then tokenizes `mt5xl`, and stores the results in a `tokens` dictionary. Finally, it uses the `clip.encode_from_tokens_scheduled` method to encode the tokenized tokens into conditions.


## Usage Examples[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#usage-examples)
  * To be updated


## Extended Content for CLIP Text Encode Hunyuan DiT Node[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#extended-content-for-clip-text-encode-hunyuan-dit-node)
### BERT (Bidirectional Encoder Representations from Transformers)[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#bert-bidirectional-encoder-representations-from-transformers)
BERT is a bidirectional language representation model based on the Transformer architecture.
It learns rich contextual information through pre-training on large amounts of text data, then fine-tunes on downstream tasks to achieve high performance.
**Key Features:**
  * **Bidirectionality** : BERT considers both left and right context information simultaneously, enabling better understanding of word meanings.
  * **Pre-training and Fine-tuning** : Through pre-training tasks (like Masked Language Model and Next Sentence Prediction), BERT can be quickly fine-tuned for various downstream tasks.


**Application Scenarios:**
  * Text Classification
  * Named Entity Recognition
  * Question Answering Systems


### mT5-XL (Multilingual Text-to-Text Transfer Transformer)[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#mt5-xl-multilingual-text-to-text-transfer-transformer)
mT5-XL is the multilingual version of the T5 model, using an encoder-decoder architecture that supports processing multiple languages.
It unifies all NLP tasks as text-to-text transformations, capable of handling various tasks including translation, summarization, and question answering.
**Key Features:**
  * **Multilingual Support** : mT5-XL supports processing of up to 101 languages.
  * **Unified Task Representation** : Converting all tasks into text-to-text format, simplifying the task processing pipeline.


**Application Scenarios:**
  * Machine Translation
  * Text Summarization
  * Question Answering Systems


### BERT and mT5-XL Research Papers[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#bert-and-mt5-xl-research-papers)
  1.      * **Description** : This foundational paper introduces BERT, a transformer-based model that achieves state-of-the-art results on a wide array of NLP tasks.
  2.      * **Description** : This paper presents mT5, a multilingual variant of T5, trained on a new Common Crawl-based dataset covering 101 languages.
  3.      * **Description** : This work develops mLongT5, a multilingual model designed to handle longer input sequences efficiently.
  4.      * **Description** : An article discussing the capabilities and applications of Google’s mT5 model in multilingual NLP tasks.
  5.      * **Description** : A curated list of research papers related to BERT, including surveys, downstream tasks, and modifications.


## Source Code[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit#source-code)
  * ComfyUI version: v0.3.10
  * 2025-01-07


```
class CLIPTextEncodeHunyuanDiT:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "clip": ("CLIP", ),
            "bert": ("STRING", {"multiline": True, "dynamicPrompts": True}),
            "mt5xl": ("STRING", {"multiline": True, "dynamicPrompts": True}),
            }}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"
    CATEGORY = "advanced/conditioning"
    def encode(self, clip, bert, mt5xl):
        tokens = clip.tokenize(bert)
        tokens["mt5xl"] = clip.tokenize(mt5xl)["mt5xl"]
        return (clip.encode_from_tokens_scheduled(tokens), )
```

Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl-refiner "CLIP Text Encode SDXL Refiner")[Conditioning Set Timestep Range](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/conditioning-settimestep-range "Conditioning Set Timestep Range")
Discover more
User interface
ComfyUI
Stable diffusion
user interface
stable diffusion
SDXL
Flux
Artificial intelligence
interface
Sdxl
