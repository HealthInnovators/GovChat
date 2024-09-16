import pytest

from GovChat.models.chain import GovChatState
from GovChat.retriever import ParameterisedElasticsearchRetriever
from GovChat.test.data import GovChatChatTestCase

test_chain_parameters = (
    {
        "rag_k": 1,
        "rag_num_candidates": 100,
        "match_boost": 1,
        "knn_boost": 2,
        "similarity_threshold": 0,
        "elbow_filter_enabled": True,
    },
    {
        "rag_k": 2,
        "rag_num_candidates": 100,
        "match_boost": 1,
        "knn_boost": 2,
        "similarity_threshold": 0,
        "elbow_filter_enabled": False,
    },
)


@pytest.mark.parametrize("chain_params", test_chain_parameters)
def test_parameterised_retriever(
    chain_params: dict,
    parameterised_retriever: ParameterisedElasticsearchRetriever,
    stored_file_parameterised: GovChatChatTestCase,
):
    for k, v in chain_params.items():
        setattr(stored_file_parameterised.query.ai_settings, k, v)

    result = parameterised_retriever.invoke(GovChatState(request=stored_file_parameterised.query))
    assert len(result) == chain_params["rag_k"], result
