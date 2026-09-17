
import pandas as pd

from src.duplicate_engine.preprocessing.cleaning import (
    clean_text,
    clean_email,
    clean_phone,
    clean_members,
)


def test_clean_text():

    assert clean_text("  Sahil   Kumar  ") == "Sahil Kumar"


def test_clean_email():

    assert clean_email("  SAHIL@EMAIL.COM ") == "sahil@email.com"


def test_clean_phone():

    assert clean_phone("+91 98765-43210") == "919876543210"


def test_clean_members():

    df = pd.DataFrame({
        "member_name": ["  Sahil   Kumar  "],
        "email": [" SAHIL@EMAIL.COM "],
        "phone": ["98765-43210"],
        "city": [" Hyderabad "],
        "join_date": ["2024-01-01"],
    })

    result = clean_members(df)

    assert result.loc[0, "member_name"] == "Sahil Kumar"
    assert result.loc[0, "email"] == "sahil@email.com"
    assert result.loc[0, "phone"] == "9876543210"
    assert result.loc[0, "city"] == "Hyderabad"
    assert pd.notna(result.loc[0, "join_date"])