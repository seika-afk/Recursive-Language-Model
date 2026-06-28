# export RLM_MODEL_BASE_URL=https://openrouter.ai/api/v1
# export RLM_MODEL_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxx


import fast_rlm
from fast_rlm import RLMConfig

config = RLMConfig(
    primary_agent="qwen/qwen3-32b",
)

result = fast_rlm.run(
    input_file="data.txt",
    instruction="Summarize this document.",
    config=config,
)

print(result["results"])
