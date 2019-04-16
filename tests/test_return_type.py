from src.create_st import create_st


def test_create_st():
    input_type = {"var" : "int"}
    output = create_st(input_type)
    assert output == 'st.integers()'
