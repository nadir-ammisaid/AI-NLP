from semantic.summarizer import generate_summary


class MockModel:

    def encode(self, paragraphs, convert_to_tensor=True):

        import torch

        return torch.tensor(
            [
                [1.0, 0.0],
                [0.9, 0.0],
                [0.1, 1.0],
            ]
        )


def test_generate_summary(monkeypatch):

    from semantic import summarizer

    monkeypatch.setattr(
        summarizer,
        "get_embedding_model",
        lambda: MockModel(),
    )

    paragraphs = [
        "Alice follows the rabbit.",
        "Alice enters Wonderland.",
        "This paragraph is unrelated.",
    ]

    summary = generate_summary(
        paragraphs,
        top_k=2,
    )

    assert "Alice follows the rabbit." in summary
    assert "Alice enters Wonderland." in summary
    assert "This paragraph is unrelated." not in summary
