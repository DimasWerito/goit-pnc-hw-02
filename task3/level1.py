def create_column_key(phrase):
    """
    Створює ключ для перестановки колонок на основі фрази-ключа.
    """
    phrase = phrase.upper()
    sorted_indices = sorted(range(len(phrase)), key=lambda i: phrase[i])
    return sorted_indices


def create_table(text, columns):
    """
    Розбиває текст на таблицю з фіксованою кількістю колонок.
    """
    rows = (len(text) + columns - 1) // columns
    padded_text = text.ljust(rows * columns, "X")  # Додаємо X до кінця для вирівнювання
    table = [padded_text[i:i + columns] for i in range(0, len(padded_text), columns)]
    return table


def apply_column_permutation(table, key):
    """
    Застосовує перестановку колонок таблиці на основі ключа.
    """
    return ["".join(row[k] for k in key) for row in table]


def apply_reverse_column_permutation(table, key):
    """
    Застосовує зворотну перестановку колонок таблиці.
    """
    reverse_key = [key.index(i) for i in range(len(key))]
    return ["".join(row[k] for k in reverse_key) for row in table]


def tabular_encrypt(text, phrase):
    """
    Виконує шифрування тексту табличним шифром.
    """
    key = create_column_key(phrase)
    columns = len(key)
    text = text.replace(" ", "").upper()  # Видаляємо пробіли та переводимо в верхній регістр
    
    # Розбиваємо текст на таблицю
    table = create_table(text, columns)
    encrypted_table = apply_column_permutation(table, key)
    
    return "".join(encrypted_table)  # Об'єднуємо рядки таблиці в один текст


def tabular_decrypt(text, phrase):
    """
    Виконує дешифрування тексту табличним шифром.
    """
    key = create_column_key(phrase)
    columns = len(key)
    rows = len(text) // columns  # Визначаємо кількість рядків у таблиці
    
    # Розбиваємо текст на таблицю
    table = [text[i:i + columns] for i in range(0, len(text), columns)]
    decrypted_table = apply_reverse_column_permutation(table, key)
    
    return "".join(decrypted_table).rstrip("X")  # Видаляємо доповнюючі символи "X"


# Текст для шифрування
text_to_encrypt = """
The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless.
"""

# Ключ для шифрування
phrase = "MATRIX"

# Шифрування тексту
encrypted_text = tabular_encrypt(text_to_encrypt, phrase)
print("Encrypted text:")
print(encrypted_text)

# Дешифрування тексту
decrypted_text = tabular_decrypt(encrypted_text, phrase)
print("\nDecrypted text:")
print(decrypted_text)
