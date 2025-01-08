def create_permutation_key(phrase):
    """
    Створює ключ перестановки на основі фрази.
    """
    phrase = phrase.upper()
    sorted_indices = sorted(range(len(phrase)), key=lambda i: phrase[i])
    return sorted_indices


def apply_permutation(text, key):
    """
    Застосовує перестановку тексту на основі ключа.
    """
    return "".join(text[k] for k in key)


def apply_reverse_permutation(text, key):
    """
    Застосовує зворотну перестановку тексту на основі ключа.
    """
    reverse_key = [key.index(i) for i in range(len(key))]
    return "".join(text[k] for k in reverse_key)


def transpose_text(text, columns):
    """
    Перетворює текст у блоки за кількістю колонок.
    """
    rows = (len(text) + columns - 1) // columns
    padded_text = text.ljust(rows * columns, "X")
    return [padded_text[i:i + columns] for i in range(0, len(padded_text), columns)]


def double_transposition_encrypt(text, key1, key2):
    """
    Виконує шифрування подвійною перестановкою.
    """
    key1 = create_permutation_key(key1)
    key2 = create_permutation_key(key2)
    
    # Видаляємо пробіли та переводимо в верхній регістр
    text = text.replace(" ", "").upper()
    
    # 1. Перша перестановка
    blocks = transpose_text(text, len(key1))
    stage1 = "".join(apply_permutation(block, key1) for block in blocks)
    
    # 2. Друга перестановка
    blocks = transpose_text(stage1, len(key2))
    encrypted_text = "".join(apply_permutation(block, key2) for block in blocks)
    
    return encrypted_text


def double_transposition_decrypt(text, key1, key2):
    """
    Виконує дешифрування подвійною перестановкою.
    """
    key1 = create_permutation_key(key1)
    key2 = create_permutation_key(key2)
    
    # 1. Зворотна друга перестановка
    blocks = transpose_text(text, len(key2))
    stage1 = "".join(apply_reverse_permutation(block, key2) for block in blocks)
    
    # 2. Зворотна перша перестановка
    blocks = transpose_text(stage1, len(key1))
    decrypted_text = "".join(apply_reverse_permutation(block, key1) for block in blocks)
    
    return decrypted_text.rstrip("X")  # Видаляємо доповнюючі символи


# Текст для шифрування
text_to_encrypt = """
The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless.
"""

# Ключі для шифрування
key1 = "SECRET"
key2 = "CRYPTO"

# Шифрування тексту
encrypted_text = double_transposition_encrypt(text_to_encrypt, key1, key2)
print("Encrypted text:")
print(encrypted_text)

# Дешифрування тексту
decrypted_text = double_transposition_decrypt(encrypted_text, key1, key2)
print("\nDecrypted text:")
print(decrypted_text)
