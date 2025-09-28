from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='qwen3-0.6b-instruct-hf',
        path='/home/romainzhou/Qwen3-0.6B',
        max_out_len=4096,
        batch_size=1,
        generation_kwargs=dict(
            do_sample=False,
            enable_thinking=False
        ),
        run_cfg=dict(num_gpus=1),
    )
]

