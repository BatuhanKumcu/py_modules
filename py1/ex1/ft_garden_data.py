class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}:, {self.height}cm, {self.age} days old")

def objects() -> None:
    rose = Plant("Rose", 42, 5)
    cactus = Plant("Cactus", 23, 2)
    sunflower = Plant("Sunflower", 14, 19)
    rose.show()
    cactus.show()
    sunflower.show()

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    objects()
