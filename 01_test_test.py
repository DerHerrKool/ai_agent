response = client.models.generate_content(...)
usage = response.usage_metadata
prompt_tokens = usage.prompt_token_count
response_tokens = usage.candidates_token_count

if args.verbose:
    print(f"User prompt: {user_prompt}")

print_response(response, prompt_tokens, response_tokens, args.verbose)

def print_response(response, prompt_tokens, response_tokens, verbose: bool):
    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    print(response.text)