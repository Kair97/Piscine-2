import pytest
from titanic_clean import clean_titanic, load


@pytest.fixture(scope="module")
def raw_data():
    return load()


@pytest.fixture(scope="module")
def cleaned_data(raw_data):
    return clean_titanic(raw_data)


def test_clean_drops_cabin_ticket(cleaned_data):
    assert "Cabin" not in cleaned_data.columns
    assert "Ticket" not in cleaned_data.columns


def test_clean_no_missing_age_or_embarked(cleaned_data):
    assert cleaned_data.isna().sum().sum() == 0
    assert cleaned_data["Age"].isna().sum() == 0
    assert cleaned_data["Embarked"].isna().sum() == 0


def test_clean_shape(cleaned_data):
    assert cleaned_data.shape == (889, 10)
