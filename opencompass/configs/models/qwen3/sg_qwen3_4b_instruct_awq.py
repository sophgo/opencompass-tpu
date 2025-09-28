from opencompass.models import SophgoModel

models = [
    dict(
        type=SophgoModel,
        abbr='qwen3-4b-instruct-awq-sophgo',
        name='qwen',
        model_path='/data/romainzhou/LLM-TPU/models/Qwen3/qwen3-4b-awq_w4bf16_seq4096_bm1684x_1dev_20250917_104725.bmodel',
        sg_tokenizer_path='/data/romainzhou/LLM-TPU/models/Qwen3/config/',
        max_out_len=4096,
        batch_size=1,
        batch_padding=False,
        device="tpu",
        devid="8",
        generation_kwargs=dict(
            do_sample=False,
            enable_thinking=False
        ),
        run_cfg=dict(),
    )
]
