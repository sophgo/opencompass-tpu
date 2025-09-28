from opencompass.models import SophgoModel

models = [
    dict(
        type=SophgoModel,
        abbr='llama3-8b-awq-sophgo',
        name='llama',
        model_path='/data/romainzhou/LLM-TPU/models/Llama3/meta-llama-3-8b-instruct-awq_w4f16_seq1024_bm1684x_1dev_20250912_103720.bmodel',
        sg_tokenizer_path='/data/romainzhou/LLM-TPU/models/Llama3/config/',
        max_out_len=1024,
        batch_size=1,
        batch_padding=False,
        device="tpu",
        devid="3",
        run_cfg=dict(),
    )
]
