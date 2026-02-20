import pytest

# 1 facciamo la classe da testare
class DataProcessor:
    def __init__(self, db_connection):
        self.db = db_connection

    def process_data(self, user_id):
        data = self.db.get_data(user_id)
        if not data:
            raise ValueError("Nessun dato trovato per l'utente")

        return {
            "status": "success",
            "items": [item.upper() for item in data]
        }

# 2 preparazione dell'ambiente per le fixtures
# 2.1 andiamo a creare una "finta" istanza del database
class MockDatabase:
    def get_data(self, user_id):
        if user_id == 1:
            return ["item_a", "item_b", "item_c"]
        return []

# 2.2 facciamo le nostre fixtures <- rappresentano le condizioni iniziali per
# il nostro test
@pytest.fixture
def mock_db():
    """Fixture che fornisce un db finto"""
    db = MockDatabase()
    yield db    # cediamo il controllo del DB al test, passando l'oggetto DB

    # qua di solito mettiamo le fasi finali, es: chiusura connessioni,
    # chiusura file, ...

@pytest.fixture
def processor(mock_db):
    """La fixture che istanza il DataProcessor con il database fasullo
    ottenuto dalla fixture scritta prima"""
    return DataProcessor(db_connection=mock_db)


# 3 definiamo le funzioni di test
def test_process_data_success(processor):
    """testiamo il percorso funzionante"""

    # usiamo le fixture per testare il nostro DataProcessor, quando lo
    # user_id è 1, ci aspettiamo un risultato di "success"
    result = processor.process_data(user_id=1)

    # controlliamo il risultato, utilizzando gli assert nativi di python
    assert result["status"] == "success"
    assert len(result["items"]) == 3
    assert result["items"][0] == "ITEM_A"

def test_process_data_not_found(processor):
    """testiamo il DataProcessor quando non dovrebbe trovare nulla"""
    # vogliamo controllare che venga sollevata la corretta eccezione
    with pytest.raises(ValueError, match="Nessun dato trovato per l'utente"):
        processor.process_data(user_id=99)
