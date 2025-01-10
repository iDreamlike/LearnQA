class TestLength:
    def test_length_phrase(self):
        phrase_length = len(input("Введите фразу: "))

        assert phrase_length<15, f"Фраза не короче 15 символов. Длина: '{phrase_length}'"