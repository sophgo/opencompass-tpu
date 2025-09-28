from opencompass.models import SophgoModel

models = [
    dict(
        type=SophgoModel,
        abbr='minicpm4-0.5b-gptq-sophgo',
        name='minicpm',
        model_path='/data/romainzhou/LLM-TPU/models/MiniCPM4/minicpm4-0.5b-qat-int4-gptq-format_w4bf16_seq4096_bm1684x_1dev_20250911_193715.bmodel',
        sg_tokenizer_path='/data/romainzhou/LLM-TPU/models/MiniCPM4/config/',
        max_out_len=4096,
        batch_size=1,
        batch_padding=False,
        device="tpu",
        devid="2",
        run_cfg=dict(),
    )
]
