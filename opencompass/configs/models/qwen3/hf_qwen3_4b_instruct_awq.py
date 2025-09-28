from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='qwen3-4b-instruct-hf-awq',
        path='/home/romainzhou/Qwen3-4B-AWQ',
        max_out_len=4096,
        batch_size=8,
        generation_kwargs=dict(
            do_sample=False,
            enable_thinking=False
        ),
        run_cfg=dict(num_gpus=1),
    )
]

