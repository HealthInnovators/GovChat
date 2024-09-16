from GovChat.models.chain import GovChatState
from GovChat.retriever import AllElasticsearchRetriever
from GovChat.test.data import GovChatChatTestCase


def test_all_chunks_retriever(
    all_chunks_retriever: AllElasticsearchRetriever, stored_file_all_chunks: GovChatChatTestCase
):
    result = all_chunks_retriever.invoke(GovChatState(request=stored_file_all_chunks.query))

    assert len(result) == len(stored_file_all_chunks.get_docs_matching_query())
    assert {c.page_content for c in result} | {c.page_content for c in stored_file_all_chunks.docs}
    assert {c.metadata["file_name"] for c in result} == set(stored_file_all_chunks.query.s3_keys)
