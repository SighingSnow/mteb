from __future__ import annotations

from mteb.model_meta import ModelMeta

qodo_languages = [
    "python-Code",
    "c++-Code",
    "c#-Code",
    "go-Code",
    "java-Code",
    "javascript-Code",
    "php-Code",
    "ruby-Code",
    "typescript-Code",
]


Qodo_Embed_1_1_5B = ModelMeta(
    name="Qodo/Qodo-Embed-1-1.5B",
    languages=qodo_languages,
    open_weights=True,
    revision="84bbef079b32e8823ec226d4e9e92902706b0eb6",
    release_date="2025-02-19",
    n_parameters=1_780_000_000,
    memory_usage_mb=6776,
    embed_dim=1536,
    license="https://huggingface.co/Qodo/Qodo-Embed-1-1.5B/blob/main/LICENSE",
    max_tokens=32768,
    reference="https://huggingface.co/Qodo/Qodo-Embed-1-1.5B",
    similarity_fn_name="cosine",
    framework=["Sentence Transformers", "PyTorch"],
    use_instructions=False,
    public_training_code=None,
    public_training_data=None,
    training_datasets=None,
    adapted_from="Alibaba-NLP/gte-Qwen2-1.5B-instruct",
)

Qodo_Embed_1_7B = ModelMeta(
    name="Qodo/Qodo-Embed-1-7B",
    languages=qodo_languages,
    open_weights=True,
    revision="f9edd9bf7f687c0e832424058e265120f603cd81",
    release_date="2025-02-24",
    n_parameters=7_613_000_000,
    memory_usage_mb=29040,
    embed_dim=3584,
    license="https://huggingface.co/Qodo/Qodo-Embed-1-1.5B/blob/main/LICENSE",
    max_tokens=32768,
    reference="https://huggingface.co/Qodo/Qodo-Embed-1-7B",
    similarity_fn_name="cosine",
    framework=["Sentence Transformers", "PyTorch"],
    use_instructions=False,
    public_training_code=None,
    public_training_data=None,
    training_datasets=None,
    adapted_from="Alibaba-NLP/gte-Qwen2-7B-instruct",
)
