from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='MiniCPM4-0.5B-hf',
        path='/home/romainzhou/MiniCPM4-0.5B-QAT-Int4-GPTQ-format',
        max_out_len=4096,
        batch_size=8,
        run_cfg=dict(num_gpus=1),
        generation_kwargs=dict(
            do_sample=False,
        ),
    )
]
