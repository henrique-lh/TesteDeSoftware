class Bola:

    def __init__(self, color: str) -> None:
        self.color = color

    def get(self) -> str:
        return self.color
    
    def set(self, new_color: str) -> None:
        self.color = new_color
