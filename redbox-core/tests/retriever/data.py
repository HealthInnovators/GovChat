from uuid import uuid4


from GovChat.models.chain import GovChatQuery
from GovChat.models.file import ChunkResolution
from GovChat.test.data import GovChatTestData, generate_test_cases

ALL_CHUNKS_RETRIEVER_CASES = [
    test_case
    for generator in [
        generate_test_cases(
            query=GovChatQuery(question="Irrelevant Question", s3_keys=["s3_key"], user_uuid=uuid4(), chat_history=[]),
            test_data=[GovChatTestData(8, 8000)],
            test_id="Successful Path",
        )
    ]
    for test_case in generator
]

PARAMETERISED_RETRIEVER_CASES = [
    test_case
    for generator in [
        generate_test_cases(
            query=GovChatQuery(question="Irrelevant Question", s3_keys=["s3_key"], user_uuid=uuid4(), chat_history=[]),
            test_data=[GovChatTestData(8, 8000, ChunkResolution.normal)],
            test_id="Successful Path",
        )
    ]
    for test_case in generator
]
