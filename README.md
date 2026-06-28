RLMS are inference technique
-Model interacts with long prompts through extr. env.
-LLM can write Code to programmatically explore and create new transformation of prompt
- can recursively invoke sub-agents to complete smaller subtasks, (can call separate llms to work on diff region of work)
- subagent responses do not get automatically loaded into parent agent's context .but returns as variable in external env.
- RLM Agent can return response
  -  Auto regressively generated answers
  - construct answers into a python var
