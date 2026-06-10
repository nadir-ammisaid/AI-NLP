from lexdiv.metrics import lexical_metrics


def test_lexical_metrics():

    tokens = [
        "cat",
        "dog",
        "cat",
        "mouse",
    ]

    result = lexical_metrics(tokens)

    assert result["tok"] == 4

    assert result["typ"] == 3

    assert result["hap"] == 2

    assert "ttr" in result

    assert "root_ttr" in result

    assert "corrected_ttr" in result

    assert "herdan" in result

    assert "maas" in result
