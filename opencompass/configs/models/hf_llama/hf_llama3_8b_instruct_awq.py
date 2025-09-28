from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='llama-3-8b-instruct-awq-hf',
        path='/home/romainzhou/Meta-Llama-3-8B-Instruct-AWQ',
        max_out_len=4096,
        batch_size=8,
        run_cfg=dict(num_gpus=1),
        stop_words=['<|end_of_text|>', '<|eot_id|>'],
        generation_kwargs=dict(
            do_sample=False,
        ),
    )
]
