

<h1 align="center">CL-CODE</h1>
<!-- 
<p align="center">
  <a href="https://img.shields.io/badge/Made%20with-Python-1f425f.svg">
    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Badge: Made with Python"/>
  </a>
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
</p>
-->

This is the code for the paper.

Authors: Seungah Son


## Description

This research explores

## Used model:

We use two models based on Llama 2-7B, with target strucutred pruning to 1.3B and 2.7B, and pre-trained with dynamic batch loading.
https://arxiv.org/pdf/2310.06694

1) princeton-nlp/Sheared-LLaMA-1.3B - `princeton-nlp`
2) princeton-nlp/Sheared-LLaMA-2.7B - `princeton-nlp`

These models are downloaded with [a_download_model.ipynb](utils/a_download_model.ipynb) and weights are saved in [model/sheared_llama_1.3B](model/sheared_llama_1.3B) and [model/sheared_llama_2.7B](model/sheared_llama_2.7B) respectively.

## Datasets

We use two different datasets:
1) Yelp Review Dataset: https://github.com/shentianxiao/language-style-transfer - `yelp`
2) GoEmotion Dataset: https://huggingface.co/datasets/go_emotions - `GoEmo`

These models are downloaded with [a_download_dataset.ipynb](utils/a_download_dataset.ipynb)

**Yelp**: We removed duplicates from the dataset, because we wanted steering vectors for as many as possible different target sentences.

**GoEmotion**: Only 5,000 samples were used that could be unambiguously mapped to the six established basic emotional categories proposed by Ekman.
