# Copyright (c) 2025 NVIDIA CORPORATION. 
#   Licensed under the MIT license.
# modified from stable-audio-tools under the MIT license

from setuptools import setup, find_packages

setup(
    name='etta',
    version='0.0.1',
    url='https://github.com/NVIDIA/elucidated-text-to-audio',
    author='NVIDIA',
    description='Training and inference code for ETTA, built on top of stable-audio-tools from Stability AI',
    packages=find_packages(),  
    install_requires=[
        'alias-free-torch>=0.0.6',
        'auraloss>=0.4.0',
        'descript-audio-codec>=1.0.0',
        'diffusers',
        'einops>=0.7.0',
        'einops-exts>=0.0.4',
        'ema-pytorch>=0.2.3',
        'encodec>=0.1.1',
        'gradio>=3.42.0',
        'huggingface_hub',
        'importlib-resources>=5.12.0',
        'k-diffusion>=0.1.1',
        'laion-clap>=1.1.4',
        'local-attention>=1.8.6',
        'notebook',
        'pandas>=2.0.2',
        'pedalboard>=0.7.4',
        'prefigure>=0.0.9',
        'pytorch_lightning>=2.1.0', 
        'PyWavelets>=1.4.1',
        'safetensors',
        'sentencepiece>=0.1.99',
        'soundfile',
        's3fs',
        'torchmetrics>=0.11.4',
        'tqdm',
        'transformers',
        'v-diffusion-pytorch>=0.0.2',
        'vector-quantize-pytorch>=1.9.14',
        'wandb>=0.15.4',
        'webdataset>=0.2.48',
        'x-transformers>=1.27.0',
        'deepspeed'
    ],
)