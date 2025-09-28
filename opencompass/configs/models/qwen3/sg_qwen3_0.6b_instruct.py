from opencompass.models import SophgoModel

models = [
    dict(
        type=SophgoModel,
        abbr='qwen3-0.6b-instruct-sophgo',
        name='qwen',
        model_path='/data/romainzhou/LLM-TPU/models/Qwen3/qwen3-0.6b_bf16_seq4096_bm1684x_1dev_20250917_171204.bmodel',
        sg_tokenizer_path='/data/romainzhou/LLM-TPU/models/Qwen3/config_0.6b/',
        max_out_len=4096,
        batch_size=16,
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
