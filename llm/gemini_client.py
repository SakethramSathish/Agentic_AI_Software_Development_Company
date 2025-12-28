from typing import Optional
import google.generativeai as genai

from config.settings import (
    GEMINI_API_KEY,
    GEMINI_FAST_MODEL,
    GEMINI_PRO_MODEL,
    DEBUG_MODE,
)

class GeminiClient:
    """
    Centralized Gemini client used by ALL agents.

    This ensures:
    - Consistent configuration
    - Easy model switching
    - Safe error handling
    """

    def __init__(self, model_type: str = "fast"):
        """
        Args:
            model_type: "fast" | "pro"
        """
        genai.configure(api_key=GEMINI_API_KEY)

        if model_type == "pro":
            self.model_name = GEMINI_PRO_MODEL
        elif model_type == "fast":
            self.model_name = GEMINI_FAST_MODEL

        self.model = genai.GenerativeModel(self.model_name)

        if DEBUG_MODE:
            print(f"[GeminiClient] Initialized with model: {self.model_name}")

        
    def generate(
            self,
            prompt: str,
            system_instruction: Optional[str] = None,
            temperature: float = 0.3,
    ) -> str:
        """
        Generate text using Gemini.

        Args:
            prompt: Main content prompt
            system_instruction: Optional system role / instruction
            temperature: Controls randomness

        Returns:
            Generated text as string
        """

        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt must be a non-empty string.")
        
        try:
            if system_instruction:
                final_prompt = f"{system_instruction.strip()}\n\n{prompt.strip()}"
            else:
                final_prompt = prompt.strip()

            response = self.model.generate_content(
                final_prompt,
                generation_config={"temperature": temperature}
            )

            if not response or not response.text:
                raise RuntimeError("Empty response from Gemini.")
            
            return response.text.strip()
        
        except Exception as e:
            raise RuntimeError(
                f"Gemini generation failed using model {self.model_name}: {str(e)}"
            )