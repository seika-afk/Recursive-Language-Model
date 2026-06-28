import fast_rlm
from fast_rlm import RLMConfig

config = RLMConfig(
    primary_agent="qwen2.5:0.5b",
)

while True:
    q = input("> ")

    if q == "exit":
        break

    result = fast_rlm.run(
        input_file="data.txt",
        instruction=q,
        config=config,
    )

    print(result["results"])
