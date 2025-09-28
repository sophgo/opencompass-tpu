from opencompass.models import SophgoModel

models = [
    dict(
        type=SophgoModel,
        abbr='minicpm4.1-8b-awq-sophgo',
        name='minicpm',
        model_path='/data/romainzhou/LLM-TPU/models/MiniCPM4/minicpm4.1-8b-autoawq_w4bf16_seq2048_bm1684x_1dev_20250926_154421.bmodel',
        sg_tokenizer_path='/data/romainzhou/LLM-TPU/models/MiniCPM4/config_8b/',
        max_out_len=2048,
        batch_size=1,
        batch_padding=False,
        device="tpu",
        devid="3",
        generation_kwargs=dict(
            do_sample=False,
            enable_thinking=False
        ),
        run_cfg=dict(),
    )
]
