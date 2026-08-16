from bert_score import BERTScorer


MODEL_TYPE = (
    "neuralmind/"
    "bert-base-portuguese-cased"
)

NUM_LAYERS = 9

MAX_LENGTH = 512


def calcular_bertscore(
    referencias: list[str],
    gerados: list[str],
):
    """
    Calcula BERTScore usando BERTimbau Base.
    """

    scorer = BERTScorer(
        model_type=MODEL_TYPE,
        num_layers=NUM_LAYERS,
        lang="pt",
        idf=False,
        rescale_with_baseline=False,
        use_fast_tokenizer=False,
    )

    # BERTimbau Base possui
    # max_position_embeddings = 512.
    scorer._tokenizer.model_max_length = (
        MAX_LENGTH
    )

    precision, recall, f1 = (
        scorer.score(
            gerados,
            referencias
        )
    )

    return (
        precision.tolist(),
        recall.tolist(),
        f1.tolist(),
        scorer.hash,
    )