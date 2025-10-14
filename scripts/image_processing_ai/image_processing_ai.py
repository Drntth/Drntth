import base64
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

VISION_API_PROMPT = """
Elemezze a következő képet, és készítsen róla egy világos, tömör összefoglaló bekezdést magyar nyelven.

Elvárások:  
- **Pontos és teljes leírás:** Minden látható részletet pontosan és hiánytalanul rögzítsen, beleértve a tárgyakat, személyeket, helyszíneket, szöveges elemeket, dátumokat és számokat. Kerülje a részletek módosítását vagy kihagyását.
- **Következtetések nélkül:** Ne vonjon le általánosításokat, ne egészítse ki a tartalmat saját megállapításokkal, és ne készítsen statisztikai vagy értelmező elemzéseket.
- **Folyamatos szöveg:** Kerülje a felsorolásokat, táblázatos formázást és egyéb strukturált elemeket. A válasz legyen összefüggő, természetes szöveg, amely pontosan tükrözi a képen látható információkat.
- **Forrássemleges megfogalmazás:** Ne utaljon a kép formátumára, típusára vagy a dokumentum szerkezetére.
- **Egységes formázás:** Minden szöveges elem, dátum és szám pontosan úgy jelenjen meg, ahogy a képen látható, beleértve a zárójeles kiegészítéseket is.
"""


class FileService:
    """Fájlműveletekhez segédosztály.

    Statikus metódusokat tartalmaz képek base64 kódolásához.
    """

    @staticmethod
    def encode_image_base64(image_path: Path | str) -> str:
        """Képet base64-re kódol.

        Args:
            image_path (Path | str): A kép elérési útja.

        Returns:
            str: A base64-re kódolt kép szövege.
        """
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")


class OpenAIVisionClient:
    """OpenAI Vision API kliens.

    Az osztály képelemzéshez használható az OpenAI Vision API-n keresztül.
    """

    def __init__(self) -> None:
        """Inicializálja az OpenAI klienst a környezeti változóból olvasott API kulccsal."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY nem található a .env fájlban.")
        self.client = OpenAI(api_key=api_key)

    def call_openai_vision_api(
        self, image_model: str, base64_image: str, detail: str
    ) -> str:
        """Meghívja az OpenAI Vision API-t egy kép elemzésére.

        Args:
            image_model (str): Az OpenAI Vision modell neve.
            base64_image (str): A kép base64 kódolt formátuma.
            detail (str): A részletesség szintje az elemzéshez ("low", "high", "auto").

        Returns:
            str: Az OpenAI Vision API válasza.
        """
        max_attempts = 5
        for attempt in range(1, max_attempts + 1):
            try:
                completion = self.client.chat.completions.create(
                    model=image_model,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": VISION_API_PROMPT},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{base64_image}",
                                        "detail": detail,
                                    },
                                },
                            ],
                        }
                    ],
                )
                return completion.choices[0].message.content
            except Exception as e:
                error_str = str(e)
                if (
                    "429" in error_str or "rate_limit_exceeded" in error_str
                ) and attempt < max_attempts:
                    wait_time = 10
                    time.sleep(wait_time)
                    continue
                return f"[Hiba az OpenAI Vision API hívásakor: {e}]"

    def summarize_image(self, image_model: str, rel_image_path: str) -> str:
        """Kép szöveges leírásának generálása OpenAI Vision API segítségével.

        Args:
            image_model (str): Az OpenAI Vision modell neve.
            rel_image_path (str): A kép relatív elérési útja.

        Returns:
            str: A kép szöveges leírása.
        """
        abs_image_path = os.path.abspath(rel_image_path)
        base64_image = FileService.encode_image_base64(abs_image_path)
        return self.call_openai_vision_api(
            image_model=image_model, base64_image=base64_image, detail="low"
        )


class Main:
    """Főosztály képfeldolgozási műveletek indításához."""

    def __init__(self, image_model: str = "gpt-4o-mini") -> None:
        """Inicializálja a főosztályt és az OpenAI Vision klienst.

        Args:
            image_model (str): Az OpenAI Vision modell neve.
        """
        self.image_model = image_model
        self.vision_client = OpenAIVisionClient()

    def process_single_file(self, image_path: str) -> None:
        """Egyetlen kép feldolgozása és összefoglaló kiírása.

        Args:
            image_path (str): A kép elérési útja.
        """
        summary = self.vision_client.summarize_image(self.image_model, image_path)
        print("\n" + "=" * 60)
        print(f"Kép: {image_path}")
        print("-" * 60)
        print("Összefoglaló:\n")
        print(summary)
        print("=" * 60 + "\n")

    def process_folder(self, folder_path: str, prefix: str = "") -> None:
        """Egy mappában lévő összes kép feldolgozása, opcionális névkezdettel.

        Args:
            folder_path (str): A mappa elérési útja.
            prefix (str): Csak az ezzel kezdődő fájlokat dolgozza fel.
        """
        supported_ext = (".jpg", ".jpeg", ".png", ".webp", ".bmp")
        folder = Path(folder_path)
        for image_file in folder.iterdir():
            if (
                image_file.is_file()
                and image_file.suffix.lower() in supported_ext
                and image_file.name.startswith(prefix)
            ):
                self.process_single_file(str(image_file))


def main(mode: str, path: str, prefix: str = "") -> None:
    """Feldolgozási belépési pont. Egy fájlt vagy egy mappát dolgoz fel.

    Args:
        mode (str): 'file' egyetlen képhez, 'folder' mappa feldolgozásához.
        path (str): A kép vagy mappa elérési útja.
    """
    processor = Main()
    if mode == "file":
        processor.process_single_file(path)
    elif mode == "folder":
        processor.process_folder(path, prefix)
    else:
        print("Hibás mód! Csak 'file' vagy 'folder' érték engedélyezett.")


if __name__ == "__main__":
    # main("file", "tesztkep.jpg")
    # main("folder", "../assets/backend/nodejs")
    main("folder", "../assets/backend/nodejs", "client_request_handling")
