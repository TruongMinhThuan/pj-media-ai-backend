from typing import List, Optional
from pydantic import BaseModel, Field


class StableDiffusionBaseSchema(BaseModel):
    """Base schema for the stable diffusion configuration."""

    prompt: str = ""
    negative_prompt: str = "Negative Prompt"
    styles: list[str] = []
    seed: int = -1
    subseed: int = 0
    subseed_strength: int = 0
    seed_resize_from_h: int = 0
    seed_resize_from_w: int = 0
    sampler_name: str = "DPM++ 2M Karras"
    batch_size: int = 1
    steps: int = 24
    cfg_scale: int = 0
    width: int = 512
    height: int = 512
    restore_faces: bool = False
    tiling: bool = False
    denoising_strength: int = 0
    override_settings: dict = {}
    override_settings_restore_afterwards: bool = False
    disable_extra_networks: bool = False
    enable_hr: bool = False
    hr_scale: int = 0
    hr_upscaler: str = ""
    hr_second_pass_steps: int = 0
    hr_resize_x: int = 0
    hr_resize_y: int = 0
    hr_checkpoint_name: str = ""
    hr_sampler_name: str = ""
    hr_prompt: str = ""
    hr_negative_prompt: str = ""
    sampler_index: str = ""
    script_name: str = ""
    script_args: list = []
    alwayson_scripts: dict = {}


class StableDiffusionTxt2ImgSchema(StableDiffusionBaseSchema):
    """Schema for the txt2img endpoint."""

    prompt: str = "Txt2Img Prompt"
    negative_prompt: str = "Negative Prompt"


class StableDiffusionImg2ImgSchema(StableDiffusionBaseSchema):
    """Schema for the img2img endpoint."""

    prompt: str = "Img2Img Prompt"
    init_images: list[str] = ["Init base64 Image"]


class StableDiffusionResponseSchema(BaseModel):
    """Schema for the stable diffusion response."""

    images: list[str] = Field(default=None, title="Image",
                              description="The generated image in base64 format.")
    parameters: dict
    info: str
