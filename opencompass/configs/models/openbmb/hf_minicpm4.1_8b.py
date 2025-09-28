from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='MiniCPM4.1-8B-awq-hf',
        path='/home/romainzhou/MiniCPM4.1-8B-AutoAWQ',
        max_out_len=4096,
        batch_size=1,
        run_cfg=dict(num_gpus=1),
        generation_kwargs=dict(
            do_sample=False,
            enable_thinking=False
        ),
        model_kwargs=dict(
            torch_dtype='torch.bfloat16',
        ),
    )
]
