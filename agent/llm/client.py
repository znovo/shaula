from openai import OpenAI

class LlmClient:
    def __init__(self):
        self.base_url = "https://api.openai.com/v1"
        self.api_key = "key"
        self.model = "gpt-4"
        self._init_client()
    def _init_client(self):
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url, model=self.model)
    def swap_model(self, new_model):
        self.model = new_model
    def swap_base_url(self, new_url):
        self.base_url = new_url
    def swap_api_key(self, new_key):
        self.api_key = new_key


    def call_llm(self, prompt, temperature=0.7, user="user"):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=temperature,
                user=user,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": prompt + "\n\nResponda obrigatoriamente em JSON válido, sem markdown, sem explicações extras e sem texto fora do JSON."},
                    {"role": "user", "content": user}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao chamar a LLM: {str(e)}"